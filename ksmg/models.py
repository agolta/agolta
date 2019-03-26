from django.db import models
import datetime
from ksmg import codes

def year_choices():
    return [(r,r) for r in range(datetime.date.today().year-1, datetime.date.today().year+5)]

def current_year():
    return datetime.date.today().year

class Ksmg(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    gubun = models.CharField(max_length=200, choices=codes.GUBUN)
    detail = models.CharField(max_length=4000)
    expect_effect_asis = models.CharField(max_length=4000)
    expect_effect_tobe = models.CharField(max_length=4000)
    next_user = models.ForeignKey('auth.user', related_name='ksmg_next_user', on_delete=models.CASCADE)
    request_confirm = models.CharField(max_length=10, choices=codes.YN)
    request_confirm_detail = models.CharField(max_length=4000)
    request_user = models.ForeignKey('auth.user', related_name='ksmg', on_delete=models.CASCADE)
    created_dt = models.DateTimeField(auto_now_add=True)

class KsmgEE(models.Model): #Expect Effect
    ksmg = models.ForeignKey(Ksmg, related_name='ksmgee', on_delete=models.CASCADE)
    year = models.IntegerField(choices=year_choices(), default=current_year())
    sales = models.IntegerField()
    cost_save = models.IntegerField()
    productivity = models.CharField(max_length=1000)
    quality = models.CharField(max_length=1000)
    etc = models.CharField(max_length=1000)
    
    class Meta:
        ordering = ['year']
