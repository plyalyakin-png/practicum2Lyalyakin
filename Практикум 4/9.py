print("Собака короткошерстной породы?", end=" ")
answer_1 = input().strip().lower()
if answer_1 == "да":
    print("Рост собаки менее 50 см?", end=" ")
    answer_2 = input().strip().lower()
    if answer_2 == "да":
        print("У собаки короткий хвост?", end=" ")
        answer_3 = input().strip().lower()
        if answer_3 == "да":
            print("английский бульдог")
        else:
            print("У собаки длинные уши?", end=" ")
            answer_4 = input().strip().lower()
            if answer_4 == "да":
                print("гончая")
            else:
                print("У собаки короткое тело?", end=" ")
                answer_5 = input().strip().lower()
                if answer_5 == "да":
                    print("мопс")
                else:
                    print("чихуахуа")
    else:
        print("Собака весит более 50 кг?", end=" ")
        answer_6 = input().strip().lower()
        if answer_6 == "да":
            print("кокер-спаниэль")
        else:
            print("датский дог")
else:
    print("Рост собаки менее 50 см?", end=" ")
    answer_7 = input().strip().lower()
    if answer_7 == "да":
        print("У собаки доброжелательный характер?", end=" ")
        answer_8 = input().strip().lower()
        if answer_8 == "да":
            print("ирландский сеттер")
        else:
            print("фоксхаунд")
    else:
        print("У собаки рост менее 70 см?", end=" ")
        answer_9 = input().strip().lower()
        if answer_9 == "да":
            print("У собаки длинные уши?", end=" ")
            answer_10 = input().strip().lower()
            if answer_10 == "да":
                print("большой ванденский грифон")
            else:
                print("колли")
        else:
            print("Окрас рыжий с белыми отметинами?", end=" ")
            answer_11 = input().strip().lower()
            if answer_11 == "да":
                print("сенбернар")
            else:
                print("Белоснежный окрас?", end=" ")
                answer_12 = input().strip().lower()
                if answer_12 == "да":
                    print("ирландский волкодав")
                else:
                    print("ньюфаундленд")