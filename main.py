import Life_Game
import argparse
import sys


def calculate_ocean(input_path, output_path):
    stdin = input
    if input_path:
        try:
            input_file = open(input_path, 'r')
            stdin = input_file.readline
        except FileNotFoundError:
            print('Неверный путь к файлу')
            sys.exit(1)
    info_list = list(map(int, stdin().strip().split()))
    lines_number = info_list[0]
    columns_number = info_list[1]
    turns_number = info_list[2]
    # массив с данными о размере океана и количестве итераций
    ocean_array = []  # массив с информацией об океане
    for line_num in range(lines_number):
        ocean_array.append(list(stdin().replace('\n', '')))
    if input_path:
        input_file.close()
    ocean_array = Life_Game.life(lines_number, columns_number,
                                 turns_number, ocean_array)
    if output_path:
        output_file = open(output_path, 'w')
        for line_num in range(lines_number):
            output_file.write(''.join(ocean_array[line_num])+'\n')
        output_file.close()
    else:
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
