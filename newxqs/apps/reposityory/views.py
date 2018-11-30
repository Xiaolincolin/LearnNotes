from django.shortcuts import render
from .models import Artcle,HotJob,HotProject,Banner,BorrowBook
from django.views.generic import View
from xq_type.models import Types,personal_type

# Create your views here.


class ReposityoryView(View):
    def get(self, request):
        "招聘列表"
        all_job = HotJob.objects.all()
        all_artcle = Artcle.objects.all()
        all_project = HotProject.objects.all()
        print(all_artcle)
        return render(request, "stydy.html", {
            "all_job":all_job,
            "all_artcle": all_artcle,
            'all_project':all_project,
        })


class JobDetailView(View):
    def get(self, request, job_id):
        #所有人点击量统计
        try:
            click_nums = HotJob.objects.get(id = job_id)
        except:
            click_nums = None
        if click_nums is not None:
            # 主要实现个人登录情况下，阅读情况统计
            if request.user.is_authenticated():
                my_type = personal_type()
                st_id = personal_type.objects.filter(st_id=request.user)
                type_name_p = personal_type.objects.filter(type_name=click_nums.type_name)
                print(st_id)
                print(type_name_p)
                if len(st_id) and len(type_name_p) != 0:
                    # 如果这一类已经存在，则直接在点击量上+1
                    s = personal_type.objects.filter(st_id=request.user, type_name=click_nums.type_name).get()  # 重点标记
                    s.click_times += 1
                    s.save()
                else:
                    # 不存在则加入新的类型或者用户
                    my_type.st_id = request.user
                    my_type.title = click_nums.title
                    my_type.type_name = click_nums.type_name
                    my_type.click_times += 1
                    my_type.save()
            type_name = Types.objects.get(type_name =click_nums.type_name)
            type_name.click_times +=1
            type_name.save()
            click_nums.click_times += 1
            click_nums.save()
        #个人点击统计，登录则记录
        all_job_detail = HotJob.objects.get(id = job_id)
        return  render(request, 'shoperlist.html',{
            'all_job_detail':all_job_detail,
        })


class ArtcleDetailView(View):
    def get(self, request, artcle_id):
        try:
            click_nums = Artcle.objects.get(id = artcle_id)
        except:
            click_nums = None
        if click_nums is not None:
            # 主要实现个人登录情况下，阅读情况统计
            if request.user.is_authenticated():
                my_type = personal_type()
                st_id = personal_type.objects.filter(st_id=request.user)
                type_name_p = personal_type.objects.filter(type_name=click_nums.type_name)
                if len(st_id) and len(type_name_p) != 0:
                    # 如果这一类已经存在，则直接在点击量上+1
                    s = personal_type.objects.filter(st_id=request.user, type_name=click_nums.type_name).get()  # 重点标记
                    s.click_times += 1
                    s.save()
                else:
                    # 不存在则加入新的类型或者用户
                    my_type.st_id = request.user
                    my_type.title = click_nums.title
                    my_type.type_name = click_nums.type_name
                    my_type.click_times += 1
                    my_type.save()

            type_name = Types.objects.get(type_name=click_nums.type_name)
            type_name.click_times += 1
            type_name.save()
            click_nums.click_times +=1
            click_nums.save()
        all_artcle_detail = Artcle.objects.get(id = artcle_id)
        return  render(request, 'showlist.html',{
            'all_artcle_detail':all_artcle_detail,
        })


class ProjectDetailView(View):
    def get(self, request, project_id):
        #所有人点击量统计
        try:
            click_nums = HotProject.objects.get(id = project_id)
        except:
            click_nums = None
        if click_nums is not None:
            #主要实现个人登录情况下，阅读情况统计
            if request.user.is_authenticated():
                my_type = personal_type()
                st_id = personal_type.objects.filter(st_id=request.user)
                type_name_p = personal_type.objects.filter(type_name=click_nums.type_name)
                if len(st_id) and len(type_name_p) !=0:
                    #如果这一类已经存在，则直接在点击量上+1
                    s=personal_type.objects.filter(st_id=request.user,type_name=click_nums.type_name).get() #重点标记
                    s.click_times +=1
                    s.save()
                else:
                    #不存在则加入新的类型或者用户
                    my_type.st_id = request.user
                    my_type.title = click_nums.title
                    my_type.type_name = click_nums.type_name
                    my_type.click_times +=1
                    my_type.save()
            #为了推荐出最热，对某一类做一个点击量统计
            type_name = Types.objects.get(type_name=click_nums.type_name)
            type_name.click_times += 1
            type_name.save()
            click_nums.click_times +=1
            click_nums.save()
        #个人点击统计，登录则记录
        project_detail = HotProject.objects.get(id = project_id)
        return  render(request, 'project.html',{
            'project_detail':project_detail,
        })