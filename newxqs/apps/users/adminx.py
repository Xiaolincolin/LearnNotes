"""
author: Colin
@time: 2018-11-28 14:55
explain:

"""
import xadmin
from xadmin import views
from .models import  MyMessage

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlonalSettings(object):
    site_title = "高校学情分析与导向式学习平台"
    site_footer = "数据与可视化团队"
    menu_style = "accordion"

class MyMessageXadmin(object):
    list_display = ['name', 'st_id','college', 'major', 'grade', 'gender', 'image', 'favor','promote_sys', 'add_time']
    search_fields = ['name', 'st_id','college', 'major', 'grade', 'gender', 'image', 'favor','promote_sys']
    list_filter= ['name', 'st_id','college', 'major', 'grade', 'gender', 'image', 'favor','promote_sys', 'add_time']
    model_icon = 'fa fa-lightbulb-o'


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlonalSettings)
xadmin.site.register(MyMessage,MyMessageXadmin)
