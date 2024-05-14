import os

import googlemaps
from datetime import datetime


def get_place_info(place_name):
    """
       Récupère des informations détaillées localisation et heures d'ouverture sur un lieu donné en utilisant l'API Google Maps.

       Paramètres:
       nom_lieu (str): Le nom du lieu à rechercher.

       Retourne:
       dict: Un dictionnaire contenant le nom du lieu, l'URL Google Maps,
             les heures d'ouverture (si disponibles), et l'URL du site web (si disponible).
             Si aucun résultat n'est trouvé, retourne un message indiquant qu'aucun résultat n'a été trouvé.
             Si des informations détaillées ne sont pas disponibles, retourne un message indiquant qu'aucune information détaillée n'a été trouvée.
       """
    # Initialize the Google Maps client
    gmaps = googlemaps.Client(key="AIzaSyBfgzILYLxCMhufm8mSIYVBCSEJy1OlPPk")
    place_name=f"{place_name} Bénin"

    # Perform a place search
    places_result = gmaps.places(query=place_name)

    if not places_result['results']:
        return "No results found"

    # Take the first result
    place = places_result['results'][0]
    place_id = place['place_id']

    # Get detailed information about the place
    place_details = gmaps.place(place_id=place_id)

    if not place_details['result']:
        return "No detailed information found"

    result = place_details['result']
    print(result)
    # Extract the required information
    place_info = {
        'name': result.get('name'),
        'google_maps_url': result.get('url'),
        'opening_hours': result.get('opening_hours', {}).get('weekday_text'),
        'website': result.get('website')
    }

    return place_info
