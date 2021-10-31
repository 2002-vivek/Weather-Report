from tkinter import * 
from tkinter import messagebox

from requests.api import delete

def weather_details():
    import requests
    import json
    API_key = "Your_API_key"

	# base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    mood = {'rain','light rain','shower rain','thunderstorm','thunderstorm with light rain','thunderstorm with rain','thunderstorm with heavy rain','light thunderstorm','light intensity drizzle rain'}
	# Give city name
    city_name = city.get()
	# complete_url variable to store
	# complete url address
    url = base_url + "appid=" + API_key + "&q=" + city_name
    weather_data = requests.get(url)
    #change format
    readable_weather_data=weather_data.json()           #Dict format contains values and keys
    if(readable_weather_data['cod'] != '404'):
        a = readable_weather_data['main']
        present_temperature=a['temp']
        present_humidity = a['humidity']
        present_pressure = a['pressure']
        b=readable_weather_data['weather']
        weather_description = b[0]["description"]
        wind_speed = readable_weather_data['wind']['speed']
        for i in mood:
            if(weather_description == i):
                email(weather_description)

        temperature.insert(15,str(present_temperature) + 'kelvin(K)')
        humidity.insert(10,str(present_humidity) + '%')
        pressure.insert(15,str(present_pressure) + 'hPa')
        description.insert(10,str(weather_description))
        speed.insert(10,str(wind_speed) + 'mph')
    else:
        messagebox.showerror('Error','Not Found,Please re-enter the city name')
        city.delete(0,END)
def Empty_all_variables():
    city.delete(0,END)
    temperature.delete(0,END)
    humidity.delete(0,END)
    pressure.delete(0,END)
    description.delete(0,END)
    speed.delete(0,END)

    city.focus_set()

def email(weather_description):
    mood=weather_description
    import smtplib, ssl
    port = 587  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sender_mail"  # Enter your address
    receiver_email = "recevier_mail"  # Enter receiver address
    password = "Your_password"
    message = """\
    Subject: Weather Report

    Warning : Bad weather.For Safety,Please carry your umbrella  ."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == "__main__" :
    gui = Tk()
    gui.title("Weather report")
    gui.configure(background='black')
    gui.geometry('400x200')
    heading = Label(gui,text='Weather Report',fg='white',bg='black')
    subheading1 = Label(gui,text='City',fg='white',bg='black')
    subheading2 = Label(gui,text='Temperature',fg='white',bg='black')
    subheading3 = Label(gui,text='Humidity',fg='white',bg='black')
    subheading4 = Label(gui,text='Pressure',fg='white',bg='black')
    subheading5 = Label(gui,text='Description',fg='white',bg='black')
    subheading6 = Label(gui,text='Wind speed',fg='white',bg='black')

    #grids
    heading.grid(row=0,column=1)
    subheading1.grid(row=1,column=0,sticky='E')
    subheading2.grid(row=3,column=0,sticky='E')
    subheading3.grid(row=4,column=0,sticky='E')
    subheading4.grid(row=5,column=0,sticky='E')
    subheading5.grid(row=6,column=0,sticky='E')
    subheading6.grid(row=7,column=0,sticky='E')

    city=Entry(gui)
    temperature=Entry(gui)
    humidity=Entry(gui)
    pressure=Entry(gui)
    description=Entry(gui)
    speed=Entry(gui)

    city.grid(row=1,column=1,ipadx='100')
    temperature.grid(row=3,column=1,ipadx='100')
    humidity.grid(row=4,column=1,ipadx='100')
    pressure.grid(row=5,column=1,ipadx='100')
    description.grid(row=6,column=1,ipadx='100')
    speed.grid(row=7,column=1,ipadx='100')

    submit_button = Button(gui,text='Submit',bg='green',fg='white',command=weather_details)
    clear_button = Button(gui,text='Clear',bg='green',fg='white',command=Empty_all_variables)

    submit_button.grid(row=2,column=1)
    clear_button.grid(row=8,column=1)

    gui.mainloop()
