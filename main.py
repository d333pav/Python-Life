import Life_Game
import argparse
import sys


def calculate_ocean(input_path, output_path):
    info_list = []  # массив с данными о размере океана и количестве итераций
    ocean_array = []  # массив с информацией об океане
    if input_path:
        try:
            input_file = open(input_path, 'r')
        except FileNotFoundError:
            print('Неверный путь к файлу')
            sys.exit(1)
        info_list = list(map(int, input_file.readline().strip().split()))
        for line in input_file:
            line = line.replace('\n', '')
            ocean_array.append(list(line))
        input_file.close()
        ocean_array = Life_Game.life(info_list, ocean_array)
        if not output_path:
            index = input_path.rfind('\\')
            if index != -1:
                output_path = input_path[:index + 1]
            output_file = open(output_path + 'ocean_output.txt', 'w')
        else:
            output_file = open(output_path, 'w')
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
    parser.add_argument('-input', dest='input')
    parser.add_argument('-output', dest='output')
    # если есть параметр -file то будем считывать данные из файла
    input_path = parser.parse_args().input
    output_path = parser.parse_args().output
    calculate_ocean(input_path, output_path)
