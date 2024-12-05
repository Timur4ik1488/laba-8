def TimeToHMS(time):
    second = time
    minutes = (time%3600)//60
    hours = time // 3600
    return second, minutes, hours

def main():
    try:
        for i in range(5):
            time = float(input("Введите интервал времени в секундах: "))
            if time >0:
                second, minutes, hours = TimeToHMS(time)
                print(f"В заданном промежутке времени {time} содержится {second} секунд, {minutes} минут и {hours} часов")
            else:
                print("Введите ненулевой интервал")
                break
    except:
        print("Неверно введено значение для интервала")

if __name__ == '__main__':
    main()