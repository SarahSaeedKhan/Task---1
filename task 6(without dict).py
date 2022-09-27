## without dictionary cricket match game

import random


def playgame():
    choice = int(input('enter choice, 1:bat, 0:ball'))
    if choice == 1:
        bat_first()
    elif choice == 0:
        ball_first()
    else:
        print('you entered invalid choice,try again')
        playgame()


def bat_first():
    print('user will bat first')
    score = 0
    while True:

        user_bat = int(input('enter the run between 1-6,except 5 you will disqualified'))
        comp_ball = random.randint(1, 6)

        if user_bat == 5 and user_bat > 6:
            print('you are disqualified')
            playgame()

        print('comp_ball', comp_ball)
        score = score + user_bat

        if comp_ball == user_bat:
            print('you are out')
            print('your score is:', score)
            break

    print('now comp will bat')
    print('comp needs ', score + 1, 'to win')
    comp_score = 0

    while True:
        comp_bat = random.randint(1, 6)
        user_ball = int(input('enter the ball'))
        if comp_bat == 5 and comp_bat > 6:
            print('you are disqualified')
            playgame()
        print('comp scored', comp_bat)
        comp_score = comp_score + comp_bat
        if comp_bat == user_ball:
            print('comp is out')
            if comp_score > score:
                print('comp win')
                break
            elif comp_score == score:
                print('draw match')
                break
            else:
                print('comp loose')
                break


def ball_first():
    print('comp will start the batting')
    comp_score = 0
    score_list = [1, 2, 3, 4, 5]
    while True:

        comp_runs_f = random.choice(score_list)
        user_ball_f = int(input('enter the ball 1-6,except 5'))
        if user_ball_f == 5:
            print('invalid number')
            playgame()
        print('comp batting', comp_runs_f)
        comp_score = comp_score + comp_runs_f

        if user_ball_f == comp_runs_f:
            print('comp is out')
            print('comp score', comp_score)
            break
    print('now user will chase the target')
    user_score = 0
    while True:
        comp_ball_s = random.choice(score_list)
        user_bat_s = int(input('enter the run 1-6,except 5'))
        if user_bat_s == 5:
            print('invalid number')
            playgame()
        print('comp ball', comp_ball_s)
        user_score = user_score + user_bat_s
        if comp_score < user_score:
            print('user win,the score is :', user_score)
        if comp_ball_s == user_bat_s:
            print('you are out', user_score)
            if comp_score > user_score:
                print('comp win')
                break
            else:
                print('tie match')
                break


playgame()
