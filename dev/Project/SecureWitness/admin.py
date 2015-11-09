from django.contrib import admin
from Project.SecureWitness.models import Document, Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','views','likes')

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title','description','detailed_description','encrypted',
                    'private','docfile','timestamp','user')

admin.site.register(Document, DocumentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
# Register your models here.
