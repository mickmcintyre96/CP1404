import random
def main():
    number_of_quick_picks = int(input("how many quick picks?"))

    for i in range(0,number_of_quick_picks):
        quick_picks=[]
        for j in range (0,6):
            number = random.randint(1,45)
            while number in quick_picks:
                number = random.randint(1,45)
            quick_picks.append(number)
        quick_picks.sort()
        print(" ".join("{:2}".format(number)for number in quick_picks))
main()




