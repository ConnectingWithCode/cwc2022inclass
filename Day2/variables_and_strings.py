def variables():
    print("----- Variables ------")
    x = 91
    print(x)
    print(type(x))
    y = 3.141592653897238
    print(y)
    print(type(y))
    name = "Dave"
    print(name)
    print(type(name))

    print(x + 10)
    print(y + 10)
    # print(name + 10)

    print(x * 10)
    print(y * 10)
    print(name * 10)


def strings():
    print("----- Strings -----")
    s1 = "Double quotes"
    print(s1)
    s2 = 'Single quotes'
    print(s2)
    s3 = '''triples'''
    print(s3)
    s4 = """triple doubles"""
    print(s4)


def main():
    print("Dave is ready")
    variables()
    strings()


main()
