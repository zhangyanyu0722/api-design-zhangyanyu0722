# !usr/bin/env python
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# HW2 : Test the data for cities and airports
# ===================================================================================

from weather import data, get_location, get_location_2
import pytest

# def city_test():
#   cityNames = ["London", "Beijing", "New York", "Tokyo", "Hangzhou", "Boston", "Seattle"]
#   for city in cityNames:
#     data(city)

def airport_test():
  assert show_position("Total Rf Heliport") == "Latitude : 40.07, Longitude : -74.93"
#   airportNames = ["Total Rf Heliport", "River Oak Airport", "Ac & R Components Heliport", "Lazy J. Aerodrome"]
#   for airport in airportNames:
#     get_location(airport)
