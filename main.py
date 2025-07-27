import os
import file_operations
from faker import Faker
import random


def main():
    
    fake = Faker("ru_RU")
    letters_mapping = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }
    skills = ["Стремительный прыжок",
            "Электрический выстрел",
            "Ледяной удар",
            "Стремительный удар",
            "Кислотный взгляд",
            "Тайный побег",
            "Ледяной выстрел",
            "Огненный заряд"]
    skills = random.sample(skills,3)

    runic_skills = []
    for skill in skills:
        for value in letters_mapping:
            for letter in skill:
                if letter == value:
                    skill = skill.replace(letter,letters_mapping[value])
        runic_skills.append(skill)
        
    if os.path.exists("charsheets") == False:
        os.makedirs("charsheets")
        
    for i in range(10):
        context = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "job" : fake.job(),
        "town": fake.city(),
        "strength": random.randint(3,18),
        "agility": random.randint(3,18),
        "endurance": random.randint(3,18),
        "intelligence": random.randint(3,18),
        "luck": random.randint(3,18),
        "skill_1": runic_skills[0],
        "skill_2": runic_skills[1],
        "skill_3": runic_skills[2]
    }
        
        file_operations.render_template("charsheet.svg","charsheets/charsheet-{}.svg".format(i+1),context)
if __name__ == '__main__':
    main()

