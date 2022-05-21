def divisors(num):
    divisors = [ i for i in range(1, num +1) if num % i == 1]
    return divisors


def run():
    num = 10
    print(divisors(num))
    print('program finished')


if __name__ == "__main__":
    run()