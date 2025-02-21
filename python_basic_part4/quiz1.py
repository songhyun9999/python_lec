class Worker:
    def __init__(self,name,hours,wage):
        self.name = name
        self.hours = hours
        self.wage = wage
    
    def pyaForWeek(self):
        if self.hours>40:
            pay = self.wage * 40
            print(f'Pay for {self.name} : '
                  f'${self.wage*(self.hours-40)*1.5 + pay:.2f}')
        else:
            print(f'Pay for {self.name} : ${self.wage*self.hours}')
            

if __name__ == '__main__':
    name = input("Enter person's name : ")
    hours = int(input("Enter number of hours worked : "))
    wage = int(input("Enter hourly wage : "))
    
    worker = Worker(name,hours,wage)
    worker.pyaForWeek()
