from django.contrib import admin
from pokemon import models


admin.site.register([
    models.Category,
    models.Pokemon,
])


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'pokemon', 'pokemon_id', 'user', 'create_dt']


