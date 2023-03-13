import datetime

fecha_actual=datetime.datetime.now()

print(fecha_actual)

fecha_actualizada=datetime.datetime.strftime(fecha_actual,"%Y/%m/%d %H:%M")

print(fecha_actualizada)