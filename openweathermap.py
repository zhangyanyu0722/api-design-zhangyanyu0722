# !usr/bin/env python
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# HW2 : For all USA Airports, Develop an API and module where we can get current
#       conditions for the airport asked by the API and we can get current weather
#       graphs for specific period
# ===================================================================================
import requests

def data(city):
	APIID = ''
	basic_url = 'http://api.openweathermap.org/data/2.5/weather?'
	url = basic_url + "&q=" + city + "&appid=" + APIID
	res = requests.get(url)
	data = res.json()
	# print(data)
	return data

def show_data(data):
    if  data["cod"] != "408":
        temp = data['main']['temp']
        wind_speed = data['wind']['speed']
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        description = data['weather'][0]['description']
        print('Temperature : {} degree celcius'.format(temp))
        print('Wind Speed : {} m/s'.format(wind_speed))
        print('Latitude : {}'.format(latitude))
        print('Longitude : {}'.format(longitude))
        print('Description : {}'.format(description))
    else:
        print("please enter valid city name:")

def quit():
    return

def main():
    print('1. ENTER CITY NAME:')
    print('2. GO BACK')
    choice = input('Enter your choice : ')

    if choice == '1':
    	city = input('Please input the city name \n')
    	show_data(data(city))
    elif choice == '2':
        quit()
    else:
        print("enter valid choice")

if __name__ == '__main__':
	main()