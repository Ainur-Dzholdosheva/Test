# Инкапсуляция - это доступ к некоторым обьект компонентам.Также он дает доступ к некоторым компонентам только внутри класса. Некоторые общедоступны а некоторые-внутренние.
# Инкапсуляция делает некоторые из компонент доступными только внутри класса.
# Наследование подразумевает что дочерние элементы наследую родительские.

class Ainur:
    def _privat(self):
        print("I am 31 years old")

s=Ainur()
s._privat()


# Наследование

class Icecream:
    def __init__(self,name,price):
        self.name=name
        self.price=price


class Plombir(Icecream):
    def __init__(self, price,taste):
        name=f"Plombir{taste}"
        super(Plombir, self).__init__(name=name, price=price)


t=Plombir("dsdsdfsf", 45)
print(t)

