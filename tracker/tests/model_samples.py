from datetime import datetime

from django.urls import reverse

from tracker.models import (
    Crew,
    Country,
    City,
    Facility,
    Airport,
    Route,
    Airplane,
    AirplaneType,
    Flight,
    Order,
    Ticket,
)

from tracker.views import OrderViewSet


def detail_url(id, api_name):
    return reverse(f"tracker:{api_name}-detail", args=[id])


def sample_crew(**params):
    defaults = {"first_name": "John", "last_name": "Doe", "position": "Pilot"}
    defaults.update(params)
    return Crew.objects.create(**defaults)


def sample_country(**params):
    defaults = {"name": "Ukraine"}
    defaults.update(params)
    return Country.objects.create(**defaults)


def sample_city(**params):
    country, created = Country.objects.get_or_create(name="Ukraine")
    defaults = {
        "name": "Kyiv",
        "country": country,
    }
    defaults.update(params)
    return City.objects.create(**defaults)


def sample_facility(**params):
    defaults = {"name": "Lounge zone"}
    defaults.update(params)
    return Facility.objects.create(**defaults)


def sample_airport(**params):
    defaults = {
        "name": "KBP",
        "closest_big_city": sample_city(),
    }
    defaults.update(params)
    airport = Airport.objects.create(**defaults)

    if "facilities" in defaults:
        airport.facilities.set(defaults["facilities"])

    return airport


def sample_route(**params):
    source = sample_airport()
    destination = sample_airport(
        name="LWO",
        closest_big_city=sample_city(name="Lviv"),
    )
    defaults = {
        "source": source,
        "destination": destination,
        "distance": 700,
    }
    defaults.update(params)
    return Route.objects.create(**defaults)


def sample_airplane_type(**params):
    defaults = {"name": "Boeing"}
    defaults.update(params)
    return AirplaneType.objects.create(**defaults)


def sample_airplane(**params):
    defaults = {
        "name": "747-200",
        "rows": 30,
        "seats_in_row": 6,
        "seat_letters": ["A", "B", "C", "D", "E", "F"],
        "airplane_type": sample_airplane_type(),
    }
    defaults.update(params)
    return Airplane.objects.create(**defaults)


def sample_flight(**params):
    defaults = {
        "route": sample_route(),
        "airplane": sample_airplane(),
        "departure_time": "2020-01-01T00:00:00",
        "arrival_time": "2020-01-03T00:00:00",
        "terminal": "D",
        "gate": 10,
    }
    defaults.update(params)
    return Flight.objects.create(**defaults)

def sample_order(**params):
    defaults = {
    }
    defaults.update(params)
    return Order.objects.create(**defaults)

def sample_ticket(**params):
    defaults = {
        "passenger_first_name": "John",
        "passenger_last_name": "Doe",
        "seat_letter": "A",
        "row": 1,
        "flight": sample_flight(),
    }
    defaults.update(params)
    return Ticket.objects.create(**defaults)
