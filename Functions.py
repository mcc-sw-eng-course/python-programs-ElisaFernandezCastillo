'''
Created on 2019 M02 4

@author: A01221781
'''
import math

import filecmp


def ceiling(number):
    return math.ceil(number)


def factorial(number):
    return math.factorial(number)


def power(x, y):
    return math.pow(x, y)


def compareFiles(file1, file2):
    return filecmp.cmp(file1, file2)


print("Comparing files:", filecmp.cmp("unitTestTxt1.txt", "unitTestTxt2.txt"))
print("Compare files", compareFiles("unitTestTxt1.txt", "unitTestTxt2.txt"))
