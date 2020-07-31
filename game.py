goods = [{'type': "Техника", "price_in": 1000, "price_out": 5000, "risk_percent": 10},
         {'type': "Сигареты", "price_in": 100, "price_out": 300, "risk_percent": 10},
         {'type': "Алкоголь", "price_in": 250, "price_out": 600, "risk_percent": 15},
         {'type': "Драгоценности", "price_in": 5000, "price_out": 15000, "risk_percent": 20}]


def purchase(lucky_person):
    print("choose your goods")
    for i, n in enumerate(goods):
        print(i, f"{n['type']}  цена покупки:{n['price_in']} цена продажи: {n['price_out']} \
        вероятный навар: {n['price_out'] - n['price_in']} риск:{n['risk_percent']}%")   # f - форматирование строки
    lucky_person['cargo'] = goods[int(input("Enter number "))]
    lucky_person['money'] -= lucky_person["cargo"]["price_in"] * ((100 - lucky_person["skills"]["eloquence"])/100)


def sale(lucky_person):
    lucky_person['money'] += lucky_person["cargo"]["price_out"] * ((100 + lucky_person["skills"]["luck"])/100)
    lucky_person['cargo'] = {}
