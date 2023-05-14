from django.urls import path
from.import views

'''
1402000218853912
224488

'''

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.loginUser, name='login'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('create_user/', views.create_user, name='create_user'),
    path('home/', views.home, name='home'),
    path('dashboard-admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard-admin1/<str:pk>', views.dashboard_admin1, name='dashboard_admin1'),
    path('convert-to/<str:pk>', views.convert_to, name='convert_to'),
    path('home-admin/', views.home_admin, name='home_admin'),
    path('file-home/', views.file_home, name='file_home'),
    path('logout/', views.logoutUser, name='logout'),
    path('print_slip/<str:pk>', views.print_slip, name='print_slip'),
    path('edit-entry/<str:pk>', views.edit_entry, name='edit_entry'),


    path('ajax/load_month',views.load_month,name='ajax_load_month'),

]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
