import random


def user_choice():
    print('-------------------start Cricket Match-------------')
    choice = int(input('enter 1 to bat 0 to ball'))
    if choice == 1:
        bat_first()
    elif choice == 0:
        ball_first()
    else:
        print('invalid choice')
        user_choice()


def bat_first():

    score_lists = [1, 2, 3, 4, 6]
    user_team = ['play_1', ' play_2', 'play_3']
    team_score = 0
    team_result = {}
    print('--------user will bat first---------')
    for p in range(len(user_team)):
        while True:
            runs = int(input('enter the number'))
            comp_ball = random.choice(score_lists)
            if runs == comp_ball:
                print("Your Guess: ", runs, ",Computer Guess: ", comp_ball, 'player', user_team[p])
                print("You are Out. Your Total Runs= ", team_score, "\n")
                break
            elif runs not in score_lists:
                print("ALERT!!\n")
                break
            else:
                team_score = team_score + runs
                print("Your Guess: ", runs, ",Computer Guess: ", comp_ball, 'player is:', user_team[p])
                print("Your runs Now are: ", team_score, "\n")

    team_result['team_players'] = user_team
    team_result['team_score'] = team_score
    print(team_result)
    print('now comp team will chase the score!!')

    comp_team = ['p1', 'p2', 'p3']
    comp_score = 0
    comp_result = {}
    for p in range(len(comp_team)):
        while True:
            user_ball = int(input("Enter Runs for Your Ball Turn: "))
            comp_bat = random.choice(score_lists)

            if comp_bat == user_ball:
                print("Computer Guess: ", comp_bat, "Your Guess: ", user_ball, 'comp player', comp_team[p])
                print("The Computer is Out. Computer Runs= ", comp_score, "\n")
                break
            elif user_ball not in score_lists:
                print("ALERT!!\n")
                break
            else:
                comp_score = comp_score + comp_bat
                print("Computer Guess: ", comp_bat, "Your Guess: ", user_ball)
                print("Computer Runs: ", comp_score, "\n")

                if comp_score > team_score:
                    break

    comp_result['comp_team'] = comp_team
    comp_result['comp_score'] = comp_score
    print(comp_result)

    print('-----------------------Result--------------------')
    if comp_score < team_score:
        print('the team won ', team_result)
    elif comp_score == team_score:
        print('its tie ', team_score == comp_score)
    else:
        print('comp win', comp_result)


def ball_first():
    print('-----------user ball first------------------')
    score_lists = [1, 2, 3, 4, 6]
    comp_team = ['p1', 'p2', 'p3']
    comp_score = 0
    comp_result = {}
    for p in range(len(comp_team)):
        while True:
            user_ball = int(input("Enter num for Your Ball Turn: "))
            comp_bat = random.choice(score_lists)

            if comp_bat == user_ball:
                print("Computer Guess: ", comp_bat, "Your Guess: ", user_ball, 'comp player', comp_team[p])
                print("The Computer is Out. Computer Runs= ", comp_score, "\n")
                break
            elif user_ball not in score_lists:
                print("ALERT!!\n")
                break
            else:
                comp_score = comp_score + comp_bat
                print("Computer Guess: ", comp_bat, "Your Guess: ", user_ball)
                print("Computer Runs: ", comp_score, "\n")

    comp_result['comp_team'] = comp_team
    comp_result['comp_score'] = comp_score
    print(comp_result)

    user_team = ['play_1', ' play_2', 'play_3']
    team_score = 0
    team_result = {}
    print('--------user will bat Now---------')
    for p in range(len(user_team)):
        while True:
            runs = int(input('enter the number'))
            comp_ball = random.choice(score_lists)
            if runs == comp_ball:
                print("Your Guess: ", runs, ",Computer Guess: ", comp_ball, 'player', user_team[p])
                print("You are Out. Your Total Runs= ", team_score, "\n")
                break
            elif runs not in score_lists:
                print("ALERT!!\n")
                break
            else:
                team_score = team_score + runs
                print("Your Guess: ", runs, ",Computer Guess: ", comp_ball, 'player is:', user_team[p])
                print("Your runs Now are: ", team_score, "\n")
                if team_score > comp_score:
                    break

    team_result['team_players'] = user_team
    team_result['team_score'] = team_score
    print(team_result)

    print('-----------------------Result--------------------')
    if comp_score < team_score:
        print('the team won ', team_result)
    elif comp_score == team_score:
        print('its tie ', team_score == comp_score)
    else:
        print('comp win', comp_result)


user_choice()

