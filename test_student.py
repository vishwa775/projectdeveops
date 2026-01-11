import unittest
from unittest.mock import patch
import io
import sys
from Student import calculate_grade, main
class TestStudentGrade(unittest.TestCase):

    # 🔹 Test grade calculation logic
    def test_grade_S(self):
        self.assertEqual(calculate_grade(95), "S")

    def test_grade_A(self):
        self.assertEqual(calculate_grade(85), "A")

    def test_grade_B(self):
        self.assertEqual(calculate_grade(70), "B")

    def test_grade_C(self):
        self.assertEqual(calculate_grade(55), "C")

    def test_grade_D(self):
        self.assertEqual(calculate_grade(45), "D")

    def test_grade_F(self):
        self.assertEqual(calculate_grade(30), "F")

    # 🔹 Test main program using sys.argv
    def test_main_output(self):
        test_args = [
            "Student.py",      # sys.argv[0] script name
            "Vishwa",       # Name
            "BSCA",             # Department
            "3",               # Semester
            "85",              # Marks1
            "78",              # Marks2
            "90"               # Marks3
        ]

        with patch.object(sys, 'argv', test_args):
            captured_output = io.StringIO()
            sys.stdout = captured_output

            main()

            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()

            # ✅ Check key content
            self.assertIn("GRADING CRITERIA", output)
            self.assertIn("STUDENT DETAILS", output)
            self.assertIn("Name       : Vishwa", output)
            self.assertIn("Department : BCA", output)
            self.assertIn("Semester   : 3", output)
            self.assertIn("Average    : 84.33", output)
            self.assertIn("Grade      : A", output)

if __name__ == "__main__":
    unittest.main()
