from random import randint


def player_choose():
    p_choose = None
    while p_choose not in ('1', '2', '3'):
        p_choose = input()
        if p_choose in ('1', '2', '3'):
            continue
        print("You select bad option")
    p_choose = int(p_choose)
    return p_choose


def what_choose(to_show):
    # showing what computer and player choose and return it in text
    names = []
    for n in to_show:
        if n == 1:
            name = 'ROCK'
        elif n == 2:
            name = 'PAPER'
        else:
            name = 'SCISSORS'
        names.append(name)
    return names


def game(player, computer):
    global computer_point
    global player_point
    if computer - player == 0:
        text = "DRAW"
    elif computer - player == 1 or (computer == 3 and computer - player == -2):
        text = "Computer"
        computer_point += 1
    else:
        text = "Player"
        player_point += 1
    return text


while True:
    player_point = 0
    computer_point = 0
    print("1. Start new game\n2.Quit")
    response = input()
    if response == '1':
        round_number = int(input("To how many victories?\t"))
        while player_point < round_number and computer_point < round_number:
            print("1.Rock\n2.Paper\n3.Scissors")
            choose = player_choose()
            comp_choose = randint(1, 3)
            text_choose = what_choose([choose, comp_choose])
            round_winner = game(choose, comp_choose)
            print(f"Player {player_point}, : {computer_point} Computer\n {text_choose[0]} vs {text_choose[1]}\nThis "
                  f"round win: {round_winner}")
        if computer_point == round_number:
            print("You lost this game. Try again")
        else:
            print("You win this game. Congratulation")
    elif response == '2':
        break
    else:
        print("There's no such option")
