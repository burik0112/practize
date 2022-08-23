from modeltranslation.translator import register, TranslationOptions


from product.models import ProductModel


@register(ProductModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'category', 'tags')