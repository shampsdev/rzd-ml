import decimal

_label2id = {
    "отказ": 0,
    "отмена": 1,
    "подтверждение": 2,
    "начать осаживание": 3,
    "осадить на (количество) вагон": 4,
    "продолжаем осаживание": 5,
    "зарядка тормозной магистрали": 6,
    "вышел из межвагонного пространства": 7,
    "продолжаем роспуск": 8,
    "растянуть автосцепки": 9,
    "протянуть на (количество) вагон": 10,
    "отцепка": 11,
    "назад на башмак": 12,
    "захожу в межвагонное,пространство": 13,
    "остановка": 14,
    "вперед на башмак": 15,
    "сжать автосцепки": 16,
    "назад с башмака": 17,
    "тише": 18,
    "вперед с башмака": 19,
    "прекратить зарядку тормозной магистрали": 20,
    "тормозить": 21,
    "отпустить": 22,
}

_id2label = {
    0: "отказ",
    1: "отмена",
    2: "подтверждение",
    3: "начать осаживание",
    4: "осадить на (количество) вагон",
    5: "продолжаем осаживание",
    6: "зарядка тормозной магистрали",
    7: "вышел из межвагонного пространства",
    8: "продолжаем роспуск",
    9: "растянуть автосцепки",
    10: "протянуть на (количество) вагон",
    11: "отцепка",
    12: "назад на башмак",
    13: "захожу в межвагонное,пространство",
    14: "остановка",
    15: "вперед на башмак",
    16: "сжать автосцепки",
    17: "назад с башмака",
    18: "тише",
    19: "вперед с башмака",
    20: "прекратить зарядку тормозной магистрали",
    21: "тормозить",
    22: "отпустить",
}


def label2id(label: str) -> int:
    global _label2id
    return _label2id[label]


def id2label(id: int) -> str:
    global _id2label
    return _id2label[id]


def labels() -> list[str]:
    global _label2id
    return list(_label2id.keys())


def parse_label(id: int, attr: int) -> str:
    label_str = id2label(id)
    if "(количество) вагон" in label_str:
        label_str = label_str.replace(
            "(количество) вагон", num2text(attr, (("вагон", "вагона", "вагонов"), "m"))
        )

    return label_str


units = (
    "ноль",
    ("один", "одна"),
    ("два", "две"),
    "три",
    "четыре",
    "пять",
    "шесть",
    "семь",
    "восемь",
    "девять",
)

teens = (
    "десять",
    "одиннадцать",
    "двенадцать",
    "тринадцать",
    "четырнадцать",
    "пятнадцать",
    "шестнадцать",
    "семнадцать",
    "восемнадцать",
    "девятнадцать",
)

tens = (
    teens,
    "двадцать",
    "тридцать",
    "сорок",
    "пятьдесят",
    "шестьдесят",
    "семьдесят",
    "восемьдесят",
    "девяносто",
)

hundreds = (
    "сто",
    "двести",
    "триста",
    "четыреста",
    "пятьсот",
    "шестьсот",
    "семьсот",
    "восемьсот",
    "девятьсот",
)

orders = (  # plural forms and gender
    # ((u'', u'', u''), 'm'), # ((u'рубль', u'рубля', u'рублей'), 'm'), # ((u'копейка', u'копейки', u'копеек'), 'f')
    (("тысяча", "тысячи", "тысяч"), "f"),
    (("миллион", "миллиона", "миллионов"), "m"),
    (("миллиард", "миллиарда", "миллиардов"), "m"),
)

minus = "минус"


def thousand(rest, sex):
    """Converts numbers from 19 to 999"""
    prev = 0
    plural = 2
    name = []
    use_teens = rest % 100 >= 10 and rest % 100 <= 19
    if not use_teens:
        data = ((units, 10), (tens, 100), (hundreds, 1000))
    else:
        data = ((teens, 10), (hundreds, 1000))
    for names, x in data:
        cur = int(((rest - prev) % x) * 10 / x)
        prev = rest % x
        if x == 10 and use_teens:
            plural = 2
            name.append(teens[cur])
        elif cur == 0:
            continue
        elif x == 10:
            name_ = names[cur]
            if isinstance(name_, tuple):
                name_ = name_[0 if sex == "m" else 1]
            name.append(name_)
            if cur >= 2 and cur <= 4:
                plural = 1
            elif cur == 1:
                plural = 0
            else:
                plural = 2
        else:
            name.append(names[cur - 1])
    return plural, name


def num2text(num, main_units=(("", "", ""), "m")):
    """
    http://ru.wikipedia.org/wiki/Gettext#.D0.9C.D0.BD.D0.BE.D0.B6.D0.B5.D1.81.\
    D1.82.D0.B2.D0.B5.D0.BD.D0.BD.D1.8B.D0.B5_.D1.87.D0.B8.D1.81.D0.BB.D0.B0_2
    """
    _orders = (main_units,) + orders
    if num == 0:
        return " ".join((units[0], _orders[0][0][2])).strip()  # ноль

    rest = abs(num)
    ord = 0
    name = []
    while rest > 0:
        plural, nme = thousand(rest % 1000, _orders[ord][1])
        if nme or ord == 0:
            name.append(_orders[ord][0][plural])
        name += nme
        rest = int(rest / 1000)
        ord += 1
    if num < 0:
        name.append(minus)
    name.reverse()
    return " ".join(name).strip()


def decimal2text(
    value, places=2, int_units=(("", "", ""), "m"), exp_units=(("", "", ""), "m")
):
    value = decimal.Decimal(value)
    q = decimal.Decimal(10) ** -places

    integral, exp = str(value.quantize(q)).split(".")
    return "{} {}".format(
        num2text(int(integral), int_units), num2text(int(exp), exp_units)
    )


if __name__ == "__main__":
    print(parse_label(4, 3))
