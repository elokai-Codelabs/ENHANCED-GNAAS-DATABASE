from django.shortcuts import render,redirect
# models
from .models import Executive,Committee,Committee_Member, Union,Zone,Fellowship, Position, Chaplain,Patron,Alumni_rep,Program, Zone_Name
# forms
from .forms import ExecutiveForm,CommitteeForm,MembersForm, UnionsForm,ZoneForm,FellowshipForm, PositionsForm,ChaplainForm,PatronForm,AlumniRepForm,ProgramForm,ZoneNameForm

# User authentication start 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm
# User authentication end 


# IMPORT PANDAS
import pandas as pd
# datetime
from datetime import datetime


# Create your views here.
@login_required(login_url='login')
def index(request):
    # counting items in tables
    union_count = Union.objects.count()
    zone_count = Zone.objects.count()
    university_fellowship_count = Fellowship.objects.filter(fellowship_type='University').count()
    nursing_training_fellowship_count = Fellowship.objects.filter(fellowship_type='Secondary').count()
    teacher_training_fellowship_count = Fellowship.objects.filter(fellowship_type='Nursing Training').count()
    shs_fellowship_count = Fellowship.objects.filter(fellowship_type='Teacher Training').count()
    patrons_count = Patron.objects.count()
    chaplains_count = Chaplain.objects.count()
    alumni_rep_count = Alumni_rep.objects.count()
    committee_count = Committee.objects.count()
    program_count = Program.objects.count()
    executive_count = Executive.objects.count()


        # get all national executives
    nationals = Executive.objects.filter(leadership_level='National')
    context = {'nationals':nationals,'union_count':union_count,'zone_count':zone_count,'university_fellowship_count':university_fellowship_count,'nursing_training_fellowship_count':nursing_training_fellowship_count,'teacher_training_fellowship_count':teacher_training_fellowship_count,'shs_fellowship_count':shs_fellowship_count,'committee_count':committee_count,'patrons_count':patrons_count,'chaplains_count':chaplains_count,'alumni_rep_count':alumni_rep_count,'program_count':program_count,'executive_count':executive_count}

    return render(request, 'app/index.html', context)


# 
# ============USER AUTHENTICATION , LOGIN AND LOGOUT==========
# ============================================================
def loginUser(request):
    # prevent already loged in users from seing login page
    context = {}
    if request.method == 'GET':
        return render(request,'app/login.html', context)
    # if request.user.is_authenticated:
    #     return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request,'User succesfully logged in')
            return redirect('index')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'app/login.html', context)   


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def show_executive(request):
    query = request.GET.get('q') or ''
    if query == '':
        executives = Executive.objects.all()
    else:
        executives = Executive.objects.filter(leadership_level=query)
    context = {'executives': executives}
    return render(request, 'app/show_executive.html', context)

# displaying executive based on page indicator does not work because 
# I need to figure it out again

# =================================================================
# ============  CREATING EXECUTIVE ============================
@login_required(login_url='login')
def create_executive(request):
    form = ExecutiveForm()

    if request.method == 'POST':
        form = ExecutiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('executives')
    context = {'forms': form}
    return render(request, 'app/create_executive.html', context)

@login_required(login_url='login')
def edit_executive(request,pk):
    executive = Executive.objects.get(pk=pk)
    form = ExecutiveForm(instance=executive)
    

    if request.method == 'POST':
        form = ExecutiveForm(request.POST, request.FILES,instance=executive)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'forms': form}
    return render(request, 'app/create_executive.html', context)


@login_required(login_url='login')
def delete_executive(request,pk):
    executive = Executive.objects.get(pk=pk)

    if request.method == 'POST':
        executive.delete()
        return redirect('executives')
    return redirect('executives')
    
# =================================================================
# ============  CREATING COMMITEE ============================

@login_required(login_url='login')
def show_committee(request):
    committees = Committee.objects.all()
    context = {'committees': committees}
    return render(request, 'app/show_committees.html', context)


@login_required(login_url='login')
def create_committee(request):
    form = CommitteeForm()

    if request.method == 'POST':
        form = CommitteeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('committees')
    context = {'forms': form}
    return render(request, 'app/create_committee.html', context)


@login_required(login_url='login')
def edit_committee(request,pk):
    committee = Committee.objects.get(pk=pk)
    form = CommitteeForm(instance=committee)
    

    if request.method == 'POST':
        form = CommitteeForm(request.POST, request.FILES,instance=committee)
        if form.is_valid():
            form.save()
            return redirect('committees')
    context = {'forms': form}
    return render(request, 'app/create_committee.html', context)


@login_required(login_url='login')
def delete_member(request,pk):
    committee = Committee.objects.get(pk=pk)

    if request.method == 'POST':
        committee.delete()
        return redirect('committees')
    return redirect('committees')




# =================================================================
# ============ END CREATING COMMITEE MEMBERS=======================

@login_required(login_url='login')
def create_member(request):
    form = MembersForm()

    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members')
    context = {'forms': form}
    return render(request, 'app/create_members.html', context)

@login_required(login_url='login')
def show_members(request):
    members = Committee_Member.objects.all()
    context = {'members': members}
    return render(request, 'app/show_members.html', context)


@login_required(login_url='login')
def edit_member(request,pk):
    members = Committee_Member.objects.get(pk=pk)
    form = MembersForm(instance=members)
    

    if request.method == 'POST':
        form = Committee_Member(request.POST, request.FILES,instance=members)
        if form.is_valid():
            form.save()
            return redirect('committees')
    context = {'forms': form}
    return render(request, 'app/create_members.html', context)

@login_required(login_url='login')
def delete_committee(request,pk):
    members = Committee_Member.objects.get(pk=pk)

    if request.method == 'POST':
        members.delete()
        return redirect('members')
    return redirect('members')

# 
# =================================================================
# ============  CREATING UNIONS ==============================
@login_required(login_url='login')
def show_unions(request):
    this_year = str(datetime.now().year)
    unions = Union.objects.all()

    # if you need unions and its executives for only a particular year, 
    # use the lines below instead of the one on top
    # 
    # unions = Union.objects.filter(academic_year=this_year)

    context = {'unions': unions,'this_year':this_year}
    return render(request, 'app/show_unions.html', context)


@login_required(login_url='login')
def create_union(request):
    form = UnionsForm()

    if request.method == 'POST':
        form = UnionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('unions')
    context = {'forms': form}
    return render(request, 'app/create_union.html', context)



@login_required(login_url='login')
def edit_union(request,pk):
    unions = Union.objects.get(pk=pk)
    form = UnionsForm(instance=unions)
    

    if request.method == 'POST':
        form = UnionsForm(request.POST, request.FILES,instance=unions)
        if form.is_valid():
            form.save()
            return redirect('unions')
    context = {'forms': form}
    return render(request, 'app/create_union.html', context)

@login_required(login_url='login')
def delete_union(request,pk):
    unions = Union.objects.get(pk=pk)

    if request.method == 'POST':
        unions.delete()
        return redirect('unions')
    return redirect('unions')

# 
# =================================================================
# ============  CREATING ZONES ==============================
@login_required(login_url='login')
def show_zones(request):
    zones = Zone.objects.all()
    context = {'zones': zones}
    return render(request, 'app/show_zones.html', context)


@login_required(login_url='login')
def create_zone(request):
    form = ZoneForm()

    if request.method == 'POST':
        form = ZoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('zones')
    context = {'forms': form}
    return render(request, 'app/create_zone.html', context)


@login_required(login_url='login')
def edit_zone(request,pk):
    zones = Zone.objects.get(pk=pk)
    form = ZoneForm(instance=zones)
    

    if request.method == 'POST':
        form = ZoneForm(request.POST, request.FILES,instance=zones)
        if form.is_valid():
            form.save()
            return redirect('zones')
    context = {'forms': form}
    return render(request, 'app/create_zone.html', context)


@login_required(login_url='login')
def delete_zone(request,pk):
    zones = Zone.objects.get(pk=pk)

    if request.method == 'POST':
        zones.delete()
        return redirect('zones')
    return redirect('zones')





# =================================================================
# ============  CREATING fellowship ==============================
@login_required(login_url='login')
def show_fellowships(request):
    query = request.GET.get('q') or ''
    if query == '':
        fellowships = Fellowship.objects.all()
    else:
        fellowships = Fellowship.objects.filter(fellowship_type=query)
    
    context = {'fellowships': fellowships}
    return render(request, 'app/show_fellowships.html', context)

@login_required(login_url='login')
def create_fellowship(request):
    form = FellowshipForm()

    if request.method == 'POST':
        form = FellowshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fellowships')
    context = {'forms': form}
    return render(request, 'app/create_fellowship.html', context)


@login_required(login_url='login')
def edit_fellowship(request,pk):
    fellowship = Fellowship.objects.get(pk=pk)
    form = FellowshipForm(instance=fellowship)
    

    if request.method == 'POST':
        form = FellowshipForm(request.POST, request.FILES,instance=fellowship)
        if form.is_valid():
            form.save()
            return redirect('fellowships')
    context = {'forms': form}
    return render(request, 'app/create_fellowship.html', context)


@login_required(login_url='login')
def delete_fellowship(request,pk):
    fellowship = Fellowship.objects.get(pk=pk)

    if request.method == 'POST':
        fellowship.delete()
        return redirect('fellowships')
    return redirect('fellowships')



# 
# =================================================================
# ============  CREATING POSITIONS ==============================
@login_required(login_url='login')
def show_positions(request):
    positions = Position.objects.all()
    context = {'positions': positions}
    return render(request, 'app/show_position.html', context)


@login_required(login_url='login')
def create_position(request):
    form = PositionsForm()

    if request.method == 'POST':
        form = PositionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('positions')
    context = {'forms': form}
    return render(request, 'app/create_position.html', context)


@login_required(login_url='login')
def edit_position(request,pk):
    positions = Position.objects.get(pk=pk)
    form = PositionsForm(instance=positions)
    

    if request.method == 'POST':
        form = PositionsForm(request.POST, request.FILES,instance=positions)
        if form.is_valid():
            form.save()
            return redirect('positions')
    context = {'forms': form}
    return render(request, 'app/create_position.html', context)


@login_required(login_url='login')
def delete_position(request,pk):
    positions = Position.objects.get(pk=pk)

    if request.method == 'POST':
        positions.delete()
        return redirect('positions')
    return redirect('positions')

# =================ZONE NAMES START==================
@login_required(login_url='login')
def show_zone_names(request):
    zones = Zone_Name.objects.all()
    context = {'zones': zones}
    return render(request, 'app/show_zone_names.html', context)


@login_required(login_url='login')
def create_zone_name(request):
    form = ZoneNameForm()

    if request.method == 'POST':
        form = ZoneNameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('names')
    context = {'forms': form}
    return render(request, 'app/create_zone_names.html', context)


@login_required(login_url='login')
def edit_zone_name(request,pk):
    zones = Zone_Name.objects.get(pk=pk)
    form = ZoneNameForm(instance=zones)
    

    if request.method == 'POST':
        form = ZoneNameForm(request.POST, request.FILES,instance=zones)
        if form.is_valid():
            form.save()
            return redirect('names')
    context = {'forms': form}
    return render(request, 'app/create_zone_names.html', context)


@login_required(login_url='login')
def delete_zone_name(request,pk):
    zones = Zone_Name.objects.get(id=pk)

    if request.method == 'POST':
        zones.delete()
        return redirect('names')
    return redirect('names')




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






    