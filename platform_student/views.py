from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views import View

from platform_student.models import Section, Material, Test
from django.views.generic import DetailView


def index(request):
    """Главная страница"""
    section_list = Section.objects.all()
    context = {
        'section_list': section_list
    }
    return render(request, "platform_student/base.html", context)


def material_list(request, section_id):
    """Страница с Материалами"""
    section = Section.objects.get(pk=section_id)
    materials = Material.objects.filter(section=section)
    return render(request, 'platform_student/material_list.html', {'section': section, 'materials': materials})


class MaterialDetailView(DetailView):
    """Модель детального просмотра материала на странице"""
    model = Material


class QuizView(View):
    template_name = 'platform_student/quiz.html'

    def get(self, request, material_id):
        questions = Test.objects.filter(material_id=material_id)
        context = {'questions': questions}
        return render(request, self.template_name, context)


def check_answer(request):
    if request.method == 'POST':
        # Получаем ответы из формы
        answers = {}
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = key.replace('question', '')
                answers[int(question_id)] = value

        # Получаем правильные ответы из базы данных
        correct_answers = {}
        for question in Test.objects.all():
            if question.correct_answer == 'option2':
                correct_option_value = question.option2
            elif question.correct_answer == 'option3':
                correct_option_value = question.option3
            else:
                correct_option_value = question.option1

            correct_answers[question.id] = correct_option_value

        # Проводим проверку ответов
        correct_count = 0
        incorrect_answers = []  # Создаем список для неверных ответов

        for question_id, user_answer in answers.items():
            correct_answer = correct_answers.get(question_id, '')
            if str(user_answer) == str(correct_answer):
                correct_count += 1
            else:
                # Если ответ неверный, добавляем в список
                question = Test.objects.get(pk=question_id)
                incorrect_answers.append({
                    'question': question.question,
                    'user_answer': user_answer,
                    'correct_answer': correct_answer
                })

        # Возвращаем результат в шаблон
        return render(request, 'platform_student/check_answer.html', {
            'correct_count': correct_count,
            'incorrect_answers': incorrect_answers
        })

    # Если запрос не POST, перенаправляем на главную страницу или возвращаем ошибку
    return HttpResponseBadRequest('Invalid request method')


