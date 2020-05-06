import requests
import PySimpleGUI as sg
import time 
import sys

# Define Colors for theme
primary = "#BB86FC"
primary_variant = "#3700B3"
secondary = "#03DAC6"
background = "#121212"
surface = "#1F1B24"
error_bg = "#CF6679"
on_primary = "#000000"
on_secondary = "#000000"
on_background = "#FFFFFF"
on_surface = "#FFFFFF"
on_error_bg = "#000000"
# Define theme
sg.LOOK_AND_FEEL_TABLE['DarkMode'] = {'BACKGROUND': background,
                                        'TEXT': on_surface,
                                        'INPUT': surface,
                                        'TEXT_INPUT': on_background,
                                        'SCROLL': surface,
                                        'BUTTON': (on_surface, surface),
                                        'PROGRESS': (primary, background),
                                        'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
# Apply theme
sg.theme('DarkMode')
# Define Custom Functions

#Define Constants for Request.
api_key = "c8728ceb75d6d63673ef6306ae4d66e3"


def getData(city_name):
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    r = requests.get(url)
    #print(r)
    #print(r.json())
    response = r.json()
    return(response)





layout = [
    [sg.T("Enter City: "), sg.In(key='city')],
    [sg.B("Show")],
    [sg.T("Temprature: "), sg.T(size=(12,1),key='temp')],
    [sg.T("Pressure: "), sg.T(size=(12,1),key='pres')],
    [sg.T("Humidity: "), sg.T(size=(12,1),key='hum')],
    [sg.T("Current Description : "), sg.T(size=(12,1),key='desc')],
    

]

window = sg.Window("DevParapalli Weather APP", layout)

while True:  # Event Loop
    event, values = window.read()       # can also be written as event, values = window()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        try:
            # change the "output" element to be the value of "input" element
            city_name = values['city']
            response = getData(city_name)
            temprature = str(response['main']['temp']) + " Kelvin"
            pressure = str(response['main']['pressure']) + " hPa"
            humidity = str(response['main']['humidity']) + " %"
            description = str(response['weather'][0]["description"])
            print(temprature)
            window['temp'](temprature)
            window['pres'](pressure)
            window['hum'](humidity)
            window['desc'](description)
        except:
            sg.Popup("Wrong Input")

