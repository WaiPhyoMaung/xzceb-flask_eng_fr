# Test for null input for frenchToEnglish
import unittest
from translator import french_to_english, english_to_french

class test_translator(unittest.TestCase):
    def test_e2f_null(self): 
        self.assertEqual(english_to_french(""), "")
    def test_e2f_hello_bonjour(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")            
    def test_f2e_null(self):
        self.assertEqual(french_to_english(""), "")
    def test_f2e_bonjour_hello(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
unittest.main()