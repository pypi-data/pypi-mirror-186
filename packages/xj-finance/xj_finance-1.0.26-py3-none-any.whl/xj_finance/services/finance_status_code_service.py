import time
import os
import datetime

from django.db.models import Q
from django.db.models import F
from rest_framework.response import Response

from ..models import StatusCode


class FinanceStatusCodeService:

    @staticmethod
    def get():
        currencies = StatusCode.objects.all()

        return list(currencies.values('id', 'finance_status_code', 'description'))

    @staticmethod
    def post(params):
        finance_status_code = params.get('finance_status_code', '')
        if finance_status_code:
            sand_box_set = StatusCode.objects.filter(finance_status_code=finance_status_code).first()
            if sand_box_set is not None:
                return None, "finance_status_code  已存在"
        try:
            StatusCode.objects.create(**params)
            return None, None
        except Exception as e:
            return None, "参数配置错误：" + str(e)
