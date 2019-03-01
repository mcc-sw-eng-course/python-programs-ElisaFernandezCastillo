import unittest
import FirstExercises
import filecmp
import os

class TestFirstExercises(unittest.TestCase):
    
    def test_setinputdata(self):
        listOfData=[55.0, 20.0, 32.0, 15.0, 1.0, 100.0, 20.0, 99.0, 7.0, 5.0, 3.0, 6.0, 7.0, 1.0, 0.5, 4.0, 1.0]
        srtDt=FirstExercises.sortingData()
        self.assertEqual(srtDt.setInputData('Book1'), listOfData)
        
        with self.assertRaises(FileNotFoundError):
            srtDt.setInputData('Book2')
    
    def test_mergeSort(self):
        orderedData=[0.5, 1.0, 1.0, 1.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.0, 15.0, 20.0, 20.0, 32.0, 55.0, 99.0, 100.0]
        srtDt=FirstExercises.sortingData()
        lista=srtDt.setInputData('Book1')
        srtDt.mergeSort(lista)
        self.assertEqual(srtDt.lst, orderedData)
    
    def test_set_output_data(self):
         srtDt=FirstExercises.sortingData()
         lista=srtDt.setInputData('Book1')
         srtDt.mergeSort(lista)
         srtDt.set_output_data("SortedBook2")
         self.assertTrue(filecmp.cmp("SortedBook2.csv","SortedBook1.csv"))
         os.remove("SortedBook2.csv") 
        
        
    