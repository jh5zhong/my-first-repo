
class Car(object):  
    def __init__(self, brand, model, year):  
        self.brand = brand  
        self.model = model  
        self.year = year  
        self.speed = 0  
  
    def start(self):  
        #print(f"{self.brand} {self.model} started.")
        print("{0} {1} started.".format(self.brand,self.model))

  
    def drive(self):  
        #print(f"The car is driving with a speed of {self.speed} km/h.")
        print("The car is driving with a speed of {} km/h.".format(self.speed)) 
  
    def speed_up(self):  
        self.speed += 5  
        #print(f"The car speed is now {self.speed} km/h.")  
        print("The car speed is now {} km/h.".format(self.speed))
  
    def slow_down(self):  
        self.speed -= 5  
        #print(f"The car speed is now {self.speed} km/h.")
        print("The car speed is now {} km/h.".format(self.speed))
  
    def stop(self):  
        self.speed = 0  
        #print(f"{self.brand} {self.model} stopped.")
        print("{} {} stopped.".format(self.brand,self.model))
  
# 使用汽车类创建对象  
my_car = Car("Toyota", "Camry", 2020)  
  
# 启动汽车  
my_car.start()  
  
# 驾驶汽车  
my_car.drive()  
  
# 加速汽车  
my_car.speed_up()  
  
# 减速汽车  
my_car.slow_down()  
  
# 停车  
my_car.stop()
