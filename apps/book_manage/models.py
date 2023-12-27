from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    bio = models.TextField(verbose_name='简介')
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='书名')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    published_date = models.DateField(verbose_name='出版日期')
    isbn = models.CharField(max_length=13, verbose_name='ISBN')
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

class Borrower(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, verbose_name='用户')
    borrowed_books = models.ManyToManyField(Book, through='BorrowedBook', verbose_name='借阅图书')
    class Meta:
        verbose_name = '借阅者'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.user.username

class BorrowedBook(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, verbose_name='借阅者')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='图书')
    borrow_date = models.DateField(auto_now_add=True, verbose_name='借阅日期')
    return_date = models.DateField(null=True, blank=True, verbose_name='归还日期')
    class Meta:
        verbose_name = '借阅图书'
        verbose_name_plural = verbose_name
    def __str__(self):
        return f"{self.borrower.user.username} - {self.book.title}"
