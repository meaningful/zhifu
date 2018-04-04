from django.shortcuts import render_to_response

'''
def index(request):
    #return HttpResponse(template.render(context))
    return render_to_response('index.html')
'''
from django.shortcuts import render
from django.http import JsonResponse
from alipay import AliPay
import os
from django.conf import settings


def index(request):
    return render(request, "blog.html")

def anyStatic(request):
    return render(request, request.path[1:])


# from django.core.mail import send_mail
# send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
# for i in range(10):
#     send_mail('主题： 这是个测试程序', '邮件内容： 如果你收到这个邮件， 说明我的程序能正常的给所有的邮箱账号批量发送邮件了.', '309@qq.com',
#         ['liu_jie_1@qq.com'], fail_silently=False)
# ['liu_jie_1@126.com', '924250451@qq.com'], fail_silently = False)
#     send_mail('主题： 我写了个自动发邮件的代码', '邮件内容： 如果你收到这个邮件， 说明我的程序能正常的给所有的邮箱账号批量发送邮件了. \n 我也不轰炸你， 就发10 封 哈哈哈', '309685872@qq.com',
#               ['763765065@qq.com'], fail_silently=False)
