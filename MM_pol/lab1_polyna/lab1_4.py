import asyncio
import time
import PySimpleGUI as sg
from threading import Thread

def asyncloop(loop):
    # Set loop as the active event loop for this thread
    asyncio.set_event_loop(loop)
    # We will get our tasks from the main thread so just run an empty loop
    loop.run_forever()


async def sleep(button_print, text_elem):
    global status_paper
    global status_print
    while status_paper != 0:
        await asyncio.sleep(2)
        status_paper -= 1
        text_elem.update(f'Состояние: Бумага:{status_paper}, Печать:{status_print}')

    button_print.update(disabled=False)
    status_print = False
    status_paper = 0
    text_elem.update(f'Состояние после печати: Бумага:{status_paper}, Печать:{status_print}')

# create a new loop
loop = asyncio.new_event_loop()
# Create the new thread, giving loop as argument
t = Thread(target=asyncloop, args=(loop,))
# Start the thread
t.start()
status_print = False
status_paper = 0
layout = [
    [sg.Button('Печать',enable_events=True, key='-FUNCTION1-', font='Helvetica 16')],
    [sg.Button('Заправка листов',enable_events=True, key='-FUNCTION2-', font='Helvetica 16')],
    [sg.Text(f'Состояние: Бумага:{status_paper}, Печать:{status_print}', key='-text-', font='Helvetica 16')],
    [sg.Text('', size=(25, 1), key='-texterror-', text_color='red', font='Helvetica 16')]
]
window = sg.Window('Принтер', layout, size=(600,250))
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-FUNCTION1-':
        if status_print == True:
            text_elem_error = window['-texterror-']
            text_elem_error.update('Вы уже печатаете')
        elif status_paper == 0:
            text_elem_error = window['-texterror-']
            text_elem_error.update('Нет бумаги')
        else:
            text_elem = window['-text-']
            text_elem_error = window['-texterror-']
            text_elem_error.update('Печать!!!')
            button_print = window['-FUNCTION1-']
            status_print = True
            button_print.update(disabled=True)
            text_elem.update(f'Состояние: Бумага:{status_paper}, Печать:{status_print}')
            asyncio.run_coroutine_threadsafe(sleep(button_print, text_elem), loop)


    elif event == '-FUNCTION2-':
        if status_print == True:
            text_elem_error = window['-texterror-']
            text_elem_error.update('Вы заправили 1 лист')
            status_paper+=1
            text_elem.update(f'Состояние: Бумага:{status_paper}, Печать:{status_print}')
        elif status_paper != 0:
            text_elem_error = window['-texterror-']
            text_elem_error.update('Заправлен')
            text_elem.update(f'Состояние после заправки: Бумага:{status_paper}, Печать:{status_print}')
        else:
            text_elem = window['-text-']
            status_paper = 10
            text_elem.update(f'Состояние: Бумага:{status_paper}, Печать:{status_print}')
            text_elem_error = window['-texterror-']
            text_elem_error.update('')
        # запускаем связанную функцию


# закрываем окно и освобождаем используемые ресурсы
window.close()