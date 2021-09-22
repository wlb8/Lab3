########################################################################
##
## CS 101 Lab
## Program 3
## Willem Battey
## wlbqx8@umsystem.edu
##
## PROBLEM : Describe the problem
##          Have to solve what number the user is thinking about
## ALGORITHM :
##  Print out statments about this being Flarshiem guesser, and that the user needs to think of a number between 1-10
##  Make empty lists to store the intergers later on
##  Have the statements in one big while loop that will rerun everything depending on the users input
##  Ask for the remainder when divided by 3. Make sure that the number inputted is between 0 and 2
##  Run a loop to check for all the numbers that have the same remainder when divided by 3, and add those to the first list
##  Keep doing that for all the remainders needed
##  Compare the three lists with the intergers
##  Print out the results
##  Ask the user if they want to play again
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


print("Flarsheim guesser")
print("Think of a number between 1-100")
play_again = "Y"
list1 = []
list2 = []
list3 = []
while play_again == "Y":
    div3 = int(input("What is the remainder when your number is divided by 3?\n"))
    if div3 < 0:
        print("The value entered must be bigger than 0")
    if div3 >= 3:
        print("The value entered must be smaller than 3")
    for x in range(1, 101):
        divx = (x % 3)
        if divx == div3:
            list1.append(x)
    div5 = int(input("What is the remainder when your number is divided by 5?\n"))
    for y in range(1, 101):
        divy = (y % 5)
        if divy == div5:
            list2.append(y)
    div7 = int(input("What is the remainder when your number is divided by 7?\n"))
    for z in range(1, 101):
        divz = (z % 7)
        if divz == div7:
            list3.append(z)

    s1 = set(list1)
    s2 = set(list2)
    s3 = set(list3)
    set1 = s1.intersection(s2)
    final = set1.intersection(s3)
    answer = list(final)

    
    print("Your num was", *answer)
    print("Isn't that cool??")
    play_again = input("Would you like to play again? (Y/N)")






