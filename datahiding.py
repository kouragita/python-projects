class Myclass:
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)


object1 = Myclass()
object1.add(9)
print(object1.__hiddenvariable)
