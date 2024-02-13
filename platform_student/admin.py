from django.contrib import admin

from platform_student.models import Material, Section, Test


@admin.register(Material)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'content',)
    search_fields = ('section', 'title', 'content',)


@admin.register(Section)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Test)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('material', 'question', 'correct_answer',)
    search_fields = ('material', 'question', 'correct_answer',)

