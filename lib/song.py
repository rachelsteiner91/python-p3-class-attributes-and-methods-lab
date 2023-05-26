class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    def add_to_genres(self, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)

    def add_to_artists(self, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)

    def add_to_genre_count(self, genre):
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

#add_to_artist_count(): creates a histogram similar to the one above, but for artists rather than genres.
    def add_to_artist_count(self, artist):
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1


# class Song:
# #2 Create a class attribute, count add it to the class Song and then add it to the init. set this attribute equal to 0
#     count = 0
# #You'll need a class attribute, let's call it genres, that is equal to an empty list.
#     genres = [""]
# #You'll need a class attribute, artists, that is equal to an empty list.
#     artists = [""]
#     genre_count = {}
#     artist_count = {}
# #1 Define your Song class such that an individual song is initialized with a name, artist and genre
#     def __init__(self, name, artist, genre):
#         self.name = name
#         self.artist = artist
#         self.genre = genre
# #Whenever a new song is created. Your __init__ method should call a class method add_song_to_count() that increments the value of count by one.
#         Song.count += 1
#         Song.genres = "Rap", "Pop", "Rock"
#         Song.artists = "Jay Z", "Beyonce", "Hall and Oates" 
#         # for artist_name in artist:
#         #     self.add_to_artists(artist_name)
    
#     def add_song_to_count():
#         pass

#     def add_to_genres():
#         pass

#     def add_to_artists():
#         pass

#     def add_to_genre_count(genre):
#         if Song.genre_count.get(genre):
#             Song.genre_count[genre] += 1
#         else:
#             Song.genre_count[genre] = 1

#     def add_to_artist_count():
#         pass

  





