from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from .models import UserProfile
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q, Sum
from django.views.generic.base import View
from .forms import LoginForm
from .models import MyMessage
from courese.models import MajorSystem


# Create your views here.


#配置登录名可以是邮箱
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


#登录逻辑
class LoginView(View):
    def get(self,request):
        return render(request, "login.html", {})

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "me.html")
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！"})

        else:
            return render(request, "login.html", {"login_form":login_form})


class MyMessageView(View):
    def get(self,request):
        if request.user.is_authenticated():
            info = MyMessage.objects.get(st_id=request.user)
            sum =MajorSystem.objects.filter(major=info.major).aggregate(sums=Sum('sum_credit'))
            print(sum['sums'])
            # .values('sum_credit').filter(major=info.major)
            # aggregate(sums=sum('sum_credit'))
            # print(credit_sum[0]['sums']).values('sum_credit').annotate(sums=Sum('sum_credit'))
            return render(request, 'me.html',{'info':info})
        else:
            return render(request, 'login.html')