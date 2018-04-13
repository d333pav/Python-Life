import Life_Game


def fun():
    lines_number = 0  # количество строк в океане
    columns_number = 0  # количество столбцов
    turns_number = 0  # количество раз обновления океана
    ocean_array = []  # массив с информацией об океане
    print('Ввод/вывод из файла?')
    if str(input()) == 'да':
        input_file = open('ocean_input.txt', 'r')
        i = True
        for line in input_file:
            if i:  # считываем основные данные только из первой строки
                i = False
                input_list = line.split()
                lines_number = int(input_list[0])
                columns_number = int(input_list[1])
                turns_number = int(input_list[2])
            else:
                line = line.replace('\n', '')
                ocean_array.append(list(line))
        input_file.close()
        ocean_array = Life_Game.life(lines_number, columns_number, turns_number, ocean_array)
        output_file = open('ocean_output.txt', 'w')
        for i in range(lines_number):
            for j in range(columns_number):
                output_file.write(ocean_array[i][j])
            output_file.write('\n')
        output_file.close()
    else:
        input_list = input().split()
        lines_number = int(input_list[0])
        columns_number = int(input_list[1])
        turns_number = int(input_list[2])
        ocean_array = []
        for i in range(lines_number):
            ocean_array.append(list(input()))
        ocean_array = Life_Game.life(lines_number, columns_number, turns_number, ocean_array)
        for i in range(lines_number):
            print(''.join(ocean_array[i]))


if __name__ == "__main__":
    fun()
