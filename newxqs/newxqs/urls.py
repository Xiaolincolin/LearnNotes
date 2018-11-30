"""newxqs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView
from reposityory.views import ReposityoryView,JobDetailView,ArtcleDetailView,ProjectDetailView
from users.views import MyMessageView


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 配置login登录
    url(r'^login/$', LoginView.as_view(), name="login"),

    #主页面
    url(r'^study/$', ReposityoryView.as_view(), name='study'),

    #招聘详情页面
    url(r'^jobdetail/(\d+)', JobDetailView.as_view(), name='jobdetail'),

    #文章的详情页面
    url(r'^artcledetail/(\d+)', ArtcleDetailView.as_view(), name='artcledetail'),

    #开源项目详情页面
    url(r'^projectdetail/(\d+)', ProjectDetailView.as_view(), name='projectdetail'),

    #个人中心
    url(r'^main/$', MyMessageView.as_view(), name='main'),

]
