'''
3. Светофор
Светофор может иметь 4 состояния: «красный», «жёлтый», «зелёный», «жёлтый
мигающий». Светофор управляется вручную оператором с помощью 3-х кнопок. Две
кнопки – это кнопки управления движением Ý и ß, которыми оператор переключает
состояния «красный», «жёлтый», «зелёный» в соответствии с их нормальной
последовательностью (кр-жёл-зел или зел-жёл-кр, кр-жёл-кр, зел-жёл-зел, но не  кр-зел,
зел-кр). При нажатии на третью кнопку «работа» светофор переключается с любого
состояния в состояние «жёлтый мигающий». В этом состоянии нажатие на кнопки Ý и ß
ничего не вызывает. Из состояния «жёлтый мигающий» нажатием кнопки «работа»
светофор переключается в состояние «жёлтый». Начальная конфигурация состояние:
«жёлтый мигающий».
'''
def print_traffic_light(states, current_state):
    print(f'Текущее состояние: {states[current_state]}')

def print_button(current_state, button):
    if current_state != 3:
        return button
    else:
        return ['work']


def change_traffic(key, current_state):
    if key == 'up':
        if current_state != 2:
            current_state += 1
        else: current_state = 0
    elif key == 'down':
        if current_state != 0:
            current_state -= 1
        else: current_state = 2
    elif current_state == 3:
        current_state = 1
    else:
        current_state = 3
    return current_state


button = ['up', 'work','down']
states = ['green', 'yellow', 'red', 'flashing_yellow']
key = ''
current_state = 3

while (True):
    print_traffic_light(states, current_state)
    print('Доступные кнопки: \n', print_button(current_state, button))
    key = input()
    if key == 'exit':
        break
    current_state = change_traffic(key, current_state)




