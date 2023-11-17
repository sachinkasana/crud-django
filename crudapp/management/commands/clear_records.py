# clear_records.py

from django.core.management.base import BaseCommand
from crudapp.models import Book

class Command(BaseCommand):
    help = 'Clear all records from specific models'

    def handle(self, *args, **kwargs):
        # Clear records from a specific model
        Book.objects.all().delete()
        # Repeat this for all models you want to clear
