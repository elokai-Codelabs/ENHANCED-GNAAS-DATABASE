from django.shortcuts import render,redirect
# models
from .models import Executive, Zone_Name,Zone, Committee,Committee_Member, Union,Fellowship, Position, Chaplain,Patron,Alumni_rep,Program

# import pandas
import pandas as pd
# 
from django.contrib import messages


# UPLOAD EXECUTIVE EXCEL SHEET TO DATABASE
def read_executive_excel(request):
    
    if request.method == 'POST':
            

        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index,row in df.iterrows():
            # if you have a foreign key for a field, you get it first
            # we are filtering where position is equal to where in the column
            position = Position.objects.filter(position=row['POSITION']).first()
            # print('message',row['FULL NAME'],row['PHONE'],row['EMAIL'])

            executives = Executive.objects.get_or_create(full_name=row['FULL NAME'],phone=row['PHONE'],email=row['EMAIL'],program_of_study=row['PROGRAM OF STUDY'],date_of_service=row['YEAR OF SERVICE'],leadership_level=row['LEADERSHIP LEVEL'],position=position,gnaas_fellowship=row['GNAAS FELLOWSHIP'],local_church=row['LOCAL CHURCH'],local_church_location=row['LOCAL CHURCH LOCATION'],local_church_elder=row['LOCAL CHURCH ELDER'],local_church_elder_contact=row['ELDER CONTACT'])
            print('inserted',index)

        messages.success(request,'Executive uploaded succesfully')
        # print('Successfully uploaded')
        return redirect('executives')


# upload zones excel
def read_zone_excel(request):
    
    if request.method == 'POST':
            

        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index,row in df.iterrows():
            # if you have a foreign key for a field, you get it first
            # we are filtering where position is equal to where in the column
            # print('message',row['FULL NAME'],row['PHONE'],row['EMAIL'])

            zones = Zone_Name.objects.get_or_create(name=row['ZONE_FULL_NAME'])

        messages.success(request,'Zones uploaded succesfully')
        # print('Successfully uploaded')

        return redirect('names')

# upload zones excel
def read_zone_details_excel(request):
    
    if request.method == 'POST':
            

        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index,row in df.iterrows():
            # if you have a foreign key for a field, you get it first
            # we are filtering where position is equal to where in the column
            # print('message',row['FULL NAME'],row['PHONE'],row['EMAIL'])

            zones = Zone.objects.get_or_create(name=row['ZONE_NAME'],school_hosting=row['SCHOOL_HOSTING'],president=row['PRESIDENT'],president_contact=row['PRESIDENT_CONTACT'],secretary=row['SECRETARY'],secretary_contact=row['SECRETARY_CONTACT'],treasurer=row['TREASURER'],treasurer_contact=row['TREASURER_CONTACT'],coordinating_secretary=row['COORDINATING_SECRETARY'],coordinating_secretary_contact=row['COORDINATING_SECRETARY_CONTACT'],)

        messages.success(request,'Zones uploaded succesfully')
        # print('Successfully uploaded')

        return redirect('zones')


# upload zones excel
def read_committee_excel(request):
    
    if request.method == 'POST':
            

        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index,row in df.iterrows():
            # if you have a foreign key for a field, you get it first
            # we are filtering where position is equal to where in the column
            # print('message',row['FULL NAME'],row['PHONE'],row['EMAIL'])

            committee = Committee.objects.get_or_create(name=row['COMMITTEE_NAME'],mandate=row['COMMITTEE_MANDATE'],date_of_assumption=row['DATE_OF_ASSUMPTION'])

        messages.success(request,'Committees uploaded succesfully')
        # print('Successfully uploaded')

        return redirect('committees')



# upload zones excel
def read_committee_member_excel(request):
    
    if request.method == 'POST':
            

        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index,row in df.iterrows():
            # if you have a foreign key for a field, you get it first
            # we are filtering where position is equal to where in the column
            # print('message',row['FULL NAME'],row['PHONE'],row['EMAIL'])
            affiliated_committee = Committee.objects.filter(name=row['AFFILIATED_COMMITTEE']).first()

            committee = Committee_Member.objects.get_or_create(full_name=row['FULL_NAME'],contact=row['CONTACT'],date_of_service=row['YEAR_OF_SERVICE'],affiliated_committee=affiliated_committee,gnaas_fellowship=row['GNAAS_FELLOWSHIP'],local_church=row['LOCAL_CHURCH'],local_church_location=row['LOCAL_CHURCH_LOCATION'],local_church_elder=row['LOCAL_CHURCH_ELDER'],local_church_elder_contact=row['LOCAL_CHURCH_ELDER_CONTACT'])

        messages.success(request,'Committee Members uploaded succesfully')
        # print('Successfully uploaded')

        return redirect('members')

    # upload POSITION excel
def read_position_excel(request):
    
    if request.method == 'POST':
            

        file = request.FILES.get("file")
        excel_file = pd.read_excel(file)
        df = pd.DataFrame(excel_file)

        for index,row in df.iterrows():
            # if you have a foreign key for a field, you get it first
            # we are filtering where position is equal to where in the column
            # print('message',row['FULL NAME'],row['PHONE'],row['EMAIL'])

            position = Position.objects.get_or_create(position=row['POSITION_NAME'])

        messages.success(request,'Positions uploaded succesfully')
        # print('Successfully uploaded')

        return redirect('positions')