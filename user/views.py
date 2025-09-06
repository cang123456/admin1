from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from user.models import SysUser


# Create your views here.


class TestView(View):

    def get(self,request):
        userList_obj = SysUser.objects.all() # 一开始就查询数据库，获取的数据是QuerySet对象，不能直接用jsonify返回
        print(userList_obj,type(userList_obj))
        userList_dict = userList_obj.values() # 转化为字典列表
        print(userList_dict,type(userList_dict))
        userList = list(userList_dict)
        return JsonResponse({'code':200,'info':'测试','data':userList})