"""
wait for db to be available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Make Django wait for DB    """

    def handle(self, *args, **options):
        pass
    