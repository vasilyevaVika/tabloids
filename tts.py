name = {"Вика": 18, "Илья": 20,"Даша": 19, "Лена": 21, "Игорь": 48, "Саша": 15}
anim = {"Вика": "енот", "Илья": "собака","Даша": "кошка", "Лена": "ласка", "Игорь": "петух", "Саша": "еж"}


while True:
    text = input("введите имя ")
    text1 = input("введите имя ")
    print("возраст:", name[text], "лет")
    print("дома живет:", anim[text1])
