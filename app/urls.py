
from django.urls import path
from .import views



urlpatterns = [
    path('',views.index, name='index' ),
    path('executives/', views.show_executive, name='executives'),
    path('create-executive/', views.create_executive, name='create-executive'),
    path('edit-executive/<str:pk>/', views.edit_executive, name='edit-executive'),
    path('delete-executive/<str:pk>/', views.delete_executive, name='delete'),

    path('committees/', views.show_committee, name='committees'),
    path('create-committee/', views.create_committee, name='create-committee'),
    path('edit-committee/<str:pk>/', views.edit_committee, name='edit-committee'),
    path('delete-committee/<str:pk>/', views.delete_committee, name='delete'),

    path('members/', views.show_members, name='members'),
    path('create-member/', views.create_member, name='create-member'),
    path('edit-member/<str:pk>/', views.edit_member, name='edit-member'),
    path('delete-member/<str:pk>/', views.delete_member, name='delete'),

    # union routes
    path('unions/', views.show_unions, name='unions'),
    path('create-union/',views.create_union, name='create-union'),
    path('edit-union/<str:pk>/',views.edit_union, name='edit-union'),
    path('delete-union/<str:pk>/',views.delete_union, name='delete'),

    # ZONES routes
    path('zones/', views.show_zones, name='zones'),
    path('create-zone/',views.create_zone, name='create-zone'),
    path('edit-zone/<str:pk>/',views.edit_zone, name='edit-zone'),
    path('delete-zone/<str:pk>/',views.delete_zone, name='delete'),

     # fellowship routes
    path('fellowships/', views.show_fellowships, name='fellowships'),
    path('create-fellowship/',views.create_fellowship, name='create-fellowship'),
    path('edit-fellowship/<str:pk>/',views.edit_fellowship, name='edit-fellowship'),
    path('delete-fellowship/<str:pk>/',views.delete_fellowship, name='delete'),

# positions routes
    path('positions/', views.show_positions, name='positions'),
    path('create-position/', views.create_position, name='create-position'),
    path('edit-position/<str:pk>/', views.edit_position, name='edit-position'),
    path('delete-position/<str:pk>/', views.delete_position, name='delete'),

# Chaplain routes
    path('chaplains/', views.show_chaplains, name='chaplains'),
    path('create-chaplain/', views.create_chaplain, name='create-chaplain'),
    path('edit-chaplain/<str:pk>/', views.edit_chaplain, name='edit-chaplain'),
    path('delete-chaplain/<str:pk>/', views.delete_chaplain, name='delete'),

# Patrons routes
    path('patrons/', views.show_patrons, name='patrons'),
    path('create-patron/', views.create_patron, name='create-patron'),
    path('edit-patron/<str:pk>/', views.edit_patron, name='edit-patron'),
    path('delete-patron/<str:pk>/', views.delete_patron, name='delete'),

    # Alumni routes
    path('alumni/', views.show_alumni, name='alumni'),
    path('create-alumni/', views.create_alumni, name='create-alumni'),
    path('edit-alumni/<str:pk>/', views.edit_alumni, name='edit-alumni'),
    path('delete-alumni/<str:pk>/', views.delete_alumni, name='delete'),

    # Alumni routes
    path('programs/', views.show_programs, name='programs'),
    path('create-program/', views.create_program, name='create-program'),
    path('edit-program/<str:pk>/', views.edit_program, name='edit-program'),
    path('delete-program/<str:pk>/', views.delete_program, name='delete'),



] 



