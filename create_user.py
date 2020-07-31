from game import goods, purchase, sale

person = {
    'name': '',
    'money': 1000,
    'cargo': {},
#    'level': 1,
#   'experience': 0,
    'skills': {
        'luck': 0,
        'eloquence': 0,
        'agility': 0
    }
}
print("Please, enter your name:")
person['name'] = input()
print("Hello, " + person['name'])
print("You have 7 skill points")
skills_count = 7
skills_used = 0
print("Please, choose your skills:")
while skills_count!= skills_used:
    print("Points left - " + str(skills_count - skills_used))
    print("1. Luck - " + str(person["skills"]["luck"]))
    print("2. Eloquence - " + str(person["skills"]["eloquence"]))
    print("3. Agility - " + str(person["skills"]["agility"]))
    print('Please, enter 1,2 or 3:')
    selected_skill = int(input())
    if selected_skill == 1:
        person["skills"]["luck"] += 1
        skills_used+=1
    elif selected_skill == 2:
        person["skills"]["eloquence"] += 1
        skills_used += 1
    elif selected_skill == 3:
        person["skills"]["agility"] += 1
        skills_used += 1
    else:
        print("Sorry, skill is undefined")

print("Your person:\n Name: " + str(person['name'])
      + "\n Money: " + str(person['money'])
      + "\n Skills: \n     Luck: " + str(person['skills']['luck'])
      + "\n     Eloquence: " + str(person['skills']['eloquence'])
      + "\n     Agility: " + str(person['skills']['agility']))

purchase(person)
sale(person)

print('ДЕНЕГ СТАЛО ', person['money'])
