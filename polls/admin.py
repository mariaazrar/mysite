from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Published", {"fields": ["pub_date"]})
    ]

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin) 