from django.contrib import admin
from .models import RecipePost, UserComment, Tips, TipComments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(RecipePost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'status', 'created_on',
                    'updated_on', 'read_time')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'content',)


@admin.register(UserComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'blog', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Tips)
class TipPostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'content',)


@admin.register(TipComments)
class TipCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_tcomment']

    def approve_tcomment(self, request, queryset):
        queryset.update(approved=True)
