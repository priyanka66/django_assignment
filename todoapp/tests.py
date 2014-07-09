from django.test import TestCase
from todoapp.models import task
from django.contrib.auth.models import User

class test_get_task(TestCase):
	def setUp(self):
		self.user = User.objects.create(username="priyanka",password="123",email = "asd@gmail.com")
		task.objects.create(task_name="Task test",user_name = self.user)

	def test_check_if_saved(self):
        task = task.objects.get(user_name = self.user)
        self.assertEqual(task, 1, 'the task was not saved')