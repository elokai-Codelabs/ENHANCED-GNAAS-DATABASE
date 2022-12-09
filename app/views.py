from django.shortcuts import render,redirect
from .models import Executive,Committee,Committee_Member, Union,Zone,Fellowship, Position, Chaplain,Patron,Alumni_rep,Program
from .forms import ExecutiveForm,CommitteeForm,MembersForm, UnionsForm,ZoneForm,FellowshipForm, PositionsForm,ChaplainForm,PatronForm,AlumniRepForm,ProgramForm, ExecutiveResource

# uploading excel
from django.contrib import messages
from tablib import Dataset

# Create your views here.
def index(request):
    # get all national executives
    nationals = Executive.objects.filter(leadership_level='National')
    context = {'nationals':nationals}
    return render(request, 'app/index.html', context)

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
def create_executive(request):
    form = ExecutiveForm()

    if request.method == 'POST':
        form = ExecutiveForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('executives')
    context = {'forms': form}
    return render(request, 'app/create_executive.html', context)

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

def delete_executive(request,pk):
    executive = Executive.objects.get(pk=pk)

    if request.method == 'POST':
        executive.delete()
        return redirect('executives')
    return redirect('executives')
    
# =================================================================
# ============  CREATING COMMITEE ============================
def show_committee(request):
    committees = Committee.objects.all()
    context = {'committees': committees}
    return render(request, 'app/show_committees.html', context)

def create_committee(request):
    form = CommitteeForm()

    if request.method == 'POST':
        form = CommitteeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'forms': form}
    return render(request, 'app/create_committee.html', context)

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

def delete_member(request,pk):
    committee = Committee.objects.get(pk=pk)

    if request.method == 'POST':
        committee.delete()
        return redirect('committees')
    return redirect('committees')




# =================================================================
# ============ END CREATING COMMITEE MEMBERS=======================
def create_member(request):
    form = MembersForm()

    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members')
    context = {'forms': form}
    return render(request, 'app/create_members.html', context)


def show_members(request):
    members = Committee_Member.objects.all()
    context = {'members': members}
    return render(request, 'app/show_members.html', context)

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

def delete_committee(request,pk):
    members = Committee_Member.objects.get(pk=pk)

    if request.method == 'POST':
        members.delete()
        return redirect('members')
    return redirect('members')

# 
# =================================================================
# ============  CREATING UNIONS ==============================
def show_unions(request):
    unions = Union.objects.all()
    context = {'unions': unions}
    return render(request, 'app/show_unions.html', context)

def create_union(request):
    form = UnionsForm()

    if request.method == 'POST':
        form = UnionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('unions')
    context = {'forms': form}
    return render(request, 'app/create_union.html', context)

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

def delete_union(request,pk):
    unions = Union.objects.get(pk=pk)

    if request.method == 'POST':
        unions.delete()
        return redirect('unions')
    return redirect('unions')

# 
# =================================================================
# ============  CREATING ZONES ==============================
def show_zones(request):
    zones = Zone.objects.all()
    context = {'zones': zones}
    return render(request, 'app/show_zones.html', context)

def create_zone(request):
    form = ZoneForm()

    if request.method == 'POST':
        form = ZoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('zones')
    context = {'forms': form}
    return render(request, 'app/create_zone.html', context)

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

def delete_zone(request,pk):
    zones = Zone.objects.get(pk=pk)

    if request.method == 'POST':
        zones.delete()
        return redirect('zones')
    return redirect('zones')



# =================================================================
# ============  CREATING fellowship ==============================
def show_fellowships(request):
    fellowships = Fellowship.objects.all()
    context = {'fellowships': fellowships}
    return render(request, 'app/show_fellowships.html', context)

def create_fellowship(request):
    form = FellowshipForm()

    if request.method == 'POST':
        form = FellowshipForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fellowships')
    context = {'forms': form}
    return render(request, 'app/create_fellowship.html', context)

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

def delete_fellowship(request,pk):
    fellowship = Fellowship.objects.get(pk=pk)

    if request.method == 'POST':
        fellowship.delete()
        return redirect('fellowships')
    return redirect('fellowships')



# 
# =================================================================
# ============  CREATING POSITIONS ==============================
def show_positions(request):
    positions = Position.objects.all()
    context = {'positions': positions}
    return render(request, 'app/show_position.html', context)

def create_position(request):
    form = PositionsForm()

    if request.method == 'POST':
        form = PositionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('positions')
    context = {'forms': form}
    return render(request, 'app/create_position.html', context)

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

def delete_position(request,pk):
    positions = Position.objects.get(pk=pk)

    if request.method == 'POST':
        positions.delete()
        return redirect('positions')
    return redirect('positions')




# =================================================================
# ============  CREATING CHAPLAINS/PCM ==============================
def show_chaplains(request):
    chaplains = Chaplain.objects.all()
    context = {'chaplains': chaplains}
    return render(request, 'app/show_chaplains.html', context)

def create_chaplain(request):
    form = ChaplainForm()

    if request.method == 'POST':
        form = ChaplainForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chaplains')
    context = {'forms': form}
    return render(request, 'app/create_chaplain.html', context)

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

def delete_chaplain(request,pk):
    chaplains = Chaplain.objects.get(pk=pk)

    if request.method == 'POST':
        chaplains.delete()
        return redirect('chaplains')
    return redirect('chaplains')



# =================================================================
# ============  CREATING PATRONS ==============================
def show_patrons(request):
    patrons = Patron.objects.all()
    context = {'patrons': patrons}
    return render(request, 'app/show_patrons.html', context)

def create_patron(request):
    form = PatronForm()

    if request.method == 'POST':
        form = PatronForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patrons')
    context = {'forms': form}
    return render(request, 'app/create_patron.html', context)

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

def delete_patron(request,pk):
    patrons = Patron.objects.get(pk=pk)

    if request.method == 'POST':
        patrons.delete()
        return redirect('patrons')
    return redirect('patrons')


    
# =================================================================
# ============  CREATING ALUMNI REPS ==============================
def show_alumni(request):
    alumni = Alumni_rep.objects.all()
    context = {'alumni': alumni}
    return render(request, 'app/show_alumni.html', context)

def create_alumni(request):
    form = AlumniRepForm()

    if request.method == 'POST':
        form = AlumniRepForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alumni')
    context = {'forms': form}
    return render(request, 'app/create_alumni.html', context)

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

def delete_alumni(request,pk):
    alumni = Alumni_rep.objects.get(pk=pk)

    if request.method == 'POST':
        alumni.delete()
        return redirect('alumni')
    return redirect('alumni')


   
# =================================================================
# ============  CREATING PROGRAMS ==============================
def show_programs(request):
    programs = Program.objects.all()
    context = {'programs': programs}
    return render(request, 'app/show_programs.html', context)

def create_program(request):
    form = ProgramForm()

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('programs')
    context = {'forms': form}
    return render(request, 'app/create_program.html', context)

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

def delete_program(request,pk):
    programs = Program.objects.get(pk=pk)

    if request.method == 'POST':
        programs.delete()
        return redirect('programs')
    return redirect('programs')