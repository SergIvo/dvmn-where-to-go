from django.http import JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from places.models import Place


def render_map(request):
    places = Place.objects.all()
    places_features = []
    for place in places:
        places_features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('places', kwargs={'id': place.id})
                }
            }
        )

    context = {
        'places_geojson': {
            'type': 'FeatureCollection',
            'features': places_features
        }
    }
    return render(request, 'index.html', context=context)


def send_place_details(request, id):
    place = get_object_or_404(Place, id=id)
    place_details = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }
    return JsonResponse(place_details, json_dumps_params={'ensure_ascii': False, 'indent': 4})
