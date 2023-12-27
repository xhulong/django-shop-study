# admin.py

from django.contrib import admin
from .models import Author, Book, Borrower, BorrowedBook

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # 在列表视图中显示的字段
    search_fields = ('name',)  # 可以进行搜索的字段

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn', 'published_date')
    list_filter = ('published_date',)  # 列表过滤器
    search_fields = ('title', 'isbn')

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)  # 注意在搜索外键字段时使用双下划线

class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ('borrower', 'book', 'borrow_date', 'return_date')
    list_filter = ('borrow_date', 'return_date')
    search_fields = ('borrower__user__username', 'book__title')

# 注册模型和其管理类
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(BorrowedBook, BorrowedBookAdmin)
