from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceAdmin(admin.StackedInline):
    fieldsets = [
        ("Вариант ответа", {"fields":["text","votes"]} ),
    ]
    model = Choice
    extra = 3

class  QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Текст вопроса", {"fields":["text"]} ),
        ("Дата вопроса", {"fields":["pub_Date"]} ),
    ]
    inlines = [ChoiceAdmin]
    list_filter = ["pub_Date"]
    search_fields = ["text"]

admin.site.register(Question, QuestionAdmin)
