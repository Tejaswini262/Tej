from django.urls import path,include
from . import views


urlpatterns = [
   # path('admin/', admin.site.urls),
  path('',views.loginpage, name = 'loginpage'),
  path('signup/',views.signup, name = 'signup'),
  path('home/',views.home, name = 'home'),
  path('download/',views.download, name='download')
 



]


# urls.py
