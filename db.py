import pymongo
client = pymongo.MongoClient('localhost', 27017)
db = client['Skate_Canada']

#######
def add_fskater(s):
    print("Введите имя")
    name = input();
    print("Введите фамилию")
    surname = input()
    print("Введите страну")
    country = input()
    skater = {"name": name, "surname": surname, "country": country}

    m = 50
    while m:
        print("Если хотите добавить информацию, нажмите 1, иначе 0")
        m = int(input())
        if m == 1:
            print("Введите название параметра")
            key = input()
            print("Введите значение параметра")
            val = input()
            skater[key] = val
    if s == "l":
        db.Ladies.insert_one(skater)
    elif s=="m":
        db.Men.insert_one(skater)

def get_fskaters(s):
    if s == "l":
        count = db.Ladies.count_documents({})
        print("Количество " + str(count))
        for lady in db.Ladies.find():
            print(lady["name"] + " " + lady["surname"] + ", " + lady["country"])
    elif s=="m":
        count = db.Men.count_documents({})
        print("Количество " + str(count))
        for man in db.Men.find():
            print(man["name"] + " " + man["surname"] + ", " + man["country"])

def get_fskaters_detailed(s):
    if s == "l":
        count = db.Ladies.count_documents({})
        print("Количество " + str(count))
        for lady in db.Ladies.find():
            print(lady)
    elif s == "m":
        count = db.Men.count_documents({})
        print("Количество " + str(count))
        for man in db.Men.find():
            print(man)

def get_fskaters_by_country(country):
    count = db.Ladies.count_documents({"country": country}) + db.Men.count_documents({"country": country})
    print()
    print("Количество " + str(count))
    print("Девушки")
    for lady in db.Ladies.find({"country": country}):
        print(lady["name"] + " " + lady["surname"])
    print()
    print("Мужчины")
    for man in db.Men.find({"country": country}):
        print(man["name"] + " " + man["surname"])

#######
n = 50
while n:
    print();
    print("Для добавления девушки нажмите 1")
    print("Для добавления мужчины нажмите 2")
    print("Для просмотра всех девушек нажмите 3")
    print("Для просмотра всех мужчин нажмите 4")
    print("Для просмотра подробной инфомации о девушках нажмите 5")
    print("Для просмотра подробной инфомации о мужчинах нажмите 6")
    print("Для просмотра участников из конкретной страны нажмите 7")
    print("Для выхода нажмите 0")
    n = int(input())
    if n == 1:
        add_fskater("l")
    elif n == 2:
        add_fskater("m")
    elif n == 3:
        get_fskaters("l")
    elif n == 4:
        get_fskaters("m")
    elif n == 5:
        get_fskaters_detailed("l")
    elif n == 6:
        get_fskaters_detailed("m")
    elif n == 7:
        print("Введите название страны")
        country = input()
        get_fskaters_by_country(country)

client.close()




