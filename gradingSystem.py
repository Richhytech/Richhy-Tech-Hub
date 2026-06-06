
try:
    # Ask the user to enter their score and convert it to a number
    score_gotten=int(input("Enter your score: "))

    if score_gotten == 100:
        print("Perfect score!") # Special case for full marks
    elif score_gotten >=70:
        print("Grade A")
    elif score_gotten >=60:
        print("Grade B")
    elif score_gotten >= 50:
        print("Grade C")
    elif score_gotten >= 40:
        print("Grade D")
    elif score_gotten >= 30:
        print("Grade E")
    else:
        print("Grade F") # returns grade as "f" if the score_gotten is below 20
# Runs if the user types letters or symbols instead of a number
except ValueError:
    print("invalid input")
