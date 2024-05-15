from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional, Tuple


class AgentOutput(BaseModel):
    """
    Modèle Pydantic pour structurer la sortie de l'agent.

    Attributs:
    - text: Réponse textuelle générée par l'agent.
    - image_link: Liste des liens vers les images générées par l'agent.
    - sources: Liste des sources référencées par l'agent dans sa réponse.
    - video_link: Lien vers une vidéo liée à la réponse de l'agent.
    - response: Réponse générale de l'agent, incluant potentiellement une combinaison de texte, liens d'images, et vidéos.
    """
    text: Optional[str] = Field(None, description="Réponse textuelle de l'agent.")
    image_link: Optional[List[str]] = Field(None,
                                            description="Liens vers des images générées par l'agent avec des paramètres spécifiés.")
    sources: Optional[List[str]] = Field(default_factory=list, description="Liste des sources référencées par l'agent.")
    video_link: Optional[List[str]] = Field(None, description="Liens vers des vidéos liées à la réponse de l'agent.")
    response: Optional[str] = Field(None,
                                    description="Réponse générale de l'agent, bien structurée et intéressante, avec des détails.")
    maps_link: Optional[List[str]] = Field(None, description="Liens Google Maps avec identifiants de lieu (cid).")
    geo_code: Optional[Tuple] = Field(None, description="Coordonnées de géolocalisation liées au lien Google Maps.")
    def to_dict(self):
        """
        Convertit le modèle Pydantic en dictionnaire pour une utilisation facile.
        """
        return {
            "text": self.text,
            "image_link": self.image_link,
            "sources": self.sources,
            "video_link": self.video_link,
            "response": self.response,
            "geo_code":self.geo_code,
            "maps_link":self.maps_link
        }

# Initialisation du parseur de sortie avec le modèle Pydantic
agent_output_parser = PydanticOutputParser(pydantic_object=AgentOutput)
