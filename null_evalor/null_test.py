import unittest
from pandas import DataFrame
from null_evalor.null_eval import assess_NA

class TestNullers(unitest.TestNulls):
    def setUp(self):
        df  = DataFrame({'a': [3, np.nan, 4, 6, np.nan, 5, 3],
                  'b': [np.nan, np.nan, 4, 6, np.nan, 5, np.nan],
                  'c': [np.nan, np.nan, np.nan, np.nan, np.nan, 5, np.nan],
                  'd': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]})
    def test_shape(self):
        assertEqual(df.shape,(7,4))


if __name__ == "__main__":
    unittest.main()

