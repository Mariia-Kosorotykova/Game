goods = [{'type': "technique", "price_in": 1000, "price_out": 5000, "risk_percent": 10},
         {'type': "cigarette", "price_in": 100, "price_out": 300, "risk_percent": 10},
         {'type': "alcohol", "price_in": 250, "price_out": 600, "risk_percent": 15},
         {'type': "jewelry", "price_in": 5000, "price_out": 15000, "risk_percent": 20}]


def get_digit(welcome_string='Enter the goods number: '):
    line = ''
    while not line.isdigit() or int(line.strip()) not in list(range(len(goods))):
        line = input(welcome_string)
    return int(line.strip())


def purchase(lucky_person):
    print("choose your goods")
    for i, n in enumerate(goods):
        print(i, f"{n['type']}  purchase price:{n['price_in']} selling price: {n['price_out']} \
        probable earnings: {n['price_out'] - n['price_in']} risk:{n['risk_percent']}%")
    lucky_person['cargo'] = goods[get_digit()]
    lucky_person['money'] -= lucky_person["cargo"]["price_in"] * ((100 - lucky_person["skills"]["eloquence"])/100)


def sale(lucky_person):
    lucky_person['money'] += lucky_person["cargo"]["price_out"] * ((100 + lucky_person["skills"]["luck"])/100)
    lucky_person['cargo'] = {}
