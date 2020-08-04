person = {
    'name': '',
    'money': 1000,
    'cargo': {'type': "Техника", "price_in":1000, "price_out": 5000, "risk_precent": 10},
#    'level': 1,
#   'experience': 0,
    'skills': {
        'luck': 100,
        'eloquence': 200,
        'agility': 100
    }
}
goods = [{'type': "Техника", "price_in":1000, "price_out": 5000, "risk_precent": 10},
       {'type': "Сигареты", "price_in":100, "price_out": 300, "risk_precent": 10},
       {'type': "Алкоголь", "price_in":250, "price_out": 600, "risk_precent": 15},
       {'type': "Драгоценности", "price_in":5000, "price_out": 15000, "risk_precent": 20}]

def skill_agility(answer): #меняет ловкость use the 1 option as negative in question
    while person['skills']["luck"] > 0 and person['skills']["agility"] > 0:
        if answer == '1':
            person['skills']["luck"] = person['skills']["luck"] - person['cargo']["risk_precent"]
            person['skills']['agility'] = person['skills']['agility'] - person['cargo']["risk_precent"]
            return print('Your luck: ', person['skills']["luck"], 'Your eloquence: ', person['skills']["luck"],
                         'Your agility: ', person['skills']["luck"])

        if answer == '2':
            person['skills']["luck"] = person['skills']["luck"] + person['cargo']["risk_precent"]
            person['skills']["agility"] = person['skills']['agility'] + person['cargo']["risk_precent"]
            return print('Your luck: ', person['skills']["luck"], 'Your eloquence: ', person['skills']["luck"],
                         'Your agility: ', person['skills']["luck"])

def skill_eloquence(answer): #use the 2 option as negative in question
    while person['skills']["luck"] > 0 and person['skills']["eloquence"] > 0:
        if answer == '2':
            person['skills']["luck"] = person['skills']["luck"] - person['cargo']["risk_precent"]
            person['skills']['eloquence'] = person['skills']['eloquence'] - person['cargo']["risk_precent"]
            return print('Your luck: ', person['skills']["luck"], 'Your eloquence: ', person['skills']["luck"],
                         'Your agility: ', person['skills']["luck"])
        if answer == '1':
            person['skills']["luck"] = person['skills']["luck"] + person['cargo']["risk_precent"]
            person['skills']["eloquence"] = person['skills']['eloquence'] + person['cargo']["risk_precent"]
            return print('Your luck: ', person['skills']["luck"], 'Your eloquence: ', person['skills']["luck"],
                         'Your agility: ', person['skills']["luck"])

def positive_1 (): #try skill_eloquence for answer
    answer = input('Print your answer here:', )
    return skill_eloquence(answer)

def positive_2():  # try skill_agility for answer
    answer = input('Print your answer here:', )
    return skill_agility(answer)
# if answer != '1' and answer != '2':
        #      print('Please choose variant 1 or 2')

person['name'] = input('Hello! Welcome to custom! May I know your name? ',  )
print('Do you have illegal items?\n Choose your option:\n 1. Yes \n 2. No')
positive_2()
print('We will need to exam your luggage, sir.\n Choose your option:\n'
      ' 1. Maybe we can avoid this somehow? \n '
      '2. Ok, here is my bag.')
positive_1()
if person['cargo']["type"] == "Техника":
    print('Oh, what is this? There are some phones. Do you have docs for them?\n Choose your option:\n'
          ' 1. No, unfortunately \n '
          '2. Seems  I left them at home.')
    positive_2()
if person['cargo']["type"] == "Сигареты":
    print('Oh, what is this? There are some packs of sigarettes. You have too many.\n Choose your option:\n '
          '1. I will leave some if required \n'
          ' 2. I do not  care about the law')
    positive_1()
if person['cargo']["type"] == "Драгоценности":
    print('Oh, what is this? There are some brilliants. \n Choose your option:'
          '\n 1. I do not want to go to prison!!!'
          ' \n 2. I hope we can resolve such the situation if you understand.')
    positive_2()
if person['cargo']["type"] == "Алкоголь":
    print('Oh, what is this? Whiskie? \n Choose your option:\n '
          '1. That is all for me. \n '
          '2. Just bring one bottle.')
    positive_2()
print('Did you have any issues with law before?\n Choose your option:\n'
      '1. No, never. \n '
      '2. To be honest, yes. I stole a heart of one girl. Just jocking.')
positive_1()