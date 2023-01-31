import random

#function to show menu
def showoptions():
    print("========")
    print("Welcome to the Sure Win TOTO and 4D generator!\n========\n")
    print("1. Generate TOTO numbers")
    print("2. Generate 4D numbers")
    print("3. Tell me my fortune")
    print("4. Generate a Chinese New Year greeting")
    print("5. Quit")

showoptions()
option = input("\nPlease select option: ")

#loop the menu unless user quit
while option != "5":
    
    # option 1 generate toto numbers
    if option == "1":
        # generate each num
        # random_num1 = random.randint(1, 49)
        # random_num2 = random.randint(1, 49)
        # random_num3 = random.randint(1, 49)
        # random_num4 = random.randint(1, 49)
        # random_num5 = random.randint(1, 49)
        # random_num6 = random.randint(1, 49)

        # Generate a list of 6 random numbers
        random_num = random.sample(range(1, 49), 6)

        # Sort the list in ascending order
        random_num.sort()

        print("\nYour lucky TOTO numbers are " + str(random_num) + ".")
    
        # print("\nYour lucky TOTO numbers are " + str(random_num1) + ", " + str(random_num2) + ", " + str(random_num3) + ", " + str(random_num4) + ", " + str(random_num5) + ", " + str(random_num6) + ".")
        print("HUAT AH! May your wishes come true! 恭喜发财!\n")

    # option 2 generate 4d numbers
    elif option == "2":
        random_num = random.randint(0000, 9999)
        # random_num = random.randrange(0000, 10000)

        print("Your lucky 4D numbers are " + str(random_num) + ".")
        print("HUAT AH! May your wishes come true! 恭喜发财!\n")

    # option 3 generate fortune
    elif option == "3":
        fortunelist = ['Be careful with new friends', 'Avoid impulsive investments as it may result in losses', 'It is a good year for promotions', 'You have luck in wealth', 'Take a break and you will improve your mental health', 'Keep a active lifestyle to stay healthy', 'Be kind to others for happiness', 'A promising year of opportunities lies ahead', 'Broaden your horizons and you will be rewarded with great wealth', 'You can expect good news frequently this year', 'Pay attention to mood and health','Stay calm when making decisions']
        fortune = random.choice(fortunelist)

        print(fortune)

    # option 4 generate greeting
    elif option == "4":
        huatgreetings = ['新年快乐', '恭喜发财', '年年有余', '万事如意', '步步高升', '兔年快乐', '兔年大吉', '兔年兴旺', '好运连连', '财源广进', '事业有成','步步高升']
        huat = random.choice(huatgreetings)

        print(huat)
    
    else:
        print("Error: please select an option.\n")
        print("========")

    showoptions()
    option = input("\nPlease select option: ")
    print("========")