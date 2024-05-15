import os

import googlemaps
from datetime import datetime

from serpapi import GoogleSearch

def search_images_from_text(query, n=5):
    """
    Recherche des liens d'images sur Internet à partir d'un texte donné en utilisant l'API SerpAPI pour Google Images.

    Paramètres:
    query (str): Le texte à rechercher.
    n (int): Le nombre de résultats d'images à retourner (par défaut 5).

    Retourne:
    list: Une liste de tuples contenant les liens des images et leurs sources, limitée à 'n' résultats.
    """
    # Définir les paramètres pour l'API SerpAPI Google Images
    params = {
        "q": query,  # Le texte de la requête de recherche
        "engine": "google_images",  # Spécifie l'utilisation du moteur de recherche d'images Google
        "ijn": "0",  # Index de page des résultats de l'image
        "api_key": "e4839d16be6f4030e3da4cbd35c2dec250fef6fb2df966a6b07183b54db6119c"  # Votre clé API SerpAPI
    }

    # Effectuer la recherche en utilisant SerpAPI
    search = GoogleSearch(params)
    results = search.get_dict()  # Obtenir les résultats sous forme de dictionnaire
    images_results = results["images_results"]  # Extraire la liste des résultats d'images

    # Extraire les liens des images et leurs sources
    image_link = [
        (i['original'], i['source'])
        for i in images_results
        if i['original'].split('.')[-1] in ['jpg', 'png', 'jpeg', 'svg']  # Filtrer pour ne conserver que certains formats d'image
    ]

    return image_link[:n]
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
    gmaps = googlemaps.Client(key=os.getenv('GOOGLE_API_KEY'))
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
        'website': result.get('website'),
        'coordonnees_geolocalisation': (result['geometry']['location'].get('lng'),result['geometry']['location'].get('lat'))
    }

    return place_info