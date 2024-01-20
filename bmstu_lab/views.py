from django.shortcuts import render, redirect
from datetime import datetime
from bmstu_lab.models import Appointment, Application, AppApp, CustomUser
import psycopg2


def GetAppointments(request):
    appointments = Appointment.objects.filter(status='Действует')
    return render(request, 'appointments.html', {'data' : appointments })


def GetAppointment(request, id):

    new_application = Application.objects.create(
        id_user = CustomUser.objects.latest('id'),
        date_creating = datetime.today(),
        status = 'Черновик'
    )
    new_application.save()

    new_appapp = AppApp.objects.create(
        id_appl = Application.objects.latest('id'),
        id_appoint = Appointment.objects.get(id=id)
    )
    new_appapp.save()

    return render(request, 'appointment.html', {'data': Appointment.objects.get(id=id)})


def GetQuery(request):
    query = request.GET.get('query', '')
    query_date = datetime.strptime(query, '%d.%m.%Y').strftime('%Y-%m-%d')
    new_data = Appointment.objects.filter(date=query_date)
    return render(request, 'appointments.html', {'data': new_data})


def DeleteAppointment(request, id):
    conn = psycopg2.connect(dbname="med_exam", user="dbuser", password="123", port="5432")
    cursor = conn.cursor()
    cursor.execute("UPDATE appointment SET status = 'Удалён' WHERE id = %s", (id,))
    conn.commit()   
    cursor.close()
    conn.close()
    return redirect('/')