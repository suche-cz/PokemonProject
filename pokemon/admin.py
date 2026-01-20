from django.contrib import admin
from pokemon import models


admin.site.register([
    models.Pokemon,
    models.Category,
    models.Comment,
])
