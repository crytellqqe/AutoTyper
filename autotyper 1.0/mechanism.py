import time
import keyboard
import os

# Переменная список для шаблонов, переменная с инедксом элемента списка, переменная отвечающая за текст, который будет печататься
templates = ["По умолчанию", "XDXD"]
template_index = 0

# Очистка консоли
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Меню
def menu():
    clear()

    print("***Autotyper by crytellqqe***")
    print("                  version: not released")
    print("")
    print(f"Выбранный шаблон: {templates[template_index]}")
    print("")
    print("Выбрать шаблон: F9")
    print("Вывести список шаблонов: F10")
    print("Добавить/удалить шаблон: CTRL + F10")
    print("")
    print("Печатать один раз: F7")
    print("Печатать без остановки по кругу: F8. Для остановки зажмите DEL до выключения")
    print("")
    print("ALT + DEL для завершения программы")
    print("")

# Функция для выбора шаблона из списка
def text_w():
    clear()

    global template_index

    print(f"Выберите шаблон от {1} до {10}")
    print("")
    
    template_index = int(input()) - 1

    menu()

# Вывод шаблонов
def show_templates():
    for i, items in enumerate(templates, start=1):
        print(i, items)

def f10_templates():
    clear()

    print("Шаблоны:")
    print("")
    show_templates()
    print("")
    print("Чтобы вернуться в меню, введите: меню")
    print("")

    while True:
        anything = input()

        if anything == "меню":
            menu()

            return

        else:
            clear()

            show_templates()
            print("")
            print("Неверный ввод, попробуйте еще раз")
            print("")
            print("Чтобы вернуться в меню, введите: меню")
            print("")

# Функция для добавления и удаления шаблонов
def template_management():
    clear()
    
    global index_management, templates
    
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
                show_templates()
                print("")
                print("Введите ваш шаблон:")
                print("")

                template_text = input()

                if template_text.lower() == "меню":
                    menu()
                    
                    return

                clear()
                print("Чтобы вернуться в меню, введите: меню")
                print("")
                print("Ваши шаблоны:")
                print("")
                show_templates()
                print("")
                print("На какое место его поставить?")
                print("")

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
                            show_templates()
                            print("")
                            print("Вы ввели не число!")
                            print("Так на какое место его поставить?")
                            print("")
                            
                            index_management = input()

                    templates.insert(index_management, template_text)

                    clear()
                    print("Ваши обновленные шаблоны:")
                    print("")
                    show_templates()
                    print("")
                    print("Вернуться в меню или добавить еще один? меню/что угодно")
                    print("")

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
                show_templates()
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
                            templates.pop(index_management)

                            break

                        except IndexError:
                            clear()

                            print("Чтобы вернуться в меню, введите: меню")
                            print("")
                            print("Ваши шаблоны:")
                            print("")
                            show_templates()
                            print("")
                            print("Шаблона под этим номером нет. Попробуйте еще раз")
                            print("")
                            
                            index_management = input()

                        except ValueError:
                            clear()

                            print("Чтобы вернуться в меню, введите: меню")
                            print("")
                            print("Ваши шаблоны:")
                            print("")
                            show_templates()
                            print("")
                            print("Вы ввели не число. Попробуйте еще раз")
                            print("")

                            index_management = input()

                clear()
                print("Чтобы вернуться в меню, введите: меню")
                print("")
                print("Ваши обновленные шаблоны:")
                print("")
                show_templates()
                print("")
                print("Удалить еще один? меню/что угодно")
                print("")
                
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
            print("")
            
            choice = input().lower()

# Функция для печати один раз
def typer():
    time.sleep(0.05)

    keyboard.write(templates[template_index], delay=0.025)
    keyboard.press_and_release('enter')

# Функция для печати без остановки (по кругу)
def typer_scr():
    while True:
        time.sleep(0.05)

        keyboard.write(templates[template_index], delay=0.025)
        keyboard.press_and_release('enter')

        if keyboard.is_pressed('del'):
            break