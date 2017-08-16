# TODO: Fix this!

score = float(input("Enter score: "))
if 0 > score or score > 100:
    print("Invalid Score")
elif score < 50:
    print("Bad")
elif score < 90:
    print("Passable")
else:
    print("Excellent")

