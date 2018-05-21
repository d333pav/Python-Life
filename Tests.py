import unittest
import Life_Game


def life_test(lines_number=0, columns_number=0, turns_number=0, test=''):
    ocean_array = []
    for element in test.split():
        ocean_array.append(list(element))
    ocean_array = Life_Game.life(lines_number, columns_number,
                                 turns_number, ocean_array)
    answer = ''
    for line_num in range(lines_number):
        answer += ' ' + ''.join(ocean_array[line_num])
    answer = answer[1:]
    return answer


def nei_finder_test(lines_number=0, columns_number=0, test='', x=0, y=0):
    ocean_array = []
    for element in test.split():
        ocean_array.append(list(element))
    dict_test = Life_Game.nei_finder(lines_number, columns_number,
                                     ocean_array, x, y)
    answer = {}
    for fish in dict_test:
        answer[fish] = dict_test['s'].get_nei()[fish]
    return answer


class TestOcean(unittest.TestCase):
    def test_fish(self):
        self.assertEqual(life_test(3, 3, 1, 'nff fff fff'), 'fnf nnn fnf')

    def test_shrimp(self):
        self.assertEqual(life_test(3, 3, 1, 'ssn nnn sss'), 'nnn nns nsn')

    def test_order(self):
        self.assertEqual(life_test(3, 3, 1, 'fff nnn sss'), 'nfn nfn nsn')

    def test_rock(self):
        self.assertEqual(life_test(3, 3, 1, 'rrr nrn rrr'), 'rrr nrn rrr')

    def test_mix(self):
        self.assertEqual(life_test(3, 3, 1, 'ssf nrn sff'), 'nnn srf nnn')

    def test_nei_corner(self):
        self.assertEqual(nei_finder_test(3, 3, 'fff fnn nnn', 0, 0),
                         {'r': 0, 'f': 2, 's': 0})

    def test_nei_center(self):
        self.assertEqual(nei_finder_test(3, 3, 'ffs rnr nnf', 1, 1),
                         {'r': 2, 'f': 3, 's': 1})


if __name__ == '__main__':
    unittest.main()
