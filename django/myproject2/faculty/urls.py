from django.urls import path

from faculty import views


urlpatterns= [
    path('index/',views.index,name="index"),
    path('home/',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path("data/",views.data,name="data"),
    path("about/",views.about,name="about"),
   # ,,data
   path('dele/<int:id>/',views.dele,name="dele"),
   path('update/<int:id>/',views.update,name="update"),
   path('mail/',views.mail,name='mail'),
   path('img/',views.img,name='img'),
   path('imgdisplay/',views.imgdisplay,name='imgdisplay'),
   path('emp/<int:id>',views.emp,name='emp'),
]