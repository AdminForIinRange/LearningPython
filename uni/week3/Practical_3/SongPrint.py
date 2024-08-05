class Song:
    def __init__(self, title, artist, album, duration, genre):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration  # Duration in seconds
        self.genre = genre

    def play(self):
        # Convert duration from seconds to minutes:seconds format
        minutes = self.duration // 60
        seconds = self.duration % 60
        duration_str = f"{minutes}:{seconds:02}"
        
        # Print out the song details
        print(f"{self.title}\n{self.artist}---{self.album}\n{duration_str}\n")

    def __str__(self):
        # Optional string representation for testing purposes
        return f"{self.title} by {self.artist} from the album '{self.album}' - {self.genre}, {self.duration} seconds"

# Example usage
song1 = Song("Game Over", "Avenged Sevenfold", "Life Is But a Dream...", 226, "Rock")
song2 = Song("Mattel", "Avenged Sevenfold", "Life Is But a Dream...", 330, "Rock")
song3 = Song("Nobody", "Avenged Sevenfold", "Life Is But a Dream...", 353, "Rock")
song4 = Song("We Love You", "Avenged Sevenfold", "Life Is But a Dream...", 375, "Rock")

# Playing the songs
song1.play()
song2.play()
song3.play()
song4.play()
