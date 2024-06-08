import random
while(True):
    user_choice=input("Lets start game/n choose a rock,paper or scissor : ")
    p=["rock","paper","scissor"]
    comp_choice=random.choice(p)
    print(f"your choose a {user_choice} and computer choose a {comp_choice}")
    if(user_choice==comp_choice):
        print("its a tie play again")
    elif(user_choice=="rock"):
        if(comp_choice=="paper"):
            print("computer wins because paper covers rock ")
        else:
            print("user wins because rock will hit scissor")
    elif(user_choice=="paper"):
        if(comp_choice=="rock"):
            print("user wins because paper covers rock ")
        else:
            print("computer wins because scissor will cut paper")
    elif(user_choice=="scissor"):
        if(comp_choice=="paper"):
            print("user wins because scissor will cut paper ")
        else:
            print("computer wins because rock will hit scissor")
    p=input("play again (y/n)")
    if p.lower()!="y":
        break




