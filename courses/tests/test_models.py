from courses.models import Course, Subject
from django.test import TestCase
from django.utils import timezone
from users.models import Account


class TestModels(TestCase):
    def setUp(self):
        self.subject = Subject.objects.create(title='Programming News')
        self.owner = Account.objects.create(
            email='test44@mail.com',
            password = 'testpass@1',
            fullname='John Doe'
        )
        self.course = Course.objects.create(
            title='Sample Course',
            owner=self.owner,
            subject=self.subject,
            overview='this is sample overview',
            created=timezone.now(),
        )

    def test_course_creation(self):
        course = self.course
        self.assertTrue(isinstance(course, Course))
        self.assertEqual(course.slug, 'sample-course')
