# Create your views here.
from django.http import HttpRequest,HttpResponse
from dj_simple_sms.models import SMS

def sendSMS(request,from_number,to,body):
    if request.method == "GET":
        message=str(body)
        messageready = SMS(to_number = to , from_number = from_number , body = body)
        messageready.send()
        
    response ='smsAPI PRO<hr><br/>SMS From <span style="color:green">%s</span> To <span style="color:red">%s</span> <br/> body %s<br/>' %(from_number,to,body)
    return HttpResponse(response)

