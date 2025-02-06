from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently","numero_votos"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    
    def numero_votos(self, obj):
      return obj.choice_set.count()


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)