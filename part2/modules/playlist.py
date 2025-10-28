from modules.song import Song
from typing import Iterator
import csv, json, random


class Playlist():
    def __init__(self, name: str, songs: list[Song]):
        if name[:9]=="Playlist-":
          self.__name= name 
        
        self.__songs={song.title: song for song in songs}
    @classmethod
    def from_csv(cls, name: str, csv_path: str):
       
        with open(csv_path, mode="r") as f:
          fichier_csv= csv.DictReader(f)
          songs=[Song.from_obj(ligne) for ligne in fichier_csv]
      
        return cls(name,songs) 
    @classmethod
    def from_json(cls, name: str, json_path: str):
       
        with open(json_path, mode="r") as f:
          fichier_json= json.load(f)
          songs=[Song.from_obj(dic) for dic in fichier_json]
      
        return cls(name,songs) 
    @property 
    def name(self):
       return self.__name
    @property 
    def songs(self):
       return self.__songs
    @name.setter 
    def name(self, valeur):
       if valeur[:9]=="Playlist-":
        self.__name= valeur 
    @songs.setter
    def song(self, valeur):
       self.__songs= {song.title:song for song in valeur}  
      

    def __iter__(self):
       return iter(self.__songs.values()) 
    
    def __add__(self, song):
        if isinstance(song, Song):
          self.__songs[song.title]=song 
          return self 
        else:
          raise TypeError(f"Impossible d'ajouter une chanson de type {type(song)}.")
    def __sub__(self, song_title):
        if song_title in self.__songs.keys():
          del self.__songs[song_title]
        return self
       
    def play_all(self, rdm_mode: bool=False):
        mode_de_lecture= "standard" if rdm_mode==False else "aléatoire"
        print(f"Lecture de {self.__name} ({len(self.__songs.keys())} chansons en mode {mode_de_lecture})")
        songs = list(self.__songs.values())
        if rdm_mode:
          for song in songs:
            song=random.choice(list(set((self.__songs.values()))))
            print(song.play())
        else:
           for song in songs:
              print(song.play())




       

    
    
    



