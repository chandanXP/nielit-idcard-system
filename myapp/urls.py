# myapp/urls.py
from django.urls import path
from .views import employee_list, employee_detail, generate_qr, download_id_card, register, student_detail

urlpatterns = [
    path('', register, name='add_employee'),  # Add this line
    path('list/', employee_list, name='employee_list'),
    path('<str:employee_id>/', employee_detail, name='employee_detail'),
    path('generate_qr/<str:employee_id>/', generate_qr, name='generate_qr'),
    path('student_detail/<str:enrollment_number>/', student_detail, name='student_detail'),
    path('list/download/', download_id_card, name='download_id_card'),
    # Add other URL patterns as needed
]
