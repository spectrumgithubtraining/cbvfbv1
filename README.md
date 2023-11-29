Function-based view vs Class-based views
In Django, a function-based view (FBV) is a view that is implemented as a Python function. 
It is one of the two primary ways to define views in Django, the other being class-based views (CBVs).
Function-based view:
**from django.http import HttpResponse
def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('Hello world')**
In class-based view, this will become:
# myapp/views.py
**from django.http import HttpResponse
from django.views import View
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('Hello world')**
    1. So in CBV, you need to import View class from django.views, then sub-class your view class from imported class.
    2. And, the request.method == ‘GET’, changes to get method, i.e. to handle ‘GET’ methods in CBV we use get method.
Now, since Django’s URL resolver expects to send the request and associated arguments to a callable function, not a class,
class-based views have an as_view method which returns a function that can be called when a request arrives for a URL matching the associated pattern. 
i.e. while calling view in your URLs file use as_view method like shown below.
# urls.pyfrom django.urls import path
from myapp.views import MyView
urlpatterns = [
    path('about/', MyView.as_view()),
]
