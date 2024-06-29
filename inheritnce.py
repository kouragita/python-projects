class IPDA:

    def __int__(self, Time, Price):
        self.Time = Time
        self.Price = Price

    def getdata(self):
        print('Accepting data')
        self.Time = input('Enter Time')
        self.Price = input('Enter price')

    def putdata(self):
        print('Time:'+self.Time, 'price:'+self.Price)

class sessions(IPDA):

    def __int__(self, AM):
        self.AM = AM

    def AM(self):
        print('midnyt to noon NY local time')

killzones = sessions()
killzones.AM()
killzones.getdata()
killzones.putdata()
