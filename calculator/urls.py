from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    bathroom_detail_view,
    bedroom_detail_view,
    bikes_detail_view,
    calculator_view,
    history_view,
    hobby_detail_view,
    home_view,
    kitchen_detail_view,
    living_room_detail_view,
    pets_detail_view,
    register_view,
    results_view,
    storage_detail_view,
    work_detail_view,
    calculation_detail_view,
    calculation_delete_view,
    calculation_edit_view,
)


urlpatterns = [
    path(
        "",
        home_view,
        name="home",
    ),

    path(
        "calculator/",
        calculator_view,
        name="calculator",
    ),

    path(
        "results/",
        results_view,
        name="results",
    ),

    path(
        "history/",
        history_view,
        name="history",
    ),

    path(
        "register/",
        register_view,
        name="register",
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="calculator/login.html",
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="home",
        ),
        name="logout",
    ),

    path(
        "rooms/living-room/",
        living_room_detail_view,
        name="living_room_detail",
    ),

    path(
        "rooms/kitchen/",
        kitchen_detail_view,
        name="kitchen_detail",
    ),

    path(
        "rooms/bedroom/",
        bedroom_detail_view,
        name="bedroom_detail",
    ),

    path(
        "rooms/bathroom/",
        bathroom_detail_view,
        name="bathroom_detail",
    ),

    path(
        "additional/work/",
        work_detail_view,
        name="work_detail",
    ),

    path(
        "additional/hobby/",
        hobby_detail_view,
        name="hobby_detail",
    ),

    path(
        "additional/bikes/",
        bikes_detail_view,
        name="bikes_detail",
    ),

    path(
        "additional/pets/",
        pets_detail_view,
        name="pets_detail",
    ),

    path(
            "additional/storage/",
            storage_detail_view,
            name="storage_detail",
    ),
    
    path(
        "history/",
        history_view,
        name="history",
    ),

    path(
        "history/<int:calculation_id>/",
        calculation_detail_view,
        name="calculation_detail",
    ),

    path(
        "history/<int:calculation_id>/edit/",
        calculation_edit_view,
        name="calculation_edit",
    ),

    path(
        "history/<int:calculation_id>/delete/",
        calculation_delete_view,
        name="calculation_delete",
    ),
]