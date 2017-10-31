# Created by Roman Beya
# Created on 31-oct-2017
# Created for ICS3U
# This program converts the temperature in celsius to fahrenheit
import ui

def convert_celsius_to_fahrenheit(temperature_in_celsius):
	# converts celsius to fahrenheit
	temperature_in_fahrenheit = 1.8 * temperature_in_celsius + 32
	# DISPLAY temp in fahrenheit
	view['output_label'].text = "The temp in fahrenheit is " + str(temperature_in_fahrenheit)
	
def convert_temperature_touch_up_inside(sender):
	# GETTING user input
	user_input = int(view['temp_textfield'].text)
	convert_celsius_to_fahrenheit(user_input)
	
view = ui.load_view()
view.present('sheet')
