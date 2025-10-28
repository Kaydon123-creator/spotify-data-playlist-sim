import modules.instruments # used in from_obj() classmethod
from modules.instruments import Instrument
from datetime import datetime


class Song():
  max_len_str_attr = 25
  def __init__(self, title: str, artist: str, release_year: int, instrument: Instrument):
    if len(title) <= Song.max_len_str_attr:
      self.__title= title 
    if len(artist) <= Song.max_len_str_attr:
      self.__artist= artist
    if release_year <= datetime.now().year and release_year >= 0:
      self.__release_year= release_year
    if isinstance(instrument,Instrument):
      self.__instrument= instrument 

  @classmethod
  def from_obj(cls, obj: dict):
      clés= ["title", "artist", "release_year", "instrument", "instrument_brand"]
      if [key for key in obj.keys()] == clés:
        instrument_cls = getattr(modules.instruments, obj["instrument"])
        instrument=instrument_cls(obj["instrument_brand"])
        return cls(obj["title"], obj["artist"], int(obj["release_year"]), instrument)
      else:
        raise ValueError(f"Impossible d'instancier une chanson depuis l'objet {obj}.")
      
  @property
  def title(self):
    return str(self.__title)
  @property
  def artist(self):
    return str(self.__artist)
  @property
  def release_year(self):
    return self.__release_year
  @property
  def instrument(self):
    return self.__instrument 
  @title.setter
  def title(self, valeur):
    if len(valeur) <= Song.max_len_str_attr:
      self.__title= valeur 
  @artist.setter 
  def artist(self, valeur):
    if len(valeur) <= Song.max_len_str_attr:
      self.__artist= valeur
  @release_year.setter
  def release_year(self, valeur):
    if valeur <= datetime.now().year and valeur >= 0:
      self.__release_year= valeur

  @instrument.setter
  def instrument(self, valeur):
     if isinstance(valeur,Instrument):
        self.__instrument= valeur 
    
  def __str__(self) -> str:
    return f"Titre: {self.__title}\n Artiste: {self.__artist}\n Année de sortie: {self.__release_year}\n Instrument: {self.__instrument}"
  def play(self):
    return f"Joue {self.__title: <{self.max_len_str_attr}} solo avec *** {self.instrument.__class__.__name__}*** du fabriquant {self.instrument._brand}"

        



