"""
This is a Darts game programme.
"""
def greet_name (): #definitions are to reuse helpful code
    print (f"hello {name} and welcome to the darts game!")
    
def current_score1(): #definitions are to reuse helpful code
    print (f"your current score is {score1}")

def current_score2(): #definitions are to reuse helpful code
    print (f"your current score is {total2}")


def total_score(): #definitions are to reuse helpful code
    print (f"your total score is {totalscore}")

name = input ("Please enter your name to continue!")
greet_name()
while True: #while true loops help with error catching, making the code more secure
    try:
        score1=int (input("please enter your score for your first shot"))
        if score1 in range (0,61):
            break #A break ensures that when the user inputs the right format, the code can continue
    except ValueError: #value errors ensure that users are inputting the correct format
        print ("Please enter your score in a numerical format, thanks")
    else:
        print ("Hey! thats not a valid input, you're not trying to cheat are you?")


current_score1() #here we use a definition, which helped reduce unneccessary code repeating

while True:
    try:
        score2=int (input("Please enter your score for your second shot"))
        if score2 in range (0,61):
            break #A break ensures that when the user inputs the right format, the code can continue
    except ValueError: #value errors ensure that users are inputting the correct format
        print ("Please enter your score in a numerical format, thanks")
    else:
        print ("Hey! thats not a valid input, you're not trying to cheat are you?")
        



while True:
    try:
        score3 = int (input("Please enter your score for your final shot"))
        if score3 in range (0,61):
            break #A break ensures that when the user inputs the right format, the code can continue
    except ValueError:#value errors ensure that users are inputting the correct format
        print ("Please enter your score in a numerical format, thanks")
    else:
        print ("Hey! thats not a valid input, you're not trying to cheat are you?")
totalscore=score1+score2+score3#here we implement an equation string, which gives us our total
total_score() #here we use a definition, which helped reduce unneccessary code repeating


while True: #This while loop allows us to add different endings depending on how well the user performed
    if totalscore <60:
        print (f"Well {name}, looks like you need more practise")
        break #A break ensures that when the user inputs the right format, the code can continue

    elif totalscore <120:
        print (f"Not bad {name}, {totalscore} is a pretty good score")
        break #A break ensures that when the user inputs the right format, the code can continue

    else:
        print (f"Wow! thats an amazing score! good job {name}!")
        break #A break ensures that when the user inputs the right format, the code can continue
