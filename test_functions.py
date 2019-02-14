'''
Created on 2019 M02 5

@author: A01221781
'''
import unittest
import Functions
import filecmp


class TestFunctions(unittest.TestCase):
    def test_ceiling(self):
        self.assertEqual(Functions.ceiling(3.50), 4)
        self.assertEqual(Functions.ceiling(3.000048), 4)
        self.assertEqual(Functions.ceiling(3.99999), 4)
        self.assertEqual(Functions.ceiling(0), 0)
        self.assertEqual(Functions.ceiling(4), 4)
        self.assertEqual(Functions.ceiling(True), 1)
        self.assertEqual(Functions.ceiling(False), 0)
        with self.assertRaises(TypeError):
            Functions.ceiling("Dog")

    def test_factorial(self):
        self.assertEqual(Functions.factorial(3), 6)
        self.assertEqual(Functions.factorial(0), 1)
        self.assertEqual(Functions.factorial(1), 1)
        self.assertEqual(Functions.factorial(True), 1)
        self.assertEqual(Functions.factorial(False), 1)
        with self.assertRaises(ValueError):
            Functions.factorial(5.5)
        with self.assertRaises(ValueError):
            Functions.factorial(-5)
        with self.assertRaises(TypeError):
            Functions.factorial("dog")

    def test_power(self):
        self.assertEqual(Functions.power(2, 3), 8)
        self.assertEqual(Functions.power(-2, 2), 4)
        self.assertEqual(Functions.power(-2, -2), 0.25)
        self.assertEqual(Functions.power(-2, -3), -0.125)
        self.assertEqual(Functions.power(2, -3), 0.125)
        self.assertEqual(Functions.power(0, 5), 0)
        self.assertEqual(Functions.power(5, 0), 1)
        self.assertEqual(Functions.power(4, 0.5), 2)
        self.assertEqual(Functions.power(0.5, 4), 0.0625)
        self.assertEqual(Functions.power(True, False), 1)
        self.assertEqual(Functions.power(False, True), 0)
        self.assertEqual(Functions.power(5, False), 1)
        self.assertEqual(Functions.power(False, 5), 0)
        self.assertEqual(Functions.power(5, True), 5)
        self.assertEqual(Functions.power(True, 5), 1)
        with self.assertRaises(TypeError):
            Functions.power(3, "dog")
        with self.assertRaises(OverflowError):
            Functions.power(5000, 89666663)

    def test_compareFiles(self):
        txt1 = open('unitTestTxt1.txt', 'w')
        txt1.write("123456789")
        txt2 = open('unitTestTxt2.txt', 'w')
        txt2.write("0000123456789\n")
        txt3 = open('unitTestTxt3.txt', 'w')
        txt3.write("123456789")

        txt1.close()
        txt2.close()
        txt3.close()

        self.assertFalse(Functions.compareFiles(
            "unitTestTxt1.txt", "unitTestTxt2.txt"))
        self.assertTrue(Functions.compareFiles(
            "unitTestTxt1.txt", "unitTestTxt1.txt"))
        self.assertTrue(Functions.compareFiles(
            "unitTestTxt1.txt", "unitTestTxt3.txt"))
        self.assertTrue(Functions.compareFiles(
            "unitTestTxt1.txt", "unitTestTxt3.txt"))
        self.assertFalse(Functions.compareFiles(True, True))
        self.assertFalse(Functions.compareFiles(True, False))
        self.assertFalse(Functions.compareFiles(False, False))
        with self.assertRaises(FileNotFoundError):
            Functions.compareFiles("unitTestTxt1.txt", "unitTestTxt4.txt")
        with self.assertRaises(OSError):
            Functions.compareFiles(3, 3)
