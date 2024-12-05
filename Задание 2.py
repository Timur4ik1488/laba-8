from functools import *
@lru_cache(None)

def fib(n):
    if n <= 0:
        print("Введите положительно значение")
    if n == 1 and n==2:
        return 1
    
    for i in range(5):
        f1, f2 = 1, 1
        for _ in range(3, n+1):
            f1, f2 = f2, f1+f2
        return f2
    
def main():
    for i in range(5):
        try:
            n = int(input("Введите элемент Фибоначчи по счёту с начала последовательности: "))
            if n > 0 and n < 1000:
                result = fib(n)
                print(f"{n}-е число Фибоначчи равно {result}")
            else:
                print("Введите ненулевое значение для элемента")
                break
        except:
            print("Неверно введено значение для элемента")
            break

if __name__ == "__main__":
    main()