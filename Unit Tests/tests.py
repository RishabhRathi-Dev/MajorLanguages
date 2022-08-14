import unittest

from majorLanguages import LanguageData

class ScrapTest(unittest.TestCase):
    def test_languagedata(self):
        """
        This test check the functionality of the function LanguageData 

        GIVEN a tuple
        WHEN scraping is done 
        THEN check the data and total are returned correctly

        """

        data, total = LanguageData("RishabhRathi-Dev")

        dataLen = True if len(data) > 0 else False

        self.assertIsInstance(data, dict)
        self.assertIsInstance(total, int)
        self.assertTrue(dataLen)
        


if __name__ == '__main__':
    unittest.main()