from game import purchase, sale
from gamequestions import question
from create_user import create_user

person = {
    'name': '',
    'money': 1000,
    'cargo': {},
    # 'level': 1,
    # 'experience': 0,
    'skills': {
        'luck': 0,
        'eloquence': 0,
        'agility': 0
    }
}

if __name__ == '__main__':
    create_user(person)
    purchase(person)
    question(person)
    sale(person)

    print('MONEY BECAME', person['money'])