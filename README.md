# Airport Weather Design Baesd on OpenWeather API

## Product Definition

### Project Mission
- For all USA Airports, Develop an API and module where we can get current conditions for the airport asked by the API and we can get current weather graphs for specific period.

### Target User(s)
- Travelers
- Airport Staff

### User Stories
- I, the traveler, want to know the location and weather conditions of the airport.
- I, the airport staff, want to know the visibility, wind, clouds and weather conditions.
- I, the traveler, want to know the wind and weather conditions of the destination.

## How to use Open Weather API
### Download Files    
clone my repo and unzip it:   
```
git clone https://github.com/BUEC500C1/twitter-summarizer-zhangyanyu0722
```

### Register an API key of Open Weather     
Click this website https://home.openweathermap.org/users/sign_up for sign up, then you can get a free API ID
Open my openweathermap.py, use your API ID to replace mine:    
```
APIID = 'Your API ID'
```
<p align="middle">
  <img src="https://github.com/BUEC500C1/twitter-summarizer-zhangyanyu0722/tree/master/picture/4.png" width="300">
</p>

### Prepare Python Env and Pkg
Check Python Version : 
```
$ Python
Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31) 
```
Install requests for current Python
```
$ pip install requests
```

### Run
Open a terminal, run
```
$ python openweathermaip.py
```
<p align="middle">
  <img src="https://github.com/BUEC500C1/twitter-summarizer-zhangyanyu0722/tree/master/picture/1.png" width="300">
</p>
<p align="middle">
  <img src="https://github.com/BUEC500C1/twitter-summarizer-zhangyanyu0722/tree/master/picture/2.png" width="300">
</p>
<p align="middle">
  <img src="https://github.com/BUEC500C1/twitter-summarizer-zhangyanyu0722/tree/master/picture/3.png" width="300">
</p>




