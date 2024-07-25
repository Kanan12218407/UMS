from multiprocessing import context
from django.shortcuts import render,HttpResponse
from django.shortcuts import redirect, reverse
from datetime import datetime
from home1.models import Contact
from django.contrib import messages
from .models import Courseregistration
from .models import scholarship
from .models import Counselling
from .models import Placement
from .models import RMS
from .models import Feees
from .models import Hostel
from .models import Transport
from .models import Semex
from .models import Leave
from .models import Re

def index(request):
    messages.success(request,"Login Successful !")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

    
def contact(request):
    if request.method == "POST":
    
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        
        contact = Contact(
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            email=email,
            desc=desc,
            date=datetime.today()  
        )
        contact.save()  
        messages.success(request, "Your Request has been sent !!")

    
    return render(request, 'contact.html')


def Admissions(request):
    return render(request, 'Admissions.html')

def cse(request):
    return render(request, 'cse.html')

def mba(request):
    return render(request, 'mba.html')

def economics(request):
    return render(request, 'economics.html')

def environmentalscience(request):
    return render(request, 'environmentalscience.html')

def publichealth(request):
    return render(request, 'publichealth.html')

def psychology(request):
    return render(request, 'psychology.html')

def courseregistration(request):
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        phone_number = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        email = request.POST.get('email')
        father_name = request.POST.get('fatherName')
        mother_name = request.POST.get('motherName')
        father_occupation = request.POST.get('fatherOccupation')
        mother_occupation = request.POST.get('motherOccupation')
        academic_details = request.POST.get('academicDetails')
        course = request.POST.get('course')
        dob = request.POST.get('dob')
        
        courseregistration = Courseregistration(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            address=address,
            email=email,
            father_name=father_name,
            mother_name=mother_name,
            father_occupation=father_occupation,
            mother_occupation=mother_occupation,
            academic_details=academic_details,
            course=course,
            date_of_birth=dob,
            registration_date=datetime.today()
        )
        courseregistration.save()
        
        messages.success(request, "Your registration has been submitted successfully!")

    return render(request, 'courseregistration.html')

def feecse(request):
    return render(request, 'feecse.html')

def feemba(request):
    return render(request, 'feemba.html')

def feeeco(request):
    return render(request, 'feeeco.html')

def feeev(request):
    return render(request, 'feeev.html')

def feemph(request):
    return render(request, 'feemph.html')

def feepsy(request):
    return render(request, 'feepsy.html')

def counselling(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        preferred_timeslot = request.POST.get('timeslot')


        try:
            counselling= Counselling(
                fullname=fullname,
                email=email,
                phone_number=phone_number,
                preferred_timeslot=preferred_timeslot
            )
            counselling.save()
            messages.success(request, "Your counseling registration has been submitted successfully.")
        except Exception as e:
            messages.error(request, f"Error occurred: {str(e)}")

    return render(request, 'counselling.html')

def acse(request):
    return render(request, 'cse.html')

def amba(request):
    return render(request, 'mba.html')

def aeconomics(request):
    return render(request, 'economics.html')

def aenvironmentalscience(request):
    return render(request, 'environmentalscience.html')

def apublichealth(request):
    return render(request, 'publichealth.html')

def apsychology(request):
    return render(request, 'psychology.html')


def acourseregistration(request):
    return render(request, 'courseregistration.html')


def Scholarship(request):
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        phone_number = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        tenth_marks = request.POST.get('10thMarks')
        twelfth_marks = request.POST.get('12thMarks')
        diploma_marks = request.POST.get('diplomaMarks')
        competitive_exam_score = request.POST.get('competitiveExamScore')
        university_exam_score = request.POST.get('universityExamScore')
        course = request.POST.get('course')


    
        Scholarship = scholarship(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                email=email,
                tenth_marks=float(tenth_marks),
                twelfth_marks=float(twelfth_marks),
                diploma_marks=float(diploma_marks) if diploma_marks else None,
                competitive_exam_score=float(competitive_exam_score),
                university_exam_score=float(university_exam_score) if university_exam_score else None,
                course=course
            )
        Scholarship.save()
        messages.success(request, "Your scholarship application has been submitted successfully.")

    return render(request, 'Scholarship.html')

def implink(request):
    return render(request, 'implink.html')

def infrastructure(request):
    return render(request, 'infrastructure.html')

def faculty(request):
    return render(request, 'faculty.html')

def students(request):
    return render(request, 'students.html')

def hostel(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        student_id = request.POST.get('studentID')
        contact_number = request.POST.get('contactNumber')
        email = request.POST.get('email')
        room_type = request.POST.get('roomType')
        duration = int(request.POST.get('duration'))
        meal_plan = request.POST.get('mealPlan')
        meal_days = int(request.POST.get('mealDays'))
        laundry_service = True if request.POST.get('laundry') else False
        gym_access = True if request.POST.get('gym') else False
        
    
        accommodation_charge = calculate_accommodation_charge(room_type, duration)
        meal_charge = calculate_meal_charge(meal_plan, meal_days)
        additional_charges = calculate_additional_charges(laundry_service, gym_access)
        total_amount = accommodation_charge + meal_charge + additional_charges
        
        hostel = Hostel(
            name=name,
            student_id=student_id,
            contact_number=contact_number,
            email=email,
            room_type=room_type,
            duration=duration,
            meal_plan=meal_plan,
            meal_days=meal_days,
            laundry_service=laundry_service,
            gym_access=gym_access
        )
        hostel.save()
        
        
    return render(request, 'hostel.html')

def calculate_accommodation_charge(room_type, duration):
    
    room_prices = {
        "4seater": 100,
        "3seater": 250,
        "2seater": 500,
        "singleseater": 700
    }
    return room_prices.get(room_type, 0) * duration

def calculate_meal_charge(meal_plan, meal_days):
    
    meal_prices = {
        "2meals": 3,
        "3meals": 5,
        "4meals": 7,
    }
    return meal_prices.get(meal_plan, 0) * meal_days

def calculate_additional_charges(laundry_service, gym_access):

    additional_charges = 0
    if laundry_service:
        additional_charges += 50
    if gym_access:
        additional_charges += 70
    return additional_charges


def transport(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('studentID')
        contact_number = request.POST.get('contactNumber')
        email = request.POST.get('email')
        transport_option = request.POST.get('transportOption')
        distance_covered = int(request.POST.get('distanceCovered'))

        transport = Transport(
            name=name,
            student_id=student_id,
            contact_number=contact_number,
            email=email,
            transport_option=transport_option,
            distance_covered=distance_covered
        )
        transport.save()


    return render(request, 'transport.html')


def semex(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('studentID')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        current_university = request.POST.get('currentUniversity')
        major = request.POST.get('major')
        comments = request.POST.get('comments')

        semex = Semex(
            name=name,
            student_id=student_id,
            email=email,
            phone=phone,
            current_university=current_university,
            major=major,
            comments=comments
        )
        semex.save()

    return render(request, 'semex.html')

def placement(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        student_id = request.POST.get('studentID')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        current_university = request.POST.get('currentUniversity')
        resume = request.POST.get('resume')
        comments = request.POST.get('comments')

        placement = Placement(
                name=name,
                student_id=student_id,
                email=email,
                phone=phone,
                current_university=current_university,
                resume=resume,
                comments=comments,
                
            )
        placement.save()
        messages.success(request, 'Placement registration submitted successfully.')
        

    return render(request, 'placement.html')

def events(request):
    return render(request, 'events.html')

def updates(request):
    return render(request, 'updates.html')

def exam(request):
    return render(request, 'exam.html')

def rms(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        category = request.POST.get('category')
        description = request.POST.get('description')

        try:
            rms = RMS(
                name=name,
                phone=phone,
                email=email,
                category=category,
                description=description
            )
            rms.save()
            messages.success(request, 'Issue submitted successfully.')
    
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')

    return render(request, 'rms.html')

def feees(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullName')
        student_id = request.POST.get('studentID')
        course = request.POST.get('course')
        year = int(request.POST.get('Year'))
        student_type = request.POST.get('studentType')
        tuition_fee = float(request.POST.get('tuitionFee', 0))
        exam_fee = float(request.POST.get('examFee', 0))
        maintenance_charges = float(request.POST.get('maintenanceCharges', 0))
        
        
        total_fee_str = request.POST.get('totalFee', '$0.00')
        total_fee = float(total_fee_str.replace('$', '').replace(',', ''))

        try:
            feees = Feees(
                fullname=fullname,
                student_id=student_id,
                course=course,
                year=year,
                student_type=student_type,
                tuition_fee=tuition_fee,
                exam_fee=exam_fee,
                maintenance_charges=maintenance_charges,
                total_fee=total_fee
            )
            feees.save()
            messages.success(request, 'Fee submission successful.')
        except Exception as e:
            messages.error(request, f'Error occurred: {str(e)}')

    return render(request, 'feees.html')

def atten(request):
    return render(request, 'atten.html')

def assign(request):
    return render(request, 'assign.html')

def result(request):
    return render(request, 'result.html')

def syllabus(request):
    return render(request, 'syllabus.html')

def leave(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        registration_number = request.POST.get('registration_number')
        course = request.POST.get('course')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')
        documents = request.FILES.get('documents')
        leave = Leave(
                student_name=student_name,
                registration_number=registration_number,
                course=course,
                phone_number=phone_number,
                email=email,
                start_date=start_date,
                end_date=end_date,
                reason=reason,
                documents=documents
            )
        leave.save()

    return render(request, 'leave.html')

def re(request):
    if request.method == 'POST':
        student_name = request.POST.get('studentName')
        registration_number = request.POST.get('registrationNumber')
        course = request.POST.get('course')
        backlog_course_code = request.POST.get('backlogCourseCode')
        backlog_subject = request.POST.get('backlogSubject')
        phone_number = request.POST.get('phoneNumber')
        email = request.POST.get('email')

        re = Re(
            student_name=student_name,
            registration_number=registration_number,
            course=course,
            backlog_course_code=backlog_course_code,
            backlog_subject=backlog_subject,
            phone_number=phone_number,
            email=email
        )
        re.save() 


    return render(request, 're.html')
