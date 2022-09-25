from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(r'D:\Learning\WorkFolder\py.basic\lections\L_4\sensor_system\log.csv', 'a') as file:
        file.write('{}; temperature; {}\n'
                    .format(time, data))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(r'D:\Learning\WorkFolder\py.basic\lections\L_4\sensor_system\log.csv', 'a') as file:
        file.write('{}; pressure; {}\n'
                    .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open(r'D:\Learning\WorkFolder\py.basic\lections\L_4\sensor_system\log.csv', 'a') as file:
        file.write('{}; wind speed; {}\n'
                    .format(time, data))
