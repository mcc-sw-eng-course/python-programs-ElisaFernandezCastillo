import unittest
from L2_14 import MyPowerList

class TestL2_14(unittest.TestCase):
    def testReadFromFile(self):
        testFileName ="testList.txt" 
        with open(testFileName, 'w') as f:
            f.write("-10 -5 0 10 15 20")
            
        pList = MyPowerList()
        pList.readFromFile(testFileName)
        pList.printList()
        with self.assertRaises(ValueError):
            wrongList = MyPowerList("hola")
        
        