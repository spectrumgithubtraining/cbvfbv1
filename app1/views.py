from django.http import HttpResponse
def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('Hello world')