class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age

    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'
    
    def __chek_adulthood(self) -> bool:
        return self.age > 18


bill = Human('Bill', 40)
print(bill.say_hello())
print(f'Вік: {bill.age}, Дорослий: {bill.is_adult}')

jill = Human('Jill', 20)
print(jill.say_hello())
print(f'Вік: {jill.age}, Дорослий: {jill.is_adult}')

