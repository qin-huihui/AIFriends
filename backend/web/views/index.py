# 返回html
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # 是templates里面的html
