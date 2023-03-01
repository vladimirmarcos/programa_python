import datetime


fecha_actual=datetime.datetime.today()
print(fecha_actual)
dia_delta=datetime.timedelta(days=30)
print(dia_delta)
for i in range(12):
    fecha_actual=fecha_actual+dia_delta
    print(fecha_actual)