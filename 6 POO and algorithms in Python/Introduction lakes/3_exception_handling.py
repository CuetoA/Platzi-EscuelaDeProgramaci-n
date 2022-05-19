# Do not silence our exceptions


def division(num1, num2):
    try:
        resul = num1 / num2
        return resul
    except ZeroDivisionError as e:
        print(e)
        return -1
        

if __name__ == "__main__":
    
    ans = division(1, 0)
    print(ans)
    ans = division(1, 2)
    print(ans)