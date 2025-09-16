from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beach House", "description": "Relax by the sea", "price_per_night": 120.50, "location": "Cape Coast"},
            {"title": "City Apartment", "description": "Modern and central", "price_per_night": 85.00, "location": "Accra"},
            {"title": "Mountain Cabin", "description": "Peaceful retreat", "price_per_night": 60.00, "location": "Aburi"},
        ]

        for data in sample_listings:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("🌱 Database seeded successfully!"))