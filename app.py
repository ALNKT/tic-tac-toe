import random


class Cell:

    def __init__(self, number, value=' '):
        self.number = number
        self.value = value

    def check_cell(self):
        if self.value == ' ':
            return False
        return True


class Board:

    def __init__(self):
        self.field = [[Cell(j + i) for i in range(1, 4)] for j in range(0, 9, 3)]

    def create_cell(self, position, value):
        for i_position in self.field:
            for i_number in i_position:
                num = i_number.number
                if position == num:
                    if not i_number.check_cell():
                        i_number.value = value


class Player:

    def __init__(self, name, position='', symbol=''):
        self.name = name
        self.position = position
        self.symbol = symbol


def print_board(board):
    for index, i_ceil in enumerate(board.field):
        print(' {} | {} | {} '.format(*[i_number.value for i_number in i_ceil]))
        if index != 2:
            print('---|---|---')


def check_winner(current_board, sym):
    for i_lst_cells in current_board:
        if len([i_cell.value for i_cell in i_lst_cells if
                i_cell.value == sym]) == 3:  # Проверяем одинаковые символы в строках матрицы
            return True
    if len([i_lst_cell[0].value for i_lst_cell in current_board if
            i_lst_cell[0].value == sym]) == 3:  # Проверяем одинаковые символы в 1-м столбце матрицы
        return True
    elif len([i_lst_cell[1].value for i_lst_cell in current_board if
              i_lst_cell[1].value == sym]) == 3:  # Проверяем одинаковые символы во 2-м столбце матрицы
        return True
    elif len([i_lst_cell[2].value for i_lst_cell in current_board if
              i_lst_cell[2].value == sym]) == 3:  # Проверяем одинаковые символы в 3-м столбце матрицы
        return True
    elif len([current_board[i][i].value for i in range(3)
              if current_board[i][i].value == sym]) == 3:  # Проверяем одинаковые символы по главной диагонали матрицы
        return True
    elif len([current_board[2 - i][i].value for i in range(2, -1, -1) if
              current_board[2 - i][i].value == sym]) == 3:  # Проверяем одинаковые символы по побочной диагонали матрицы
        return True
    return False


def print_rules(board):
    print('''\n{}
Поле имеет размер 3х3. Каждая клетка поля пронумерована от 1 до 9 (включительно).
Для того, чтобы установить свое значение в клетку, Вам необходимо указать номер этой клетки в поле для ввода.
Поле пронумеровано следующим образом:'''.format('Правила игры:'.center(80)))
    for index, i_ceil in enumerate(board.field):
        print(' {} | {} | {} '.format(*[i_number.number for i_number in i_ceil]))
        if index != 2:
            print('---|---|---')


def start_game():
    one_more = 'да'

    while one_more == 'да':
        print('Добро пожаловать в игру крестики-нолики!')
        board = Board()
        player = Player(input('Введите ваше имя: '))
        player.symbol = input('Введите символ для игры ("x" или "0"): ')

        while player.symbol not in 'xх0o':
            player.symbol = input('Введите корректный символ для игры ("x" или "0"): ')

        opponent = int(input(f'{player.name}, выберите оппонента: компьютер (1), второй игрок (2): '))
        if opponent == 1:
            comp = Player('Компьютер')
        if opponent == 2:
            comp = Player(input('Введите ваше имя: '))

        if player.symbol in 'xх':
            comp.symbol = '0'
        else:
            comp.symbol = 'x'

        print(f'\nРады Вас приветствовать, {player.name}! Давайте начнём!')
        rules = int(input('Чтобы прочитать правила, введите 1, если Вы знаете правила, введите 0: '))

        if rules:
            print_rules(board)

        lst_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        while len(lst_pos) > 0:
            player.position = int(input(f'{player.name}, введите номер клетки: '))
            while player.position not in lst_pos:
                player.position = int(input(f'{player.name}, некорректный ввод. Введите позицию: '))
            lst_pos.remove(player.position)
            board.create_cell(player.position, player.symbol)
            if opponent == 2:
                print_board(board)
            if check_winner(board.field, player.symbol):
                print(f'\n{"У нас есть победитель!".center(70)}\n{player.name}. Поздравляем!!!')
                print_board(board)
                break
            if opponent == 1:
                if len(lst_pos) != 0:
                    print('Ход компьютера')
                    while comp.position not in lst_pos:
                        comp.position = random.choice(lst_pos)
                    lst_pos.remove(comp.position)
            else:
                if len(lst_pos) != 0:
                    comp.position = int(input(f'{comp.name}, введите номер клетки: '))
                    while comp.position not in lst_pos:
                        comp.position = int(input(f'{comp.name}, некорректный ввод. Введите позицию: '))
                    lst_pos.remove(comp.position)
            board.create_cell(comp.position, comp.symbol)
            if check_winner(board.field, comp.symbol):
                print(
                    f'\n{"У нас есть победитель!".center(70)}\nЭто {comp.name}!\n{player.name}, не расстраивайтесь, '
                    f'повезет в другой раз!')
                print_board(board)
                break
            print_board(board)
        else:
            print('Ничья!')
        one_more = input('\nСыграем еще раз? ')


if __name__ == '__main__':
    start_game()
