from django.db import models
from datetime import datetime

# Create your models here.

class Coursetable(models.Model):
    c_id = models.CharField(verbose_name='课程代码', max_length=30, null=False, unique=True)
    title = models.CharField(verbose_name='课程名', max_length=50)
    credit = models.FloatField(verbose_name='学分', default=0.0)
    period = models.CharField(verbose_name='学时', max_length=10)
    semester = models.CharField(verbose_name='开课学期', max_length=10)
    c_type = models.CharField(verbose_name='课程性质', max_length=100)
    major = models.CharField(verbose_name='专业', max_length=50)
    college = models.CharField(verbose_name='学院', max_length=50)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = '所有课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class StCredit(models.Model):
    st_id = models.CharField(verbose_name='学号', max_length=50, unique=True)
    name = models.CharField(verbose_name='姓名', max_length=50)
    accomplish = models.FloatField(verbose_name='已修学分',default=0)
    unfinshed = models.FloatField(verbose_name='未修学分', default=0)
    c_type = models.CharField(verbose_name='课程性质', max_length=100)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = '学生学分管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class StGgrade(models.Model):
    st_id = models.CharField(verbose_name='学号', max_length=50, unique=True)
    title = models.CharField(verbose_name='课程名', max_length=50)
    credit = models.FloatField(verbose_name='学分', default=0.0)
    grade = models.FloatField(verbose_name='成绩', default=0.0)
    c_type = models.CharField(verbose_name='课程性质', max_length=100)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = '历年成绩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class MajorSystem(models.Model):
    college = models.CharField(verbose_name='学院', max_length=50)
    major = models.CharField(verbose_name='专业', max_length=50)
    c_type = models.CharField(verbose_name='课程性质', max_length=100, unique=True)
    sum_credit = models.FloatField(verbose_name='总学分', default=0)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = '学分要求'
        verbose_name_plural = verbose_name
        get_latest_by = 'add_time'
        ordering = ['id']

    def __str__(self):
        return self.major