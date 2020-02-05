# !usr/bin/env python
# ===================================================================================
# Copyright @2020 Yanyu Zhang zhangya@bu.edu
# HW2 : Test the data for cities and airports
# ===================================================================================

from weather import data, get_location
import pytest

# def test():
#   pass

def test_city():
  cityNames = ["London", "Beijing", "New York", "Tokyo", "Hangzhou", "Boston", "Seattle"]
  for city in cityNames:
    data(city)

def test_airport():
  airportNames = ["Total Rf Heliport", "River Oak Airport", "Ac & R Components Heliport", "Lazy J. Aerodrome"]
  for airport in airportNames:
    get_location(airport)

