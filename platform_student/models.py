from django.db import models
NULLABLE = {'blank': True, 'null': True}


class Section(models.Model):
    """Модель секции"""
    name = models.CharField(max_length=255, verbose_name="Название секции")
    description = models.TextField(verbose_name="Описание секции", max_length=110,  **NULLABLE)


class Material(models.Model):
    """Модель Материала. В каждой секции, есть несколько статей(материал для изучения)"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="Название секции")
    title = models.CharField(max_length=255, verbose_name="название")
    content = models.TextField(verbose_name="контент")
    summary = models.TextField(verbose_name="Краткое содержание", **NULLABLE)

    def __str__(self):
        return f'{self.title}, {self.content}'

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "материалы"


class Test(models.Model):
    """Модель Тест. В каждом матере есть тесть, который поможет проверить знания псоле прочитанного"""
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="материал")
    question = models.CharField(max_length=255, verbose_name="вопрос")
    option1 = models.CharField(max_length=255, **NULLABLE)
    option2 = models.CharField(max_length=255, **NULLABLE)
    option3 = models.CharField(max_length=255, **NULLABLE)
    correct_answer = models.CharField(max_length=255, verbose_name="правильный оответ", choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')])

    def __str__(self):
        return f'{self.question}, {self.correct_answer}'

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"





