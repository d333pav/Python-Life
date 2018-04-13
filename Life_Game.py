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


def life(lines_number=0, columns_number=0, turns_number=0, ocean_array=[]):
    for i in range(turns_number):
        new_ocean = [['n'] * columns_number for i in range(lines_number)]
        for x in range(lines_number):
            for y in range(columns_number):
                if ocean_array[x][y] == 'r':
                    new_ocean[x][y] = 'r'
                else:
                    dict_fishes = {
                        's': Shrimp(),
                        'f': Fish()
                    }
                    for j1 in range(-1, 2):
                        for j2 in range(-1, 2):
                            if (j1 != 0 or j2 != 0) and lines_number > x + j1 > -1 and columns_number > y + j2 > -1\
                                    and ocean_array[x + j1][y + j2] != 'n' and ocean_array[x + j1][y + j2] != 'r':
                                dict_fishes[ocean_array[x + j1][y + j2]].add_nei()
                    for s in dict_fishes:
                        if ocean_array[x][y] == s and dict_fishes[s].stay_alive():
                            new_ocean[x][y] = s
                        if ocean_array[x][y] == 'n' and dict_fishes[s].new_fish():
                            new_ocean[x][y] = s
                    '''
                    if a[x][y] == 's' and dict_fishes['s'].stay_alive():
                        b[x][y] = 's'
                    if a[x][y] == 'f' and dict_fishes['f'].stay_alive():
                        b[x][y] = 'f'
                    if a[x][y] == 'n' and dict_fishes['s'].new_fish():
                        b[x][y] = 's'
                    if a[x][y] == 'n' and dict_fishes['f'].new_fish():
                        b[x][y] = 'f'
                    '''
        ocean_array = new_ocean
    return ocean_array
