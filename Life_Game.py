from collections import OrderedDict


class Fish:
    nei_count = 0  # количество соседей

    def add_nei(self):  # функция добавления соседа
        self.nei_count += 1

    def stay_alive(self):  # условия для продолжения жизни
        if self.nei_count == 2 or self.nei_count == 3:
            return True
        else:
            return False

    def new_fish(self):  # условие появления новой рыбы
        if self.nei_count == 3:
            return True
        else:
            return False


class Shrimp(Fish):
    pass


def life(info_list=[0, 0, 0], ocean_array=[]):
    lines_number = info_list[0]  # количество строк в океане
    columns_number = info_list[1]  # количество столбцов
    turns_number = info_list[2]  # количество раз обновления океана
    for turn in range(turns_number):
        new_ocean = [['n'] * columns_number for line in range(lines_number)]
        for x in range(lines_number):
            for y in range(columns_number):
                if ocean_array[x][y] == 'r':
                    new_ocean[x][y] = 'r'
                else:
                    dict_fish = OrderedDict()
                    dict_fish['s'] = Shrimp()
                    dict_fish['f'] = Fish()
                    for nei_x in range(x-1, x+2):
                        for nei_y in range(y-1, y+2):
                            if (nei_x != x or nei_y != y)\
                                    and lines_number > nei_x > -1\
                                    and columns_number > nei_y > -1\
                                    and ocean_array[nei_x][nei_y] != 'n'\
                                    and ocean_array[nei_x][nei_y] != 'r':
                                dict_fish[ocean_array[nei_x][nei_y]].add_nei()
                    if ocean_array[x][y] == 'n':
                        for fish in dict_fish:
                            if dict_fish[fish].new_fish():
                                new_ocean[x][y] = fish
                    else:
                        if dict_fish[ocean_array[x][y]].stay_alive():
                            new_ocean[x][y] = ocean_array[x][y]
        ocean_array = new_ocean
    return ocean_array
