# !usr/bin/env python
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# HW2 : Test the data for cities and airports
# ===================================================================================

from weather import data, get_location
import pytest

def city_test():
  cityNames = ["London", "Beijing", "New York", "Tokyo", "Hangzhou", "Boston", "Seattle"]
  for city in cityNames:
    data(city)
  assert data("London") == "Temperature : 277.71 degree celcius Wind Speed : 8.2 m/s Latitude : 51.51 Longitude : -0.13 Description : clear sky"


def airport_test():
  airportNames = ["Total Rf Heliport", "River Oak Airport", "Ac & R Components Heliport", "Lazy J. Aerodrome"]
  for airport in airportNames:
    get_location(airport)
  assert get_location("Total Rf Heliport") == "Temperature : 279.2 degree celcius Wind Speed : 1.5 m/s Latitude : 40.07 Longitude : -74.93 Description : clear sky"

