from random import shuffle


def print_card(arr):
    a = ['Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет',
         'Дама', 'Король', 'Туз']
    b = ['Черви', 'Буби', 'Черви', 'Крести']
    print(a[arr[0]], b[arr[1]])



NUMBER_OF_PLAYER = 4

# генерация колоды (1 число номинал, второе масть)
stuck = [[i // 4, i % 4] for i in range(52)]
shuffle(stuck)  # перемешивание колоды

# каждая комбинация дает некое количество очков
scores = [0 for i in range(NUMBER_OF_PLAYER)]


def high_card(c_list: list):
    """старшая карта"""
    return max(c_list[0][0], c_list[1][0]) + 100


# noinspection PyUnresolvedReferences
def same(c_list: list):
    """пара,тройка,сет, флэш"""
    suits = [i[1] for i in c_list]
    suits = [[key] * suits.count(key) for key in set(suits)]
    c_list = [i[0] for i in c_list]
    c_list = [[key] * c_list.count(key) for key in set(c_list)].sort(key=len)
    c_list.sort(key=len)

    # ветка ифов для определения комбо (другого способа не придумал)

    if len(c_list[0]) == 4:
        points = c_list[0][0] + 800  # Каре(800)
    elif len(c_list[0]) == 3 and len(c_list[1]) == 2:
        points = c_list[0][0] * 1.3 + c_list[1][0] + 700  # фуллхаус(700)
    elif len(c_list[0]) == 3:
        points = c_list[0][0] + 400  # трипс(400)
    elif len(suits[0]) >= 5:
        points = max(filter(lambda x: x[1] == 2, c_list))[0] + 600 #флеш(600)
    elif len(c_list[0]) == 2 and len(c_list[1]) == 2:
        points = c_list[0][0] * 1.3 + c_list[1][0] + 300  # 2 пары(300)
    elif len(c_list[0]) == 2 and len(c_list[1]) == 1:
        points = c_list[0][0] + 200  # пара (200)
    else:
        points = 0

    return points


def in_row(c_list: list):
    """стрит стритфлеш, флеш и роял флеш(нет блять,клеш рояль)"""

    c_list.sort(reverse=True)
    pre = [c_list[0]]

    for i in range(len(c_list)):
        i = (i + 1) % len(c_list)
        if pre[-1][0] == c_list[i][0]:
            pre[-1].append(c_list[i][1])
        elif (pre[-1][0] == c_list[i][0] + 1) or (pre[-1][0] == c_list[i][0] - 12):
            pre.append(c_list[i])
        elif len(pre) < 5:
            pre = [c_list[i]]

    points = 0
    if len(c_list) >= 5:
        c_list = sorted(pre, key=lambda x: x[0] == 12)

        siuts = [i[1::] for i in pre]
        pre = [{*siuts[0]}]
        start = 0
        for i in range(1, len(siuts)):
            inresection = set(pre[-1]) & set(siuts[i])
            if inresection != set():
                pre.append(inresection)
            elif len(pre) < 5:
                pre = [{siuts[i]}]
                start = i
        if len(siuts) >= 5:
            points = c_list[start][0] + 900  # Стрит флеш(900)
            if c_list[start][0] == 8 and c_list[-1][0] == 12:  #роял флеш(1000)
                points = 1000
        else:
            points = c_list[start][0] + 500  # Стрит(500)
    return points
