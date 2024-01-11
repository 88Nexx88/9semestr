'''
8. Фотоаппарат
Фотоаппарат имеет две кнопки: «фото» и «перемотка».
Фотоплёнка имеет ёмкость 10  кадров.
Нажатием на кнопку «фото» фотоаппарат делает снимок.
При нажатии  на кнопку «перемотка» фотоаппарат прокручивает плёнку на один кадр вперёд.
Без перемотки делать снимок фотоаппарат не может (кроме первого кадра).
Без снимка фотоаппарат также не может сделать перемотку.
После снимка  последнего, 10 кадра, перемотка не работает, пока не будет заменена фотоплёнка.
Пока не будет отснята вся плёнка, её также нельзя заменить.
Если фотоаппарат пуст (нет плёнки), то нажатие на кнопки ничего не дает.
Начальная конфигурация: фотоаппарат пуст.
'''


import time
import PySimpleGUI as sg



status_peremotka = False
status_last = 0
layout = [
    [sg.Button('Фото',enable_events=True, key='-FUNCTION1-', font='Helvetica 16')],
    [sg.Button('Фотоплёнка добавить',enable_events=True, key='-FUNCTION2-', font='Helvetica 16')],
    [sg.Button('Перемотка',enable_events=True, key='-FUNCTION3-', font='Helvetica 16', disabled=True)],
    [sg.Text(f'Состояние: Фотоплёнка:{status_last}, Перемотка:{status_peremotka}', key='-text-', font='Helvetica 16')],
    [sg.Text('', size=(25, 1), key='-texterror-', text_color='red', font='Helvetica 16')]
]
window = sg.Window('8. Фотоаппарат', layout, size=(600,250))
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-FUNCTION1-':
        if status_last == 10 and status_peremotka == True:
            text_elem = window['-text-']
            status_peremotka = False

            status_last -= 1
            button1 = window['-FUNCTION1-']
            button1.update(disabled=True)
            text_elem.update(
                f'Состояние: Фотоплёнка:{status_last}, Перемотка:{status_peremotka}')
            text_elem_error = window['-texterror-']
            text_elem_error.update('')
            button3 = window['-FUNCTION3-']
            button3.update(disabled=False)
        elif status_last == 1 and status_peremotka == True:
            text_elem = window['-text-']
            status_peremotka = False

            status_last -= 1
            button1 = window['-FUNCTION1-']
            button1.update(disabled=True)
            button2 = window['-FUNCTION2-']
            button2.update(disabled=False)
            button3 = window['-FUNCTION3-']
            button3.update(disabled=True)
            text_elem.update(
                f'Состояние: Фотоплёнка:{status_last}, Перемотка:{status_peremotka}')
            text_elem_error = window['-texterror-']
            text_elem_error.update('')

        elif status_last == 0:
            button3 = window['-FUNCTION3-']
            button3.update(disabled=True)
            button2 = window['-FUNCTION2-']
            button2.update(disabled=False)
            text_elem_error = window['-texterror-']
            text_elem_error.update('Фотоплёнка пустая')
        elif status_peremotka == True:
            text_elem = window['-text-']
            status_peremotka = False

            status_last -= 1
            button1 = window['-FUNCTION1-']
            button1.update(disabled=True)
            button3 = window['-FUNCTION3-']
            button3.update(disabled=False)
            text_elem.update(
                f'Состояние: Фотоплёнка:{status_last}, Перемотка:{status_peremotka}')
            text_elem_error = window['-texterror-']
            text_elem_error.update('')


    elif event == '-FUNCTION2-':
            text_elem = window['-text-']
            status_last = 10
            status_peremotka = True
            button = window['-FUNCTION1-']
            button.update(disabled=False)
            button = window['-FUNCTION2-']
            button.update(disabled=True)
            button = window['-FUNCTION3-']
            button.update(disabled=True)
            text_elem.update(f'Состояние: Фотоплёнка:{status_last}, Перемотка:{status_peremotka}')
            text_elem_error = window['-texterror-']
            text_elem_error.update('')
        # запускаем связанную функцию
    elif event == '-FUNCTION3-':
        button1 = window['-FUNCTION1-']
        button1.update(disabled=False)
        button3 = window['-FUNCTION3-']
        button3.update(disabled=True)
        status_peremotka = True
        text_elem.update(f'Состояние: Фотоплёнка:{status_last}, Перемотка:{status_peremotka}')
        text_elem_error = window['-texterror-']
        text_elem_error.update('')


# закрываем окно и освобождаем используемые ресурсы
window.close()
