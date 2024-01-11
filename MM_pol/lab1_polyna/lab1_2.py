'''
В лифте есть 9 кнопок, соответствующих этажам, и кнопка открытия/закрытия дверей.
Нажатием на каждую кнопку сопровождается движение лифта на соответствующий этаж.
Движение от этажа к этажу осуществляется в течение одной минуты (в условных единицах времени).
Двери могут открываться во время остановки и не могут – во время движения.
При нажатии кнопки этажа с открытыми дверьми двери автоматически закрываются.
С одного этажа на один и тот же этаж лифт в движение не приводится.
Счётчик этажей реализовать визуально.
Начальная конфигурация:  лифт на первом этаже двери открыты.
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

async def sleep(button_door, window, text_elem):
    global status_end_floor
    global status_floor
    global status_door
    status_door = False
    button_door.update(disabled=True)
    if status_end_floor > status_floor:
        step = 1
    else:
        step = -1
    while status_floor != status_end_floor:
        await asyncio.sleep(1.5)
        text_last = window[text[status_floor]]
        text_last.update(f'')
        status_floor+=step
        text_now = window[text[status_floor]]
        text_now.update(f'|😀|')
        text_elem.update(f'Состояние: Этаж:{status_floor}, Дверь:{"Закрыта" if not status_door else "Открыта"}')
    else:
        for i in fun:
            if i != 0:
                button = window[i]
                button.update(disabled=False)
        button_door.update(disabled=False)


loop = asyncio.new_event_loop()
# Create the new thread, giving loop as argument
t = Thread(target=asyncloop, args=(loop,))
# Start the thread
t.start()


status_floor = 1
status_door = True
layout = [
    [sg.Button('9',enable_events=True, key='-F9-', font='Helvetica 16'), sg.Text(f'', key='-text9-', font='Helvetica 16')],
    [sg.Button('8',enable_events=True, key='-F8-', font='Helvetica 16'), sg.Text(f'', key='-text8-', font='Helvetica 16')],
    [sg.Button('7',enable_events=True, key='-F7-', font='Helvetica 16'), sg.Text(f'', key='-text7-', font='Helvetica 16')],
    [sg.Button('6',enable_events=True, key='-F6-', font='Helvetica 16'), sg.Text(f'', key='-text6-', font='Helvetica 16')],
    [sg.Button('5',enable_events=True, key='-F5-', font='Helvetica 16'), sg.Text(f'', key='-text5-', font='Helvetica 16')],
    [sg.Button('4',enable_events=True, key='-F4-', font='Helvetica 16'), sg.Text(f'', key='-text4-', font='Helvetica 16')],
    [sg.Button('3',enable_events=True, key='-F3-', font='Helvetica 16'), sg.Text(f'', key='-text3-', font='Helvetica 16')],
    [sg.Button('2',enable_events=True, key='-F2-', font='Helvetica 16'), sg.Text(f'', key='-text2-', font='Helvetica 16')],
    [sg.Button('1',enable_events=True, key='-F1-', font='Helvetica 16'), sg.Text(f'😀|', key='-text1-', font='Helvetica 16')],
    [sg.Button('Открыть / закрыть',enable_events=True, key='-FUNCTION1-', font='Helvetica 16')],
    [sg.Text(f'Состояние: Этаж:{status_floor}, Дверь:{"Закрыта" if not status_door else "Открыта"}', key='-text-', font='Helvetica 16')],

]


sg.theme('LightBrown1')

window = sg.Window('Лифт', layout, size=(400,550))
fun = [0]
text = [0]
for i in range(1, 10):
    fun.append(f'-F{i}-')
    text.append(f'-text{i}-')


while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == '-FUNCTION1-':
        text_elem = window['-text-']
        if status_door == True:
            status_door = False
            text_now = window[text[status_floor]]
            text_now.update(f'|😀|')
            text_elem.update(f'Состояние: Этаж:{status_floor}, Дверь:{"Закрыта" if not status_door else "Открыта"}')
        else:
            status_door = True
            text_now = window[text[status_floor]]
            text_now.update(f'😀|')
            text_elem.update(f'Состояние: Этаж:{status_floor}, Дверь:{"Закрыта" if not status_door else "Открыта"}')
        text_elem.update(f'Состояние: Этаж:{status_floor}, Дверь:{"Закрыта" if not status_door else "Открыта"}')
    elif event == '-F1-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 1:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 1
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)
    elif event == '-F2-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 2:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 2
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)
    elif event == '-F3-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 3:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 3
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)
    elif event == '-F4-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 4:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 4
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)
    elif event == '-F5-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 5:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 5
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)

    elif event == '-F6-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 6:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 6
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)

    elif event == '-F7-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 7:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 7
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)

    elif event == '-F8-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 8:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 8
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)

    elif event == '-F9-':
        button_door = window['-FUNCTION1-']
        text_elem = window['-text-']
        if status_floor != 9:
            status_door = False
            for i in fun:
                if i != 0:
                    button = window[i]
                    button.update(disabled=True)
            status_end_floor = 9
            asyncio.run_coroutine_threadsafe(sleep(button_door, window, text_elem), loop)


