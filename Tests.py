import unittest
import Life_Game


def life_test(test=''):
    el_num = 0  # номер элемента
    info_list = []
    ocean_array = []
    for element in test.split():
        if el_num < 3:  # считываем основные информацию только
            # из первых трех элементов
            info_list.append(int(element))
            el_num += 1
        else:
            ocean_array.append(list(element))
    ocean_array = Life_Game.life(info_list, ocean_array)
    return ocean_array


def read_ans(ans):
    ocean_array = []
    for line in ans.split():
        ocean_array.append(list(line))
    return ocean_array


class TestOcean(unittest.TestCase):
    def test_simple(self):
        test = '3 3 1 nff fff fff'
        ans = 'fnf nnn fnf'
        test_ocean = life_test(test)
        expect_ocean = read_ans(ans)
        self.assertEqual(test_ocean, expect_ocean)

    def test_order(self):
        test = '3 3 1 fff nnn sss'
        ans = 'nfn nfn nsn'
        test_ocean = life_test(test)
        expect_ocean = read_ans(ans)
        self.assertEqual(test_ocean, expect_ocean)

    def test_rocks(self):
        test = '3 3 1 rnr srf rnr'
        ans = 'rnr nrn rnr'
        test_ocean = life_test(test)
        expect_ocean = read_ans(ans)
        self.assertEqual(test_ocean, expect_ocean)


if __name__ == '__main__':
    unittest.main()
