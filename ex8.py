formatter = "%r %r %r %r"  #格式化方式赋值给变量

#给格式化方式赋值，也是给之前定义的变量赋值
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
	"That you could type u right.",
	"But it didn't sing.",
	"So I said goodnight."
))

# 
#错误 print 是一个函数，在应用时要加括号, 而且通常是错误提示哪行的上一行括号有问题，原因是否是上一个print把下面的当做自己的参数处理了？