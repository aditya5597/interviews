from uuid import uuid4

from django.test import TestCase

from backend.models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        self.task_uuid = uuid4()
        self.task_order = 1
        self.task_title = 'Test task title 1'
        self.task_description = 'Test task description 1--bit longer than the title'
        Task.objects.create(
            uuid=self.task_uuid,
            order=self.task_order,
            title=self.task_title,
            description=self.task_description,
        )

    def test_getting_fields(self):
        """Task fields are retreived correctly"""
        task = Task.objects.get(uuid=self.task_uuid)
        self.assertEqual(task.order, self.task_order)
        self.assertEqual(task.title, self.task_title)
        self.assertEqual(task.description, self.task_description)
