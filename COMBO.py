from random import shuffle


def print_card(arr):
    a = ['Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет',
         'Дама', 'Король', 'Туз']
    b = ['Черви', 'Буби', 'Черви', 'Крести']
    print(a[arr[0]], b[arr[1]])
    return


NUMBER_OF_PLAYER = 4

# генерация колоды (1 число номинал, второе масть)
stuck = [[i // 4, i % 4] for i in range(52)]
shuffle(stuck)  # перемешивание колоды

# каждая комбинация дает некое количество очков
scores = [0 for i in range(NUMBER_OF_PLAYER)]


def hight_card(c_list: list):
    """старшая карта 100+x"""
    return max(c_list[0][0], c_list[1][0]) + 100


# паралельно провдим его и для карт на столе, чтобы убрать лишние комбинации

def same(c_list: list):
    '''пара,тройка,сет алгоритм 2.0(28)'''
    c_list:list = [i[0] for i in c_list].sort(reverse=True)
    c_list = [[key] * c_list.count(key) for key in set(c_list)]
    c_list.sort(key=lambda i: len(i), reverse=True)


    # ветка ифов для определения комбо (другого сбособа не придумал)

    if len(c_list[0]) == 4:
        end = c_list[0][0] + 800  # Каре(800)
    elif len(c_list[0]) == 3 and len(c_list[1]) == 2:
        end = c_list[0][0] * 1.3 + c_list[1][0] + 700  # фуллхаус(700)
    elif len(c_list[0]) == 3:
        end = c_list[0][0] + 400  # трипс(400)
    elif len(c_list[0]) == 2 and len(c_list[1]) == 2:
        end = c_list[0][0] * 1.3 + c_list[1][0] + 300  # 2 пары или +170р(300)
    elif len(c_list[0]) == 2 and len(c_list[1]) == 1:
        end = c_list[0][0] + 200  # (шм)пара (200)
    else:
        end = 0
    # сука андрей ты мне до сих пор 90р торчишь
    return end


def in_row(c_list: list):
    '''стрит стритфлеш, флеш и роял флеш(нет блять,клеш рояль)'''

    c_list.sort(key=lambda a: a[0], reverse=True)

    if count == 5:
        if list[0][0] == 12 and list[-1][0] == 0:
            pre.append(list[0][0])

        suit = pre[0][1]
        stritflash = True
        for i in pre:
            if i[1] != suit:
                stritflash = False

        if stritflash and pre[0][0] == 12:
            end = 1000  # как получишь, позвони
        elif stritflash:
            end = pre[0][0] + 900
        else:
            end = pre[0][0] + 500


def flesh(list: list):
    '''Просто флеш'''
    end = 0
    list.sort(key=lambda i: i[1], reverse=True)
    pre = []
    count = 0
    for i in range(1, len(list)):
        if count == 4:
            list.append(list[i])
            break
        elif list[i - 1][1] == list[i][1]:
            count += 1
            pre.append(list[i - 1])
        else:

            pre.clear()
            count = 0
    if count == 4:
        end = 600 + pre[0][0]
    return end


combo = [hight_card, same, in_row, flesh]
table = desk[-1]

# print_array(desk[:-1])
for hand in range(len(desk) - 1):  # применяем все функции ко всем рукам()
    for func in combo:
        if func != 'hight_card':  # хотел сделать через декоратры? А ебись оно в рот!
            t = desk[hand].copy()
            t.extend(table)
            scores[hand] = func(t)
        else:
            t = desk[hand].copy()
            scores[hand] = func(t)

print(scores)

# илья, ещё раз такую хуйню напишешь и все узнают что ты на бабанова по ночам дрочишь
# ветка шпака

# TODO: Нужно ли дать Шпаку по жопе? пасаси
