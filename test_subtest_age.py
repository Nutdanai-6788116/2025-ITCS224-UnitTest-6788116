import unittest
from age import categorize_by_age

class TestCategorizeByAgeSubTest(unittest.TestCase):
    def test_child_age(self):
        for age in range(0, 9):   
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Child")
                print(f"\n{age} is considered as a child.")

    def test_adult_age(self):
        for age in range(19, 66):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Adult")
                # print(f"\n{age} is considered as an adult.")

    def test_golden_age(self):
        for age in range(66, 151):
            with self.subTest(age=age):
                self.assertEqual(categorize_by_age(age), "Golden age")
                # print(f"\n{age} is considered as golden age.")

if __name__ == "__main__":
    unittest.main(verbosity=2)