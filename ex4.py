cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90  # 给变量赋值
cars_not_driven = cars - drivers # 用变量参数运算结果赋予变量值
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.") #打印字符与参数变量
print("There are onle", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
#附加 name "car_pool_capacity' is not defined 该变量没有被定义，不能参与运算
#在程序中用4.0 很有必要再计算平均拉的人数有可能不是整数