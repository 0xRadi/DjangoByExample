from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'author', 'publish', )
    search_fields = ('title', 'body', )
    # autocomplete a field based on another
    prepopulated_fields = {'slug': ('title',)}
    # username drop list to user IDs
    raw_id_fields = ('author', )

    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)