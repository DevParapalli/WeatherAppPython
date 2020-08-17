import ast
options_file = ast.literal_eval(open("options.txt", "r").read())
choice = options_file['mode']
if choice == "tkinter":
    import PySimpleGUI as sg
elif choice == "remi":
    import PySimpleGUIWeb as sg
elif choice == "pyqt":
    import PySimpleGUIQt as sg
import time 
import sys
import requests
from icons import icondict as icon
from logo import logo
'''
See files put along with this .py for more insight


'''
# Define Colors for theme
image_background = "#2D2D2D"
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
                                        'BUTTON': (on_primary, primary),
                                        'PROGRESS': (primary, background),
                                        'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
# Apply theme
sg.theme('DarkMode')
# Define Custom Functions

#Define Constants for Request.
api_key = options_file["api-key"] #change this later
# define time variable for caching
cache_time = 120.0 # seconds but in float cuz time is in float

current_time = time.time()
time_to_live = current_time + cache_time
cached_response = ""
city_cname = ""
# print(time.ctime(current_time))
# Very Strictly Naive Code Ahead for caching

def getData(city_name, city_cname, cached_response, time_to_live): # current variables and data are input
    current_time = time.time() # we set current time 
    if (current_time >= time_to_live): # time to live is given by input then we perform checks
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
        r = requests.get(url)
        #print(r)
        #print(r.json())
        response = r.json()
        city_cname = city_name # cached city name
        time_to_live = current_time + cache_time # we define new time so that new data is cached 
        cached_response = response # we have response stored in a cached vaariable
        return(response, city_cname, cached_response, current_time, time_to_live) # these terms are redefined to update changes
    elif ((current_time < time_to_live) and (city_name == city_cname)):
        print("Serving Cache") # we dont update the time to live here since we are using the cache
        return(cached_response, city_cname, cached_response, current_time, time_to_live) # the time to live is the same as in input
    elif ((current_time < time_to_live) and (city_name != city_cname)): # If city name is changed we need to make new request
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
        r = requests.get(url)
        #print(r)
        #print(r.json())
        response = r.json()
        city_cname = city_name
        time_to_live = current_time + cache_time # we update time to live here as new data is cached
        cached_response = response
        return(response, city_cname, cached_response, current_time, time_to_live)
        
def truncate(f, n): # taken from https://stackoverflow.com/a/783927/13331594
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def getIconVariable(icon_id): # OWM gives icons in the format "10n" which are not proper variable names in python, 
    icon_id = str(icon_id) #    this function changes the name to be more pythonic
    new_icon_id_0 = icon_id[0] #it changes from "10d" to "d10", yes it always is 3 digits
    new_icon_id_1 = icon_id[1]
    new_icon_id_2 = icon_id[2]
    icon_id_n = str(new_icon_id_2 + new_icon_id_0 + new_icon_id_1)
    return(icon_id_n)

def getIconData(icon_id_pythonic): # this returns the icon data in Base64 from another file(dict) that is imported
    return(icon[icon_id_pythonic])

def getTemperatureReadout(temp_in):
    TemperatureK = str(temp_in) + " Kelvin"  # data formatting
    TemperatureCpreFormat = float(temp_in) - float(273.15)
    TemperatureC = str(truncate(TemperatureCpreFormat, 3)) + "°C"
    Temperature = TemperatureK + " OR " + TemperatureC
    return(Temperature)

class cityNameCannotBeEmpty(Exception):
    pass

layout = [
    [sg.T("Enter Location: "), sg.In(key='cityI')],
    [sg.B("Show"), sg.Quit()],
    [sg.T("")],
    [sg.T("Current Time[SYS]: ",size=(29,1)), sg.T(size=(26,1), key='current_time')],
    [sg.T("Time To Live[SYS]: ",size=(29,1)), sg.T(size=(26,1), key='ttl')],
    [sg.T("Pictorial Representation[SYS+API]:",size=(29,1)),sg.Image(data=logo, background_color=image_background, key='icon'), sg.T("")], # there is a logo to prevent the window from being out of alignment when no request has been made
    [sg.T("Location[API]: ",size=(29,1)), sg.T(size=(24,1),key='cityT')], 
    [sg.T("DateAtLocation[API]: ",size=(29,1)), sg.T(size=(24,1),key='locDate')],
    [sg.T("Sunrise[API]: ",size=(29,1)), sg.T(size=(24,1),key='timerise')],
    [sg.T("Sunset[API]: ",size=(29,1)), sg.T(size=(24,1),key='timeset')],
    [sg.T("Temperature[API]: ",size=(29,1)), sg.T(size=(24,1),key='temp')],
    [sg.T("TemperatureFeels[API]: ",size=(29,1)), sg.T(size=(24,1),key='tempfeels')],
    [sg.T("TemperatureMax[API]: ",size=(29,1)), sg.T(size=(24,1),key='tempmax')],
    [sg.T("TemperatureMin[API]: ",size=(29,1)), sg.T(size=(24,1),key='tempmin')],
    [sg.T("Pressure[API]: ",size=(29,1)), sg.T(size=(24,1),key='pres')],
    [sg.T("Humidity[API]: ",size=(29,1)), sg.T(size=(24,1),key='hum')],
    [sg.T("Main Description[API]: ",size=(29,1)), sg.T(size=(24,1),key='main')],
    [sg.T("Additional Description[API]: ",size=(29,1)), sg.T(size=(24,1),key='desc')],
    [sg.T("WindSpeed[API]: ",size=(29,1)), sg.T(size=(24,1),key='wspeed')],
    [sg.T("WindDeg[API]: ",size=(29,1)), sg.T(size=(24,1),key='wdeg')],
    [sg.T("Latitude[API]: ",size=(29,1)), sg.T(size=(24,1),key='lat')],
    [sg.T("longitude[API]: ",size=(29,1)), sg.T(size=(24,1),key='lon')],
    [sg.B('Quit',key='Quit_alt')]
    

] # this is the GUI layout for the window

if choice == "remi": window = sg.Window("DevParapalli Weather OWM - REMI", layout, no_titlebar=True, grab_anywhere=True, web_port=42069)
elif choice == "tkinter": window = sg.Window("DevParapalli Weather OWM - Tkinter", layout, no_titlebar=True, grab_anywhere=True)
elif choice == "pyqt": window = sg.Window("DevParapalli Weather OWM - PyQt", layout)
else: window = sg.Window("DevParapalli Weather OWM - Else", layout, no_titlebar=True, grab_anywhere=True)

while True:  # Event Loop
    event, values = window.read()       # can also be written as event, values = window()
    print(event, values) # debugging, do not remove
    if event in (None, 'Quit', 'Quit_alt'): # if close button is pressed
        break
    if event == 'Show': # If button is pressed
        try:
            # change the "output" element to be the value of "input" element's API's coresponding response
            city_name = values['cityI']
            if city_name == "":
                print("City Name Cannot be Empty")
                raise cityNameCannotBeEmpty("City Name Cannot be Empty")
            response, city_cname, cached_response, current_time, time_to_live  = getData(city_name, city_cname, cached_response, time_to_live) # updates and refreshes all values.
            #print(response)            
            pressure = str(response['main']['pressure']) + " hPa" # data formatting
            humidity = str(response['main']['humidity']) + " %" # data formatting
            main_desc = str(response['weather'][0]['main'])
            description = str(response['weather'][0]["description"])
            icon_details = getIconData(getIconVariable(str(response['weather'][0]["icon"]))) # i am high as a kite
            window['current_time'](time.ctime(current_time))
            window['ttl'](time.ctime(time_to_live))
            window.Element('icon').Update(data=icon_details)
            window['cityT'](response['name']) # this is the short form of the update function
            window['locDate'](time.ctime(response['dt']))
            window['timerise'](time.ctime(response['sys']['sunrise']))
            window['timeset'](time.ctime(response['sys']['sunset']))
            
            print(getTemperatureReadout(response['main']['temp']))
            window['temp'](getTemperatureReadout(response['main']['temp']))
            window['tempmin'](getTemperatureReadout(response['main']['temp_min']))
            window['tempmax'](getTemperatureReadout(response['main']['temp_max']))
            window['tempfeels'](getTemperatureReadout(response['main']['feels_like']))
            window['pres'](pressure)
            window['hum'](humidity)
            window['main'](main_desc)
            window['desc'](description)
            window['wspeed'](str(response['wind']['speed']) + " m/s")
            window['wdeg'](str(response['wind']['deg']) + "°")
            window['lat'](str(response['coord']['lat']) + " °N")
            window['lon'](str(response['coord']['lon']) + " °E")
        except cityNameCannotBeEmpty:
            sg.PopupError("City Name Cannot Be Empty")
        except:
            sg.PopupError("Malformed Request/Network Error", "Press \"Error\" Button to continue")

