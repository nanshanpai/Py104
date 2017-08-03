#带转义字符的 字符串 赋值给变量
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# 多行字符串赋值
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

while True:
    for i in ["/", "-", "|", "\\", "|"]:
	    print("%s\r" % i,)
    exit()