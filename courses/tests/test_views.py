from django.contrib.auth.models import Group
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from courses.models import Subject


def create_sample_user(client):
    Group.objects.get_or_create(name='instructor')
    data = {
        'email': 'test44@mail.com',
        'password': 'vf94@@ds!ID8',
        'password2': 'vf94@@ds!ID8',
        'fullname': 'VF SIEUR',
        'is_instructor': True,
    }
    client.post(reverse('users:register'),
                data=data)


def login_sample_user(client):
    logged_in = client.post(reverse('users:login'),
                            data={
                                'username': 'test44@mail.com',
                                'password': 'vf94@@ds!ID8',
                            })
    return logged_in


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.subject = Subject.objects.create(title='Programming News')
        create_sample_user(self.client)
        logged_in = login_sample_user(self.client)
        self.user = logged_in

    def test_home_page(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_course_creation(self):
        data = {
            'title': 'Sample Course',
            'owner': self.user,
            'subject': self.subject,
            'overview': 'this is sample overview',
            'created': timezone.now(),
        }
        url = reverse('courses:create-course')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name='courses/create_course.html')
