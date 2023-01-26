from django.shortcuts import render
from rest_framework.views import APIView
from .models import Cnab, UploadFileForm
from .serializers import UploadCnabSerializer
from .utils import (
    total_value_1,
    total_value_2,
    total_value_3,
    total_value_4,
    total_value_5,
)


class UploadCnabView(APIView):
    def get(self, request, *args, **kwargs):
        form = UploadFileForm()
        return render(request, "home.html", {"form": form})

    def post(self, request, *args, **kwargs):
        serializer = UploadCnabSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        cnab_list_1 = Cnab.objects.filter(shop_name="BAR DO JOÃO")
        cnab_list_2 = Cnab.objects.filter(shop_name="LOJA DO Ó - MATRIZ")
        cnab_list_3 = Cnab.objects.filter(shop_name="MERCADO DA AVENIDA")
        cnab_list_4 = Cnab.objects.filter(shop_name="MERCEARIA 3 IRMÃOS")
        cnab_list_5 = Cnab.objects.filter(shop_name="LOJA DO Ó - FILIAL")

        value_1 = total_value_1()
        value_2 = total_value_2()
        value_3 = total_value_3()
        value_4 = total_value_4()
        value_5 = total_value_5()

        return render(
            request,
            "results.html",
            context={
                "cnab_list_1": cnab_list_1,
                "cnab_list_2": cnab_list_2,
                "cnab_list_3": cnab_list_3,
                "cnab_list_4": cnab_list_4,
                "cnab_list_5": cnab_list_5,
                "value_1": value_1,
                "value_2": value_2,
                "value_3": value_3,
                "value_4": value_4,
                "value_5": value_5,
            },
        )
