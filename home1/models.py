

from django.db import models
from django.utils import timezone  # Import timezone if not imported

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    desc = models.TextField()
    date = models.DateTimeField(default=timezone.now) 
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Courseregistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    academic_details = models.TextField()
    course = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"

class scholarship(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    tenth_marks = models.DecimalField(max_digits=5, decimal_places=2)
    twelfth_marks = models.DecimalField(max_digits=5, decimal_places=2)
    diploma_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    competitive_exam_score = models.DecimalField(max_digits=8, decimal_places=2)
    university_exam_score = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"
    
class Counselling(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    preferred_timeslot = models.CharField(max_length=20, choices=[
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ])

    def __str__(self):
        return self.fullname
    
    from django.db import models

class Placement(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    current_university = models.CharField(max_length=100)
    resume = models.FileField(upload_to='resumes/', null=True)
    comments = models.TextField(blank=True)
    

    def __str__(self):
        return self.name
    
class RMS(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    category = models.CharField(max_length=50, choices=[
        ('Technical Issue', 'Technical Issue'),
        ('Facilities', 'Facilities'),
        ('General Inquiry', 'General Inquiry'),
    ])
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.category}"
    
class Feees(models.Model):
    fullname = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    student_type = models.CharField(max_length=20)
    tuition_fee = models.DecimalField(max_digits=8, decimal_places=2)
    exam_fee = models.DecimalField(max_digits=8, decimal_places=2)
    maintenance_charges = models.DecimalField(max_digits=8, decimal_places=2)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fullname} - {self.course}"
    

class Hostel(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    room_type = models.CharField(max_length=20)
    duration = models.IntegerField()
    meal_plan = models.CharField(max_length=20)
    meal_days = models.IntegerField()
    laundry_service = models.BooleanField(default=False)
    gym_access = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name + ' - ' + self.student_id
    

class Transport(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    transport_option = models.CharField(max_length=20, choices=[
        ('shuttle', 'Shuttle Service'),
        ('citybus', 'City Bus Service'),
        ('custom', 'Custom Route'),
    ])
    distance_covered = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + self.student_id
    
class Semex(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    current_university = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    comments = models.TextField()

    def __str__(self):
        return self.name + ' - ' + self.student_id
    


class Leave(models.Model):
    student_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    documents = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.registration_number} ({self.course})"

class Re(models.Model):
    student_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    backlog_course_code = models.CharField(max_length=50)
    backlog_subject = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.student_name} - {self.registration_number} ({self.course})"