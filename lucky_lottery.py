import random
from faker import Faker

PERCENT = 80
PARTICIPATE_NUM = 100
DRAW_COUNT = 10000
FILE_NAME = "participate_person.txt"

FUNCTION_DICT = {
    1:"single_draw",
    2:"multiple_draw",
    3:"read_file_lottery",
    4:"write_file"
}

def lottery(percent):
    rand_num = random.randint(0, 99)
    if rand_num < percent:
        return True
    else:
        return False

def single_draw():
    result = lottery(percent=PERCENT)

    if result:
        print("Jackpot")
        return True
    else:
        print("Nope")
        return False

def multiple_draw(draw_count):
    success_count = 0
    fail_count = 0

    for i in range(draw_count):
        if lottery(percent=PERCENT):
            success_count += 1
        else:
            fail_count += 1

    print("Succeeded Count", success_count)
    print("Failed Count", fail_count)

def read_file_lottery():
    result = None
    try:
        file = open(FILE_NAME, 'r', encoding='UTF-8')
        people = []

        for line in file.readlines():
            people.append(line)

        file.close()

        if people:
            jackpot_person = random.sample(people, 1)
            print("Jackpot Person:", jackpot_person)
        else:
            raise Exception("Read File Empty")

        result = True
    except BaseException as e:
        result = False
        print(e)
    finally:
        return result


def write_file(person_num):
    result = None
    try:
        print("---GENERATE_PEOPLE_DATA---")
        file = open(FILE_NAME, 'w', encoding='UTF-8')
        people = []

        for i in range(person_num):
            fake = Faker("zh_TW")
            people.append(fake.name())
        for name in people:
            file.write("%s\n" % name)

        file.close()
        result = True
    except BaseException as e:
        result = False
        print(e)
    finally:
        print("---GENERATE_PEOPLE_DATA_END---")
        return result

if __name__ == '__main__':
    round_count = 0
    while True:
        round_count += 1
        print("---ROUND:", round_count, "---")
        print("Choice mode:")
        for key, values in FUNCTION_DICT.items():
            print(key, ":", values)
        try:
            input_value = input("Input:")

            result = input_value.isnumeric()
            if not result:
                raise ValueError("Input ValueError: input_value is not a number")

            input_value = int(input_value)

            if not FUNCTION_DICT.get(input_value):
                raise ValueError("Input ValueError: Function is not exist")

            function_name = FUNCTION_DICT.get(input_value)
            print("EXE:", function_name)

            if input_value == 2:
                multiple_draw(draw_count=DRAW_COUNT)
            elif input_value == 4:
                write_file(person_num=PARTICIPATE_NUM)
            else:
                locals().get(function_name)()

        except BaseException as e:
            print(e)
        finally:
            print("END")

