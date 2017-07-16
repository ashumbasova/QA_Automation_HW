import unittest
from EmployeeVsITEmployee import ITEmployee
class ITEmployeeWithNameAndSurname(unittest.TestCase):
    def setUp(self):
        self.emp = ITEmployee("Anna Shumbasova", "QA", 1000, "python", 2)

    def test_input(self):
        self.assertEqual(self.emp.fullName, "Anna Shumbasova")
        self.assertEqual(self.emp.name(), "Anna")
        self.assertEqual(self.emp.surname(), "Shumbasova")
        self.assertEqual(self.emp.income(3), 3000)
        self.assertEqual(self.emp.salary, 1000)
        self.emp.add_skill("python")
        self.assertEqual(self.emp.skills, ["python"])
        self.emp.add_seniority(2)
        self.assertEqual(self.emp.add_seniority(2), "Junior QA")