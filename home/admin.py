from django.contrib import admin
from .models import Category, SubCategory, Icon, CareerMail
# Register your models here.

class role_inline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryModelAdmin(admin.ModelAdmin):
    inlines = (role_inline,)
    fields = [
        'id',
        'title',
        'thumbnail_url',
        'icon',
        'active'
    ]

    readonly_fields = ['id',]
    list_display = ('title', 'thumbnail_url', 'icon', 'active')

    class Meta:
        model = Category

class SubCategoryModelAdmin(admin.ModelAdmin):
    
    fields = [
        'id',
        'title',
        'view_count',
        'icon',
        'categories',
        'price'
    ]

    readonly_fields = ['id',]
    list_display = ('title', 'view_count','icon','categories','price')

    class Meta:
        model = SubCategory


admin.site.register(Category,CategoryModelAdmin)
admin.site.register(SubCategory)
admin.site.register(Icon)
admin.site.register(CareerMail)




