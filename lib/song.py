class Song:
    # class atrributes
    count = 0
    genres = []
    artists = []
    # dictionary: { genre: number_of_songs }
    genre_count = {}
    # dictionary: { artist: number_of_songs }
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
    # class methods to trigger upon a new song being created
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()
  
    def add_song_to_count(self):
        # increment total song count by 1
        Song.count += 1


    def add_to_genres(self):
        # only add genre if it's new/unique
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)


    def add_to_artists(self):
        # only add artist if new/unique
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        # update genre count dictionary
        pass


    def add_to_artists_count(self):
        # update artist count dictionary
        pass