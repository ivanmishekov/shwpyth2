# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть. 
# С клавиатуры вводятся число монет и сами монеты построчно.
# Пример:
# Ввод: 1 1 1 1 0 0 -> 2

coins = 0
coins_list = []
numb_coin = 1
coin_zero = []
coin_one = []

while coins <= 0:
    coins = int(input('Введите кол-во монет: '))
else:
    while len(coins_list) != coins:
        coin = int(input(f'Введите сторону монетки{numb_coin} цифрой 0(решка) или 1(орёл): '))
        if coin == 1 or coin == 0:
            coins_list.append(coin)
            numb_coin += 1
    for x in coins_list:
        if x == 0:
            coin_zero.append(x)
        if x == 1:
            coin_one.append(x)
    if len(coin_zero) > len(coin_one):
        print(len(coin_one))
    elif len(coin_zero) < len(coin_one):
        print(len(coin_zero))
    else:
        print(len(coin_zero))