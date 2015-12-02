import random # For random accesing the question from dictionary
def qGame():
    q_dict = {
        # here will be our question and answere also.
        "What is OOP" : "Object Oriented Programming",
        "what is your name" : "lol",
        "What is POP" : "Procedure Oriented Programming",
        "Is there any snake named 'Python'": "Yes",
        "How many version of python have" : "two",
    }

    question = (random.choice(list(q_dict.keys())))
    answere = q_dict[question]
    playing = True
    while playing:
        score = 0      # here is your scorecard
        num = int(input("\nHow many question you want to face ? "))
        for n in range(1, num+1):
            print ("Question " + str(n))
            print (question, "?")
            user = input("Your Answere : ")
            if answere.lower() == user.lower():
                print ("Success !!")
                score += 1
            else:
                print ("Sorry !! Failed !!")
        # Now let's print final score.
        print ("Your Final Score : ", str(score))
        user1 = input("Q for exit. otherwise play again. -->  ")
        if user1.lower() == "q":
            playing = False
