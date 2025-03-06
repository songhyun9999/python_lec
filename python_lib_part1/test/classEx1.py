class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = 1000

    def greeting(self):
        print('안녕하세요 제 이름은 {}입니다. 제나이는 {}입니다'.
              format(self.name,self.age))

    def balance_info(self):
        print(self.__wallet)


maria = Person('maria',40,'seoul')
maria.greeting()
maria.balance_info()
