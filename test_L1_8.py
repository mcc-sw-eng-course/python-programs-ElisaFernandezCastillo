import unittest
from L1_8 import calcMean, calcStdDev, calcPercentile, calcMedian, calcQuartile


class TestL1_8(unittest.TestCase):
    def test_calcMean(self):
        arr = [5, 10, 15,20,25]
        self.assertEqual(calcMean(arr), 15)
        with self.assertRaises(ValueError):
            calcMean(["dog", 5, 10])
        with self.assertRaises(TypeError):
            calcMean(5)
        with self.assertRaises(ValueError):
            calcPercentile(arr, -10)
        
        self.assertAlmostEqual(calcStdDev([5, 10, 15, 20, 25]), 7.071067812)
        self.assertAlmostEqual(calcMedian([5, 10, 15, 20, 25]), 15)
        self.assertAlmostEqual(calcMedian([5, 10, 15, 20, 25, 30]), 17.5)
        self.assertAlmostEqual(calcQuartile([5, 10, 15, 20, 25], 1), 7.5)
        self.assertAlmostEqual(calcQuartile([1, 5, 10, 15, 20, 25], 3), 22.5)
        
        with self.assertRaises(ValueError):
            calcPercentile(calcQuartile([5, 10, 15, 20, 25], 0), 7.5)
        with self.assertRaises(ValueError):
            calcPercentile([1, 5, 10, 15, 20], 1.5)
        with self.assertRaises(ValueError):
            calcPercentile([1, 5, 10, 15, 20], "test")
        calcPercentile([1, 5, 10, 15, 20], 30)
        #L1_8.calcMean("ASFSD")
        
        