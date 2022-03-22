import unittest
from DateDifferenceClass import DateDifferenceClass
from DateDifferenceService import readInput, diffCalculator

class UnitTest(unittest.TestCase):
  def test_WhenInputIsInvalid_then_ShouldThrowException(self):
    val1 = 'aa/bb/cccc'
    with self.assertRaises(Exception):
      readInput(val1)
      
  def test_WhenBothStartAndEndDatesAreTheSame_then_ShouldReturn0(self):
    date1 = DateDifferenceClass(1, 1, 2021)
    date2 = DateDifferenceClass(1, 1, 2021)
    self.assertEqual(diffCalculator(date1, date2), 0)

  def test_WhenStartDateIs02061983AndEndDate22061983_then_ShouldShow19days(self):
    date1 = DateDifferenceClass(2, 6, 1983)
    date2 = DateDifferenceClass(22, 6, 1983)
    self.assertEqual(diffCalculator(date1, date2), 19)

  def test_WhenStartDateIs03082021AndEndDate04082021_then_ShouldShow0days(self):
    date1 = DateDifferenceClass(3, 8, 2021)
    date2 = DateDifferenceClass(4, 8, 2021)
    self.assertEqual(diffCalculator(date1, date2), 0)

  def test_WhenStartDateIs01012021AndEndDate03012021_then_ShouldShow0days(self):
    date1 = DateDifferenceClass(1, 1, 2021)
    date2 = DateDifferenceClass(3, 1, 2021)
    self.assertEqual(diffCalculator(date1, date2), 1)

  def test_WhenStartDateIs04071984AndEndDate25121984_then_ShouldShow0days(self):
    date1 = DateDifferenceClass(4, 7, 1984)
    date2 = DateDifferenceClass(25, 12, 1984)
    self.assertEqual(diffCalculator(date1, date2), 173)

  def test_WhenStartDateIs03011989AndEndDate03081983_then_ShouldShow0days(self):
    date1 = DateDifferenceClass(3, 1, 1989)
    date2 = DateDifferenceClass(3, 8, 1983)
    self.assertEqual(diffCalculator(date1, date2), 1979)

if __name__ == '__main__' :
  unittest.main()