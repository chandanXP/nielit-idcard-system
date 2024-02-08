import time
import qrcode
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm, StudentForm, CourseForm, BranchForm
import os
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .models import Employee, Student
from .Card.GenerateCard import *


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})


def student_detail(request, enrollment_number):
    student = get_object_or_404(Student, enrollment_number=enrollment_number)
    return render(request, 'student_detail.html', {'student': student})


def register(request):
    employee_form = EmployeeForm()
    student_form = StudentForm()

    if request.method == 'POST':
        if 'employee_submit' in request.POST:
            employee_form = EmployeeForm(request.POST, request.FILES)
            if employee_form.is_valid():
                employee_form.save()
                messages.success(request, 'Your registration successful.')
                return redirect('/')  # Replace with your actual URL pattern for employee list
            else:
                messages.error(request, 'Registration failed. Please check the form.')
        elif 'student_submit' in request.POST:
            student_form = StudentForm(request.POST, request.FILES)
            if student_form.is_valid():
                student_form.save()
                messages.success(request, 'Your registration successful.')
                return redirect('/')  # Replace with your actual URL pattern for student list
            else:
                messages.error(request, 'Registration failed. Please check the form.')

    return render(request, 'register.html', {'employee_form': employee_form, 'student_form': student_form})


def generate_qr(modeladmin, request, queryset):
    for emp in queryset:
        try:
            # Define a mapping between department names and template file names
            department_templates = {
                'WBL': 'WBL_TEMPLATE',
                'Faculty': 'FACULTY_TEMPLATE',
                'Guest Faculty': 'GUEST_FACULTY_TEMPLATE',
                # Add more mappings as needed
            }

            # Get the department name
            department = emp.department

            # Check if the department has a corresponding template
            if department in department_templates:
                # Construct the template file names
                front_template_path = f"C:\\wbl\\vishal\\myapp\\Card\\{department_templates[department]}_FRONT.png"
                back_template_path = f"C:\\wbl\\vishal\\myapp\\Card\\{department_templates[department]}_BACK.png"

                # Generate QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                url = f'https://idcardnielit.pythonanywhere.com/employee/{emp.employee_id}'
                qr.add_data(url)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")

                # Save the QR code image in the STATIC_ROOT directory
                qr_code_directory = os.path.join(settings.STATIC_ROOT, 'QR')
                os.makedirs(qr_code_directory, exist_ok=True)  # Ensure the directory exists
                img_path = os.path.join(qr_code_directory, f"{emp.employee_id}.png")
                img.save(img_path)

                time.sleep(2)

                name = emp.name
                employee_id = emp.employee_id  # Use a different variable name to avoid conflicts
                email = emp.email
                phone = emp.contact
                profile_img = emp.profile_image
                jdate = emp.join_date
                edate = emp.end_date
                image_bytes = profile_img.read()

                # writing on template card
                write_front_text(name, employee_id, email, phone, front_template_path)
                write_text_back(department, jdate, edate, back_template_path, employee_id)
                write_front_image(image_bytes, employee_id)
                write_qr(rf"C:\wbl\vishal\static\QR\{employee_id}.png", employee_id)

            else:
                response_data = {"message": f"No template found for department: {department}"}
                return JsonResponse(response_data, status=404)

        except Employee.DoesNotExist:
            response_data = {"message": "Employee not found."}
            return JsonResponse(response_data, status=404)

    # Move the return statement outside the loop
    response_data = {"message": "QR code generated and saved successfully."}
    return JsonResponse(response_data)


def generate_student(modeladmin, request, queryset):
    for stu in queryset:
        try:
            # Retrieve employee details
            stu = Student.objects.get(enrollment_number=stu.enrollment_number)

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            url = f'https://idcardnielit.pythonanywhere.com/student_detail/{stu.enrollment_number}'
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image in the STATIC_ROOT directory
            qr_code_directory = os.path.join(settings.STATIC_ROOT, 'QR')
            os.makedirs(qr_code_directory, exist_ok=True)  # Ensure the directory exists
            img_path = os.path.join(qr_code_directory, f"{stu.enrollment_number}.png")
            img.save(img_path)

            time.sleep(2)

            id = stu.enrollment_number
            name = stu.name
            course = stu.course
            branch = stu.branch
            phone = stu.contact
            profile_img = stu.profile_image
            batch = stu.batch
            valid_date_from = stu.valid_date_from
            date_upto = stu.date_upto
            image_bytes = profile_img.read()
            address1 = stu.city + " " + stu.district
            address2 = stu.state + " " + stu.pincode
            img_path = r"C:\wbl\vishal\myapp\Card\STUDENT_TEMPLATE_FRONT.png"

            # writing on template card
            write_front_text_student(name, id, course, branch, phone, img_path)
            write_text_back_student(batch, valid_date_from, date_upto, address1, address2, r"C:\wbl\vishal\myapp\Card\STUDENT_TEMPLATE_BACK.png", id)
            write_front_image(image_bytes, id)
            write_qr_student(rf"C:\wbl\vishal\static\QR\{id}.png", id)

        except Student.DoesNotExist:
            response_data = {"message": "Student not found."}
            return JsonResponse(response_data, status=404)

    response_data = {"message": "QR code generated and saved successfully."}
    return JsonResponse(response_data)


def download_id_card(request):
    file_paths = [
        os.path.join(settings.STATIC_ROOT, 'download/idcard_front.jpg'),
        os.path.join(settings.STATIC_ROOT, 'download/idcard_back.jpg')
    ]
    zip_file_name = "wbl-card.zip"  # Name for the zip file to contain both images

    if all(os.path.exists(path) for path in file_paths):
        # Create a zip file containing both images
        import zipfile
        from io import BytesIO

        in_memory_zip = BytesIO()
        with zipfile.ZipFile(in_memory_zip, 'w') as zipf:
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                zipf.write(file_path, file_name)

        # Prepare the HttpResponse with the zip content
        response = HttpResponse(in_memory_zip.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_file_name}"'
        return response

    else:
        return HttpResponse("Files not found!")


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')  # Redirect to the course list view (create it in urls.py)
    else:
        form = CourseForm()

    return render(request, 'create_course.html', {'form': form})


def create_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')  # Redirect to the desired view
    else:
        form = BranchForm()

    return render(request, 'create_branch.html', {'form': form})
