from django.test import TestCase
from django.urls import reverse
from platform_student.models import Test, Section, Material


class YourTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name='Секция 1', description='Хорошая секция')
        self.material = Material.objects.create(section=self.section, title='Материал 1', content='История',
                                                summary='История России')

        # Выполняется перед каждым тестом
        Test.objects.create(
            material=self.material,
            question='Вопрос?',
            option1='A',
            option2='B',
            option3='C',
            correct_answer='option1'
        )

    def test_example(self):
        """Пример теста"""

        url = reverse('platform_student:check_answer')

        response = self.client.post(url, {'question1': 'A'})

        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        """Проверка отображении секции на экране"""
        url = reverse('platform_student:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Секция 1')

    def test_material_list_view(self):
        """Проверка отображения материала на экране"""
        url = reverse('platform_student:material_list', args=[self.section.id])
        response = self.client.get(url)

        # Update the test to check for a more general content
        self.assertContains(response, 'Добро пожаловать в мир самообучения')
        self.assertContains(response, 'Проект создан с целью помощи студентам')

        self.assertEqual(response.status_code, 200)

    def test_quiz_view(self):
        """Проверка отображения вопросов теста на экране"""
        url = reverse('platform_student:quiz', args=[self.material.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Вопрос?')