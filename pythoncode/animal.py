"""
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
"""
import yaml


class Animal:
    name = "default"
    color = "红色"
    age = 10
    sex = "男"

    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def cry(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


"""
创建子类【猫】，继承【动物类】，

- 复写父类的__init__方法，继承父类的属性，

- 添加一个新的属性，毛发=短毛，

- 添加一个新的方法， 会捉老鼠，

- 复写父类的‘【会叫】的方法，改成【喵喵叫】
"""


class Cat(Animal):
    def __init__(self, name, color, age, sex, hair="短毛"):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def catch_mouse(self):
        print(f"{self.name}会捉老鼠")

    def cry(self):
        print(f"{self.name}喵喵叫")


"""
创建子类【狗】，继承【动物类】，

- 复写父类的__init__方法，继承父类的属性，

- 添加一个新的属性，毛发=长毛，

- 添加一个新的方法， 会看家，

- 复写父类的【会叫】的方法，改成【汪汪叫】
"""


class Dog(Animal):
    def __init__(self, name, color, age, sex, hair="长毛"):
        super().__init__(name, color, age, sex)
        self.hair = hair

    def watch_house(self):
        print(f"{self.name}会看家")

    def cry(self):
        print(f"{self.name}汪汪叫")


if __name__ == '__main__':
    """
    创建一个猫猫实例
    
    - 调用捉老鼠的方法
    
    - 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
    """
    cat1 = Cat("七月", "灰色", 2, "公")
    cat1.catch_mouse()
    print(f"{cat1.name},{cat1.color},{cat1.age},{cat1.sex},{cat1.hair} 捉到了老鼠")

    """
    创建一个狗狗实例
    
    - 调用【会看家】的方法
    
    - 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
    """
    dog1 = Dog("旺仔", "白色", 3.5, "公")
    dog1.watch_house()
    print(dog1.name, dog1.color, dog1.age, dog1.sex, dog1.hair)

    print("------这是分割线----------")
    """
    使用 yaml 来管理实例的属性
    """
    with open("../datas/animal.yaml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    dogs = datas["dog"]
    dog = dogs["dog_default"]
    dog_name = dog["name"]
    dog_color = dog["color"]
    dog_age = dog["age"]
    dog_sex = dog["sex"]

    cats = datas["cat"]
    cat = cats["cat_default"]
    cat_name = cat["name"]
    cat_color = dog["color"]
    cat_age = dog["age"]
    cat_sex = dog["sex"]

    dog2 = Dog(dog_name, dog_color, dog_age, dog_sex)
    print("yaml文件读取", dog2.name, dog2.color, dog2.age, dog2.sex, dog2.hair)

    cat2 = Cat(cat_name, cat_color, cat_age, cat_sex)
    print("yaml文件读取", cat2.name, cat2.color, cat2.age, cat2.sex, cat2.hair)
