'''
1 餐馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。
创建一个名 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，
而后者打印一条消息，指出餐馆正在营业。 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。
'''
'''4 就餐人数 ：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。
根据这个类创建一个名为restaurant 的实 例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。 
添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。 
添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：
你认为这家餐馆每天可能接待的就 餐人数。 '''
class Restaurant():
    def __init__(self):
        self.restaurant_name=''
        self.cuisine_type =''
        self.number_served=0
    def describe_restaurant(self):
        return '这个餐馆叫'+self.restaurant_name+'主要菜品'+self.cuisine_type
    def open_restaurant(self):
        return '餐馆正在营业'
    def set_number_served(self):
        self.number_served1=self.number_served+100
        return '今天来了'+str(self.number_served1)+'人'
    def increment_number_served(self):
        self.number_served=self.number_served+10
        return self.number_served
restaurant=Restaurant()
restaurant.restaurant_name='好吃餐馆'
restaurant.cuisine_type ='东北菜'
print(restaurant.open_restaurant())
print(restaurant.describe_restaurant())
print(f"增加人数{restaurant.increment_number_served()}")
print(restaurant.set_number_served())

# restaurant.restaurant_name='绝味餐馆'
# restaurant.cuisine_type ='川菜'
# print(restaurant.open_restaurant())
# print(restaurant.describe_restaurant())
#
# restaurant.restaurant_name='美味餐馆'
# restaurant.cuisine_type ='粤菜'
# print(restaurant.open_restaurant())
# print(restaurant.describe_restaurant())

