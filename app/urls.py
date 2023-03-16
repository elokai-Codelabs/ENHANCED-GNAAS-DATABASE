
from django.urls import path
from .import views
from .import excel_to_db



urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),

    path('dashboard/',views.IndexView.as_view(), name='index' ),
    # Uers authentication
    path('logout/', views.LogoutView.as_view(), name='logout'),

    # executive routes
    path('executives/', views.ShowExecutiveView.as_view(), name='executives'),
    path('create-executive/', views.CreateExecutiveView.as_view(), name='create-executive'),
    path('edit-executive/<str:pk>/', views.EditExecutiveView.as_view(), name='edit-executive'),
    path('delete-executive/<str:pk>/', views.DeleteExecutiveView.as_view(), name='delete-executive'),
# commitee
    path('committees/', views.ShowCommitteeView.as_view(), name='committees'),
    path('create-committee/', views.CreateCommitteeView.as_view(), name='create-committee'),
    path('edit-committee/<str:pk>/', views.EditCommitteeView.as_view(), name='edit-committee'),
    path('delete-committee/<str:pk>/', views.DeleteExecutiveView.as_view(), name='delete-committee'),
# committee members
    path('members/', views.ShowMembersView.as_view(), name='members'),
    path('create-member/', views.CreateMemberView.as_view(), name='create-member'),
    path('edit-member/<str:pk>/', views.EditMemberView.as_view(), name='edit-member'),
    path('delete-member/<str:pk>/', views.DeleteMemberView.as_view(), name='delete-member'),

    # union routes
    path('unions/', views.ShowUnionsView.as_view(), name='unions'),
    path('create-union/',views.CreateUnionView.as_view(), name='create-union'),
    path('edit-union/<str:pk>/',views.EditUnionView.as_view(), name='edit-union'),
    path('delete-union/<str:pk>/',views.DeleteUnionView.as_view(), name='delete-union'),

    # ZONES routes
    path('zones/', views.ShowZonesView.as_view(), name='zones'),
    path('create-zone/',views.CreateZoneView.as_view(), name='create-zone'),
    path('edit-zone/<str:pk>/',views.EditZoneView.as_view(), name='edit-zone'),
    path('delete-zone/<str:pk>/',views.DeleteZoneView.as_view(), name='delete-zone'),

     # fellowship routes
    path('fellowships/', views.ShowFellowshipsView.as_view(), name='fellowships'),
    path('create-fellowship/',views.CreateFellowshipView.as_view(), name='create-fellowship'),
    path('edit-fellowship/<str:pk>/',views.EditFellowshipView.as_view(), name='edit-fellowship'),
    path('delete-fellowship/<str:pk>/',views.DeleteFellowshipView.as_view(), name='delete-fellowship'),

# positions routes
    path('positions/', views.ShowPositionView.as_view(), name='positions'),
    path('create-position/', views.CreatePositionView.as_view(), name='create-position'),
    path('edit-position/<str:pk>/', views.EditPositionView.as_view(), name='edit-position'),
    path('delete-position/<str:pk>/', views.DeletePositionView.as_view(), name='delete-position'),

# Chaplain routes
    path('chaplains/', views.show_chaplains, name='chaplains'),
    path('create-chaplain/', views.create_chaplain, name='create-chaplain'),
    path('edit-chaplain/<str:pk>/', views.edit_chaplain, name='edit-chaplain'),
    path('delete-chaplain/<str:pk>/', views.delete_chaplain, name='delete-chaplain'),

# Patrons routes
    path('patrons/', views.show_patrons, name='patrons'),
    path('create-patron/', views.create_patron, name='create-patron'),
    path('edit-patron/<str:pk>/', views.edit_patron, name='edit-patron'),
    path('delete-patron/<str:pk>/', views.delete_patron, name='delete-patron'),

    # Alumni routes
    path('alumni/', views.show_alumni, name='alumni'),
    path('create-alumni/', views.create_alumni, name='create-alumni'),
    path('edit-alumni/<str:pk>/', views.edit_alumni, name='edit-alumni'),
    path('delete-alumni/<str:pk>/', views.delete_alumni, name='delete-alumni'),

    # Alumni routes
    path('programs/', views.show_programs, name='programs'),
    path('create-program/', views.create_program, name='create-program'),
    path('edit-program/<str:pk>/', views.edit_program, name='edit-program'),
    path('delete-program/<str:pk>/', views.delete_program, name='delete-program'),


    # reading excel into database    
    path('read_executive/', excel_to_db.read_executive_excel, name='read_executives'),
    path('read_zone/details', excel_to_db.read_zone_details_excel, name='read_zone_details'),
    path('read_committee/', excel_to_db.read_committee_excel, name='read_committee'),
    path('read_committee_member/', excel_to_db.read_committee_member_excel, name='read_committee_member'),
    path('read_position/', excel_to_db.read_position_excel, name='read_position'),
    path('read_program/', excel_to_db.read_program_excel, name='read_program'),
    path('read_union/', excel_to_db.read_union_excel, name='read_union'),
    path('read_fellowship/', excel_to_db.read_fellowship_excel, name='read_fellowship'),
    path('read_chaplain/', excel_to_db.read_chaplains_excel, name='read_chaplain'),
    path('read_patron/', excel_to_db.read_patrons_excel, name='read_patron'),
    path('read_alumni/', excel_to_db.read_alumni_excel, name='read_alumni'),

    # SMS       
    path('sms/', views.show_sms, name='sms'),
    path("sms/executives/", views.sms_to_executive, name='sms_to_executive'),
    path("sms/fellowship/", views.sms_to_fellowships, name='sms_to_fellowship'),

    # file uploads
    path("files/", views.show_documents, name='documents'),
    path("add-document/", views.add_document, name='add-document')

] 



