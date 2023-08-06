from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.contrib.sites.models import Site
from django.shortcuts import render
import httplib2
from requests_oauthlib import OAuth2Session
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from csgoogleanalytics.models import CredentialsModel, AnalyticsProfile


def get_oauth(request):
    client_id = getattr(settings, "GOOGLE_OAUTH2_CLIENT_ID", "")
    scope = "https://www.googleapis.com/auth/analytics.readonly"
    redirect_uri = "{0}".format(request.build_absolute_uri(reverse("auth_return")))
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    return oauth


@login_required
def set_google(request):
    oauth = get_oauth(request)
    authorization_url, state = oauth.authorization_url(
        "https://accounts.google.com/o/oauth2/auth",
        # access_type and prompt are Google specific extra
        # parameters.
        access_type="offline",
        prompt="select_account",
    )
    return HttpResponseRedirect(authorization_url)


@login_required
def auth_return(request):
    oauth = get_oauth(request)
    client_secret = getattr(settings, "GOOGLE_OAUTH2_CLIENT_SECRET", "")
    uri = "https://%s%s" % (Site.objects.get_current(), request.get_full_path())
    token = oauth.fetch_token(
        "https://accounts.google.com/o/oauth2/token",
        authorization_response=uri,
        # Google specific extra parameter used for client
        # authentication
        client_secret=client_secret,
    )
    credential = Credentials(token["access_token"])
    credential_model = CredentialsModel(
        id=request.user, credential=credential, site=Site.objects.get_current()
    )
    credential_model.save()
    return HttpResponseRedirect(reverse("select_property"))


@login_required
def select_property(request):
    credential_model = CredentialsModel.objects.get(id=request.user, site=settings.SITE_ID)
    credential = credential_model.credential
    analytics = build("analytics", "v3", credentials=credential)
    profiles = (
        analytics.management()
        .profiles()
        .list(accountId="~all", webPropertyId="~all")
        .execute()
    )
    items = profiles.get("items", [])
    return render(
        request, "csgoogleanalytics/select_analytics_property.html", context=locals()
    )


@login_required
def set_property(request, track_id):
    site = Site.objects.get(id=settings.SITE_ID)
    credentialmodel = CredentialsModel.objects.get(id=request.user)
    if AnalyticsProfile.objects.filter(site=site).exists():
        profile = AnalyticsProfile.objects.get(site=site)
        profile.delete()
    AnalyticsProfile.objects.create(
        tracking_code=track_id, credentials=credentialmodel, site=site
    )
    return HttpResponseRedirect(reverse("admin:csgoogleanalytics_analytics_changelist"))
