def DigitCounts(s):
    if not s:
        return 0
    if s[0].isdigit():
        return 1 + DigitCounts(s[1:])
    else:
        return DigitCounts(s[1:])

def main():
    for i in range(5):
        try:
            s = input("Введите строку: ")
            result = DigitCounts(s)
            print(f"В строке {s} содержится {result} цифр")
        except:
            raise ValueError("Введено неверное значение")
        
if __name__ == "__main__":
    main()