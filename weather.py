# !usr/bin/env python
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# HW2 : For all USA Airports, Develop an API and module where we can get current
#       conditions for the airport asked by the API and we can get current weather
#       graphs for specific period
# ===================================================================================
import requests
import csv

APIID = '7079bdec57c8dd9409e0803a9fafb586'

def data(city):
    basic_url = 'http://api.openweathermap.org/data/2.5/weather?'
    url = basic_url + "&q=" + city + "&appid=" + APIID
    res = requests.get(url)
    data = res.json()
    show_data(data)

def get_location(airport_Name):
    airportName = airport_Name
    file2 = "airport-codes.csv"
    with open(file2) as csv_file:
        csvitem = list(csv.reader(csv_file) )
    
    for row in csvitem:
        if row[2] == airport_Name:
            position = row[11].split(', ')
            lati = position[0]
            longi = position[1]
            # print(lati, longi)
            search_by_positon(lati, longi)

def search_by_positon(lati, longi):
    basic_url = 'http://api.openweathermap.org/data/2.5/weather?'
    url = basic_url + "lat=" + lati + "&lon=" + longi + "&appid=" + APIID
    res = requests.get(url) 
    data = res.json()
    # print(data)
    # return data
    show_data(data)

def show_position(lati, longi):
    basic_url = 'http://api.openweathermap.org/data/2.5/weather?'
    url = basic_url + "lat=" + lati + "&lon=" + longi + "&appid=" + APIID
    res = requests.get(url) 
    data = res.json()
    # print(data)
    # return data
    show_data_2(data)

    # {'coord': {'lon': -74.93, 'lat': 40.07}, 
    # 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 
    # base': 'stations', 
    # 'main': {'temp': 279.77, 'feels_like': 276.55, 'temp_min': 276.15, 'temp_max': 283.15, 'pressure': 1011, 'humidity': 65}, 
    # 'visibility': 16093, 
    # 'wind': {'speed': 1.87, 'deg': 142}, 
    # 'clouds': {'all': 1}, 
    # 'dt': 1580787145, 
    # 'sys': {'type': 1, 'id': 5384, 'country': 'US', 'sunrise': 1580731617, 'sunset': 1580768399}, 
    # 'timezone': -18000, 
    # 'id': 5095691, 
    # 'name': 'Beverly', 
    # 'cod': 200}

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

def show_data_2(data):
    if  data["cod"] != "408":
        latitude = data['coord']['lat']
        longitude = data['coord']['lon']
        print('Latitude : {}, Longitude : {}'.format(latitude,longitude))
    else:
        print("please enter valid city name:")


def quit():
    return

def main():
    print('1. ENTER CITY NAME:')
    print('2. ENTER AIRPORT NAME:')
    print('3. GO BACK')
    choice = input('Enter your choice : ')

    if choice == '1':
    	city = input('Please Input City Name\n')
    	data(city)
    elif choice == '2':
        airport = input('Please Input Airport Name \n')
        get_location(airport)
    elif choice == '3':
        quit()
    else:
        print("enter valid choice")

if __name__ == '__main__':
    main()

