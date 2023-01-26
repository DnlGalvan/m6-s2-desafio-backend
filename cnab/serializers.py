from rest_framework import serializers
from .models import Cnab, UploadCnabFile


class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = "__all__"
        extra_kwargs = {"type": {"read_only": True}}


class UploadCnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadCnabFile
        fields = "__all__"
        extra_kwargs = {"cnabs": {"read_only": True}}

    def create(self, validated_data):
        file = validated_data["file"]
        file_obj = UploadCnabFile.objects.create(file=file)

        file_list = []

        with open(
            f"cnab_files/{str(file_obj.file)}", "r", encoding="utf-8"
        ) as reading_file:
            for line in reading_file:
                file_list.append(line)

        for item in file_list:
            type:str = item[:1]
            day:str = item[7:9]
            month:str = item[5:7]
            year:str = item[1:5]
            date:str = f"{year}-{month}-{day}"
            value_item:str = item[9:19]
            value = int(value_item) / 100.00
            cpf:str = item[19:30]
            credit_card:str = item[30:42]
            hour_item:str = item[42:44]
            minutes:str = item[44:46]
            seconds:str = item[46:48]
            hour:str = f"{hour_item}:{minutes}:{seconds}"
            owner_shop:str = item[48:62]
            shop_name:str = item[62:81]

            if type == "1":
                type = "Débito"

            elif type == "2":
                type = "Boleto"

            elif type == "3":
                type = "Financiamento"

            elif type == "4":
                type = "Crédito"

            elif type == "5":
                type = "Recebimento Empréstimo"

            elif type == "6":
                type = "Vendas"

            elif type == "7":
                type = "Recebimento TED"

            elif type == "8":
                type = "Recebimento DOC"

            elif type == "9":
                type = "Aluguel"

            cnab_obj = Cnab.objects.create(
                type=type.strip(),
                date=date.strip(),
                value=value,
                cpf=cpf.strip(),
                credit_card=credit_card.strip(),
                hour=hour.strip(),
                owner_shop=owner_shop.strip(),
                shop_name=shop_name.strip(),
                cnab_file=file_obj,
            )
        file_obj.file_content = cnab_obj
        file_obj.save()

        return file_obj
