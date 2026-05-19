from dataclasses import dataclass


@dataclass
class Artista:
    ArtistId: int
    Name: str

    def __hash__(self):
        return hash(self.ArtistId)

    def __str__(self):
        return f"{self.ArtistId} - {self.Name}"