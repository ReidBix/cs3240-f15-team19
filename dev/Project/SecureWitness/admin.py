from django.contrib import admin
from Project.SecureWitness.models import *

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','views','likes')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('title','description','detailed_description','private','timestamp','user', 'aesKey')

class FolderAdmin(admin.ModelAdmin):
    list_display = ('title',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture', 'publickey', 'tempprivate')

class UploadAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'report','encrypted')

admin.site.register(Report, ReportAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Upload, UploadAdmin)
admin.site.register(Folder, FolderAdmin)
