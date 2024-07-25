from django.contrib import admin
from django.urls import path, re_path
from home1 import views
from django.views.generic.base import RedirectView


urlpatterns = [
  
    path('',views.index,name='home1'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('importantlinks/',views.implink,name='implink'),
    path('contact/',views.contact,name='contact'),
    path('Admissions/',views.Admissions,name='Admissions'),
    path('cse/', views.cse, name='cse'),
    path('mba/', views.mba, name='mba'),
    path('economics/', views.economics, name='economics'),
    path('environmentalscience/', views.environmentalscience, name='environmentalscience'),
    path('publichealth/', views.publichealth, name='publichealth'),
    path('psychology/', views.psychology, name='psychology'),
    path('courseregistration/', views.courseregistration, name='courseregistration'),
    path('feecse/', views.feecse, name='feecse'),
    path('feemba/', views.feemba, name='feemba'),
    path('feeeco/', views.feeeco, name='feeeco'),
    path('feeev/', views.feeev, name='feeev'),
    path('feemph/', views.feemph, name='feemph'),
    path('feepsy/', views.feepsy, name='feepsy'),
    path('counselling/', views.counselling, name='counselling'),
    path('Scholarship/', views.Scholarship, name='Scholarship'),
    path('infrastructure/',views.infrastructure,name='infrastructure'),
    path('faculty/',views.faculty,name='faculty'),
    path('students/',views.students,name='students'),
    path('hostel/',views.hostel,name='hostel'),
    path('transport/',views.transport,name='transport'),
    path('semex/',views.semex,name='semex'),
    path('placement/',views.placement,name='placement'),
    path('events/',views.events,name='events'),
    path('updates/',views.updates,name='updates'),
    path('exam/',views.exam,name='exam'),
    path('rms/',views.rms,name='rms'),
    path('feees/',views.feees,name='feees'),
    path('atten/',views.atten,name='atten'),
    path('assign/',views.assign,name='assign'),
    path('result/',views.result,name='result'),
    path('syllabus/',views.syllabus,name='syllabus'),
    path('leave/',views.leave,name='leave'),
    path('re/',views.re,name='re'),


]
