import tkinter as tk
import requests
import os
from dotenv import load_dotenv
import json
from tkinter import messagebox 
from tkinter import ttk
master= tk.Tk()
load_dotenv()
api_key = os.getenv('apikey')
class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather App")
        master.geometry("800x800")
        self.api_key = api_key
        self.city_name = tk.StringVar()
        self.create_widgets()
        master.mainloop()

    def create_widgets(self):
        cur_frame=ttk.Labelframe(self.master, text="Current weather", padding=10)
        cur_frame.pack(side='left',fill="both", expand="yes", padx=20, pady=10)
        tk.Label(cur_frame, text="Enter City Name:", font=('arial', 14)).pack(pady=10)
        tk.Entry(cur_frame, textvariable=self.city_name, font=('arial', 14), bd=5).pack(pady=10)
        tk.Button(cur_frame, text="Get Weather", font=('arial', 14), command=self.get_cur_weather).pack(pady=10)
        self.result_cur_label = tk.Label(cur_frame, text="", font=('arial', 14))
        self.result_cur_label.pack(pady=20)
        #forecast frame
        forecast_frame=ttk.Labelframe(self.master, text="forecast weather", padding=10)
        forecast_frame.pack(side='right',fill="both", expand="yes", padx=20, pady=10)
        tk.Label(forecast_frame, text="Enter City Name:", font=('arial', 14)).pack(pady=10)
        tk.Entry(forecast_frame, textvariable=self.city_name, font=('arial', 14), bd=5).pack(pady=10)
        tk.Button(forecast_frame, text="Get Weather", font=('arial', 14), command=self.get_fore_weather).pack(pady=10)
        self.result_label = tk.Label(forecast_frame, text="", font=('arial', 14))
        self.result_label.pack(pady=20)
        #function to get current weather
    def get_cur_weather(self):
        city = self.city_name.get()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            if weather_data.get("cod") != 200:
                messagebox.showerror("Error", f"City not found: {city}")
                return
            temp = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']
            result = (f"Temperature: {temp}°C\n"
                      f"Description: {description}\n"
                      f"Humidity: {humidity}%\n"
                      f"Wind Speed: {wind_speed} m/s")
            self.result_cur_label.config(text=result)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
 #function to get 5-time forecast
    def get_fore_weather(self):
        city = self.city_name.get()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            if weather_data.get("cod") != "200":
                messagebox.showerror("Error", f"City not found: {city}")
                return
            forecast_list = weather_data['list'][:5]
            result = "5-Time Forecast:\n"
            for forecast in forecast_list:
                time = forecast['dt_txt']
                temp = forecast['main']['temp']
                description = forecast['weather'][0]['description']
                result += (f"{time} - Temp: {temp}°C, Desc: {description}\n")
            self.result_label.config(text=result)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
WeatherApp( master)