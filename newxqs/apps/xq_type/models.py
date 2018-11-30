from django.db import models
from datetime import datetime


class Types(models.Model):

    type_name = models.CharField(verbose_name='类名',max_length=50,unique=True)
    desc = models.TextField(verbose_name='描述',null=True, blank=True)
    click_times = models.IntegerField(verbose_name='点击次数',default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '总分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.type_name


class personal_type(models.Model):
    st_id = models.CharField(verbose_name='学号', max_length=50, default='')
    title = models.CharField(verbose_name='标题',max_length=200,)
    type_name = models.ForeignKey(Types,verbose_name='类名')
    click_times = models.IntegerField(verbose_name='点击次数',default=0)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '个人分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.st_id


