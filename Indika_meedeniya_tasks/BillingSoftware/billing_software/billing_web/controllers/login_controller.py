from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from .. import urls
# Create your views here

class LoginController :
    def __init__(self) -> None:
        self.db_connect = sqlite3.connect("/media/thiloka/Programming/GIT_UBUNTU/mytestcode/Indika_meedeniya_tasks/BillingSoftware/billing_software/billing_web/data.db", check_same_thread=False)
        self.db_cursor = self.db_connect.cursor()

    def login_page(self, request) :
        return render(request, "login.html")
    
    def check_log(self, request) :
        self.name = request.POST['name']
        self.password = request.POST['password']
        get_from_db = self.db_cursor.execute("SELECT * FROM login WHERE name=(?)",(self.name,))
        fetch_data = get_from_db.fetchall()

        if (len(fetch_data)>0) :
            return render(request, "log_report.html", {"error":"You are already logged in."})


        else :
            self.db_cursor.execute("INSERT INTO login(name, password) VALUES (?,?)", (self.name, self.password))
            self.db_connect.commit()
            return render(request, "log_report.html", {"notice":"Added to the database."})
