from django.db import models

# Create your models here.

class Userinfo(models.Model):
    user_id = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_gender = models.CharField(max_length=1)
    user_rrn1 = models.IntegerField()
    user_rrn2 = models.IntegerField()
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_address_num = models.IntegerField(blank=True, null=True)
    user_address_doro = models.CharField(max_length=100, blank=True, null=True)
    user_address_jibun = models.CharField(max_length=100, blank=True, null=True)
    user_address_detail = models.CharField(max_length=100, blank=True, null=True)
    user_img = models.TextField(blank=True, null=True)
    user_code = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'userinfo'

    # def __str__(self):
    #     return self.user_id

# IntegerField 는 max_length를 할 필요가 없다고 한다.
# ImageField를 사용할꺼면 -m pip install Pillow를 다운받아야 한다고 한다. 물론 적용해보면 터미널에 error와 해결방법이 뜬다.
# 모델의 업데이트 적용을 위해 makemigrations를 진행하고, migrate를 진행해서 정보를 업데이트 시켜야한다.