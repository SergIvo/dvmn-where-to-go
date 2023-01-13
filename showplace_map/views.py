from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from places.models import Place


def render_map(request):
    template = loader.get_template('index.html')
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
                    'detailsUrl': 'json_file'
                }
            }
        )

    context = {
        'places_geojson': {
            'type': 'FeatureCollection',
            'features': places_features
        }
    }
    rendered_page = template.render(context)
    return HttpResponse(rendered_page)


def send_place_description(request, id):
    place = get_object_or_404(Place, id=id)
    place_features = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }
    return JsonResponse(place_features, json_dumps_params={'ensure_ascii': False, 'indent': 4})
