import unittest

from main import get_saturdays, get_billboard_top_100

class TestGetSaturdays(unittest.TestCase):
    def test_march_2018(self):
        expected = [
                '2018-03-03',
                '2018-03-10',
                '2018-03-17',
                '2018-03-24',
                '2018-03-31'
        ]
        actual = get_saturdays(2018, 3, 2018, 3)
        self.assertEquals(expected, actual)

    def test_october_2018(self):
        expected = [
                '2018-10-06',
                '2018-10-13',
                '2018-10-20',
                '2018-10-27'
        ]
        actual = get_saturdays(2018, 10, 2018, 10)
        self.assertEquals(expected, actual)

    def test_december_2017_to_january_2018(self):
        expected = [
                '2017-12-02',
                '2017-12-09',
                '2017-12-16',
                '2017-12-23',
                '2017-12-30',
                '2018-01-06',
                '2018-01-13',
                '2018-01-20',
                '2018-01-27'
        ]
        actual = get_saturdays(2017, 12, 2018, 1)
        self.assertEquals(expected, actual)

    def test_january_2018_to_february_2018(self):
        expected = [
                '2018-01-06',
                '2018-01-13',
                '2018-01-20',
                '2018-01-27',
                '2018-02-03',
                '2018-02-10',
                '2018-02-17',
                '2018-02-24'
        ]
        actual = get_saturdays(2018, 1, 2018, 2)
        self.assertEquals(expected, actual)

class TestGetBillboardTop100(unittest.TestCase):
    def test_week_of_april_14_2018(self):
        songs = get_billboard_top_100('2018-04-14')
        expected = 'Drake - God\'s Plan'
        actual = songs[0]
        self.assertEquals(expected, actual)

if __name__ == '__main__':
    unittest.main()
