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
        # increment count for this genre, or set to 1 if genre doesn't exist in genre_count
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1


    def add_to_artists_count(self):
        # update artist count dictionary
        # increment count for this artist, or set to 1 if artist doesn't exist in artists_count
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1