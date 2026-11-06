from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Exam import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # مسیرهای احراز هویت
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # مسیرهای اصلی پروژه
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expenses/', views.expenses, name='expenses'),
    path('invoices/', views.invoices, name='invoices'),
    path('investments/', views.investments, name='investments'),
    path('payrolls/', views.payrolls, name='payrolls'),
    path('reports/', views.reports, name='reports'),
    path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
]