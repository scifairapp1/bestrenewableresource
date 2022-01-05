import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('/scifair.csv')
X = df.drop('renewable_source', axis=1).astype(float)
Y = df['renewable_source'].astype(float)
regr = linear_model.LinearRegression()
regr.fit(X, Y)


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


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
