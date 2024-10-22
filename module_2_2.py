first = int(input("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))

if first == second and second == third:
    print(3)

elif first == second or second == third or first == third:
    print(2)

else:
    not first == second and not second == third and not first == third
    print(0)

# правильно понимаю, в операторе else строка подсвечивается жёлтым потому, что Pycharm не понимает, зачем я пишу лишние
# символы, если строку можно оставить пустой?
