from django.contrib import admin

from .models import Question,Choice

admin.site.site_header = "poll admin"
admin.site.site_title = ("the world slickest admin panel")
admin.site.index_title = "admin UI"

admin.site.register(Question)

admin.site.register(Choice)