# lucky_lottery

###### tags: `portfolio`

[簡易抽獎程式 HackMD](https://hackmd.io/@zz8yeJXcQYOjqL6CsPNdlg/HyA91S3wo)

[TOC]

## 環境部署

位於 cmd (Terminal) 下指令

> 安裝隨機生成變數的 library
```cmd=
pip install Faker
```

> 安裝生成假人人名的 library
```cmd
pip install Faker
```

## 單次抽獎

透過 single_draw() 呼叫 loettry() 再代入抽獎機率 (PERCENT)，進行單次抽獎：回傳成功與否

```python=
import random

PERCENT = 80

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
    
if __name__ == '__main__':
    single_draw()
```

> 執行結果：
![](https://i.imgur.com/tD4tdLR.png)

## 多次抽獎
透過　multiple_draw() 呼叫　loettry() 代入抽獎次數 (DRAW_COUNT)，進行多次抽獎，顯示抽獎成功、失敗次數
```python=
import random

PERCENT = 80
DRAW_COUNT = 10000

def lottery(percent):
    rand_num = random.randint(0, 99)
    if rand_num < percent:
        return True
    else:
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
    
if __name__ == '__main__':
    multiple_draw(draw_count=DRAW_COUNT)
```

> 執行結果：
![](https://i.imgur.com/PzYerHU.png)


## 讀檔抽獎

透過 read_file_lottery() 讀取參與抽獎人的名單，再進行抽獎，顯示出中獎者名單

```python=
import random

FILE_NAME = "participate_person.txt"

def file_lottery():
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

if __name__ == '__main__':
    result = read_file_lottery()
    print("執行成功與否", result)
```

> 執行結果：
![](https://i.imgur.com/QtqbZyG.png)

## 生成抽獎名單
```python=
import random
from faker import Faker

FILE_NAME = "participate_person.txt"
PARTICIPATE_NUM = 10000

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
    result = write_file(person_num=PARTICIPATE_NUM)
    print("執行成功與否", result)    
```
> 執行結果：
![](https://i.imgur.com/p4KkpEs.png)
![](https://i.imgur.com/oRZa5GM.png)


## 主程式運行

透過設定好的資訊(dict)，輸入對應選擇的模式，依照輸入的值(dict:key)，啟動對應的函式執行(dict:value)

```python=
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
```
> 執行結果：

![](https://i.imgur.com/ifqWdjV.png)
