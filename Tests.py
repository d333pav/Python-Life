import unittest
import Life_Game


def life_test(num=1):
    test_file = open('tests/test'+str(num)+'.txt', 'r')
    lines_number = 0
    columns_number = 0
    turns_number = 0
    i = True
    ocean_array = []
    for line in test_file:
        if i:  # считываем основные данные только из первой строки
            i = False
            input_list = line.split()
            lines_number = int(input_list[0])
            columns_number = int(input_list[1])
            turns_number = int(input_list[2])
        else:
            line = line.replace('\n', '')
            ocean_array.append(list(line))
    test_file.close()
    ocean_array = Life_Game.life(lines_number, columns_number, turns_number, ocean_array)
    return ocean_array


def fread_ans(num=1):
    f = open('tests/test' + str(num) + '_ans.txt', 'r')
    a = []
    for line in f:
        line = line.replace('\n', '')
        a.append(list(line))
    f.close()
    return a


class TestOcean(unittest.TestCase):
    def test1(self):
        test_ocean = life_test(1)
        expect_ocean = fread_ans(1)
        self.assertEqual(test_ocean, expect_ocean)

    def test2(self):
        test_ocean = life_test(2)
        expect_ocean = fread_ans(2)
        self.assertEqual(test_ocean, expect_ocean)

    def test3(self):
        test_ocean = life_test(3)
        expect_ocean = fread_ans(3)
        self.assertEqual(test_ocean, expect_ocean)

    def test4(self):
        test_ocean = life_test(4)
        expect_ocean = fread_ans(4)
        self.assertEqual(test_ocean, expect_ocean)


if __name__ == '__main__':
    unittest.main()
    n = input()
