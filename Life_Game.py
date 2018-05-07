import copy


class Animal:
    pass


class Fish(Animal):
    symbol = 'f'
    nei_count = 0  # количество соседей

    def add_nei(self):  # функция добавления соседа
        self.nei_count += 1

    def stay_alive(self):  # условия для продолжения жизни
        if self.nei_count == 2 or self.nei_count == 3:
            return self.symbol
        else:
            return 'n'

    def new_fish(self):  # условие появления новой рыбы
        if self.nei_count == 3:
            return self.symbol
        else:
            return 'n'

    def action(self, elem='n', new_elem='n'):  # производим действие\
        # основываясь на текущем элементе в океане и уже предложенным
        if elem == 'n':
            return self.new_fish()
        elif elem == self.symbol:
            return self.stay_alive()


class Shrimp(Fish):
    symbol = 's'

    def action(self, elem='n', new_elem='n'):
        if elem == 'n' and new_elem == 'n':
            return self.new_fish()
        elif elem == self.symbol:
            return self.stay_alive()


def life(info_list=[0, 0, 0], ocean_array=[]):
    lines_number = info_list[0]  # количество строк в океане
    columns_number = info_list[1]  # количество столбцов
    turns_number = info_list[2]  # количество раз обновления океана
    dict_fish = {}  # словарь для хранения классов

    def sub_finder(obj):
        for sub in obj.__subclasses__():
            if dict_fish.get(sub.symbol) is None:
                dict_fish[sub.symbol] = sub()
                sub_finder(sub)
    sub_finder(Animal)
    for turn in range(turns_number):
        new_ocean = copy.deepcopy(ocean_array)
        for x in range(lines_number):
            for y in range(columns_number):
                current_dict = copy.deepcopy(dict_fish)
                for nei_x in range(x - 1, x + 2):
                    for nei_y in range(y - 1, y + 2):
                        if (nei_x != x or nei_y != y) \
                                and lines_number > nei_x > -1 \
                                and columns_number > nei_y > -1 \
                                and ocean_array[nei_x][nei_y] != 'n' \
                                and ocean_array[nei_x][nei_y] != 'r':
                            current_dict[ocean_array[nei_x][nei_y]]. \
                                add_nei()
                    for fish in current_dict:
                        new_element = current_dict[fish].\
                            action(ocean_array[x][y], new_ocean[x][y])
                        if new_element:
                            new_ocean[x][y] = new_element
        ocean_array = new_ocean
    return ocean_array
