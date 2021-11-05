import unittest;
from Student import Student;
from Student import Unit as Report;
from unittest.mock import MagicMock, call, patch;


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.grade = Student("firstName", "FamilyName", 50)
        self.report = Report([])

    def test_hd_grade(self):
        grade = Student("firstname", "surname", 95);
        self.assertEqual(grade.letter_grade(), "HD");

    def test_d_grade(self):
        grade = Student("firstname", "surname", 75);
        self.assertEqual(grade.letter_grade(), "D");

    def test_c_grade(self):
        grade = Student("firstname", "surname", 65);
        self.assertEqual(grade.letter_grade(), "C");

    def test_p_grade(self):
        grade = Student("firstname", "surname", 55);
        self.assertEqual(grade.letter_grade(), "P");

    def test_fail_grade(self):
        grade = Student("firstname", "surname", 40);
        self.assertEqual(grade.letter_grade(), "N");

    @patch.object(Student, 'pass_subject')
    def test_fail_report(self, mock_pass_subject):

        result = MagicMock()

        result.return_value = True

        mock_pass_subject = result

        self.assertTrue(result, True)

def main():
    # Create a test suit
    suit = unittest.TestLoader().loadTestsFromTestCase(TestStudent)
    # Run the test suit
    unittest.TextTestRunner(verbosity=2).run(suit)

main()
