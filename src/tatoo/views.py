from django.http import HttpResponse

from tatoo.tasks import *


def normalize_email(request):
    normalize_email_task.delay(filter={"email__endswith": ".com"})
    return HttpResponse("Task is started")


def get_data(request):
    generate_data.delay()
    return HttpResponse("Task is started")
