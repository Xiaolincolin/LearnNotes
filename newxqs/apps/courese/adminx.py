"""
author: Colin
@time: 2018-11-28 19:30
explain:

"""
import xadmin
from .models import  Coursetable,StGgrade,StCredit,MajorSystem


class MajorSystemXadmin(object):
    list_display = ['college', 'major', 'c_type', 'sum_credit', 'add_time']
    search_fields = ['college', 'major', 'c_type', 'sum_credit']
    list_filter = ['college', 'major', 'c_type', 'sum_credit', 'add_time']
    model_icon = 'fa fa-lightbulb-o'


class CoursetableXadmin(object):
    list_display = ['college', 'major', 'c_type', 'c_id', 'title','credit', 'period', 'semester', 'add_time']
    search_fields = ['college', 'major', 'c_type', 'c_id', 'title','credit', 'period', 'semester']
    list_filter= ['college', 'major', 'c_type', 'c_id', 'title','credit', 'period', 'semester', 'add_time']
    model_icon = 'fa fa-table'


class StCreditXadmin(object):
    list_display = ['st_id', 'name', 'accomplish', 'unfinshed', 'c_type', 'add_time']
    search_fields = ['st_id', 'name', 'accomplish', 'unfinshed', 'c_type']
    list_filter = ['st_id', 'name', 'accomplish', 'unfinshed', 'c_type', 'add_time']
    model_icon = 'fa fa-bars'


class StGgradeXadmin(object):
    list_display = ['st_id', 'name', 'credit', 'grade', 'c_type', 'add_time']
    search_fields = ['st_id', 'name', 'credit', 'grade', 'c_type']
    list_filter = ['st_id', 'name', 'credit', 'grade', 'c_type', 'add_time']
    model_icon = 'fa fa-folder-open-o'




xadmin.site.register(MajorSystem,MajorSystemXadmin)
xadmin.site.register(Coursetable,CoursetableXadmin)
xadmin.site.register(StGgrade,StGgradeXadmin)
xadmin.site.register(StCredit,StCreditXadmin)

