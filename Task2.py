from random import randint
 
CANDIES = 100
MAX_STEP = 28
 
human = True
cur_candies = CANDIES
 
 
def get_ai_step():
    if cur_candies<=28:
        return cur_candies
    elif cur_candies>=30 and cur_candies<=57:
        return cur_candies-29
    elif cur_candies>=59 and cur_candies<=86:
        return cur_candies-58
    elif cur_candies>=88 and cur_candies<=115:
        return cur_candies-87
    else:
       return randint(1, min(MAX_STEP, cur_candies))
 ###Ему долго можно дописывать элементы разума, я дописал до 115, дальше суть та же
 
def get_human_step():
    while True:
        cnt = input('Введите количество конфет: ')
        if cnt.isdigit() and 1 <= int(cnt) <= min(MAX_STEP, cur_candies):
            return int(cnt)
        print('Введено некорректное значение')
 
 
while cur_candies:
    if human:
        cnt = get_human_step()
        cur_candies -= cnt
        print(f'Пользователь взял {cnt} конфет. Осталось {cur_candies}.')
    else:
        cnt =get_ai_step()
        cur_candies -= cnt
        print(f'Бот взял {cnt} конфет. Осталось {cur_candies}.')
    human = not human
 
if human:
    print('Победил БОТ')
else:
    print('Победил человек')