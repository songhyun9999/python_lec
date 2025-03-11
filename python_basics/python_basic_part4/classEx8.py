class Purchase:
    def __init__(self,description='', price=0, quantity=0):
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    # getter 정의
    @property
    def price(self):
        return self.__price
    @property
    def quantity(self):
        return self.__quantity
    @property
    def description(self):
        return self.__description   
    
    # setter 정의
    @price.setter
    def price(self,price):
        self.__price = price
        
    @quantity.setter
    def quantity(self,quantity):
        self.__quantity = quantity
    
    @description.setter
    def description(self,description):
        self.__description = description
        

class Cart:
    def __init__(self,items=[]):
        self.__items = items
    
    def addItemToCart(self,item):
        self.__items.append(item)
    
    def getItems(self):
        return self.__items

    def calculateTotal(self):
        amount = 0
        for item in self.__items:
            amount += item.price* item.quantity
        return amount

def printReceipt(myCart):
    print('\n{0:12} {1:<10s} {2:<12}'.format('ARTICLE','PRICE','QUANTITY'))
    
    for purchase in myCart.getItems():
        print('{0:12s} ${1:<10.2f} {2:^5}'.format(
            purchase.description,purchase.price,
            purchase.quantity))
        
    print(f'\nTotal Cost : ${myCart.calculateTotal():.2f}')        
        

if __name__ == '__main__':
    carry_on = 'y'
    myCart = Cart()
    while carry_on == 'y':
        description = input('Enter description of article: ')
        price = float(input('Enter price of article: '))
        quantity = int(input('Enter quantity of article: '))
        article = Purchase(description,price,quantity)
        myCart.addItemToCart(article)
        
        carry_on = input('Do you want to enter more articles (y/n)? ')

    printReceipt(myCart)