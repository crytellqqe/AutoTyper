import time
import keyboard
import os

# Переменная список для шаблонов, переменная с инедксом элемента списка, переменная отвечающая за текст, который будет печататься
texts = ["По умолчанию", "XDXD"]
x = 0
a = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Меню
def menu():
    clear()

    print("***Autotyper by crytellqqe***")
    print("                  version: not released")
    print("")
    print(f"Выбранный шаблон: {texts[x]}")
    print("")
    print("Выбрать шаблон: F9")
    print("Вывести список шаблонов: F10")
    print("Добавить/удалить шаблон: CTRL + F10")
    print("")
    print("Печатать один раз: F7")
    print("Печатать без остановки по кругу: F8. Для остановки зажмите DEL до выключения")
    print("")
    print("ALT + DEL для завершения программы")

# Функция для выбора шаблона из списка
def text_w():
    clear()

    print(f"Выберите шаблон от {1} до {10}")

    global x

    x = int(input()) - 1

    print("") # Здесь позже сделать функцию для очистки консоли
    menu()

# Вывод шаблонов
def templates():
    for i, items in enumerate(texts, start=1):
        print(i, items)

def f10_templates():
    clear()
    templates()
    print("")
    print("Чтобы вернуться в меню, введите: меню")
    while True:
        back = input()
        if back == "меню":
            menu()
            break
        else:
            clear()
            templates()
            print("")
            print("Неверный ввод, попробуйте еще раз")
            print("Чтобы вернуться в меню, введите: меню")

# Функция для добавления и удаления шаблонов
def template_management():
    clear()
    
    global index_management, texts
    
    print("Добавить, удалить или переместить шаблон? Добавить/Удалить/Переместить")
    print("")
    print("Чтобы вернуться в меню, введите: меню")
    print("")

    choice = input().lower()

    while True:
        clear()

        if choice == "меню":
                menu()
                
                return

        elif choice == "добавить":
            while True:
                clear()

                print("Чтобы вернуться в меню, введите: меню")
                print("")
                print("Ваши шаблоны:")
                print("")
                templates()
                print("")
                print("Введите ваш шаблон:")

                template_text = input()

                if template_text.lower() == "меню":
                    menu()
                    
                    return

                clear()
                print("Чтобы вернуться в меню, введите: меню")
                print("")
                print("Ваши шаблоны:")
                print("")
                templates()
                print("")
                print("На какое место его поставить?")

                index_management = input()

                while True:
                    if index_management.lower() == "меню":
                        menu()

                        return

                    else:
                        try:
                            index_management = int(index_management) - 1

                            break

                        except ValueError:
                            clear()

                            print("Чтобы вернуться в меню, введите: меню")
                            print("")
                            print("Ваши шаблоны:")
                            print("")
                            templates()
                            print("")
                            print("Вы ввели не число!")
                            print("Так на какое место его поставить?")
                            print("")
                            
                            index_management = input()

                    texts.insert(index_management, template_text)

                    clear()
                    print("Ваши обновленные шаблоны:")
                    print("")
                    templates()
                    print("")
                    print("Вернуться в меню или добавить еще один? меню/что угодно")

                    anything = input().lower()
                    if anything == "меню":
                        menu()

                        return

        elif choice == "удалить":
            while True:
                clear()

                print("Чтобы вернуться в меню, введите: меню")
                print("")
                print("Ваши шаблоны:")
                print("")
                templates()
                print("")
                print("Какой шаблон удалить?")
                print("")

                index_management = input()

                while True:
                    if index_management.lower() == "меню":
                        menu()

                        return

                    else:
                        try:
                            index_management = int(index_management) - 1
                            texts.pop(index_management)

                            break

                        except IndexError:
                            clear()

                            print("Чтобы вернуться в меню, введите: меню")
                            print("")
                            print("Ваши шаблоны:")
                            print("")
                            templates()
                            print("")
                            print("Шаблона под этим номером нет. Попробуйте еще раз")
                            print("")
                            
                            index_management = input()

                clear()
                print("Чтобы вернуться в меню, введите: меню")
                print("")
                print("Ваши обновленные шаблоны:")
                print("")
                templates()
                print("")
                print("Удалить еще один? меню/что угодно")
                
                anything = input()
                if anything == "меню":
                    menu()

                    return

        elif choice == "переместить":
            clear()

            print("Какой шаблон и куда вы хотите переместить?")

            break

        else:
            print("Добавить, удалить или переместить шаблон? Добавить/Удалить/Переместить")
            print("")
            print("Неверный ввод, попробуйте еще раз")
            print("")
            print("Чтобы вернуться в меню, введите: меню")
            
            choice = input().lower()

# Функция для печати один раз
def typer():
    time.sleep(0.05)

    keyboard.write(texts[x], delay=0.025)
    keyboard.press_and_release('enter')

# Функция для печати без остановки (по кругу)
def typer_scr():
    while True:
        time.sleep(0.05)

        keyboard.write(texts[x], delay=0.025)
        keyboard.press_and_release('enter')

        if keyboard.is_pressed('del'):
            break