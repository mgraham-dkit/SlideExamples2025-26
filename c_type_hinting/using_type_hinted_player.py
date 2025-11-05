# Import the class
from players import TypeHintedMusicPlayer


# Create a TypeHintedMusicPlayer with a default library
my_zune = TypeHintedMusicPlayer("Michelle Graham")
# Play a random song from my_zune - this will display a message saying
# to add songs as the default library is empty!
my_zune.play_random_song()

# Create a second music player and supply a library as well as owner info
backup_zune = TypeHintedMusicPlayer("Also Michelle Graham", ["Wildest Dreams", "Style", "Father Figure", "Tolerate It", "Peter"])
# Play a random song from the second player object (backup_zune) -
# this will display a message saying a random song is being played
backup_zune.play_random_song()