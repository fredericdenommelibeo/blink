from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from courses.forms import ModuleFormSet
from courses.models import Subject
from users.models import Account


class TestForms(TestCase):
    def setUp(self):
        self.formset = ModuleFormSet
        self.subject = Subject.objects.create(title='Programming News')
        self.owner = Account.objects.create(
            email='test44@mail.com',
            password = 'testpass@1',
            fullname='John Doe'
        )

    def test_module_formset(self):
        payload = {
            'modules-TOTAL_FORMS': '2',
            'modules-MAX_NUM_FORMS': '2',
            'modules-INITIAL_FORMS': '1',
            'global_param': 100,
            'form-0-id': 1,
            'form-0-title': 'Sample Course',
            'form-0-owner': self.owner,
            'form-0-subject': self.subject,
            'form-0-overview': 'this is sample overview',
            'form-0-created': timezone.now(),
            'modules-0-title': 'module1',
            'modules-0-course': 1,
            'modules-0-description': 'this is a test module',
        }
        formset = ModuleFormSet(payload)
        self.assertFalse(formset.is_valid(), msg=formset.errors)
        # {'id': ['This field is required.'], 'course': ['The inline value did not match the parent instance.']}
