import os
from django.core.management.base import BaseCommand
from csgoogleanalytics.utils import create_analytics
from django.conf import settings


class Command(BaseCommand):
    args = "Updates Analytics most viewed data"
    help = "Updates Analytics most viewed data"

    def handle(self, *args, **options):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(
            settings.SECRET_ROOT, "secrets/csgoogleanalytics_secrets.json"
        )
        create_analytics()
