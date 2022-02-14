from django.test import Client

c = Client()  # enforce_csrf_checks=True

response = c.post('/login/',
                    {'email': 'john@example.com',
                    'password': 'doe'})
response = c.get('/home')
