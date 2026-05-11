# tv = Television(10,15,True)
# tv.show() #결과 : 10,15,True
# tv.setChannel(12) # 결과 :  channel 값이 12로 변경
# tv.getChannel() # 결과 : channel에 있는 값 리턴

class Television : #클레스
    def __init__(self, channel, volume, on): # 기본 생성자
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self): # self,는 거의 필수라고 생각하고 넣기
        print(self.channel, self.volume, self.on)

    def setChannel(self,channel) : #set
        self.channel = channel
        
    def getChannel(self) :
        return self.channel #set으로 수정된 걸 가져온다.(수정하지 않았을 경우 디폴트값 가져옴)