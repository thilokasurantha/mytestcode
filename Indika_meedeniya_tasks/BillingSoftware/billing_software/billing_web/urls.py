from .controllers import login_controller
from django.urls import path

change = ""
urlpatterns = [
    path("login_page/", login_controller.LoginController().login_page, name="login_page"),
    path("login_page/check_log/", login_controller.LoginController().check_log, name="check_log")
]
