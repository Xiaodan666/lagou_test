"""
没有参数的方法，有返回值
"""
name = "xiaodan"


def have_return():
    global name
    name = "xiaodantest"
    return name


"""
有参数的方法，没有返回值，返回值为None
"""


def no_return(sex):
    print(sex)


print(have_return())

print(no_return("女"))
