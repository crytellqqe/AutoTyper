from mechanism import menu, text_w, templates, f10_templates, template_management, typer, typer_scr
import keyboard

# Запуск скрипта
menu()

# Горячие клавиши
keyboard.add_hotkey('f9', text_w)
keyboard.add_hotkey('f10', f10_templates)
keyboard.add_hotkey('ctrl + f10', template_management)
keyboard.add_hotkey('f7', typer)
keyboard.add_hotkey('f8', typer_scr)
    
keyboard.wait('alt+del')