import time
# property 정의이후 getter -> setter, deleter 정의 해야함
# 순서를 지켜야만 하고 _ 에 대해 정의시에는 _ 없이 나타냄
# 해당 함수들은 setter 와 getter를 정의해주므로 직접 접근을 안함
# 접근시에는 self.name 이런식으로 접근
class Worker:
    def __init__(self,name,hours,wage):
        self._name = name
        self._hours = hours
        self._wage = wage
    
    # Getter
    @property
    def name(self):
        return self._name
    @property
    def hours(self):
        return self._hours
    @property
    def wage(self):
        return self._wage  
    
    # Setter    
    @hours.setter
    def hours(self,hours):
        if hours < 0:
            raise ValueError
        self._hours = hours
    @name.setter
    def name(self,name):
        self._name = name
    @wage.setter
    def wage(self,wage):
        if wage < 0:
            raise ValueError
        self._wage = wage
        
    # Deleter
    @wage.deleter
    def wage(self):
        print('wage 인자 삭제')
        del self._wage       
    
    def payForWeek(self):
        if self.hours>40:
            pay = self.wage * 40
            print(f'Pay for {self.name} : '
                  f'${self.wage*(self.hours-40)*1.5 + pay:.2f}')
        else:
            print(f'Pay for {self.name} : ${self._wage*self.hours}')
            
def createWorker():
    while True:
        try:
            name = input("Enter person's name : ")
            hours = float(input("Enter number of hours worked : "))
            wage = float(input("Enter hourly wage : "))
            
            worker = Worker(name,hours,wage)
            # worker.pyaForWeek()
            return worker
        except ValueError as e:
            print(f"입력 오류 {e} 다시 입력해주세요.")
        except KeyboardInterrupt as e:
            print('프로그램 종료')
            break
        finally:
            time.sleep(0.1)


if __name__ == '__main__':
    worker = createWorker()
    worker.payForWeek()
