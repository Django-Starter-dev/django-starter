from django.contrib import admin

# Register your models here.

from .models import Choice, Question



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_filter = ['pub_date']
    search_fields = ['question_text']
    

## ----------- changing the sequence of the fields in the model ------------ ##

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

## ------------------------------------------------------------------------- ##

admin.site.register(Question, QuestionAdmin)