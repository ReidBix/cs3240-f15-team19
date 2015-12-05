from django.contrib import admin
from Project.SecureWitness.models import *

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','views','likes')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('title','description','detailed_description','encrypted',
                    'private','timestamp','reporter', 'key')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'website', 'picture', 'uKey', 'rKey', 'publickey', 'tempprivate')

admin.site.register(Report, ReportAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# Register your models here.
