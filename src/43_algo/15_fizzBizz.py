for i in range(50):
    result = ""
    if i % 3 == 0:
        result = "fizz"

    if i % 5 == 0:
        result += "buzz"

    print("{}:{}".format(i, result))
