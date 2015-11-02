from django.contrib import admin
from Project.SecureWitness.models import Category, Page
from Project.SecureWitness.models import Document

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','views','likes')

admin.site.register(Document)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
# Register your models here.
