'''
9. Троллейбус
Имеется три кнопки управления: «газ», открытие/закрытие дверей и «свет в салоне».
Если двери троллейбуса закрыты и водитель нажимает «газ», то он начинает движение в пределах одной минуты.
Если водитель во время движения нажимает «газ», то троллейбус дополнительно движется одну минуту.
Если двери открыты, то троллейбус с места тронутся не может. Во время движения двери открываться не могут.
Если время истекло, троллейбус останавливается. Двери можно открыть, только включив свет в салоне, закрыть,
только когда свет отключен. Начальная конфигурация: троллейбус стоит, двери закрыты, освещение выключено.
'''
import asyncio
import time
import PySimpleGUI as sg
from threading import Thread

def asyncloop(loop):
    # Set loop as the active event loop for this thread
    asyncio.set_event_loop(loop)
    # We will get our tasks from the main thread so just run an empty loop
    loop.run_forever()

async def sleep(button_door, button_light, text_elem):
    global status_gas
    global status_door
    global status_light
    status_door = False
    status_light = False
    while status_gas != 0:
        await asyncio.sleep(0.5)
        status_gas -= 1
        text_elem.update(f'Состояние: Газ:{"Стоит" if status_gas==0 else "Движение"}, {status_gas}, '
                         f'Дверь:{status_door} , Свет:{status_light}')
    else:
        button_door.update(disabled=True)
        button_light.update(disabled=False)


loop = asyncio.new_event_loop()
# Create the new thread, giving loop as argument
t = Thread(target=asyncloop, args=(loop,))
# Start the thread
t.start()
status_gas = 0
status_door = False
status_light = False
layout = [
    [sg.Button('Газ',enable_events=True, key='-FUNCTION1-', font='Helvetica 16')],
    [sg.Button('Дверь',enable_events=True, key='-FUNCTION2-', font='Helvetica 16', disabled=True)],
    [sg.Button('Свет',enable_events=True, key='-FUNCTION3-', font='Helvetica 16')],
    [sg.Text(f'Состояние: Газ:{"Стоит" if status_gas==0 else "Движение"}, {status_gas}, Дверь:{status_door} , Свет:{status_light}', key='-text-', font='Helvetica 16')],
    [sg.Text('', key='-texterror-', text_color='red', font='Helvetica 16')]
]

sg.theme('LightBrown1')

window = sg.Window('9. Троллейбус', layout, size=(600,250))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-FUNCTION1-':
        test_error = window['-texterror-']
        test_error.update(f'')
        if status_door == False and status_gas == 0:
            text_elem = window['-text-']
            button_door = window['-FUNCTION2-']
            button_door.update(disabled=True)
            button_light = window['-FUNCTION3-']
            button_light.update(disabled=True)
            status_gas = 60
            text_elem.update(f'Состояние: Газ:{"Стоит" if status_gas == 0 else "Движение"}, {status_gas}, '
                             f'Дверь:{status_door} , Свет:{status_light}')
            asyncio.run_coroutine_threadsafe(sleep(button_door, button_light, text_elem), loop)
        elif status_door == False and status_gas != 0:
            text_elem = window['-text-']
            status_gas+=60
            text_elem.update(f'Состояние: Газ:{"Стоит" if status_gas == 0 else "Движение"}, {status_gas}, '
                             f'Дверь:{status_door} , Свет:{status_light}')
        else:
            test_error = window['-texterror-']
            test_error.update(f'Закройте дверь!')

    elif event == '-FUNCTION2-':
        test_error = window['-texterror-']
        test_error.update(f'')
        text_elem = window['-text-']
        if status_light == True and status_door == False:
            button_door = window['-FUNCTION2-']
            button_door.update(disabled=True)
            status_door = True
            button_light = window['-FUNCTION3-']
            button_light.update(disabled=False)
        elif status_light == False and status_door == True:
            button_door = window['-FUNCTION2-']
            button_door.update(disabled=True)
            status_door = False
            button_light = window['-FUNCTION3-']
            button_light.update(disabled=False)
        elif status_light == False and status_door == False:
            test_error = window['-texterror-']
            test_error.update(f'Включите свет, чтобы открыть дверь!')
        elif status_light == True and status_door == True:
            test_error = window['-texterror-']
            test_error.update(f'Выключите свет, чтобы закрыть дверь!')
        text_elem.update(f'Состояние: Газ:{"Стоит" if status_gas == 0 else "Движение"}, {status_gas}, '
                         f'Дверь:{status_door} , Свет:{status_light}')


    elif event == '-FUNCTION3-':
        test_error = window['-texterror-']
        test_error.update(f'')
        if status_door == True and status_light == True:
            text_elem = window['-text-']
            button_door = window['-FUNCTION2-']
            button_door.update(disabled=False)
            status_light = False

            button_light = window['-FUNCTION3-']
            button_light.update(disabled=True)

            text_elem.update(f'Состояние: Газ:{"Стоит" if status_gas == 0 else "Движение"}, {status_gas}, '
                             f'Дверь:{status_door} , Свет:{status_light}')
        elif status_door == False and status_light == False:
            text_elem = window['-text-']
            button_door = window['-FUNCTION2-']
            button_door.update(disabled=False)
            status_light = True
            button_light = window['-FUNCTION3-']
            button_light.update(disabled=True)
            text_elem.update(f'Состояние: Газ:{"Стоит" if status_gas == 0 else "Движение"}, {status_gas}, '
                             f'Дверь:{status_door} , Свет:{status_light}')



window.close()