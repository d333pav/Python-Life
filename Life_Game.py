class Animal:
    symbol = ''
    nei_dict = {}

    def set_nei_dict(self, cur_dict={}):
        self.nei_dict = cur_dict

    def get_nei(self):
        return self.nei_dict

    def add_nei(self):
        pass

    def stay_alive(self):
        pass

    def new_fish(self):
        pass

    def action(self, cur_elem='n', new_elem='n'):
        pass


class Fish(Animal):
    symbol = 'f'

    def stay_alive(self):  # условия для продолжения жизни
        if self.nei_dict[self.symbol] == 2 or self.nei_dict[self.symbol] == 3:
            return self.symbol
        else:
            return 'n'

    def new_fish(self):  # условие появления новой рыбы
        if self.nei_dict[self.symbol] == 3:
            return self.symbol
        else:
            return 'n'

    def action(self, cur_element='n', new_element='n'):
        # производим действие основываясь на текущем элементе в океане
        # и предложенным, другими видами
        # cur_elem - текущий элемент, new_elem - тот,
        # который прелагается поставить
        if cur_element == 'n':
            return self.new_fish()
        elif cur_element == self.symbol:
            return self.stay_alive()


class Shrimp(Animal):
    symbol = 's'

    def stay_alive(self):  # условия для продолжения жизни
        if self.nei_dict[self.symbol] == 2 or self.nei_dict[self.symbol] == 3:
            return self.symbol
        else:
            return 'n'

    def new_fish(self):  # условие появления новой рыбы
        if self.nei_dict[self.symbol] == 3:
            return self.symbol
        else:
            return 'n'

    def action(self, cur_elem='n', new_elem='n'):
        if cur_elem == 'n' and new_elem == 'n':
            return self.new_fish()
        elif cur_elem == self.symbol:
            return self.stay_alive()


class Rock(Animal):
    symbol = 'r'

    def action(self, cur_elem='n', new_elem='n'):
        return self.symbol if cur_elem == self.symbol else new_elem

    def stay_alive(self):
        return self.symbol


def sub_finder(obj, dict_fish={}):
    for sub in obj.__subclasses__():
        if dict_fish.get(sub.symbol) is None:
            dict_fish[sub.symbol] = sub()
            sub_finder(sub, dict_fish)
    return dict_fish


def nei_finder(lines_number=0, columns_number=0, ocean_array=[], x=0, y=0):
    new_dict = {}  # словарь для хранения классов
    new_dict = sub_finder(Animal, new_dict)
    nei_dict = {fish: 0 for fish in new_dict}
    # словарь с количеством соседей данной клетки
    for fish in new_dict:
        new_dict[fish].set_nei_dict(nei_dict)
    for nei_x in range(x - 1, x + 2):
        for nei_y in range(y - 1, y + 2):
            if (nei_x != x or nei_y != y) \
                    and lines_number > nei_x > -1 \
                    and columns_number > nei_y > -1 \
                    and ocean_array[nei_x][nei_y] != 'n':
                nei_dict[ocean_array[nei_x][nei_y]] += 1
    return new_dict


def life(lines_number=0, columns_number=0, turns_number=0, ocean_array=[]):
    # количество строк в океане
    # количество столбцов
    # количество раз обновления океана
    # сам океан

    for turn in range(turns_number):
        new_ocean = ['n']*lines_number  # создание пустого океана
        for line in range(lines_number):
            new_ocean[line] = ['n']*columns_number

        for x in range(lines_number):
            for y in range(columns_number):
                current_dict = nei_finder(lines_number, columns_number,
                                          ocean_array, x, y)
                if ocean_array[x][y] == 'n':
                    for fish in current_dict:
                        new_element = current_dict[fish]. \
                            action(ocean_array[x][y], new_ocean[x][y])
                        if new_element:
                            new_ocean[x][y] = new_element
                else:
                    new_ocean[x][y] = current_dict[ocean_array[x][y]]. \
                        stay_alive()
        ocean_array = new_ocean
    return ocean_array
