class Phone:
    def call(self,number):
        print(f'{number}''에게 전화를 겁니다')
        
    def sendMessage(self,number,message):
        print(f'{number} 에게 {message} 를 보냅니다')
        

phone = Phone()
phone.call('010-1234-1234')
phone.sendMessage('010-1234-1234','hihihihi')
print()

class CM_Phone(Phone):
    def playMusic(self,title):
        print(f'{title} 을 플레이합니다.')
        
    def takePicture(self):
        print('사진을 찍습니다.')
        
cm_phone = CM_Phone()
cm_phone.call('010-1234-1234')
cm_phone.sendMessage('010-1234-1234','hihihhihihi')
cm_phone.playMusic('좋은날')
cm_phone.takePicture()        