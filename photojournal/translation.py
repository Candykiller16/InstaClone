from modeltranslation.translator import TranslationOptions, register
from .models import *


@register(Profile)
class ProfileTranslationOptions(TranslationOptions):
    fields = ('short_intro', 'bio')


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Comments)
class CommentsTranslationOptions(TranslationOptions):
    fields = ['body']
