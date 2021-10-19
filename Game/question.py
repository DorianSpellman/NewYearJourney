import random

class QA:
    def __init__(self, que, ans, explanation):
        self.que = que
        self.ans = ans
        self.explanation = explanation # объяснение

questions = [
"Диван, \n шкаф, \n лампа, \n стул\n",
"Волк, \n лиса, \n медведь, \n кот\n",
"Лето, \n утро, \n зима, \n весна\n",
"Дельфин, \n лягушка, \n акула, \n кит\n",
"Сом, \n щука, \n жук, \n окунь\n",
"Самолёт, \n машина, \n воробей, \n муха\n",
"Грузовик, \n велосипед, \n скутер, \n машина\n",
"Телефон, \n блокнот, \n компьютер, \n ноутбук\n",
"Квадрат, \n круг, \n прямоугольник, \n ромб\n",
"Метр, \n килограмм, \n сантиметр, \n километр\n",
"Лиса, \n подушка, \n перо, \n игрушка\n",
"Красноярск, \n Москва, \n Россия, \n Санкт-Петербург\n",
"Свеча, \n Солнце, \n лампочка, \n фонарик\n",
"Ноябрь, \n сентябрь, \n октябрь, \n декабрь\n",
"Май, \n июнь, \n апрель, \n март\n",
"17, \n 10, \n 5, \n 24\n",
"Корова, \n корабль, \n коробка, \n страус\n",
"Берёза, \n кедр, \n шиповник, \n ива\n",
"Медведь, \n иса, \n волк, \n слон\n",
"Ромашка, \n лилия, \n малина, \n пион\n"
]

que_ans = [
    QA(questions[0],["лампа", "третье", "3"], 'Лампа может освещать комнату, а другие предметы – нет'),
    QA(questions[1],['кот', 'четвертое', '4'],'Кот — домашнее животное, остальные из группы — дикие животные' ),
    QA(questions[2],['утро', 'второе', '2'], 'Утро — время суток, остальные слова обозначают времена года'),
    QA(questions[3],['лягушка', 'второе', '2'], 'Лягушка  живёт в небольших водоёмах: озёрах, прудах, болотах. Остальные животные обитают в солёных морях и океанах'),
    QA(questions[4],['жук', 'третье', '3'], 'Жук – насекомое, остальные животные – рыбы'),
    QA(questions[5],['машина', 'второе', '2'], 'Лишняя – машина, она не умеет летать'),
    QA(questions[6],['велосипед', 'второе', '2'],'Велосипед. Все транспортные средства из этого ряда работают на топливе, кроме велосипеда' ),
    QA(questions[7],['блокнот', 'второе', '2'],'Лишнее – блокнот. Все остальные предметы – техника'),
    QA(questions[8],['круг', 'второе', '2'], 'Лишний – круг. У остальных фигур есть углы'),
    QA(questions[9],['килограмм', 'второе', '2'], 'Лишнее – килограмм. В килограммах измеряется масса предмета, а в метрах, сантиметрах и километрах – длина'),
    QA(questions[10],['лиса', 'первое', '1'], 'Лиса. Всё остальное – предметы неживой природы'),
    QA(questions[11],['россия', 'третье', '3'], 'Россия – это страна. Всё остальное – её города'),
    QA(questions[12],['солнце', 'второе', '2'], 'Лишнее – Солнце, это звезда, которая освещает нашу Землю. Всё остальное – предметы, созданные человеком'),
    QA(questions[13],['декабрь', 'четвертый', '4'], 'Декабрь – зимний месяц. Все остальные месяцы соответствуют осени'),
    QA(questions[14],['июнь', 'второе', '2'], 'Июнь – летний месяц, все остальные – весенние'),
    QA(questions[15],['пять', 'третье', '3'], '5 – однозначное число, остальные числа состоят из двух цифр – их называют двузначными'),
    QA(questions[16],['страус', 'четвертое', '4'], 'Страус – начинается на букву «С», все остальные на букву «К»'),
    QA(questions[17],['шиповник', 'третье', '3'], 'Шиповник – кустарник небольшой высоты. Остальные слова означают породы деревьев'),
    QA(questions[18],['слон', 'четвертое', '4'], 'Лишний здесь – слон. Он не живёт в лесу, в отличие от других зверей'),
    QA(questions[19],['малина', 'третье', '3'], 'Лишнее – малина, это кустарник. Остальные из группы – название цветов')
]

random.shuffle(que_ans) # перетасовывает вопросы

# def game(que_ans):
#     for QA in que_ans:
#         a = input(QA.que)
#         # if a == "стоп" or a == "отмена" or a == "завершить" or a == "заверши игру":
#         #     Transition('900', ["стоп", "отмена", "завершить", "заверши игру"])
#         if a == QA.ans[0] or a == QA.ans[1] or a == QA.ans[2]:
#             print('Верно! ' + str(QA.explanation))
#         else:
#             print("Неверно! " + str(QA.explanation))

# game(que_ans)



        