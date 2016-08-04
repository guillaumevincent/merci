import unittest

from api import models


class MyUserTestCase(unittest.TestCase):
    def test_create_user_call_create_employee(self):
        original_nb_of_users = models.Employee.objects.count()
        user = models.MyUser.objects.create(email='email@example.org')
        self.assertEqual(original_nb_of_users + 1, models.Employee.objects.count())
        self.assertEqual(user.employee, models.Employee.objects.first())


if __name__ == '__main__':
    unittest.main()
