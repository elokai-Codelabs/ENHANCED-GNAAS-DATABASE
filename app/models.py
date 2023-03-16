from datetime import datetime
from django.db import models
import uuid
from gnaasDatabase.utils.constants import Leadership

# import constants
from .constants import ZONE_NAMES, UNION_NAME,LEADERSHIP_LEVEL,FELLOWSHIP_TYPE,get_years


# EXECUTIVE TABLE
class Executive(models.Model):
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])

    LEADERSHIP_LEVEL = (
        # Exact names were used as query in show_executive html page. Changing the order or caps can affect the code
        ('National', 'National'),
        ('Union','Union'),
        ('Zone','Zone'),
        ('Fellowship','Fellowship'),
    )
    full_name = models.CharField(max_length=255, )
    executive_image = models.ImageField(null=True, blank=True, default='gnaas.jfif')
    phone = models.CharField(max_length=10, blank=True,null=True)
    email = models.EmailField(max_length = 200,null=True, blank=True)
    program_of_study = models.CharField(max_length=255, blank=True,null=True)
    date_of_service = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    leadership_level = models.CharField(max_length=100, choices=LEADERSHIP_LEVEL)
    position =models.ForeignKey('Position', on_delete=models.CASCADE, null=True, blank=True)
    gnaas_fellowship =models.CharField(max_length=100, blank=True,null=True) 
    local_church =models.CharField(max_length=100, blank=True,null=True) 
    local_church_location =models.CharField(max_length=100, blank=True,null=True) 
    district =models.CharField(max_length=150, blank=True,null=True) 
    conference =models.CharField(max_length=150, blank=True,null=True) 
    created = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.full_name


class Position(models.Model):
    position = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.position = self.position.upper()
        return self.position
  

class Committee(models.Model):
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])
    name = models.CharField(max_length=255)
    mandate = models.CharField(max_length=255,blank=True, null=True)
    date_of_assumption = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Committee_Member(models.Model):
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])
    full_name = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, default='gnaas.jfif')
    contact = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_of_service = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    affiliated_committee = models.ForeignKey(Committee, on_delete = models.CASCADE, blank=True,null=True)
    gnaas_fellowship = models.CharField(max_length=200,blank=True, null=True)
    local_church =models.CharField(max_length=150, blank=True,null=True) 
    local_church_location =models.CharField(max_length=100, blank=True,null=True) 
    local_church_elder =models.CharField(max_length=100, blank=True,null=True) 
    local_church_elder_contact =models.CharField(max_length=50, blank=True,null=True) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    def year_of_service(self):
        return self.date_of_service.strftime('%Y')

class Union(models.Model):
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])
    UNION_NAME = (
       ('Southern Ghana Union', 'Southern Ghana Union'),
        ('Northern Ghana Union','Northern Ghana Union'),
        
    )
    name = models.CharField(max_length=100, choices=UNION_NAME)
    school_hosting = models.CharField(max_length=200,blank=True,null=True)
    academic_year = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    president = models.CharField(max_length=200,blank=True,null=True)
    president_contact = models.IntegerField(blank=True,null=True)
    secretary = models.CharField(max_length=200,blank=True,null=True)
    secretary_contact = models.IntegerField(blank=True,null=True)
    treasurer = models.CharField(max_length=200,blank=True,null=True)
    treasurer_contact = models.IntegerField(blank=True,null=True)
    coordinating_secretary = models.CharField(max_length=200,blank=True,null=True)
    coordinating_secretary_contact = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return self.name

class Zone(models.Model):
    UNION_NAME = (
       ('Southern Ghana Union', 'Southern Ghana Union'),
        ('Northern Ghana Union','Northern Ghana Union'),
        
    )
        
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])
  
    name = models.CharField(max_length=200, blank=True,null=True)
    school_hosting = models.CharField(max_length=200,blank=True,null=True)
    affiliated_union = models.CharField(max_length=200, blank=True,null=True,choices = UNION_NAME)
    academic_year = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    president = models.CharField(max_length=200,blank=True,null=True)
    president_contact = models.IntegerField(blank=True,null=True)
    secretary = models.CharField(max_length=200,blank=True,null=True)
    secretary_contact = models.IntegerField(blank=True,null=True)
    treasurer = models.CharField(max_length=200,blank=True,null=True)
    treasurer_contact = models.IntegerField(blank=True,null=True)
    coordinating_secretary = models.CharField(max_length=200,blank=True,null=True)
    coordinating_secretary_contact = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Fellowship(models.Model):
    UNION_NAME = (
       ('Southern Ghana Union', 'Southern Ghana Union'),
        ('Northern Ghana Union','Northern Ghana Union'),
        
    )
    FELLOWSHIP_TYPE = (
        ('University', 'University'),
       ('Secondary', 'Secondary'),
        ('Nursing Training', 'Nursing Training'),
        ('Teacher Training ', 'Teacher Training'),    
    )

    ZONE_NAMES = (
       ( "Central Ghana","Central Ghana"),
        ("South Central","South Central"),
       ( "Mid South","Mid South"),
       ( "Mid West","Mid West"),
        ("North Mission","North Mission"),
       ( "Mid Central","Mid Central"),
       ( "Ashanti South","Ashanti South"),
        ("Mountain View","Mountain View"),
       ( "Mid North","Mid North"),
       ( "Green View","Green View"),
       ( "Mid South","Mid South"),
        ("Accra City","Accra City"),
        ("Pioneeer Ghana","Pioneeer Ghana"),
        ("West Central","West Central"),
       ( "South West","South West"),
       ( "Western North","Western North"),
       ( "Volta Ghana","Volta Ghana"),
        ("East Ghana","East Ghana"),
        ("Meridian Ghana","Meridian Ghana"),
       ( "Eastern View","Eastern View"),
       ( "Diamond Field","Diamond Field"),
    )
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])
      
    name = models.CharField(max_length=200, blank=True,null=True)
    fellowship_type =models.CharField(max_length=200, blank=True,null=True, choices=FELLOWSHIP_TYPE) 
    academic_year = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    location = models.CharField(max_length=100, blank=True,null=True)
    digital_address = models.CharField(max_length=100, blank=True,null=True)
    population = models.IntegerField(blank=True,null=True)
    males = models.IntegerField(blank=True,null=True)
    females = models.IntegerField(blank=True,null=True)
    union = models.CharField(max_length=200, blank=True,null=True, choices=UNION_NAME)
    zone = models.CharField(max_length=200, blank=True,null=True, choices=ZONE_NAMES)
    president = models.CharField(max_length=200,blank=True,null=True)
    president_contact = models.IntegerField(blank=True,null=True)
    secretary = models.CharField(max_length=200,blank=True,null=True)
    secretary_contact = models.IntegerField(blank=True,null=True)
    treasurer = models.CharField(max_length=200,blank=True,null=True)
    treasurer_contact = models.IntegerField(blank=True,null=True)
    chaplain_or_patron = models.CharField(max_length=200,blank=True,null=True)
    chaplain_contact = models.IntegerField(blank=True,null=True)


    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Patron(models.Model):
    UNION_NAME = (
        ('Southern Ghana Union', 'Southern Ghana Union'),
        ('Northern Ghana Union','Northern Ghana Union'),    
    )
    ZONE_NAMES = (
       ( "Central Ghana","Central Ghana"),
        ("South Central","South Central"),
       ( "Mid South","Mid South"),
       ( "Mid West","Mid West"),
        ("North Mission","North Mission"),
       ( "Mid Central","Mid Central"),
       ( "Ashanti South","Ashanti South"),
        ("Mountain View","Mountain View"),
       ( "Mid North","Mid North"),
       ( "Green View","Green View"),
       ( "Mid South","Mid South"),
        ("Accra City","Accra City"),
        ("Pioneeer Ghana","Pioneeer Ghana"),
        ("West Central","West Central"),
       ( "South West","South West"),
       ( "Western North","Western North"),
       ( "Volta Ghana","Volta Ghana"),
        ("East Ghana","East Ghana"),
        ("Meridian Ghana","Meridian Ghana"),
       ( "Eastern View","Eastern View"),
       ( "Diamond Field","Diamond Field"),
    )
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])
        
    academic_year = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    fellowship = models.CharField(max_length=150)
    zone = models.CharField(max_length=100, choices=ZONE_NAMES)
    union = models.CharField(max_length=100, choices=UNION_NAME)

    def __str__(self):
        return self.name

class Chaplain(models.Model):
    UNION_NAME = (
        ('Southern Ghana Union', 'Southern Ghana Union'),
        ('Northern Ghana Union','Northern Ghana Union'),
        
    )
    ZONE_NAMES = (
       ( "Central Ghana","Central Ghana"),
        ("South Central","South Central"),
       ( "Mid South","Mid South"),
       ( "Mid West","Mid West"),
        ("North Mission","North Mission"),
       ( "Mid Central","Mid Central"),
       ( "Ashanti South","Ashanti South"),
        ("Mountain View","Mountain View"),
       ( "Mid North","Mid North"),
       ( "Green View","Green View"),
       ( "Mid South","Mid South"),
        ("Accra City","Accra City"),
        ("Pioneeer Ghana","Pioneeer Ghana"),
        ("West Central","West Central"),
       ( "South West","South West"),
       ( "Western North","Western North"),
       ( "Volta Ghana","Volta Ghana"),
        ("East Ghana","East Ghana"),
        ("Meridian Ghana","Meridian Ghana"),
       ( "Eastern View","Eastern View"),
       ( "Diamond Field","Diamond Field"),
    )
  
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])

    academic_year = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100)
    fellowship = models.CharField(max_length=150)
    zone = models.CharField(max_length=100, choices=ZONE_NAMES)
    union = models.CharField(max_length=100, choices=UNION_NAME)
    
    def __str__(self):
            return self.name

class Alumni_rep(models.Model):
    UNION_NAME = (
        ('Southern Ghana Union', 'Southern Ghana Union'),
        ('Northern Ghana Union','Northern Ghana Union'),
        
    )
    ZONE_NAMES = (
       ( "Central Ghana","Central Ghana"),
        ("South Central","South Central"),
       ( "Mid South","Mid South"),
       ( "Mid West","Mid West"),
        ("North Mission","North Mission"),
       ( "Mid Central","Mid Central"),
       ( "Ashanti South","Ashanti South"),
        ("Mountain View","Mountain View"),
       ( "Mid North","Mid North"),
       ( "Green View","Green View"),
       ( "Mid South","Mid South"),
        ("Accra City","Accra City"),
        ("Pioneeer Ghana","Pioneeer Ghana"),
        ("West Central","West Central"),
       ( "South West","South West"),
       ( "Western North","Western North"),
       ( "Volta Ghana","Volta Ghana"),
        ("East Ghana","East Ghana"),
        ("Meridian Ghana","Meridian Ghana"),
       ( "Eastern View","Eastern View"),
       ( "Diamond Field","Diamond Field"),
    )
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])

    academic_year = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    name = models.CharField(max_length=255)
    phone = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100)
    gnaas_fellowship = models.CharField(max_length=150)
    local_church = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    zone = models.CharField(max_length=100, choices=UNION_NAME)
    union = models.CharField(max_length=100, choices=UNION_NAME)

    def __str__(self):
            return self.name


class Program(models.Model):
    LEADERSHIP_LEVEL = (
       ('National', 'National'),
        ('Union','Union'),
        ('Zone','Zone'),
        ('Fellowship','Fellowship'),
    )
    def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])

    academic_year = models.CharField(max_length=100, null=True, blank=True, choices=get_years())
    name = models.CharField(max_length=150)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=300,null=True, blank=True)
    cost = models.FloatField(max_length=40)
    program_level =models.CharField(max_length=100, choices=LEADERSHIP_LEVEL)
    def __str__(self):
            return self.name


# Create your models here.
class SMS(models.Model):
    sender_id = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    messages_sent = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title


class Document(models.Model):
    ACADEMIC_YEAR = (
          ('2021',2021),
         ('2022',2022),
          ('2023',2023),
    )
    PROGRAM_LEVEL = (
          ('National','National'),
         ('SGUC','SGUC'),
          ('NGUC','NGUC'),
    )
    name = models.CharField(max_length=255)
    academic_year =models.CharField(max_length=255, choices=ACADEMIC_YEAR)
    status =models.CharField(max_length=255, choices=PROGRAM_LEVEL)
    file = models.FileField(upload_to='documents/')
    def __str__(self):
            return self.name





    