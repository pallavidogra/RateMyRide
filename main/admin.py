from django.contrib import admin
from .models import Post, Rating, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Rating)



class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'description', 'date_posted')
    list_filter = ('author', 'date_posted')
    search_fields = ['title', 'description']
    prepopulated_fields = {'title': ('description',)}

    summernote_fields = ('description',)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)