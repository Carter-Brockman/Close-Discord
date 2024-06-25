import os
import time

programIsRunning = True
counter = 0


while (programIsRunning == True) and (counter <= 2):

    if counter >= 1:
        print('')

    userChoice = input("End Discord? (y/n): ")
    userChoice = userChoice.upper()


    if (userChoice == 'Y'):
        os.system("taskkill /f /IM Discord.exe")
        programIsRunning = False

    elif (userChoice == 'N'):
        programIsRunning = False

    else:
        os.system("cls")
        print("Wrong input, type either 'y' or 'n'")
        counter += 1
        programIsRunning = True


if counter >= 3:
    os.system("cls")
    print("\nToo many incorrect inputs...\nClosing program")
    time.sleep(3)
    exit(0)