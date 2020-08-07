def create_user(lucky_person):
    print("Please, enter your name:")
    lucky_person['name'] = input()
    print("Hello, " + lucky_person['name'])
    print("You have 7 skill points")
    skills_count = 7
    skills_used = 0
    print("Please, choose your skills:")
    while skills_count != skills_used:
        print("Points left - " + str(skills_count - skills_used))
        print("1. Luck - " + str(lucky_person["skills"]["luck"]))
        print("2. Eloquence - " + str(lucky_person["skills"]["eloquence"]))
        print("3. Agility - " + str(lucky_person["skills"]["agility"]))
        print('Please, enter 1,2 or 3:')
        selected_skill = int(input())
        if selected_skill == 1:
            lucky_person["skills"]["luck"] += 1
            skills_used += 1
        elif selected_skill == 2:
            lucky_person["skills"]["eloquence"] += 1
            skills_used += 1
        elif selected_skill == 3:
            lucky_person["skills"]["agility"] += 1
            skills_used += 1
        else:
            print("Sorry, skill is undefined")

    print("Your person:\n Name: " + str(lucky_person['name'])
          + "\n Money: " + str(lucky_person['money'])
          + "\n Skills: \n     Luck: " + str(lucky_person['skills']['luck'])
          + "\n     Eloquence: " + str(lucky_person['skills']['eloquence'])
          + "\n     Agility: " + str(lucky_person['skills']['agility']))
