def increment(num):
    try:
        return int(num) + 1
    except Exception as e:
        raise ValueError("This is not good")


a = increment('1')
print(a)
