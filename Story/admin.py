from django.contrib import admin

from Story.models import Story, StoryStream

admin.site.register(Story)
admin.site.register(StoryStream)