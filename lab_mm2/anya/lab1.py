button = ['rejim', 'power', 'work']
rejim = ['cold', 'hot']
power = ['turn_off', 'turn_on']

current_rejim = 0
current_power = 0
current_time = 0

def print_status():
    print('Питание= ',power[current_power], '| Режим= ', rejim[current_rejim], '| Время работы ', current_time)

def calculsting_status(key, current_rejim, current_power, current_time):
    if key == 'power':
        if current_power == 1:
            current_power = 0
            current_rejim = 0
            current_time = 0
        else:
            current_power = 1
    elif key == 'rejim':
        if current_power == 1:
            if current_rejim == 1:
                current_rejim = 0
            else:
                current_rejim = 1
        else:
            print('\"Приятный звук кнопки, которая ничего не сделала\"')
    elif key == 'work':
        if current_power == 1:
            current_time+=1
        else:
            print('\"Приятный звук кнопки, которая ничего не сделала\"')
    return current_rejim, current_power, current_time


while(True):
    print('Текущее состояние: ')
    print_status()

    print('Кнопки: ', button)
    key = input()
    if key == 'exit':
        break
    current_rejim, current_power, current_time = calculsting_status(key, current_rejim, current_power, current_time)

