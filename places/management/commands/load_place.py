import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, SortableImage


class Command(BaseCommand):
    help = 'Fetches details for places from given url'
    
    def add_arguments(self, parser):
        parser.add_argument('source_url', type=str)

    def download_image_to_db(self, image_url, place):
        response = requests.get(image_url)
        response.raise_for_status()
        image_bytes = response.content
        image_name = image_url.split('/')[-1]
        with ContentFile(image_bytes, name=image_name) as image_file:
            SortableImage.objects.create(
                place=place,
                image=image_file
            )
        
    def handle(self, *args, **options):
        source_url = options.get('source_url')
        response = requests.get(source_url)
        response.raise_for_status()
        details = response.json()

        place, just_created = Place.objects.get_or_create(
            title=details['title'],
            defaults={
                'description_short': details.get('description_short', ''),
                'description_long': details.get('description_long', ''),
                'longitude': details['coordinates']['lng'],
                'latitude': details['coordinates']['lat']
            }
        )

        if just_created:
            for image_url in details.get('imgs', []):
                try:
                    self.download_image_to_db(image_url, place)
                except requests.exceptions.InvalidSchema:
                    continue
