from django.contrib import admin
from apps.categories.models import Category
from mptt.admin import DraggableMPTTAdmin


admin.site.register(
    Category,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
    
    


