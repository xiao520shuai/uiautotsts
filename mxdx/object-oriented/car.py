class Car(object):
    def __init__(self):
        self.color='greet'
        self.wheelnum='4'
    def move(self):
        return self.color+'汽车带动'+self.wheelnum+'移动'
    def tot(self):
        return self.color + '汽车带动' + self.wheelnum + '鸣笛'

    def __str__(self):
        return  "这是一个汽车呀"
mycar=Car()
mycar.color='red'
print(mycar.move()+mycar.__str__())

print(Car().tot())