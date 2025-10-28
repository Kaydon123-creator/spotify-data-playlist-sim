from modules.instruments import Guitar, Piano, Drum, Instrument
from modules.song import Song
from modules.playlist import Playlist
from modules.utils import print_section_separator

import json

csv_path = "data/songs.csv"
json_path = "data/songs.json"

# 2.1.3. Fonction à compléter après avoir compléter le code de modules/instruments.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testInstruments():
  
  print_section_separator("Tests partie 2.1")
  
  # TODO: Instancier un objet de la classe Instrument.
  try:
    instrument_1=Instrument("test frabiquant")
    print(instrument_1)
  except:
    print("Impossible d'instancier un Instrument.")

  # TODO: Instancier une Guitar du "fabricant-g", l'afficher, et appeler sa méthode play().

  guitare= Guitar("fabricant-g")
  print(guitare)
  guitare.play()

  # TODO: Instancier un Piano du "fabricant-p", l'afficher, et appeler sa méthode play().
  piano= Piano("fabricant-p")
  print(piano)
  piano.play()

  # TODO: Instancier un Drum du "fabricant-b", l'afficher, et appeler sa méthode play().
  drum= Drum("fabricant-b")
  print(drum)
  drum.play()


# 2.2.6. Fonction à compléter après avoir compléter le code de modules/song.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testSong():
  
  print_section_separator("Tests partie 2.2")

  # TODO: Instancier une Song appelée "Title", de l'artiste "Artist",
  #       sortie en 2024 et qui se joue avec une batterie du fabriquant "brand".
  song_1= Song("Title","Artist",2024, Drum("brand"))
  #       Afficher l'instance créée.
  print(song_1)
  # TODO: Instancier une Song à partir d'un dictionnaire/objet vide (i.e. {}).
  #       Afficher l'instance créée.
  try: 
    song_2= Song("Title","Artist",2024, Drum("brand")).from_obj({})
    print(song_2)
  except ValueError as a:
    print(f"ValueError, message:{a}")

  # TODO: Instancier une Song à partir de la 1ère chanson du fichier "data/songs.json"
  #       Afficher l'instance créée.
  first_data = json.load(open("data/songs.json"))[0]
  song_json= Song.from_obj(first_data)
  print(song_json)


# 2.3.6. Fonction à compléter après avoir compléter le code de modules/playlist.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testPlaylist():
  
  print_section_separator("Tests partie 2.3")

  # TODO: Instancier une Playlist nommée "Playlist-csv" depuis le fichier CSV data/songs.csv.
  playlist_csv= Playlist.from_csv("Playlist-csv", "data/songs.csv")
  # TODO: Instancier une Playlist nommée "Playlist-json" depuis le fichier JSON data/songs.json.
  playlist_json= Playlist.from_json("Playlist-json", "data/songs.json")
  # TODO:Ajouter un dictionnaire/objet vide (i.e. {}) à la playlist "Playlist-json".
  try:
    playlist_json = playlist_json + {}
  except TypeError:
    print("TypeError, message:{TypeError}")

  # TODO: Ajouter les chansons de la playlist "Playlist-json" à la playlist "Playlist-csv".
  for song in playlist_json.songs.values():
    playlist_csv= playlist_csv + song 

  
  # TODO: Retirer la chanson intitulée "We Will Rock You" de la playlist "Playlist-csv".
  playlist_csv= playlist_csv - "We Will Rock You"

  # TODO: Jouer toutes les chansons de la playlist "Playlist-json" en mode normal.
  playlist_json.play_all(False)
  #TODO: Jouer toutes les chansons de la playlist "Playlist-csv" en mode aléatoire.
  playlist_csv.play_all(True)

if __name__ == "__main__":
  testInstruments()
  testSong()
  testPlaylist() 


