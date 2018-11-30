from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '添加用户'
        verbose_name_plural = verbose_name


class MyMessage(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50)
    st_id = models.CharField(verbose_name='学号', max_length=50, default='')
    college = models.CharField(verbose_name='学院', max_length=20, default='')
    major = models.CharField(verbose_name='专业', max_length=20, default='')
    grade = models.CharField(verbose_name='年级', max_length=20)
    myclass = models.CharField(verbose_name='班级',max_length=10)
    gender = models.CharField(max_length=6, choices=((u"male", "男"), ("famale", "女")), default="男")
    image = models.ImageField(verbose_name='头像', upload_to='my_info/%Y/%m', default='my_info/default.png',max_length=100)
    favor = models.TextField(verbose_name='专业兴趣', max_length=50, null=True, blank=True)
    promote_sys = models.URLField(verbose_name="助学系统",max_length=200,null=True,blank=True)
    early_warning = models.CharField(max_length=10,choices=(("normal", "正常"), ("caution", "警告"), ("fw_st","跟班"),("demotion","降级"), ("dropout","退学")),default="正常")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '个人中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

