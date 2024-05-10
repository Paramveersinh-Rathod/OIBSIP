import requests
from datetime import datetime
from tkinter import *
from tkinter import messagebox
from math import floor

BGCOLOR = "#CBEEF4"
FONT = "System"


# This function fetch data using api
def fetch_weather_data(city):
    api_key = 'ccac6381d9704d85ba433048242904'
    url = f'http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=7&aqi=no&alerts=no'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


# This function fetch current date and time
def get_current_day_and_time():
    now = datetime.now()
    day = now.strftime('%A')
    time = now.strftime('%I:%M %p').lower()
    return day, time


# This function is responsible for updating data
def get_current_weather(data):
    current = data['current']
    current_day, current_time = get_current_day_and_time()
    current_temp = str(int(current['temp_c']))
    condition = current['condition']['text']
    humidity = "Humidity: " + str(int(current['humidity'])) + "%"
    wind_speed = "Wind: " + str(int(current['wind_kph'])) + "km/h"
    precipitation = "Precipitation: " + str(int(current['precip_mm'])) + "%"
    current_temp_label.config(text=current_temp)
    weather_type_label.config(text=condition)
    wind_label.config(text=wind_speed)
    precipitation_label.config(text=precipitation)
    humidity_label.config(text=humidity)
    daydate = f"{current_day}, {current_time}"
    day_label.config(text=daydate)


# This function updates forecast data
def get_weekly_forecast(data):
    forecast_data = data['forecast']['forecastday'][1:]
    for i, forecast in enumerate(forecast_data, start=1):
        date = forecast['date']
        day_name = datetime.strptime(date, '%Y-%m-%d').strftime('%a')
        day = forecast['day']
        max_temp = floor(int(day['maxtemp_c']))
        min_temp = floor(int(day['mintemp_c']))
        forecast_text = f"{day_name}\n\n{max_temp}\u00B0C\n{min_temp}°C"
        if i == 1:
            day1.config(text=forecast_text)
        elif i == 2:
            day2.config(text=forecast_text)
        elif i == 3:
            day3.config(text=forecast_text)
        elif i == 4:
            day4.config(text=forecast_text)
        elif i == 5:
            day5.config(text=forecast_text)
        elif i == 6:
            day6.config(text=forecast_text)


# This function is used for error handling while performing functions
def fetch_and_display_weather(city):
    try:
        weather_data = fetch_weather_data(city)
        if weather_data:
            get_current_weather(weather_data)
            get_weekly_forecast(weather_data)
        else:
            messagebox.showinfo(title="City-Not-Found", message="Please enter City Name correctly!")
    except Exception as e:
        messagebox.showerror(title="Error", message=f"An error occurred: {e}")


# GUI development using tkinter 👇
window = Tk()
window.title("Weather App")
window.config(padx=30, pady=50, bg=BGCOLOR)

# image
canvas = Canvas(width=150, height=150, highlightthickness=0)
weather_img = PhotoImage(file="weather.png")
weather_img_item = canvas.create_image(75, 75, image=weather_img)
canvas.grid(column=0, row=0, rowspan=3, columnspan=2, stick="w")

# city input and label
city_name_label = Label(text="Enter City Name ", font=(FONT, 18), bg=BGCOLOR)
city_name_label.grid(column=2, row=0, columnspan=4, stick="e", padx=(16, 0))
city_name_input = Entry(width=27, font=(FONT, 10))
city_name_input.grid(column=2, row=1, columnspan=4, stick="e", padx=(0, 1))
city_name_input.focus()


search_button = Button(text="Search", width=27, command=lambda: fetch_and_display_weather(city_name_input.get()),
                       font=(FONT, 9, "bold"))
search_button.grid(column=2, row=2, columnspan=4, stick="e", pady=(0, 20), padx=(10, 0))
current_temp_label = Label(text="25", font=("System", 52), bg=BGCOLOR)
current_temp_label.grid(column=0, row=3, columnspan=7, stick="w", padx=(0, 0))
degree_label = Label(text="\u00B0C", font=(FONT, 17), bg=BGCOLOR)
degree_label.grid(column=0, row=3, padx=(75, 0), rowspan=3, stick="w", pady=(0, 155))
precipitation_label = Label(text="Precipitation: 0%", font=(FONT, 11), bg=BGCOLOR)
precipitation_label.grid(column=0, row=3, columnspan=7, pady=(0, 40), stick="w", padx=(100, 0))
humidity_label = Label(text="Humidity:  27%", font=(FONT, 11), bg=BGCOLOR)
humidity_label.grid(column=0, row=3, columnspan=7, pady=(0, 0), stick="w", padx=(100, 0))
wind_label = Label(text="Wind: 8km/h", font=(FONT, 11), bg=BGCOLOR)
wind_label.grid(column=0, row=3, columnspan=7, pady=(40, 0), stick="w", padx=(100, 0))
weather_label = Label(text="Weather", font=(FONT, 18), bg=BGCOLOR)
weather_label.grid(column=0, row=3, columnspan=7, pady=(0, 30), stick="e")
day_label = Label(text="Tuesday, 4:00 am", font=(FONT, 14), bg=BGCOLOR)
day_label.grid(column=0, row=3, columnspan=7, stick="e", pady=(20, 0))
weather_type_label = Label(text="Smoke", font=(FONT, 10), bg=BGCOLOR)
weather_type_label.grid(column=0, row=3, columnspan=7, pady=(65, 0), stick="e", padx=(300, 0))


# Weekly forecast labels
day1 = Label(text="Mon\n\n21\u00B0C\n32\u00B0C", font=(FONT, 13), bg=BGCOLOR, bd=1, relief="solid", padx=5, pady=5,
             highlightthickness=2)
day1.grid(column=0, row=5, columnspan=7, stick="w", padx=(0, 0), pady=(20, 0))
day2 = Label(text="Tue\n\n21\u00B0C\n32\u00B0C", font=(FONT, 13), bg=BGCOLOR, bd=1, relief="solid", padx=5, pady=5,
             highlightthickness=2)
day2.grid(column=0, row=5, columnspan=7, stick="w", padx=(70, 0), pady=(20, 0))
day3 = Label(text="Wed\n\n21\u00B0C\n32\u00B0C", font=(FONT, 13), bg=BGCOLOR, bd=1, relief="solid", padx=5, pady=5,
             highlightthickness=2)
day3.grid(column=0, row=5, columnspan=7, stick="w", padx=(140, 0), pady=(20, 0))
day4 = Label(text="Thu\n\n21\u00B0C\n32\u00B0C", font=(FONT, 13), bg=BGCOLOR, bd=1, relief="solid", padx=5, pady=5,
             highlightthickness=2)
day4.grid(column=0, row=5, columnspan=7, stick="w", padx=(210, 0), pady=(20, 0))
day5 = Label(text="Fri\n\n21\u00B0C\n32\u00B0C", font=(FONT, 13), bg=BGCOLOR, bd=1, relief="solid", padx=5, pady=5,
             highlightthickness=2)
day5.grid(column=0, row=5, columnspan=7, stick="w", padx=(280, 0), pady=(20, 0))
day6 = Label(text="Sat\n\n21\u00B0C\n32\u00B0C", font=(FONT, 13), bg=BGCOLOR, bd=1, relief="solid", padx=5, pady=5,
             highlightthickness=2)
day6.grid(column=0, row=5, columnspan=7, stick="w", padx=(350, 0), pady=(20, 0))

window.mainloop()
