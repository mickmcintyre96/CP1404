# #  1
# out_file = open("name.txt", "w")
# name = input("What is your name? ")
# out_file.write(name)
# out_file.close()
#
# # 2
# in_file = open("name.txt", "r")
# name =  in_file.read()
# print ("Your name is {}".format(name))
# in_file.close()

# 3 extension
sum = 0
in_file = open("numbers.txt", "r")
for lines in in_file:
    number = int(lines)
    sum += number
print("Sum of all numbers is: {}".format(sum))
in_file.close()
