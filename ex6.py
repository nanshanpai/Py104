x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
#----把字符串赋值给变量， 变量通过格式化把字符串嵌入字符串中

print(x)
print(y)

print("I said: %r." % x)
print("I also said: '%s'." % y)

hilrious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilrious)# 一个是字符串带格式化的末班，一个是变量，直接在print函数中输出
w = "This is the left side of..."
e = "a string with a right side."

print(w + e) #字符串可以进行加法和乘法的游戏print(w * 8)