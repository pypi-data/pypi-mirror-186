import unittest
from TfidfTransformer_afinitiv2 import TfidfFramework
from sklearn.feature_extraction.text import TfidfVectorizer

class TestTfidfFramework(unittest.TestCase):
    def setUp(self):
        """
        Initialize test data and an instance of TfidfFramework
        """
        self.data = ["This is the first document.", "This document is the second document.", "And this is the third one."]
        
        self.framework = TfidfFramework()
        
        for d in self.data:
            self.framework.append_data(d)

    def test_init(self):
        """
        Test that the TfidfFramework instance is initialized correctly
        """
        self.assertIsNotNone(self.framework.tfidf_matrix)
        self.assertIsInstance(self.framework.vectorizer, TfidfVectorizer)
        self.assertEqual(self.framework.data, ["This is the first document.", "This document is the second document.", "And this is the third one."])

    def test_fit_transform(self):
        """
        Test that the fit_transform method correctly updates the tfidf_matrix variable
        """
        self.framework.fit_transform()
        self.assertIsNotNone(self.framework.tfidf_matrix)

    def test_append_data(self):
        """
        Test that the append_data method correctly adds data to the data list
        """
        self.assertEqual(self.framework.tfidf_matrix.shape[0], len(self.data))

        self.framework.append_data("This is a new document.")

        self.assertEqual(self.framework.data, (self.data + ["This is a new document."]))

        self.assertEqual(self.framework.tfidf_matrix.shape[0], len(self.data + ["This is a new document."]))

    def test_append_data_invalid(self):
        """
        Test that the append_data method raises a ValueError for invalid data
        """
        with self.assertRaises(ValueError):
            self.framework.append_data("")
        with self.assertRaises(ValueError):
            self.framework.append_data(None)
        with self.assertRaises(ValueError):
            self.framework.append_data(123)
            

    def test_append_list_data_invalid(self):
        """
        Test that the append_list_data method raises a ValueError for invalid data
        """
        with self.assertRaises(ValueError):
            self.framework.append_list_data(["This is a valid string.", None])
        with self.assertRaises(ValueError):
            self.framework.append_list_data([123, "This is a valid string."])
        with self.assertRaises(ValueError):
            self.framework.append_list_data("This is not a list")

if __name__ == '__main__':
    unittest.main()
