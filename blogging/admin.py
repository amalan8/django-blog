from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)
#
class CategoryInLine(admin.StackedInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]
    model = Post
    list_display = ['title', 'author', 'created_date', 'modified_date', 'published_date']


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'description',]
    exclude = ["posts"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
#Category Inline to show on Post.
