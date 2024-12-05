from functools import *
@lru_cache(None)

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
def main():
    for i in range(5):
        try:
            n = int(input("Введите значение: "))
            if n > 0:
                result = fib(n)
                print(f"{n}-е число Фибоначчи равно {result}")
            else:
                print("Введено нулевое значение")
                break
        except:
            print("Неверно введено значение")
            break
        
if __name__ == "__main__":
    main()
