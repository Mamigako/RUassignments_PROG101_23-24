import sys


def main():
    # Simple test script.
    sys.stderr.write("Input music, group, singer: ")
    music, group, singer = input().split(",")

    state_music_opinion(music, group, singer)
    print()
    state_music_opinion()

#Prints which genre, band and vocalist are the best. Defaults to someone´s favourites.

def state_music_opinion(genre="Classic Rock", music_group="The Beatles", vocalist="Freddie Mercury"):
    print(f"The best type of music is {genre}.")
    print(f"The best music group is {music_group}.")
    print(f"The best lead vocalist is {vocalist}.")

if __name__ == "__main__":
    main()
