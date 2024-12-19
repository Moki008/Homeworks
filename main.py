import logic


capital = int(input("Enter Capital: "))
def main(capital):

    min_num = int(input("Please enter min number: "))

    max_num = int(input("Please enter max number: "))

    new_capital = logic.play_round(min_num, max_num, capital)
    print(f'Ваш новый капитал {new_capital}')
    return new_capital


while capital != 0:
    capital = main(capital)




