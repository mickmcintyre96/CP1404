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

song_title = input("title")
artist = input("h")
year = input("h")


new_song = []
new_song.extend((song_title.title(), artist.title(), year, 'y\n'))
print(new_song)