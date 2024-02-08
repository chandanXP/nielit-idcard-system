# myapp/admin.py
import os
import zipfile
from io import BytesIO

import pandas as pd
from django.conf import settings
from django.contrib import admin
from django.core.checks import messages
from django.contrib import messages
from django.http import HttpResponse
from django.utils.html import format_html
from .models import Employee, Student, Course, Branch
from .views import generate_qr, generate_student
import csv
# from openpyxl import Workbook


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'employee_id', 'department', 'dob', 'gender', 'contact', 'email', 'job_title', 'join_date', 'end_date', 'work_location', 'display_image']
    search_fields = ['name', 'employee_id', 'job_title', 'department']
    list_filter = ['department', 'job_title', 'join_date', 'end_date', 'gender']  # Add these lines to include filters
    ordering = ['name', 'employee_id', 'join_date', 'end_date']

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;">', obj.profile_image.url)

    display_image.short_description = 'Profile Image'

    actions = ['generate_qr_action', 'download_id_card_action', 'export_to_excel_csv']

    def generate_qr_action(self, request, queryset):
        generate_qr(self, request, queryset)  # Pass the entire queryset

    generate_qr_action.short_description = "Generate QR Code for Selected Employees"

    def download_id_card_action(self, request, queryset):
        # Display a confirmation pop-up
        if "_download_id_card_action" in request.POST:
            messages.warning(request, "Make sure that you have generated cards for all the selected employees.")
            return None

        # Assuming generate_qr_action is triggered before download_id_card_action
        # The ID card images should be available in the STATIC_ROOT directory

        # Assuming that the primary key name is 'employee_id'
        employee_id_field_name = 'employee_id'

        zip_file_name = "employee-card.zip"
        in_memory_zip = BytesIO()
        with zipfile.ZipFile(in_memory_zip, 'w') as zipf:
            for obj in queryset:
                front_file_path = os.path.join(settings.STATIC_ROOT, 'download', f'{obj.employee_id}_front.jpg')
                back_file_path = os.path.join(settings.STATIC_ROOT, 'download', f'{obj.employee_id}_back.jpg')
                print(obj.employee_id)

                if os.path.exists(front_file_path):
                    file_name = os.path.basename(front_file_path)
                    zipf.write(front_file_path, file_name)
                    os.remove(front_file_path)

                if os.path.exists(back_file_path):
                    file_name = os.path.basename(back_file_path)
                    zipf.write(back_file_path, file_name)
                    os.remove(back_file_path)

        response = HttpResponse(in_memory_zip.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_file_name}"'
        return response

    download_id_card_action.short_description = "Download ID Card for Selected Employees"

    def export_to_excel_csv(self, request, queryset):
        try:
            fields = ['name', 'employee_id', 'department', 'dob', 'gender', 'contact', 'email', 'job_title', 'join_date', 'end_date', 'work_location']

            df = pd.DataFrame(list(queryset.values(*fields)))

            file_name = "employee_data.csv"  # Change the file extension to .csv

            # Save the DataFrame to CSV
            df.to_csv(file_name, index=False)

            # Send the file as a response
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            df.to_csv(response, index=False)

            return response
        except Exception as e:
            messages.error(request, f'Error exporting data: {str(e)}')
            return None

    export_to_excel_csv.short_description = "Export selected data to Excel/CSV"
    export_to_excel_csv.allowed_permissions = ('change',)


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'batch',
        'enrollment_number',
        'course',
        'branch',
        'name',
        'dob',
        'gender',
        'contact',
        'email',
        'city',
        'district',
        'state',
        'pincode',
        'valid_date_from',
        'date_upto',
        'location',
        'display_image']
    search_fields = ['name', 'enrollment_number', 'batch', 'course', 'branch']
    list_filter = ['batch', 'course', 'branch', 'gender']
    ordering = ['name', 'enrollment_number', 'valid_date_from', 'date_upto']

    def display_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;">', obj.profile_image.url)

    display_image.short_description = 'Profile Image'

    actions = ['generate_qr_action', 'download_id_card_action', 'export_to_excel_csv']

    def generate_qr_action(self, request, queryset):
        generate_student(self, request, queryset)

    generate_qr_action.short_description = "Generate Cards for Selected Students"

    def download_id_card_action(self, request, queryset):
        # Display a confirmation pop-up
        if "_download_id_card_action" in request.POST:
            messages.warning(request, "Make sure that you have generated cards for all the selected students.")
            return None

        # Assuming generate_qr_action is triggered before download_id_card_action
        # The ID card images should be available in the STATIC_ROOT directory

        zip_file_name = "student-card.zip"
        in_memory_zip = BytesIO()
        with zipfile.ZipFile(in_memory_zip, 'w') as zipf:
            for student in queryset:
                front_file_path = os.path.join(settings.STATIC_ROOT, 'download', f'{student.enrollment_number}_front.jpg')
                back_file_path = os.path.join(settings.STATIC_ROOT, 'download', f'{student.enrollment_number}_back.jpg')
                print(student.enrollment_number)

                if os.path.exists(front_file_path):
                    file_name = os.path.basename(front_file_path)
                    zipf.write(front_file_path, file_name)
                    os.remove(front_file_path)

                if os.path.exists(back_file_path):
                    file_name = os.path.basename(back_file_path)
                    zipf.write(back_file_path, file_name)
                    os.remove(back_file_path)

        response = HttpResponse(in_memory_zip.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_file_name}"'
        return response

    download_id_card_action.short_description = "Download Card for Selected Students"

    def export_to_excel_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="students_export.csv"'

        writer = csv.writer(response)
        writer.writerow(['Batch', 'Enrollment Number', 'Course', 'Branch', 'Name', 'DOB', 'Gender',
                         'Contact', 'Email', 'City', 'District', 'State', 'Pincode',
                         'Valid Date From', 'Date Upto', 'Location'])

        for student in queryset:
            writer.writerow([
                student.batch,
                student.enrollment_number,
                student.course,
                student.branch,
                student.name,
                student.dob,
                student.gender,
                student.contact,
                student.email,
                student.city,
                student.district,
                student.state,
                student.pincode,
                student.valid_date_from,
                student.date_upto,
                student.location,
            ])

        return response

    export_to_excel_csv.short_description = "Export selected students to Excel/CSV"


# @admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name']
    search_fields = ['course_name']


# @admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name', 'course']


admin.site.register(Course)
admin.site.register(Branch)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Student, StudentAdmin)
