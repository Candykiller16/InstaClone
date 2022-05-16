from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin

from .models import Post, Profile, Category, Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'get_image', 'title', 'description', 'created')
    list_display_links = ('owner', 'title')
    search_fields = ['created', 'title', 'owner__username']
    prepopulated_fields = {"slug": ("title",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.featured_image.url} width="100" height="100"')

    get_image.short_description = "Picture"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'email', 'username', 'short_intro', 'bio')
    list_display_links = ('username', )
    search_fields = ('name', 'email', 'username', 'short_intro')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.profile_image.url} width="100" height="100"')

    get_image.short_description = "Picture"


class CategoryAdmin(TranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)


#
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('body', 'owner', 'created')
    list_display_links = ('body', 'owner')
    search_fields = ('body', 'owner__username', 'created')


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Category)
admin.site.register(Comments, CommentsAdmin)
