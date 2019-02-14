import unittest
import Exercise15_Directory
import filecmp

class TestDirectory(unittest.TestCase):
   def test_directory(self):
       directory=Exercise15_Directory.userDirectory()
       firstUser=directory.createNewRecord("Elisa")
       secondUser=directory.createNewRecord("Carolina","R.Laureles 2068")
       thirdUser=directory.createNewRecord("Marisol",None,"3310389654")
       fourtUser=directory.createNewRecord("Pedro","R.Crisantemos Pte. 2644","39874513","pedro.tre@gmail.com")
       self.assertEqual(firstUser["name"],"Elisa")
       self.assertEqual(secondUser["phone"],None)
       directory.saveToTextFile("records_test")
       self.assertTrue(filecmp.cmp("records_test.txt","records_4users.txt"))
       self.assertEqual(directory.searchDataFromRecord("Marisol"),{'name': 'Marisol', 'address': None, 'phone': '3310389654', 'email': None})
       self.assertEqual(directory.searchDataFromRecord('Sergio'),None)
       directory.loadRecordsFromFile("contactos")
       self.assertEqual(directory.searchDataFromRecord('Sergio Zamora'),{'name': 'Sergio Zamora', 'address': 'Ricardo Guiraldes 5779', 'phone': '3316457891', 'email': 'sergio.zam@yahoo.com.mx'})
       with self.assertRaises(FileNotFoundError):
            directory.loadRecordsFromFile("contacts")
        
       
       
        