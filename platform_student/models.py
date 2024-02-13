from django.db import models
NULLABLE = {'blank': True, 'null': True}


class Section(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название секции")
    description = models.TextField(verbose_name="Описание секции", **NULLABLE)


class Material(models.Model):
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
    material = models.ForeignKey(Material, on_delete=models.CASCADE, verbose_name="материал")
    question = models.CharField(max_length=255, verbose_name="вопрос")
    correct_answer = models.CharField(max_length=255, verbose_name="правильный оответ")

    def __str__(self):
        return f'{self.question}, {self.correct_answer}'

    class Meta:
        verbose_name = "тест"
        verbose_name_plural = "тесты"


