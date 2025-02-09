import unittest
from main import class_media

class TestStudentClassification(unittest.TestCase):

    def test_classification_excellent(self):
        self.assertEqual(class_media(95), "Excelente!")

    def test_classification_good(self):
        self.assertEqual(class_media(75), "Bom!")
    
    def test_classification_regular(self):
        self.assertEqual(class_media(60), "Regular!")
    
    def test_classification_needs_improvement(self):
        self.assertEqual(class_media(40), "Precisa ser melhor!")

if __name__ == "__main__":
    unittest.main()
