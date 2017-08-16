name = input("what is your name? ")
if len(name) == 0:
    print("error, blank")
    name = input("what is your name? ")
second_letter = name[1:len(name):2]
print (second_letter)


# for i in range (1, len(name),2):
#     if i == space or:
#         print(name[i + 1])
#         i += 1
#     else:
#         print(name[i])
