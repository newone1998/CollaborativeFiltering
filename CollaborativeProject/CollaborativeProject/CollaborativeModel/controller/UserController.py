import json

from CollaborativeModel.domain.RequestClass import RequestClass
from CollaborativeProject.CollaborativeModel.services.UserService import get_user_by_name_service
from django.core import serializers
from django.http import HttpResponse


def get_user_by_name_controller(request):
    name = request.GET["name"]
    result = get_user_by_name_service(name)
    request_class = RequestClass()
    request_class.msg = '查询成功'
    if not result:
        request_class.status = RequestClass.FAULT_STATUS
        request_class.msg = '未查询到用户'
    result = serializers.serialize("json", request_class)
    return HttpResponse(result)
