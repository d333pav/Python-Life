import unittest
import Life_Game


def life_test(info_list=[], test=''):
    ocean_array = []
    for element in test.split():
        ocean_array.append(list(element))
    ocean_array = Life_Game.life(info_list, ocean_array)
    answer = ''
    for line_num in range(info_list[0]):
        answer += ' ' + ''.join(ocean_array[line_num])
    answer = answer[1:]
    return answer


def read_ans(ans):
    ocean_array = []
    for line in ans.split():
        ocean_array.append(list(line))
    return ocean_array


class TestOcean(unittest.TestCase):
    def test_fish(self):
        self.assertEqual(life_test([3, 3, 1], 'nff fff fff'), 'fnf nnn fnf')

    def test_shrimp(self):
        self.assertEqual(life_test([3, 3, 1], 'ssn nnn sss'), 'nnn nns nsn')

    def test_order(self):
        self.assertEqual(life_test([3, 3, 1], 'fff nnn sss'), 'nfn nfn nsn')

    def test_rock(self):
        self.assertEqual(life_test([3, 3, 1], 'rrr nrn rrr'), 'rrr nrn rrr')

if __name__ == '__main__':
    unittest.main()
