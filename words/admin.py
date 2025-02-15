from django.contrib import admin

from words.models import Word

# Register your models here.


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass
