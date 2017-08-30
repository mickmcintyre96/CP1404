# def add_song():
#     new_song=[]
#     valid_input= False
#     song_title = input("name of song?")
#     while song_title == "":
#         print("Cannot be be blank")
#         song_title = input("name of song?")
#     # new_song.append(song_title.title())
#     artist = input("name of artist? ")
#     while artist == "":
#         print("Cannot be be blank")
#         artist = input("name of artist?")
#     # new_song.append(artist.title())
#     while not valid_input:
#         try:
#             year = int(input("year"))
#             valid_input = True
#         except ValueError:
#             print("Please enter a number")
#
#     new_song.extend((song_title.title(), artist.title(), year))
#     return(new_song)
# # new_song.append(year)


# valid_input = False
# while not valid_input:
#     try:
#         age = int(input("Age: "))
#         valid_input = True
#     except ValueError:  # or just  except:
#         print("Invalid (not an integer)")
# print("Next year you will be", age + 1)

# song_title = input("title")
# artist = input("h")
# year = input("h")
#
#
# new_song = []
# new_song.extend((song_title.title(), artist.title(), year, 'y\n'))
# print(new_song)

"""
Mick McIntyre Assignment 1.
"""
SONG_NAME = 0
ARTIST = 1
YEAR = 2
LEARNT = 3
MENU = """Menu:\nL- List Songs\nA- Add new song\nC- Complete a song\nQ- Quit"""


def main():
    print("Songs To Learn 1.0 - by <Your Name>")
    load_songs()
    print("{} songs loaded \n{}".format(len(load_songs()), MENU))
    choice = input(">>>").upper()
    song_list = load_songs()
    while choice != "Q":
        if choice == "L":
            list_songs(song_list)
        elif choice == "A":
            adds_new_song(song_list)
        elif choice == "C":
            complete_song(song_list)
        print(MENU)
        choice = input(">>>").upper()
        # new_song=(add_song(song_title,artist,year))

        # song_list.append(add_song(song_title,artist,year))

    print("thank you ")
    # #save songs to list
    saves_changes(song_list)


def saves_changes(song_list):
    out_file = open("songs.csv", "w")
    for song in range(0, len(song_list)):
        out_file.write(
            '{0},{1},{2},{3}'.format(song_list[song][SONG_NAME], song_list[song][ARTIST], song_list[song][YEAR],
                                     song_list[song][LEARNT]))
    out_file.close()


def complete_song(song_list):
    print("Enter the number of a song to mark as learned")
    song_to_learn = int(input(">>>"))
    if 'y\n' in song_list[song_to_learn]:
        song_list[song_to_learn][LEARNT] = 'n\n'
        print("{} by {} learned".format(song_list[song_to_learn][SONG_NAME], song_list[song_to_learn][ARTIST]))

    else:
        print("{} by {} already learned".format(song_list[song_to_learn][SONG_NAME],
                                                song_list[song_to_learn][ARTIST]))


def adds_new_song(song_list):
    valid_input = False
    song_title = input("Title:")
    while not song_title:
        print("Input can not be blank")
        song_title = input("Title: ")
    artist = input("Artist:")
    while not artist:
        print("Input can not be be blank")
        artist = input("Artist: ")
    while not valid_input:
        try:
            year = int(input("Year:"))
            if year < 0:
                print("Number must be >= 0")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input; please enter a valid number")
    add_song(song_title, artist, year, song_list)
    new_song = song_list[-1]
    print("{} by {} ({}) added to the song list".format(new_song[SONG_NAME], new_song[ARTIST], new_song[YEAR]))


def list_songs(my_list):
    number_of_songs_learned = 0
    number_of_songs_to_learn = 0
    from operator import itemgetter
    my_list.sort(key=itemgetter(ARTIST, YEAR))
    for i in range(0, len(my_list)):
        if my_list[i][LEARNT] == 'n\n':
            print(
                '{}. {:30}- {:25} ({}) '.format(i, my_list[i][SONG_NAME], my_list[i][ARTIST], my_list[i][YEAR]))
            number_of_songs_learned += 1
        else:
            print(
                '{}.*{:30}- {:25} ({}) '.format(i, my_list[i][SONG_NAME], my_list[i][ARTIST], my_list[i][YEAR]))
            number_of_songs_to_learn += 1
    print("{} songs learned, {} songs still to learn".format(number_of_songs_learned, number_of_songs_to_learn))


def load_songs():
    # open the file songs.csv
    in_file = open("songs.csv", "r")
    # save the contents of the file into a variable called songs
    songs = []
    for lines in (in_file):
        song = lines.split(',')
        songs.append(song)
    return songs


def add_song(song_title, artist, year, my_list):
    new_song = []
    new_song.extend((song_title.title(), artist.title(), year, 'y\n'))
    my_list.append(new_song)
    return [my_list, new_song]


def count_learned_song(song_list):
    number_of_songs_learned = 0
    for i in range(0, len(song_list)):
        if song_list[i][LEARNT] == 'n':
            number_of_songs_learned += 1
    return number_of_songs_learned


def count_songs_to_learn(song_list):
    number_of_songs_to_learn = 0
    for i in range(0, len(song_list)):
        if song_list[i][LEARNT] == 'y':
            number_of_songs_to_learn += 1
    return number_of_songs_to_learn

main()