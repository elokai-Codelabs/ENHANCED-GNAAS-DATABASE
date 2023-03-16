from datetime import datetime


ZONE_NAMES = (
    ("Central Ghana", "Central Ghana"),
    ("South Central", "South Central"),
    ("Mid South", "Mid South"),
    ("Mid West", "Mid West"),
    ("North Mission", "North Mission"),
    ("Mid Central", "Mid Central"),
    ("Ashanti South", "Ashanti South"),
    ("Mountain View", "Mountain View"),
    ("Mid North", "Mid North"),
    ("Green View", "Green View"),
    ("Mid South", "Mid South"),
    ("Accra City", "Accra City"),
    ("Pioneeer Ghana", "Pioneeer Ghana"),
    ("West Central", "West Central"),
    ("South West", "South West"),
    ("Western North", "Western North"),
    ("Volta Ghana", "Volta Ghana"),
    ("East Ghana", "East Ghana"),
    ("Meridian Ghana", "Meridian Ghana"),
    ("Eastern View", "Eastern View"),
    ("Diamond Field", "Diamond Field"),
)


LEADERSHIP_LEVEL = (
        # Exact names were used as query in show_executive html page. Changing the order or caps can affect the code
        ('National', 'National'),
        ('Union','Union'),
        ('Zone','Zone'),
        ('Fellowship','Fellowship'),)

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


def get_years() -> tuple:
        BASE_YEAR = 2021
        CURRENT_YEAR = datetime.now().year
        diff = (int(CURRENT_YEAR - BASE_YEAR)) if (CURRENT_YEAR - BASE_YEAR) else 1
        return tuple([(str(BASE_YEAR + i), str(BASE_YEAR + i)) for i in range(0, diff+1)])