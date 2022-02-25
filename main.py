import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pandas as pd
import flask

import os
os.environ['DISPLAY'] = ':0'
from sklearn import linear_model

app = flask.Flask(__name__)

@app.route('/')

@app.route('/home')
def home():
    return "Hello World"


Best_Renewable_Resource = {
    'low_temp_(f)': [35, 28, 39, 44, 50, 45, 56, 38, 37, 50, 40, 66, 63, 44, 60, 35, 36, 42, 39, 35, 43, 60, 36, 42, 48,
                     44, 52, 44, 32],
    'high_temp_(f)': [53, 56, 58, 59, 67, 58, 75, 55, 56, 64, 60, 36, 80, 64, 78, 60, 50, 64, 60, 57, 66, 78, 59, 62,
                      71, 64, 76, 62, 54],
    'precipitation_(in)': [44.85, 24.93, 39.35, 43.56, 39.74, 34.1, 49.76, 9.3, 36.82, 23.64, 42.94, 9.67, 54.69, 47,
                           52.71, 12.52, 29.13, 53.4, 37.77, 13.3, 44.75, 45.28, 34.66, 2.15, 54.37, 42.64, 53, 41.5,
                           24.31],
    'wind_speed_(mph)': [9.28, 5.21, 4.84, 6.94, 7.78, 3.83, 10.75, 9.6, 5.85, 7.85, 10.43, 6.24, 9.38, 3.69, 8.95,
                         11.63, 8.75, 6.8, 10.45, 4.3, 6.83, 8.11, 11.21, 10.96, 6.58, 8.45, 4.31, 5.83, 11.82],
    'humidity_(d)': [0.11, 0, 2.25, 2.37, 2.33, 0, 11.75, 1.94, 1.42, 0.02, 3.23, 0, 19.4, 0.008, 17.37, 0, 0.45, 0,
                     2.91, 0, 5.65, 14.78, 3.57, 3.91, 8.32, 5.34, 10.09, 3.65, 1.45],
    'cloudy_(percentage)': [50.75, 39.33, 49, 47.58, 44.75, 52.83, 44.42, 47.25, 49.75, 33.75, 46.67, 34.58, 46.75,
                            55.16, 46.83, 41.25, 54.92, 43.16, 48.67, 50.33, 42.33, 40.58, 42.92, 40.91, 42.42, 43.5,
                            43.58, 46.5, 44.58],
    'snowy_(in)': [38.4, 14.91, 59, 38.5, 15, 0.24, 0.1, 4.58, 81, 0, 37, 1.73, 0, 3, 0, 75, 119, 0.62, 16.4, 1.69, 14,
                   0, 23, 0.99, 2, 1, 0.1, 2.04, 33],
    'best_renewable_resource': [1, 2, 1, 3, 2, 1, 2, 1, 2, 2, 1, 2, 3, 1, 3, 2, 4, 1, 1, 1, 2, 2, 1, 1, 1, 2, 1, 1, 1],
}

df = pd.DataFrame(Best_Renewable_Resource,
                  columns=['low_temp_(f)', 'high_temp_(f)', 'precipitation_(in)', 'wind_speed_(mph)', 'humidity_(d)',
                           'cloudy_(percentage)', 'snowy_(in)', 'best_renewable_resource'])

X1 = df[['high_temp_(f)', 'low_temp_(f)', 'precipitation_(in)',  'wind_speed_(mph)', 'humidity_(d)','cloudy_(percentage)'
    , 'snowy_(in)']].astype(
    float)
Y1 = df['best_renewable_resource'].astype(float)

regr = linear_model.LinearRegression()
regr.fit(X1, Y1)




class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Low Temp (f): "))
        # Add Input Box
        self.lowtemp = TextInput(multiline=True)
        self.add_widget(self.lowtemp)

        self.add_widget(Label(text="High Temp (f): "))
        # Add Input Box
        self.hightemp = TextInput(multiline=True)
        self.add_widget(self.hightemp)

        self.add_widget(Label(text="Precipitation (in): "))
        # Add Input Box
        self.precipitation = TextInput(multiline=True)
        self.add_widget(self.precipitation)

        self.add_widget(Label(text="Wind Speed (mph): "))
        # Add Input Box
        self.windspeed = TextInput(multiline=True)
        self.add_widget(self.windspeed)

        self.add_widget(Label(text="Humidity (d): "))
        # Add Input Box
        self.humidity = TextInput(multiline=True)
        self.add_widget(self.humidity)

        self.add_widget(Label(text="Snowy (in): "))
        # Add Input Box
        self.snowy = TextInput(multiline=True)
        self.add_widget(self.snowy)

        self.add_widget(Label(text="Cloudy (percentage): "))
        # Add Input Box
        self.cloudy = TextInput(multiline=True)
        self.add_widget(self.cloudy)

        # Create a Submit Button
        self.submit = Button(text="Predict Best Renewable Resource", font_size=22)
        # Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        lowtemp = self.lowtemp.text
        hightemp = self.hightemp.text
        precipitation = self.precipitation.text
        windspeed = self.windspeed.text
        humidity = self.humidity.text
        snowy = self.snowy.text
        cloudy = self.cloudy.text

        prediction_result1 = regr.predict([[lowtemp, hightemp, precipitation, windspeed, humidity, snowy, cloudy]])
        prediction_result_final = round(max(prediction_result1))
        prediction_result_val = ""
        if prediction_result_final == 1:
            prediction_result_val = 'biomass'
        if prediction_result_final == 2:
            prediction_result_val = 'geothermal'
        if prediction_result_final == 3:
            prediction_result_val = 'solar'
        if prediction_result_final == 4:
            prediction_result_val = 'wind'
        if prediction_result_final == 5:
            prediction_result_val = 'hydro'
        if prediction_result_final == 6:
            prediction_result_val = 'tidal'
        self.add_widget(Label(text=f'Best Renewable Resource:{prediction_result_val}'))

        # Clear the input boxes
        self.lowtemp.text = ""
        self.hightemp.text = ""
        self.precipitation.text = ""
        MyGridLayout()


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    app.run()
