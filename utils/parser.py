from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional

class AgentOutput(BaseModel):
    text: Optional[str] = Field(None, description="Réponse textuelle de l'agent")
    image_link: Optional[List[str]] = Field(None, description="Lien vers une image générée par l'agent")
    sources: Optional[List[str]] = Field(default_factory=list, description="Liste des sources référencées par l'agent")
    video_link: Optional[str] = Field(None, description="Lien vers une vidéo liée à la réponse de l'agent")
    response: Optional[str] = Field(None, description="Réponse générale de l'agent")

    def to_dict(self):
        return {
            "text": self.text,
            "image_link": self.image_link,
            "sources": self.sources,
            "video_link": self.video_link,
            "response": self.response
        }


# Initialize the output parser with the Pydantic model
agent_output_parser = PydanticOutputParser(pydantic_object=AgentOutput)