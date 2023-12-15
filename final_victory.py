


def game():
    from victory import victory_game
    print('Приветсвую! Ты можешь поиграть со мной в викторину!')
    player_name = input('Как тебя зовут?')

    print('Отлично!')
    start = input('Так как тебя зовут?')

    if  start == 'да':
        victory_game()
    elif start == 'нет':
        print('Готовься тогда')
    else:
        print('Я тебя не понимаю, давай говорить по русски')