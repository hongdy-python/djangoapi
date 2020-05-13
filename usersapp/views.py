from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from usersapp.models import Usera


def user(request):
    if request.method == "GET":
        print("GET 查询")
        return HttpResponse("GET SUCCESS")
    elif request.method == "POST":
        print("POST 添加")
        return HttpResponse("POST SUCCESS")
    elif request.method == "PUT":
        print("PUT 修改")
        return HttpResponse("PUT SUCCESS")
    elif request.method == "DELETE":
        print("DELETE 删除")
        return HttpResponse("DELETE SUCCESS")


# csrf_exempt: 可以免除某个方法的csrf认证
# csrf_protect：可以为某个视图单独添加csrf认证
@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):

    def get(self, request, *args, **kwargs):
        """提供查询单个  多个用户的API"""
        user_id = kwargs.get("pk")
        if user_id:  # 查询单个
            user_values = Usera.objects.filter(pk=user_id).values("id","username", "password", "gender").first()
            if user_values:
                return JsonResponse({
                    "status": 200,
                    "message": "获取用户成功",
                    "results": user_values
                })
        else:  # 如果用户id不存且发的是get请求  代表是获取全部用户信息
            user_list = Usera.objects.all().values("id","username", "password", "gender")
            if user_list:
                return JsonResponse({
                    "status": 201,
                    "message": "获取用户列表成功",
                    "results": list(user_list)
                })

        return JsonResponse({
            "status": 400,
            "message": "获取用户不存在",
        })

    def post(self, request, *args, **kwargs):
        """完成新增单个用户的操作"""
        print(request.POST)
        # 对post传递过来的参数进行校验
        try:
            user_obj = Usera.objects.create(**request.POST.dict())
            if user_obj:
                return JsonResponse({
                    "status": 200,
                    "message": "新增用户成功",
                    "results": {"username": user_obj.username, "gender": user_obj.gender}
                })
            else:
                return JsonResponse({
                    "status": 500,
                    "message": "新增用户失败",
                })
        except:
            return JsonResponse({
                "status": 501,
                "message": "参数有误",
            })

    def put(self, request, *args, **kwargs):
        print("PUT 修改")
        # print(**request.query_params.dict())
        # try:
        #
        #     user_obj = Usera.objects.filter(**request.POST.id)
        #     # user_obj = Usera.objects.create(**request.POST.dict())
        #     if user_obj:
        #         user_obj.username=request.POST.username
        #         user_obj.password=request.POST.password
        #         user_obj.gender=request.POST.gender
        #         user_obj.save()
        #         return JsonResponse({
        #             "status": 200,
        #             "message": "修改用户成功",
        #             "results": {"username": user_obj.username, "gender": user_obj.gender}
        #         })
        #     else:
        #         return JsonResponse({
        #             "status": 500,
        #             "message": "修改用户失败",
        #         })
        # except:
        #     return JsonResponse({
        #         "status": 501,
        #         "message": "参数有误",
        #     })

    def delete(self, request, *args, **kwargs):
        print("DELETE 删除")
        # try:
        #     user_obj = Usera.objects.filter(**request.POST.dict())
        #
        #     if user_obj:
        #         user_obj.delete()
        #         return JsonResponse({
        #             "status": 200,
        #             "message": "删除用户成功",
        #
        #         })
        #     else:
        #         return JsonResponse({
        #             "status": 500,
        #             "message": "删除用户失败",
        #         })
        # except:
        #     return JsonResponse({
        #         "status": 501,
        #         "message": "参数有误",
        #     })


class StudentView(APIView):
    # renderer_classes = [BrowsableAPIRenderer]

    parser_classes = [JSONParser]  # json数据包
    # parser_classes = [FormParser]   # urlencoded数据包
    # parser_classes = [MultiPartParser]  # form-data数据包

    def get(self, request, *args, **kwargs):
        """DRF获取get请求参数的方式"""
        print(request._request.GET)  # 原生django request对象
        print(request.GET)  # DRF request 对象
        print(request.query_params)  # DRF 扩展的get请求参数
        return Response("GET SUCCESS")

    def post(self, request, *args, **kwargs):
        """DRF 获取POST请求参数的方式"""
        # POST传递参数的形式 formdata urlencoding Json
        print(request._request.POST)  # 原生django request对象
        print(request.POST)  # DRF request 对象
        print(request.data)  # DRF 扩展post请求参数   兼容性最强

        return Response("POST SUCCESS")