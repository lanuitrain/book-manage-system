from django.db import models

# Create your models here.
# ORM 相关的只能写在这个文件里，写到别的文件中Django都找不到


class Publisher(models.Model):
    '''
    出版社表
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False)
    addr = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    publisher = models.ForeignKey(to='Publisher',on_delete=models.CASCADE)
    # author = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False, unique=True)
    book = models.ManyToManyField(to='Book')

    def __str__(self):
        return self.name


class Admin(models.Model):
    Aid = models.AutoField(verbose_name='管理员id', primary_key=True)
    Aname = models.CharField(verbose_name='管理员账号', max_length=20)
    Apassword = models.CharField(verbose_name='管理员密码', max_length=40)
    Aemail = models.CharField(verbose_name='管理员邮箱', max_length=20)

