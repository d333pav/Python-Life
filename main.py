import Life_Game
import argparse
import sys


def fun(file_path):
    info_list = []  # массив с данными о размере океана и количестве итераций
    ocean_array = []  # массив с информацией об океане
    if file_path:
        try:
            input_file = open(file_path, 'r')
        except FileNotFoundError:
            print('Неверный путь к файлу')
            sys.exit(1)
        first_line = True
        for line in input_file:
            if first_line:  # считываем основные данные только из первой строки
                first_line = False
                info_list = list(map(int, line.strip().split()))
            else:
                line = line.replace('\n', '')
                ocean_array.append(list(line))
        input_file.close()
        ocean_array = Life_Game.life(info_list, ocean_array)
        index = file_path.rfind('\\')
        if index != -1:
            file_path = file_path[:index + 1]
        output_file = open(file_path + 'ocean_output.txt', 'w')
        for x in range(info_list[0]):
            for y in range(info_list[1]):
                output_file.write(ocean_array[x][y])
            output_file.write('\n')
        output_file.close()
    else:
        info_list = list(map(int, input().strip().split()))
        ocean_array = []
        for i in range(info_list[0]):
            ocean_array.append(list(input()))
        ocean_array = Life_Game.life(info_list, ocean_array)
        for i in range(info_list[0]):
            print(''.join(ocean_array[i]))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', dest='file')
    # если есть параметр -file то будем считывать данные из файла
    path = parser.parse_args().file
    fun(path)
