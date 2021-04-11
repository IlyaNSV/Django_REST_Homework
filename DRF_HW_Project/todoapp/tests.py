import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User, Group

from .models import Project, ToDoNote
from .views import ProjectModelViewSet
from ..userapp.models import DefaultUser


class TestProjectViewSet(TestCase):

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {
            "uuid": "a67bbee1-e0f8-48c9-aa61-430b8dec6a9b",
            "members": [
                "http://127.0.0.1:8000/api/users/3bd0ed20-5705-4228-a751-3076581c13fc/",
                "http://127.0.0.1:8000/api/users/d0972e76-6141-4f73-bcbd-d445dfbf6b30/"
            ],
            "name": "DRF_Homework",
            "repository_link": ""
        }, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/', {
            "uuid": "a67bbee1-e0f8-48c9-aa61-430b8dec6a9b",
            "members": [
                "http://127.0.0.1:8000/api/users/3bd0ed20-5705-4228-a751-3076581c13fc/",
                "http://127.0.0.1:8000/api/users/d0972e76-6141-4f73-bcbd-d445dfbf6b30/"
            ],
            "name": "DRF_Homework",
            "repository_link": ""
        }, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_guest(self):
        note = ToDoNote.objects.create(
            project=mixer.blend(Project),
            creator_user=mixer.blend(DefaultUser),
            text="We can do it!!!",
            created="2021-03-16T07:05:41.432582Z",
            updated="2021-03-16T07:22:35.996569Z",
            actual_sign="CLD")
        client = APIClient()
        response = client.put(f'/api/todonotes/1/', {'text': 'We cannot do it ;(', 'actual_sign': 'ACT'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        note = ToDoNote.objects.create(
            project=mixer.blend(Project),
            creator_user=mixer.blend(DefaultUser),
            text="We can do it!!!",
            created="2021-03-16T07:05:41.432582Z",
            updated="2021-03-16T07:22:35.996569Z",
            actual_sign="CLD")

        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/todonotes/1/', {'text': 'We cannot do it ;(', 'actual_sign': 'ACT'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        note = ToDoNote.objects.get(url=note.url)
        self.assertEqual(note.text, 'We cannot do it ;(')
        self.assertEqual(note.actual_sign, 'ACT')
        client.logout()


class ProjectViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        project = mixer.blend(Project, name="Name1")
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/api/projects/{project.uuid}/', {'name': 'Test 1 name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(uuid=project.uuid)
        self.assertEqual(project.name, 'Test 1 name')
