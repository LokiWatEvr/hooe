def victory_game():

    import random

    FAMOUS_PEOPLE = {'Александр Сергеевич пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                    'Сергей Александрович Есенин': '21.06.1962'}

    rounds = int(input('Сколько раз мы будем играть?:'))
    for i in range (rounds):
        name, date = random.choice(list(FAMOUS_PEOPLE.items()))
        answer = input(f'Когда родился {name}')
        if answer == date:
            print('Верно')
        else:
            print('Неверно')
    print('Пока')
