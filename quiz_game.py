# Initial Welcome Message
wlcm_mssg = "Hello and Welcome to The Capstone Quiz Game! \n\nPick: A, B, C, or D for the answer you think is right! \n "
print(wlcm_mssg)

# Questions and answers for EASY
e_ques = [
    {
        "question": "How many faces does a sphere have?\n\n A.Two \n B.Three \n C.One \n D.Five\n\n",
        "answer": "C"
    },
    {
        "question": "What is the capital of France?\n\n A.Paris \n B.London \n C.Rome \n D.Madrid\n\n",
        "answer": "A"
    },
    {
        "question": "Which planet is known as the 'red planet'?\n\n A.Venus \n B.Mars \n C.Jupiter \n D.Saturn\n\n",
        "answer": "B"
    },
    {
        "question": "What is the tallest mountain in the world?\n\n A.Mount Kilimanjaro \n B.Mount Fuji \n C.K2 \n D.Mount Everest\n\n",
        "answer": "D"
    },
    {
        "question": "What animal has black and white stripes?\n\n A.Giraffe \n B.Zebra \n C.Lion \n D.Elephant\n\n",
        "answer": "B"
    },
    {
        "question": "What is the main language spoken in Brazil?\n\n A.Spanish \n B.Portuguese \n C.French \n D.English\n\n",
        "answer": "B"
    },
]

# Questions and answers for MEDIUM
m_ques=[{
        "question": "What is the currency used in Denmark?\n\n A.USD \n B.GBP \n C.DKK \n D.EUR\n\n",
        "answer": "C"
    },
    {
        "question": "What is the name of a newly hatched butterfly?\n\n A.Moth \n B.Chrysalis \n C.Butter \n D.Caterpillar\n\n",
        "answer": "D"
    },
    {
        "question": "What is the main component of the sun?\n\n A.Liquid lava\n B.Gas \n C.Molten iron \n D.Rock\n\n",
        "answer": "B"
    },
    {
        "question": "Which animal runs the fastest?\n\n A.Tiger \n B.Cheetah \n C.Leopard \n D.Lion\n\n",
        "answer": "B"
    },
    {
        "question": "What is the most points you can score with a single throw in darts?\n\n A.20 \n B.40 \n C.60\n D.80\n\n",
        "answer": "C"
    },
    {
        "question": "What does the term 'SOS' stand for?\n\n A.Save Our Sheep \n B.Save Our Sky \n C.Save Our Self \n D.Save Our Souls\n\n",
        "answer": "D"
    },
    {
        "question": "What does the term 'SOS' stand for?\n\n A.Save Our Sheep \n B.Save Our Sky \n C.Save Our Self \n D.Save Our Souls\n\n",
        "answer": "D"
    },
    {
        "question": "Which company published the Mario game?\n\n A.Xbox \n B.SEGA \n C.Electronic Arts \n D.Nintendo\n\n",
        "answer": "D"
    },
    {
        "question": "Who was the second astronaut to step on the moon?\n\n A.Yuri Gagarian \n B.James Irwin \n C.Buzz Aldrin \n D.Alan Bean\n\n",
        "answer": "C"
    },]

# Questions and answers for HARD
h_ques = [
    {
        "question": "How many faces does a sphere have?\n\n A.Two \n B.Three \n C.One \n D.Five\n\n",
        "answer": "C"
    },
    {
        "question": "What is the capital of France?\n\n A.Paris \n B.London \n C.Rome \n D.Madrid\n\n",
        "answer": "A"
    },
    {
        "question": "Which planet is known as the 'red planet'?\n\n A.Venus \n B.Mars \n C.Jupiter \n D.Saturn\n\n",
        "answer": "B"
    },
    {
        "question": "What is the tallest mountain in the world?\n\n A.Mount Kilimanjaro \n B.Mount Fuji \n C.K2 \n D.Mount Everest\n\n",
        "answer": "D"
    },
    {
        "question": "What animal has black and white stripes?\n\n A.Giraffe \n B.Zebra \n C.Lion \n D.Elephant\n\n",
        "answer": "B"
    },
    {
        "question": "What is the main language spoken in Brazil?\n\n A.Spanish \n B.Portuguese \n C.French \n D.English\n\n",
        "answer": "B"
    },
  {
        "question": "How many faces does a sphere have?\n\n A.Two \n B.Three \n C.One \n D.Five\n\n",
        "answer": "C"
    },
    {
        "question": "What is the capital of France?\n\n A.Paris \n B.London \n C.Rome \n D.Madrid\n\n",
        "answer": "A"
    },
    {
        "question": "Which planet is known as the 'red planet'?\n\n A.Venus \n B.Mars \n C.Jupiter \n D.Saturn\n\n",
        "answer": "B"
    },
    {
        "question": "What is the tallest mountain in the world?\n\n A.Mount Kilimanjaro \n B.Mount Fuji \n C.K2 \n D.Mount Everest\n\n",
        "answer": "D"
    },
    {
        "question": "What animal has black and white stripes?\n\n A.Giraffe \n B.Zebra \n C.Lion \n D.Elephant\n\n",
        "answer": "B"
    },
    {
        "question": "What is the main language spoken in Brazil?\n\n A.Spanish \n B.Portuguese \n C.French \n D.English\n\n",
        "answer": "B"
    },
]

# Variables for calculating EASY score
earn_per_R_ans = 50

# Variables for calculating MEDIUM score
earn_per_M_ans = 100

# Variables for calculating HARD score
earn_per_H_ans = 150


while True:
    difficulty = input("Choose your difficulty: EASY, MEDIUM, or HARD\n\n")
    if difficulty.lower() == "EASY".lower():
        i_d = input("Please type in your name for the leaderboard: \n\n")
        r_ans = 0

        for i in range(5):
            ans = input("\n" + e_ques[i] ["question"])
            if ans.lower() == str(e_ques[i]["answer"]).lower():
                print("\n" + "Well Done! That is correct!\n")
                r_ans += 1
            else:
                print("\n" + "Ohh :( Unfortunately, that is incorrect!\n")

        print(f"You scored {r_ans * earn_per_R_ans} out of a potential 300!\n\nWill you beat your score next time?")
    

        # Create fake EASY high scores so the board isn't empty and has a goal to beat on replay
        e_highscores = [
            {"score": 250, "name": "Nathan"},
            {"score": 200, "name": "Khalil"},
            {"score": 150, "name": "Trust"},
            {"score": 100, "name": "Nimo"},
            {"score": 50, "name": "Adam"}
        ]

        def highScSrt(e_highscore):
            return e_highscore["score"]

        e_highscores = sorted(e_highscores, key=highScSrt)

        # Function to Keep EASY high scores updated
        if r_ans > e_highscores[0]["score"]:
            e_highscores[0]["name"] = i_d
            e_highscores[0]["score"] = r_ans
            e_highscores = sorted(e_highscores, key=highScSrt)

        print(f"Leaderboard:\n1st Place = {e_highscores[-1]['name']}: {e_highscores[-1]['score']}")
        print(f"2nd Place = {e_highscores[-2]['name']}: {e_highscores[-2]['score']}")
        print(f"3rd Place = {e_highscores[-3]['name']}: {e_highscores[-3]['score']}")
        print(f"4th Place = {e_highscores[-4]['name']}: {e_highscores[-4]['score']}")
        print(f"5th Place = {e_highscores[-5]['name']}: {e_highscores[-5]['score']}")

        if r_ans > e_highscores[0]["score"]:
            print("Congratulations! Thats a new record!")
        else:
            print("Cheers for playing!")

        play_again = input("Do you want to have another go? Type, Yes or No: ")
        if play_again.lower() != "Yes".lower():
            break

    elif difficulty.lower() == "MEDIUM".lower():
        i_d = input("Please type in your name for the leaderboard: \n\n")
        r_ans = 0

        for i in range(5):
            ans = input("\n" + m_ques[i]["question"])
            if ans.lower() == str(m_ques[i]["answer"]).lower():
                print("\n" + "Well Done! That is correct!\n")
                r_ans += 1
            else:
                print("\n" + "Ohh :( Unfortunately, that is incorrect!\n")

        print(f"You scored {r_ans * earn_per_M_ans} out of a potential 900!\n\nWill you beat your score next time?")
    

        # Create fake MEDIUM high scores so the board isn't empty and has a goal to beat on replay
        m_highscores = [
            {"score": 800, "name": "Nathan"},
            {"score": 600, "name": "Khalil"},
            {"score": 500, "name": "Trust"},
            {"score": 300, "name": "Nimo"},
            {"score": 200, "name": "Adam"}
        ]

        def highScSrt(m_highscore):
            return m_highscore["score"]

        m_highscores = sorted(m_highscores, key=highScSrt)

        # Function to Keep MEDIUM high scores updated
        if r_ans > m_highscores[0]["score"]:
            m_highscores[0]["name"] = i_d
            m_highscores[0]["score"] = r_ans
            m_highscores = sorted(m_highscores, key=highScSrt)

        print(f"Leaderboard:\n1st Place = {m_highscores[-1]['name']}: {m_highscores[-1]['score']}")
        print(f"2nd Place = {m_highscores[-2]['name']}: {m_highscores[-2]['score']}")
        print(f"3rd Place = {m_highscores[-3]['name']}: {m_highscores[-3]['score']}")
        print(f"4th Place = {m_highscores[-4]['name']}: {m_highscores[-4]['score']}")
        print(f"5th Place = {m_highscores[-5]['name']}: {m_highscores[-5]['score']}")

        if r_ans > m_highscores[0]["score"]:
            print("Congratulations! Thats a new record!")
        else:
            print("Cheers for playing!")

        play_again = input("Do you want to have another go? Type, Yes or No: ")
        if play_again.lower() != "Yes".lower():
            break

    elif difficulty.lower() == "HARD".lower():
        i_d = input("Please type in your name for the leaderboard: \n\n")
        r_ans = 0

        for i in range(5):
            ans = input("\n" + h_ques[i]["question"])
            if ans.lower() == str(h_ques[i]["answer"]).lower():
                print("\n" + "Well Done! That is correct!\n")
                r_ans += 1
            else:
                print("\n" + "Ohh :( Unfortunately, that is incorrect!\n")

        print(f"You scored {r_ans * earn_per_H_ans} out of a potential 1800!\n\nWill you beat your score next time?")
    

        # Create fake HARD high scores so the board isn't empty and has a goal to beat on replay
        h_highscores = [
            {"score": 1700, "name": "Nathan"},
            {"score": 1200, "name": "Khalil"},
            {"score": 900, "name": "Trust"},
            {"score": 600, "name": "Nimo"},
            {"score": 400, "name": "Adam"}
        ]

        def highScSrt(h_highscore):
            return h_highscore["score"]

        h_highscores = sorted(h_highscores, key=highScSrt)

        # Function to Keep HARD high scores updated
        if r_ans > h_highscores[0]["score"]:
            h_highscores[0]["name"] = i_d
            h_highscores[0]["score"] = r_ans
            h_highscores = sorted(h_highscores, key=highScSrt)

        print(f"Leaderboard:\n1st Place = {h_highscores[-1]['name']}: {h_highscores[-1]['score']}")
        print(f"2nd Place = {h_highscores[-2]['name']}: {h_highscores[-2]['score']}")
        print(f"3rd Place = {h_highscores[-3]['name']}: {h_highscores[-3]['score']}")
        print(f"4th Place = {h_highscores[-4]['name']}: {h_highscores[-4]['score']}")
        print(f"5th Place = {h_highscores[-5]['name']}: {h_highscores[-5]['score']}")

        if r_ans > h_highscores[0]["score"]:
            print("Congratulations! Thats a new record!")
        else:
            print("Cheers for playing!")

        play_again = input("Do you want to have another go? Type, Yes or No: ")
        if play_again.lower() != "Yes".lower():
            break

    else:
        print("Invalid difficulty level. Try again")
