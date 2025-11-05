import random as rand

class MusicPlayer:
    count = 0

    def __init__(self, owner, library=None):
        self.owner = owner

        MusicPlayer.count += 1
        self.id = MusicPlayer.count

        if library is None:
            library = []

        self.library = library

    def display(self):
        print(f"{self.__class__.__name__}[Count={MusicPlayer.count}, id={self.id}, owner={self.owner}, library={self.library}]")

    def add(self, song):
        # Convert the song information to lowercase (makes the search easier)
        song = song.lower()
        # If the song is not already present
        if song not in self.library:
            # Add the song to the library
            self.library.append(song)
            # Return true as the song was added
            return True

        # Return false as the song could not be added
        return False

    def get_random_song(self):
        # If the library is empty
        if not self.library:
            # Return no song
            return None

        # Generate a random position within the song library
        index = rand.randint(0, len(self.library)-1)
        # Return the song at that position of the library list
        return self.library[index]

    def play_random_song(self):
        # Get a randomly selected song
        song = self.get_random_song()

        # If a real song was returned (i.e. the library is not empty)
        if not song:
            # Display a message to the user
            print("Library is empty. Please add some songs!")
        else:
            # Otherwise, play the song
            print(f"Now playing {song}!")


class TypeHintedMusicPlayer:
    count: int = 0

    def __init__(self, owner:str, library: list[str] | None = None):
        self.owner = owner

        TypeHintedMusicPlayer.count += 1
        self.id = TypeHintedMusicPlayer.count

        if library is None:
            library = []

        self.library = library

    def display(self) -> None:
        print(f"{self.__class__.__name__}[Count={TypeHintedMusicPlayer.count}, id={self.id}, owner={self.owner}, library={self.library}]")

    def add(self, song: str) -> bool:
        # Convert the song information to lowercase (makes the search easier)
        song = song.lower()
        # If the song is not already present
        if song not in self.library:
            # Add the song to the library
            self.library.append(song)
            # Return true as the song was added
            return True

        # Return false as the song could not be added
        return False

    def get_random_song(self) -> str | None:
        if not self.library:
            return None

        index = rand.randint(0, len(self.library)-1)
        return self.library[index]

    def play_random_song(self) -> None:
        # Get a randomly selected song
        song = self.get_random_song()

        # If a real song was returned (i.e. the library is not empty)
        if not song:
            # Display a message to the user
            print("Library is empty. Please add some songs!")
        else:
            # Otherwise, play the song
            print(f"Now playing {song}!")