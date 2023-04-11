# Initiating the program
print("Do you want to use this calculator program? [y/n]")
answer = input()

# Looping the calculator
while answer.casefold() == "y":
    Eqn = input("Give input: ")
    Eqn_0 = list(Eqn.split("**"))
    Eqn_1 = list(Eqn.split("/"))
    Eqn_2 = list(Eqn.split("*"))
    Eqn_3 = list(Eqn.split("+"))
    Eqn_4 = list(Eqn.split("-"))

    # Defining the calculator function
    def calculator(_):
        # For Exponential Calculations
        if len(Eqn_0) == 2:
            result = float(Eqn_0[0])**float(Eqn_0[1])
        # For Dividing
        elif len(Eqn_1) == 2:
            result = float(Eqn_1[0])/float(Eqn_1[1])
        # For Multiplying
        elif len(Eqn_2) == 2:
            result = float(Eqn_2[0])*float(Eqn_2[1])
        # For Adding
        elif len(Eqn_3) == 2:
            result = float(Eqn_3[0])+float(Eqn_3[1])
        # For Subtracting
        elif len(Eqn_4) == 2:
            result = float(Eqn_4[0])-float(Eqn_4[1])
        # For preventing crashes
        elif len(Eqn_0) > 2 or len(Eqn_1) > 2 or len(Eqn_2) > 2 or len(Eqn_3) > 2 or len(Eqn_4) > 2:
            result = "This program is not yes supported with inputs over 2 terms long"
        # For things that can not be calculated
        else:
            # For Single term inputs
            if Eqn.isnumeric():
                result = Eqn
            # For non-numeric inputs
            else:
                result = "Please use a valid input............"
        return result

    # Printing out the result
    print(calculator(Eqn))
    # Asking if they want to continue using this program
    print("Do you want to continue using this calculator? [y/n]")
    answer = input()

# If the provided answer is not a proper input
if answer.casefold() != "n":
    print("Please use a valid input............")

# If the user doesn't want to use the program anymore
else:
    print("Thanks for using my Program ^_^")
