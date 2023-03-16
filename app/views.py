from django.shortcuts import render,redirect
# models
from .models import Executive,Committee,Committee_Member, Union,Zone,Fellowship, Position, Chaplain,Patron,Alumni_rep,Program,  SMS, Document
# forms
from .forms import ExecutiveForm,CommitteeForm,MembersForm, UnionsForm,ZoneForm,FellowshipForm, PositionsForm,ChaplainForm,PatronForm,AlumniRepForm,ProgramForm

# User authentication start 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm
# User authentication end 
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseServerError

# IMPORT PANDAS
import pandas as pd
# datetime
from datetime import datetime

# IMPORT REQUESTS
import requests 
# count







class IndexView(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = 'app/index.html'

    def get(self, request):
        try:
            # counting items in tables
            union_count = Union.objects.count()
            zone_count = Zone.objects.count()

            # count institutions starts
            university_fellowship_count = Fellowship.objects.filter(fellowship_type='University').count()
            shs_fellowship_count = Fellowship.objects.filter(fellowship_type='Secondary').count()
            nursing_training_fellowship_count = Fellowship.objects.filter(fellowship_type='Nursing Training').count()
            teacher_training_fellowship_count = Fellowship.objects.filter(fellowship_type='Teacher Training').count()
            # count institutions ends 

            patrons_count = Patron.objects.count()
            chaplains_count = Chaplain.objects.count()
            alumni_rep_count = Alumni_rep.objects.count()
            committee_count = Committee.objects.count()
            program_count = Program.objects.count()
            executive_count = Executive.objects.count()

            # get all national executives
            nationals = Executive.objects.filter(leadership_level='National')

            # FELLOWSHIP POPULATION CHART.JS
            # gender based count in fellowship starts
            # Count the number of males and females in Fellowship model
            males_count = Fellowship.objects.aggregate(males_count=Sum('males'))['males_count']
            females_count = Fellowship.objects.aggregate(females_count=Sum('females'))['females_count']
            gender_list = ['Male', 'Female']
            gender_count = [males_count,females_count]

            # UNION BASED POPULATION
            count_sguc = Fellowship.objects.filter(union='Southern Ghana Union').aggregate(Count('id'))['id__count']
            count_nguc = Fellowship.objects.filter(union='Northern Ghana Union').aggregate(Count('id'))['id__count']

            context = {'nationals':nationals,'union_count':union_count,'zone_count':zone_count,'university_fellowship_count':university_fellowship_count,'nursing_training_fellowship_count':nursing_training_fellowship_count,'teacher_training_fellowship_count':teacher_training_fellowship_count,'shs_fellowship_count':shs_fellowship_count,'committee_count':committee_count,'patrons_count':patrons_count,'chaplains_count':chaplains_count,'alumni_rep_count':alumni_rep_count,'program_count':program_count,'executive_count':executive_count,'males_count':males_count, 'females_count':females_count,'gender_list':gender_list,'gender_count':gender_count,'count_sguc':count_sguc,'count_nguc':count_nguc}

            return render(request, self.template_name, context)

        except Exception as e:
            # Handle any exceptions here
            messages.error(request, str(e))
            return redirect('index')
    
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        context = {}
        return render(request, 'app/login.html', context)
    
    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request,'User succesfully logged in')
                return redirect('index')
            else:
                messages.error(request,'Invalid username or password')
                return redirect('login')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('login')
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')




class ShowExecutiveView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        try:
            query = request.GET.get('q') or ''
            if query == '':
                executives = Executive.objects.all()
            else:
                executives = Executive.objects.filter(leadership_level=query)
            context = {'executives': executives}
            return render(request, 'app/show_executive.html', context)
        except Exception as e:
            # Handle the error appropriately
            return HttpResponse('An error occurred: {}'.format(str(e)))

class CreateExecutiveView(LoginRequiredMixin, View):
    login_url='login'
    def get(self, request):
        try:
            form = ExecutiveForm()
            context = {'forms': form}
            return render(request, 'app/create_executive.html', context)
        except Exception as e:
            # Handle the error appropriately
            return HttpResponse('An error occurred: {}'.format(str(e)))

    def post(self, request):
        try:
            form = ExecutiveForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('executives')
            context = {'forms': form}
            return render(request, 'app/create_executive.html', context)
        except Exception as e:
            # Handle the error appropriately
            return HttpResponse('An error occurred: {}'.format(str(e)))

class EditExecutiveView(LoginRequiredMixin,View):
    login_url='login'
    def get(self, request, pk):
        try:
            executive = Executive.objects.get(pk=pk)
            form = ExecutiveForm(instance=executive)
            context = {'forms': form}
            return render(request, 'app/create_executive.html', context)
        except ObjectDoesNotExist:
            # Handle the error if the Executive object with the given pk does not exist
            return HttpResponse('Executive object does not exist')
        except Exception as e:
            # Handle other errors appropriately
            return HttpResponse('An error occurred: {}'.format(str(e)))

    def post(self, request, pk):
        try:
            executive = Executive.objects.get(pk=pk)
            form = ExecutiveForm(request.POST, request.FILES, instance=executive)
            if form.is_valid():
                form.save()
                return redirect('executives')
            context = {'forms': form}
            return render(request, 'app/create_executive.html', context)
        except Exception as e:
            # Handle the error appropriately
            return HttpResponse('An error occurred: {}'.format(str(e)))

class DeleteExecutiveView(LoginRequiredMixin, View):
    login_url='login'
    def post(self, request, pk):
        try:
            executive = Executive.objects.get(pk=pk)
            executive.delete()
            return redirect('executives')
        except ObjectDoesNotExist:
            # Handle the error if the Executive object with the given pk does not exist
            return HttpResponse('Executive object does not exist')
        except Exception as e:
            # Handle other errors appropriately
            return HttpResponse('An error occurred: {}'.format(str(e)))


# =================================================================
# ============  CREATING COMMITEE ============================

# @method_decorator(login_required(login_url='login'), name='dispatch')
class ShowCommitteeView(LoginRequiredMixin,View):
    login_url='login'
    def get(self, request):
        try:
            committees = Committee.objects.all()
            context = {'committees': committees}
            return render(request, 'app/show_committees.html', context)
        except Exception:
            return HttpResponseServerError()


# @method_decorator(login_required(login_url='login'), name='dispatch')
class CreateCommitteeView(LoginRequiredMixin,View):
    login_url='login'
    def get(self, request):
        try:
            form = CommitteeForm()
            context = {'forms': form}
            return render(request, 'app/create_committee.html', context)
        except Exception:
            return HttpResponseServerError()

    def post(self, request):
        try:
            form = CommitteeForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('committees')
            else:
                context = {'forms': form}
                return render(request, 'app/create_committee.html', context)
        except Exception:
            return HttpResponseServerError()


# @method_decorator(login_required(login_url='login'), name='dispatch')
class EditCommitteeView(LoginRequiredMixin,View):
    login_url='login'
    def get(self, request, pk):
        try:
            committee = get_object_or_404(Committee, pk=pk)
            form = CommitteeForm(instance=committee)
            context = {'forms': form}
            return render(request, 'app/create_committee.html', context)
        except Exception:
            return HttpResponseServerError()

    def post(self, request, pk):
        try:
            committee = get_object_or_404(Committee, pk=pk)
            form = CommitteeForm(request.POST, request.FILES, instance=committee)
            if form.is_valid():
                form.save()
                return redirect('committees')
            else:
                context = {'forms': form}
                return render(request, 'app/create_committee.html', context)
        except Exception:
            return HttpResponseServerError()


# @method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteCommitteeView(LoginRequiredMixin,View):
    login_url='login'
    def post(self, request, pk):
        try:
            committee = get_object_or_404(Committee, pk=pk)
            committee.delete()
            return redirect('committees')
        except Exception:
            return HttpResponseServerError()

    def get(self, request, pk):
        return redirect('committees')



# =================================================================
# ============ END CREATING COMMITEE MEMBERS=======================

class CreateMemberView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'app/create_members.html'

    def get(self, request):
        form = MembersForm()
        context = {'forms': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = MembersForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('members')
        except Exception as e:
            print(str(e))
        context = {'forms': form}
        return render(request, self.template_name, context)

class ShowMembersView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'app/show_members.html'

    def get(self, request):
        members = Committee_Member.objects.all()
        context = {'members': members}
        return render(request, self.template_name, context)

class EditMemberView(LoginRequiredMixin, View):
    login_url = '/login/'
    template_name = 'app/create_members.html'

    def get(self, request, pk):
        members = Committee_Member.objects.get(pk=pk)
        form = MembersForm(instance=members)
        context = {'forms': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        members = Committee_Member.objects.get(pk=pk)
        form = MembersForm(request.POST, request.FILES, instance=members)
        try:
            if form.is_valid():
                form.save()
                return redirect('committees')
        except Exception as e:
            print(str(e))
        context = {'forms': form}
        return render(request, self.template_name, context)

class DeleteMemberView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, pk):
        members = Committee_Member.objects.get(pk=pk)
        try:
            members.delete()
            return redirect('members')
        except Exception as e:
            print(str(e))
        return redirect('members')

# 
# =================================================================
# ============  CREATING UNION ==============================

class ShowUnionsView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request):
        try:
            this_year = str(datetime.now().year)
            unions = Union.objects.all()
            # if you need unions and its executives for only a particular year, 
            # use the lines below instead of the one on top
            # 
            # unions = Union.objects.filter(academic_year=this_year)
            context = {'unions': unions,'this_year':this_year}
            return render(request, 'app/show_unions.html', context)
        except Exception:
            return redirect('unions')

class CreateUnionView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request):
        form = UnionsForm()
        context = {'forms': form}
        return render(request, 'app/create_union.html', context)
    
    def post(self, request):
        form = UnionsForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('unions')
        except Exception:
            return redirect('create_union')
        context = {'forms': form}
        return render(request, 'app/create_union.html', context)


class EditUnionView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self, request, pk):
        unions = Union.objects.get(pk=pk)
        form = UnionsForm(instance=unions)
        context = {'forms': form}
        return render(request, 'app/create_union.html', context)
    
    def post(self, request, pk):
        unions = Union.objects.get(pk=pk)
        form = UnionsForm(request.POST, request.FILES, instance=unions)
        try:
            if form.is_valid():
                form.save()
                return redirect('unions')
        except Exception:
            return redirect('edit_union', pk=pk)
        context = {'forms': form}
        return render(request, 'app/create_union.html', context)


class DeleteUnionView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def post(self, request, pk):
        try:
            unions = Union.objects.get(pk=pk)
            unions.delete()
        except Exception:
            pass
        return redirect('unions')


# 
# =================================================================
# ============  CREATING ZONES ==============================

class ShowZonesView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        try:
            zones = Zone.objects.all()
        except Zone.DoesNotExist:
            zones = None
        context = {'zones': zones}
        return render(request, 'app/show_zones.html', context)


class CreateZoneView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = ZoneForm()
        context = {'forms': form}
        return render(request, 'app/create_zone.html', context)

    def post(self, request):
        form = ZoneForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('zones')
        except Exception:
            pass
        context = {'forms': form}
        return render(request, 'app/create_zone.html', context)


class EditZoneView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        zones = Zone.objects.get(pk=pk)
        form = ZoneForm(instance=zones)
        context = {'forms': form}
        return render(request, 'app/create_zone.html', context)

    def post(self, request, pk):
        zones = Zone.objects.get(pk=pk)
        form = ZoneForm(request.POST, request.FILES, instance=zones)
        try:
            if form.is_valid():
                form.save()
                return redirect('zones')
        except Exception:
            pass
        context = {'forms': form}
        return render(request, 'app/create_zone.html', context)


class DeleteZoneView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def post(self, request, pk):
        zones = Zone.objects.get(pk=pk)
        try:
            zones.delete()
        except Exception:
            pass
        return redirect('zones')





# =================================================================
# ============  CREATING fellowship ==============================

class ShowFellowshipsView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        query = request.GET.get('q') or ''
        try:
            if query == '':
                fellowships = Fellowship.objects.all()
            else:
                fellowships = Fellowship.objects.filter(fellowship_type=query)
        except Fellowship.DoesNotExist:
            fellowships = None
        context = {'fellowships': fellowships}
        return render(request, 'app/show_fellowships.html', context)


class CreateFellowshipView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = FellowshipForm()
        context = {'forms': form}
        return render(request, 'app/create_fellowship.html', context)

    def post(self, request):
        form = FellowshipForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('fellowships')
        except Exception:
            pass
        context = {'forms': form}
        return render(request, 'app/create_fellowship.html', context)


class EditFellowshipView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get(self, request, pk):
        fellowship = Fellowship.objects.get(pk=pk)
        form = FellowshipForm(instance=fellowship)
        context = {'forms': form}
        return render(request, 'app/create_fellowship.html', context)

    def post(self, request, pk):
        fellowship = Fellowship.objects.get(pk=pk)
        form = FellowshipForm(request.POST, request.FILES, instance=fellowship)
        try:
            if form.is_valid():
                form.save()
                return redirect('fellowships')
        except Exception:
            pass
        context = {'forms': form}
        return render(request, 'app/create_fellowship.html', context)


class DeleteFellowshipView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def post(self, request, pk):
        fellowship = Fellowship.objects.get(pk=pk)
        try:
            fellowship.delete()
        except Exception:
            pass
        return redirect('fellowships')

# 
# =================================================================
# ============  CREATING POSITIONS ==============================


class ShowPositionView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        try:
           positions = Position.objects.all()
        except Zone.DoesNotExist:
            zones = None
        context = {'zones': zones}
        return render(request, 'app/show_position.html', context)


class CreatePositionView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        form = PositionsForm()
        context = {'forms': form}
        return render(request, 'app/create_position.html', context)

    def post(self, request):
        form = PositionsForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                form.save()
                return redirect('positions')
        except Exception:
            pass
        context = {'forms': form}
        return render(request, 'app/create_position.html', context)


class EditPositionView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request, pk):
        positions = Position.objects.get(pk=pk)
        form = PositionsForm(instance=positions)
        context = {'forms': form}
        return render(request, 'app/create_position.html', context)

    def post(self, request, pk):
        positions = Position.objects.get(pk=pk)
        form = PositionsForm(request.POST, request.FILES, instance=positions)
        try:
            if form.is_valid():
                form.save()
                return redirect('positions')
        except Exception:
            pass
        context = {'forms': form}
        return render(request, 'app/create_position.html', context)
    

class DeletePositionView(LoginRequiredMixin, View):
    login_url = 'login'

    def post(self, request, pk):
        positions = Position.objects.get(pk=pk)
        try:
            positions.delete()
        except Exception:
            pass
        return redirect('positions')
# # =================ZONE NAMES START==================
# @login_required(login_url='login')
# def show_zone_names(request):
#     zones = Zone_Name.objects.all()
#     context = {'zones': zones}
#     return render(request, 'app/show_zone_names.html', context)


# @login_required(login_url='login')
# def create_zone_name(request):
#     form = ZoneNameForm()

#     if request.method == 'POST':
#         form = ZoneNameForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('names')
#     context = {'forms': form}
#     return render(request, 'app/create_zone_names.html', context)


# @login_required(login_url='login')
# def edit_zone_name(request,pk):
#     zones = Zone_Name.objects.get(pk=pk)
#     form = ZoneNameForm(instance=zones)
    

#     if request.method == 'POST':
#         form = ZoneNameForm(request.POST, request.FILES,instance=zones)
#         if form.is_valid():
#             form.save()
#             return redirect('names')
#     context = {'forms': form}
#     return render(request, 'app/create_zone_names.html', context)


# @login_required(login_url='login')
# def delete_zone_name(request,pk):
#     zones = Zone_Name.objects.get(id=pk)

#     if request.method == 'POST':
#         zones.delete()
#         return redirect('names')
#     return redirect('names')




# =================================================================
# ============  CREATING CHAPLAINS/PCM ==============================

@login_required(login_url='login')
def show_chaplains(request):
    chaplains = Chaplain.objects.all()
    context = {'chaplains': chaplains}
    return render(request, 'app/show_chaplains.html', context)


@login_required(login_url='login')
def create_chaplain(request):
    form = ChaplainForm()

    if request.method == 'POST':
        form = ChaplainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chaplains')
    context = {'forms': form}
    return render(request, 'app/create_chaplain.html', context)


@login_required(login_url='login')
def edit_chaplain(request,pk):
    chaplains = Chaplain.objects.get(pk=pk)
    form = ChaplainForm(instance=chaplains)
    

    if request.method == 'POST':
        form = ChaplainForm(request.POST, request.FILES,instance=chaplains)
        if form.is_valid():
            form.save()
            return redirect('fellowships')
    context = {'forms': form}
    return render(request, 'app/create_chaplain.html', context)


@login_required(login_url='login')
def delete_chaplain(request,pk):
    chaplains = Chaplain.objects.get(pk=pk)

    if request.method == 'POST':
        chaplains.delete()
        return redirect('chaplains')
    return redirect('chaplains')



# =================================================================
# ============  CREATING PATRONS ==============================
@login_required(login_url='login')
def show_patrons(request):
    patrons = Patron.objects.all()
    context = {'patrons': patrons}
    return render(request, 'app/show_patrons.html', context)


@login_required(login_url='login')
def create_patron(request):
    form = PatronForm()

    if request.method == 'POST':
        form = PatronForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patrons')
    context = {'forms': form}
    return render(request, 'app/create_patron.html', context)


@login_required(login_url='login')
def edit_patron(request,pk):
    patrons = Patron.objects.get(pk=pk)
    form = PatronForm(instance=patrons)
    

    if request.method == 'POST':
        form = PatronForm(request.POST, request.FILES,instance=patrons)
        if form.is_valid():
            form.save()
            return redirect('patrons')
    context = {'forms': form}
    return render(request, 'app/create_patron.html', context)
@login_required(login_url='login')
def delete_patron(request,pk):
    patrons = Patron.objects.get(pk=pk)

    if request.method == 'POST':
        patrons.delete()
        return redirect('patrons')
    return redirect('patrons')


    
# =================================================================
# ============  CREATING ALUMNI REPS ==============================
@login_required(login_url='login')
def show_alumni(request):
    alumni = Alumni_rep.objects.all()
    context = {'alumni': alumni}
    return render(request, 'app/show_alumni.html', context)




@login_required(login_url='login')
def create_alumni(request):
    form = AlumniRepForm()

    if request.method == 'POST':
        form = AlumniRepForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alumni')
    context = {'forms': form}
    return render(request, 'app/create_alumni.html', context)


@login_required(login_url='login')
def edit_alumni(request,pk):
    alumni = Alumni_rep.objects.get(pk=pk)
    form = AlumniRepForm(instance=alumni)
    

    if request.method == 'POST':
        form = AlumniRepForm(request.POST, request.FILES,instance=alumni)
        if form.is_valid():
            form.save()
            return redirect('alumni')
    context = {'forms': form}
    return render(request, 'app/create_alumni.html', context)



@login_required(login_url='login')
def delete_alumni(request,pk):
    alumni = Alumni_rep.objects.get(pk=pk)

    if request.method == 'POST':
        alumni.delete()
        return redirect('alumni')
    return redirect('alumni')


   
# =================================================================
# ============  CREATING PROGRAMS ==============================

@login_required(login_url='login')
def show_programs(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'app/show_programs.html', context)


@login_required(login_url='login')
def create_program(request):
    form = ProgramForm()

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('programs')
    context = {'forms': form}
    return render(request, 'app/create_program.html', context)



@login_required(login_url='login')
def edit_program(request,pk):
    programs = Program.objects.get(pk=pk)
    form = ProgramForm(instance=programs)
    

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES,instance=programs)
        if form.is_valid():
            form.save()
            return redirect('programs')
    context = {'forms': form}
    return render(request, 'app/create_program.html', context)


@login_required(login_url='login')
def delete_program(request,pk):
    programs = Program.objects.get(id=pk)

    if request.method == 'POST':
        programs.delete()
        return redirect('programs')
    return redirect('programs')



def show_sms(request):
    
    sms = SMS.objects.all()    
    context = {'sms': sms}
    return render(request, 'app/show_sms.html',context)

def sms_in_base(request):
    context_sms = SMS.objects.all()    
    context = {'context_sms': context_sms}
    return context


def sms_to_executive(request):
    if request.method == 'POST':
        executive = Executive.objects.all()
        
        sender_id = request.POST.get('sender_id')
        title = request.POST.get('title')
        body = request.POST.get('body')
        message_count = len(executive)
        message = ", ".join([title, body]) 
        print(message)

        # print(len(parents))
        for worker in executive:
            to_number =str(worker.phone)
            # print(parent.phone)
            
            API_KEY = "OjRHbjdNV0doSXRUOFRTb0s="
            if to_number and len(to_number)==10 and to_number.startswith("0"):

                url = f"https://sms.arkesel.com/sms/api?action=send-sms&api_key={API_KEY}&to={to_number}&from={sender_id}&sms={message}"
                print(url)
                res = requests.get(url)
                print(worker.phone)
                print(res.status_code)
                print(res.content)
                messages.success(request, res.content)
                
        
               
            else:
                messages.error(request, "Invalid phone number")
                # print("invalid phone number")
        SMS.objects.create(
                sender_id=sender_id,
                title=title,
                body=body,
                messages_sent=message_count
               )
        return redirect('sms')
    context = {}
    return render(request, 'app/sms_to_executive.html',context)


    # HOW TO FILL SHOW TABLE WITH INFO FROM SEND_SMS

#            <!-- Send SMS to Fellowship throught their presients -->
def sms_to_fellowships(request):
    if request.method == 'POST':
        fellowship = Fellowship.objects.all()
        
        sender_id = request.POST.get('sender_id')
        title = request.POST.get('title')
        body = request.POST.get('body')
        message_count = len(fellowship)
        message = ", ".join([title, body]) 
        print(message)

        # print(len(parents))
        for worker in fellowship:
            to_number =str(worker.president_contact)
            # print(parent.phone)
            
            API_KEY = "OjRHbjdNV0doSXRUOFRTb0s="
            if to_number and len(to_number)==10 and to_number.startswith("0"):

                url = f"https://sms.arkesel.com/sms/api?action=send-sms&api_key={API_KEY}&to={to_number}&from={sender_id}&sms={message}"
                print(url)
                res = requests.get(url)
                print(worker.president_contact)
                print(res.status_code)
                print(res.content)
                messages.success(request, res.content)
                
        
               
            else:
                messages.error(request, "Invalid phone number")
                # print("invalid phone number")
        SMS.objects.create(
                sender_id=sender_id,
                title=title,
                body=body,
                messages_sent=message_count
               )
        return redirect('sms')
    context = {}
    return render(request, 'app/sms_to_executive.html',context)

def show_documents(request):
    # documents = Document.objects.all()
    national_doc = Document.objects.filter(status__iexact="National")
    sguc_doc = Document.objects.filter(status__iexact="SGUC")
    nguc_doc = Document.objects.filter(status__iexact="NGUC")
    context = {'national_doc':national_doc,'sguc_doc':sguc_doc,'nguc_doc':nguc_doc}
    return render(request, 'app/show_document.html', context)


def add_document(request):
    if request.method == 'POST':
        name = request.POST['name']
        file = request.FILES['file']
        # it means check the document table(model), file_name = name in the html as well as file
        document = Document(name=name, file=file)
        document.save()
        return redirect('documents')
    return render(request, 'app/add_document.html')




    