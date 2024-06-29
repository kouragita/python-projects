class IPDA:

    def __int__(self, Time, Price):
        self.time = Time
        self.price = Price

    def getdata(self):
        print('Accepting data')
        self.Time = input('Enter Time')
        self.Price = input('Enter Price')

    def putdata(self):
        print('Time:'+self.Time, 'Price:'+self.Price)


ICT = IPDA()
ICT.getdata()
ICT.putdata()
