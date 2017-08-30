# # #  1
# name = ["a","c",[1,2,3]]
# out_file = open("name.txt", "w")
# # name = input("What is your name? ")
# out_file.writelines(name)
# out_file.close()
# #
# # 2
# in_file = open("name.txt", "r")
# name =  in_file.read()
# print ("Your name is {}".format(name))
# in_file.close()

# 3 extension
# sum = 0
# in_file = open("numbers.txt", "r")
# for lines in in_file:
#     number = int(lines)
#     sum += number
# print("Sum of all numbers is: {}".format(sum))
# in_file.close()
SONG_NAME = 0
ARTIST = 1
YEAR = 2
LEARNT = 3

my_list = [['Heartbreak Hotel', 'Elvis Presley', '1956', 'y\n'],
           ['Somebody That I Used to Know', 'Gotye featuring Kimbra', '2012', 'n\n'],
           ['Macarena', 'Los Del Rio', '1996', 'n\n']]
out_file = open("songs.csv", "w")
for song in range(0, len(my_list)):
    print (len(my_list))
    out_file.write('{0}, {1}, {2}, {3}'.format(my_list[song][SONG_NAME], my_list[song][ARTIST], my_list[song][YEAR],my_list[song][LEARNT]))
out_file.close()
