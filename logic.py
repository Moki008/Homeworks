import random

def play_round(min_number, max_number, capital):
    if capital <= 0:
        print("У вас нет денег для ставки.")
        return capital


    bet = int(input(f"Сделайте ставку (у вас {capital} сомов): "))
    if bet > capital:
        print("Ставка не может быть больше вашего капитала.")




    guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))


    secret_number = random.randint(min_number, max_number)
    print(f"Загаданное число: {secret_number}")

    if guess == secret_number:
        print(f"Поздравляем! Вы угадали число и удвоили свою ставку.")
        capital += bet
    else:
        print(f"Вы не угадали. Вы теряете ставку.")
        capital -= bet

    return capital
