# Projet 2 : Traitement de données et OOP

Ce projet se divise en 2 parties distinctes.

#### Partie 1 : Traitement de données

Nous allons **traiter un jeu de données de chansons à l'aide de librairies scientifiques**.
Nous utilisons pour cela un cahier Jupyter, format idéal de travail pour l'exploration de données.

Le répertoire de travail pour cette partie est `part1/`.



#### Partie 2 : Programmation orientée objet
Nous allons **faire de la programmation orientée objet** pour créer une application qui permet de "jouer" des playlists de chansons à partir d'instruments de musique.

Le répertoire de travail pour cette partie est `part2/`.

## Structure du projet

```plaintext
<répertoire-principal>/
│   README.md
└─── part1/
│   └─── plots/
│           ...
│        songs-analysis.ipynb
└─── part2/
    └─── data/
    │       songs.csv
    │       songs.json
    └─── modules/
    │       utils.py
    │       instruments.py
    │       song.py
    │       playlist.py
    └─── main.py
```

### Répertoire `part1/`

- `songs.csv` : fichier CSV avec les données de chansons.
- `songs-analysis.ipynb` : fichier Notebook Jupyter où nous allons procéder à l'exploration des chansons.
- `plots/` : contient l'exemple de sorties visuelles attendues depuis le cahier Jupyter.


### Répertoire `part2/`

- `data/` : contient un fichier CSV et un fichier JSON avec les données de chansons.
- `modules/` : contient les fichiers où nous allons implémenter les classes de notre application de playlists.
- `main.py` : fichier où nous testerons notre implémentation.


# Partie 1 : Traitement de données
Notre objectif est de manipuler et de traiter le jeu de données (contenu dans le fichier `songs.csv`) des chansons les plus écoutées sur Spotify en 2024. Nos traitement serviront ensuite à entraîner un modèle simple de régression linéaire pour la prédiction du nombre total d'écoutes d'une chanson sur Spotify.


## Contenu du jeu de données
| Nom de la colonne | Description |
| -- | -- |
| Track Name | Titre de la chanson. |
| Album Name | Nom de l'album auquel la chanson appartient. |
| Artist | Nom de l'artiste ou des artistes de la chanson. |
| Release Date | Date de sortie de la chanson. |
| ISRC | International Standard Recording Code de la chanson. |
| All Time Rank | Classement de la chanson basé sur sa popularité historique. |
| Track Score | Score attribué au titre selon divers facteurs. |
| Spotify Streams | Nombre total d'écoutes sur Spotify. |
| Spotify Playlist Count | Nombre de playlists Spotify contenant la chanson. |
| Spotify Playlist Reach | Portée de la chanson à travers les playlists Spotify. |
| Spotify Popularity | Score de popularité de la chanson sur Spotify. |
| YouTube Views | Nombre total de vues de la vidéo officielle de la chanson sur YouTube. |
| YouTube Likes | Nombre total de likes sur la vidéo officielle de la chanson sur YouTube. |
| TikTok Posts | Nombre de publications TikTok incluant la chanson. |
| TikTok Likes | Nombre total de likes sur les publications TikTok incluant la chanson. |
| TikTok Views | Nombre total de vues sur les publications TikTok incluant la chanson. |
| YouTube Playlist Reach | Portée de la chanson à travers les playlists YouTube. |
| Apple Music Playlist Count | Nombre de playlists Apple Music contenant la chanson. |
| AirPlay Spins | Nombre de fois que la chanson a été diffusée sur les stations de radio. |
| SiriusXM Spins | Nombre de fois que la chanson a été diffusée sur SiriusXM. |
| Deezer Playlist Count | Nombre de playlists Deezer contenant la chanson. |
| Deezer Playlist Reach | Portée de la chanson à travers les playlists Deezer. |
| Amazon Playlist Count | Nombre de playlists Amazon Music contenant la chanson. |
| Pandora Streams | Nombre total d'écoutes sur Pandora. |
| Pandora Track Stations | Nombre de stations Pandora incluant la chanson. |
| Soundcloud Streams | Nombre total d'écoutes sur Soundcloud. |
| Shazam Counts | Nombre total de fois que la chanson a été recherchée sur Shazam. |
| TIDAL Popularity | Score de popularité de la chanson sur TIDAL. |
| Explicit Track | Indique si la chanson contient un contenu explicite. |



# Partie 2 : Programmation orientée objet
Notre objectif est de créer un système de lecture de playlists.
On veut être capable de créer des playlists à partir d'une base de données de chansons (enregistrée dans les fichiers `data/songs.csv` et `data/songs.json`) et jouer ces chansons en mode "solo" (à l'aide d'un seul instrument) à partir d'une playlist.

## Vue d'ensemble
Le diagramme ci-bas montre les classes qui vont représenter les objets de notre système ainsi que leurs liens. Par simplicité, seul les attributs des classes et leurs méthodes standards publics y sont représentés.


![Vue d'ensemble](/assets/part2-class-diagram.png)

