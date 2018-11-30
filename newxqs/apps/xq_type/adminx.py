"""
author: Colin
@time: 2018-11-28 15:22
explain:

"""
from .models import Types,personal_type
import xadmin

class TypesXadmin(object):
    list_display = ['type_name', 'click_times','desc', 'add_time']
    search_fields = ['type_name', 'click_times', 'desc']
    list_filter = ['type_name', 'click_times', 'desc', 'add_time']
    model_icon = 'fa fa-location-arrow'


class personal_typeXadmin(object):
    list_display = ['st_id', 'title', 'type_name', 'click_times', 'add_time']
    search_fields = ['st_id', 'title', 'type_name', 'click_times']
    list_filter = ['st_id', 'title', 'type_name', 'click_times', 'add_time']
    model_icon = 'fa fa-location-arrow'


xadmin.site.register(Types,TypesXadmin)
xadmin.site.register(personal_type, personal_typeXadmin)
