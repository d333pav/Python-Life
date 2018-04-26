import unittest
import Life_Game


def life_test(name=''):
    test_file = open('tests/test_'+name+'.txt', 'r')
    first_line = True
    info_list = []
    ocean_array = []
    for line in test_file:
        if first_line:  # считываем основные информацию только из первой строки
            first_line = False
            info_list = list(map(int, line.strip().split()))
        else:
            line = line.replace('\n', '')
            ocean_array.append(list(line))
    test_file.close()
    ocean_array = Life_Game.life(info_list, ocean_array)
    return ocean_array


def fread_ans(name=''):
    test_file = open('tests/test_' + name + '_ans.txt', 'r')
    ocean_array = []
    for line in test_file:
        line = line.replace('\n', '')
        ocean_array.append(list(line))
    test_file.close()
    return ocean_array


class TestOcean(unittest.TestCase):
    def test_simple(self):
        name = 'simple'
        test_ocean = life_test(name)
        expect_ocean = fread_ans(name)
        self.assertEqual(test_ocean, expect_ocean)

    def test_order(self):
        name = 'order'
        test_ocean = life_test(name)
        expect_ocean = fread_ans(name)
        self.assertEqual(test_ocean, expect_ocean)

    def test_big(self):
        name = 'big'
        test_ocean = life_test(name)
        expect_ocean = fread_ans(name)
        self.assertEqual(test_ocean, expect_ocean)

    def test_iterations(self):
        name = 'iterations'
        test_ocean = life_test(name)
        expect_ocean = fread_ans(name)
        self.assertEqual(test_ocean, expect_ocean)


if __name__ == '__main__':
    unittest.main()
