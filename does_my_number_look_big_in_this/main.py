def narcissistic(value):
    arr = [*str(value)]
    exp = len(arr)
    return sum(list(map(lambda x: pow(int(x), exp), arr))) == value


print(narcissistic(153))
