import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, SortableImage


class Command(BaseCommand):
    help = 'Fetches details for places from given url'
    
    def add_arguments(self, parser):
        parser.add_argument('source_url', type=str)
        
    def handle(self, *args, **options):
        source_url = options.get('source_url')
        
        response = requests.get(source_url)
        response.raise_for_status()
        details = response.json()
        
        place, _ = Place.objects.get_or_create(
            title=details['title'],
            defaults={
                'description_short': details['description_short'],
                'description_long': details['description_long'],
                'longitude': details['coordinates']['lng'],
                'latitude': details['coordinates']['lat']
            }
        )
        
        for image_url in details['imgs']:
            try:
                response = requests.get(image_url)
            except requests.exceptions.InvalidSchema:
                continue
            response.raise_for_status()
            image_name = image_url.split('/')[-1]
            with ContentFile(response.content, name=image_name) as image_file:
                saved_image = SortableImage.objects.create(place=place, image=image_file)
        
        
