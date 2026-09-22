# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Aviation tools for route planning, airport information, and aircraft performance."""

import math
from typing import Any, Dict

# Database of commercial airports (IATA / ICAO / coordinates / longest runway in feet / elevation / timezone)
AIRPORTS_DB: Dict[str, Dict[str, Any]] = {
    "AUS": {
        "iata": "AUS",
        "icao": "KAUS",
        "name": "Austin-Bergstrom International Airport",
        "city": "Austin",
        "country": "United States",
        "lat": 30.1945,
        "lon": -97.6699,
        "elevation_ft": 542,
        "longest_runway_ft": 12250,
        "timezone": "America/Chicago",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "DUB": {
        "iata": "DUB",
        "icao": "EIDW",
        "name": "Dublin Airport",
        "city": "Dublin",
        "country": "Ireland",
        "lat": 53.4213,
        "lon": -6.2701,
        "elevation_ft": 242,
        "longest_runway_ft": 10203,
        "timezone": "Europe/Dublin",
        "customs_port_of_entry": True,
        "us_preclearance": True,
    },
    "JFK": {
        "iata": "JFK",
        "icao": "KJFK",
        "name": "John F. Kennedy International Airport",
        "city": "New York",
        "country": "United States",
        "lat": 40.6413,
        "lon": -73.7781,
        "elevation_ft": 13,
        "longest_runway_ft": 14511,
        "timezone": "America/New_York",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "EWR": {
        "iata": "EWR",
        "icao": "KEWR",
        "name": "Newark Liberty International Airport",
        "city": "Newark",
        "country": "United States",
        "lat": 40.6895,
        "lon": -74.1745,
        "elevation_ft": 18,
        "longest_runway_ft": 11000,
        "timezone": "America/New_York",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "BOS": {
        "iata": "BOS",
        "icao": "KBOS",
        "name": "Boston Logan International Airport",
        "city": "Boston",
        "country": "United States",
        "lat": 42.3656,
        "lon": -71.0096,
        "elevation_ft": 20,
        "longest_runway_ft": 10083,
        "timezone": "America/New_York",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "ORD": {
        "iata": "ORD",
        "icao": "KORD",
        "name": "Chicago O'Hare International Airport",
        "city": "Chicago",
        "country": "United States",
        "lat": 41.9742,
        "lon": -87.9073,
        "elevation_ft": 668,
        "longest_runway_ft": 13000,
        "timezone": "America/Chicago",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "LAX": {
        "iata": "LAX",
        "icao": "KLAX",
        "name": "Los Angeles International Airport",
        "city": "Los Angeles",
        "country": "United States",
        "lat": 33.9425,
        "lon": -118.4081,
        "elevation_ft": 128,
        "longest_runway_ft": 12923,
        "timezone": "America/Los_Angeles",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "SFO": {
        "iata": "SFO",
        "icao": "KSFO",
        "name": "San Francisco International Airport",
        "city": "San Francisco",
        "country": "United States",
        "lat": 37.6190,
        "lon": -122.3749,
        "elevation_ft": 13,
        "longest_runway_ft": 11870,
        "timezone": "America/Los_Angeles",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "SEA": {
        "iata": "SEA",
        "icao": "KSEA",
        "name": "Seattle-Tacoma International Airport",
        "city": "Seattle",
        "country": "United States",
        "lat": 47.4502,
        "lon": -122.3088,
        "elevation_ft": 433,
        "longest_runway_ft": 11901,
        "timezone": "America/Los_Angeles",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "DFW": {
        "iata": "DFW",
        "icao": "KDFW",
        "name": "Dallas/Fort Worth International Airport",
        "city": "Dallas-Fort Worth",
        "country": "United States",
        "lat": 32.8998,
        "lon": -97.0403,
        "elevation_ft": 607,
        "longest_runway_ft": 13401,
        "timezone": "America/Chicago",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "ATL": {
        "iata": "ATL",
        "icao": "KATL",
        "name": "Hartsfield-Jackson Atlanta International Airport",
        "city": "Atlanta",
        "country": "United States",
        "lat": 33.6407,
        "lon": -84.4277,
        "elevation_ft": 1026,
        "longest_runway_ft": 12390,
        "timezone": "America/New_York",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "MIA": {
        "iata": "MIA",
        "icao": "KMIA",
        "name": "Miami International Airport",
        "city": "Miami",
        "country": "United States",
        "lat": 25.7959,
        "lon": -80.2870,
        "elevation_ft": 8,
        "longest_runway_ft": 13016,
        "timezone": "America/New_York",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "DEN": {
        "iata": "DEN",
        "icao": "KDEN",
        "name": "Denver International Airport",
        "city": "Denver",
        "country": "United States",
        "lat": 39.8561,
        "lon": -104.6737,
        "elevation_ft": 5434,
        "longest_runway_ft": 16000,
        "timezone": "America/Denver",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "LHR": {
        "iata": "LHR",
        "icao": "EGLL",
        "name": "London Heathrow Airport",
        "city": "London",
        "country": "United Kingdom",
        "lat": 51.4700,
        "lon": -0.4543,
        "elevation_ft": 83,
        "longest_runway_ft": 12802,
        "timezone": "Europe/London",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "CDG": {
        "iata": "CDG",
        "icao": "LFPG",
        "name": "Paris Charles de Gaulle Airport",
        "city": "Paris",
        "country": "France",
        "lat": 49.0097,
        "lon": 2.5479,
        "elevation_ft": 392,
        "longest_runway_ft": 13829,
        "timezone": "Europe/Paris",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "AMS": {
        "iata": "AMS",
        "icao": "EHAM",
        "name": "Amsterdam Airport Schiphol",
        "city": "Amsterdam",
        "country": "Netherlands",
        "lat": 52.3105,
        "lon": 4.7683,
        "elevation_ft": -11,
        "longest_runway_ft": 12467,
        "timezone": "Europe/Amsterdam",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "FRA": {
        "iata": "FRA",
        "icao": "EDDF",
        "name": "Frankfurt Airport",
        "city": "Frankfurt",
        "country": "Germany",
        "lat": 50.0379,
        "lon": 8.5622,
        "elevation_ft": 364,
        "longest_runway_ft": 13123,
        "timezone": "Europe/Berlin",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "MAD": {
        "iata": "MAD",
        "icao": "LEMD",
        "name": "Adolfo Suárez Madrid-Barajas Airport",
        "city": "Madrid",
        "country": "Spain",
        "lat": 40.4839,
        "lon": -3.5680,
        "elevation_ft": 1998,
        "longest_runway_ft": 13779,
        "timezone": "Europe/Madrid",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "HND": {
        "iata": "HND",
        "icao": "RJTT",
        "name": "Tokyo Haneda Airport",
        "city": "Tokyo",
        "country": "Japan",
        "lat": 35.5494,
        "lon": 139.7798,
        "elevation_ft": 35,
        "longest_runway_ft": 11024,
        "timezone": "Asia/Tokyo",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "NRT": {
        "iata": "NRT",
        "icao": "RJAA",
        "name": "Narita International Airport",
        "city": "Tokyo",
        "country": "Japan",
        "lat": 35.7720,
        "lon": 140.3929,
        "elevation_ft": 141,
        "longest_runway_ft": 13123,
        "timezone": "Asia/Tokyo",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "SIN": {
        "iata": "SIN",
        "icao": "WSSS",
        "name": "Singapore Changi Airport",
        "city": "Singapore",
        "country": "Singapore",
        "lat": 1.3644,
        "lon": 103.9915,
        "elevation_ft": 22,
        "longest_runway_ft": 13123,
        "timezone": "Asia/Singapore",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "SYD": {
        "iata": "SYD",
        "icao": "YSSY",
        "name": "Sydney Kingsford Smith Airport",
        "city": "Sydney",
        "country": "Australia",
        "lat": -33.9399,
        "lon": 151.1753,
        "elevation_ft": 21,
        "longest_runway_ft": 12999,
        "timezone": "Australia/Sydney",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
    "DXB": {
        "iata": "DXB",
        "icao": "OMDB",
        "name": "Dubai International Airport",
        "city": "Dubai",
        "country": "United Arab Emirates",
        "lat": 25.2532,
        "lon": 55.3657,
        "elevation_ft": 62,
        "longest_runway_ft": 14764,
        "timezone": "Asia/Dubai",
        "customs_port_of_entry": True,
        "us_preclearance": False,
    },
}

# Aircraft specifications database
AIRCRAFT_DB: Dict[str, Dict[str, Any]] = {
    "A321XLR": {
        "model": "Airbus A321XLR",
        "family": "A321neo",
        "manufacturer": "Airbus",
        "category": "Narrowbody / Long-range Single-Aisle",
        "max_range_nm": 4700,
        "typical_2class_seats": 182,
        "max_seats": 220,
        "mtow_takeoff_runway_ft": 7800,
        "cruise_speed_mach": 0.78,
        "cruise_speed_knots": 450,
        "fuel_burn_kg_per_hour": 2400,
        "etops_rating_minutes": 180,
        "suitable_for_thin_longhaul": True,
    },
    "A321NEO": {
        "model": "Airbus A321neo",
        "family": "A321neo",
        "manufacturer": "Airbus",
        "category": "Narrowbody",
        "max_range_nm": 3500,
        "typical_2class_seats": 196,
        "max_seats": 244,
        "mtow_takeoff_runway_ft": 7200,
        "cruise_speed_mach": 0.78,
        "cruise_speed_knots": 450,
        "fuel_burn_kg_per_hour": 2400,
        "etops_rating_minutes": 180,
        "suitable_for_thin_longhaul": False,
    },
    "B787-8": {
        "model": "Boeing 787-8 Dreamliner",
        "family": "787 Dreamliner",
        "manufacturer": "Boeing",
        "category": "Widebody",
        "max_range_nm": 7355,
        "typical_2class_seats": 248,
        "max_seats": 359,
        "mtow_takeoff_runway_ft": 8500,
        "cruise_speed_mach": 0.85,
        "cruise_speed_knots": 490,
        "fuel_burn_kg_per_hour": 4900,
        "etops_rating_minutes": 330,
        "suitable_for_thin_longhaul": True,
    },
    "B787-9": {
        "model": "Boeing 787-9 Dreamliner",
        "family": "787 Dreamliner",
        "manufacturer": "Boeing",
        "category": "Widebody",
        "max_range_nm": 7565,
        "typical_2class_seats": 296,
        "max_seats": 389,
        "mtow_takeoff_runway_ft": 8900,
        "cruise_speed_mach": 0.85,
        "cruise_speed_knots": 490,
        "fuel_burn_kg_per_hour": 5400,
        "etops_rating_minutes": 330,
        "suitable_for_thin_longhaul": False,
    },
    "A350-900": {
        "model": "Airbus A350-900",
        "family": "A350 XWB",
        "manufacturer": "Airbus",
        "category": "Widebody",
        "max_range_nm": 8100,
        "typical_2class_seats": 315,
        "max_seats": 440,
        "mtow_takeoff_runway_ft": 8600,
        "cruise_speed_mach": 0.85,
        "cruise_speed_knots": 490,
        "fuel_burn_kg_per_hour": 5800,
        "etops_rating_minutes": 370,
        "suitable_for_thin_longhaul": False,
    },
    "B737-MAX8": {
        "model": "Boeing 737 MAX 8",
        "family": "737 MAX",
        "manufacturer": "Boeing",
        "category": "Narrowbody",
        "max_range_nm": 3550,
        "typical_2class_seats": 162,
        "max_seats": 178,
        "mtow_takeoff_runway_ft": 7500,
        "cruise_speed_mach": 0.79,
        "cruise_speed_knots": 453,
        "fuel_burn_kg_per_hour": 2200,
        "etops_rating_minutes": 180,
        "suitable_for_thin_longhaul": False,
    },
    "A330-900NEO": {
        "model": "Airbus A330-900neo",
        "family": "A330neo",
        "manufacturer": "Airbus",
        "category": "Widebody",
        "max_range_nm": 7200,
        "typical_2class_seats": 287,
        "max_seats": 440,
        "mtow_takeoff_runway_ft": 8800,
        "cruise_speed_mach": 0.82,
        "cruise_speed_knots": 470,
        "fuel_burn_kg_per_hour": 5200,
        "etops_rating_minutes": 240,
        "suitable_for_thin_longhaul": True,
    },
}


def _lookup_airport(query: str) -> Dict[str, Any] | None:
    """Helper to match airport by IATA, ICAO, or city name."""
    clean = query.strip().upper()
    if clean in AIRPORTS_DB:
        return AIRPORTS_DB[clean]
    for apt in AIRPORTS_DB.values():
        if clean == apt["icao"] or clean == apt["city"].upper() or clean in apt["name"].upper():
            return apt
    return None


def _lookup_aircraft(query: str) -> Dict[str, Any] | None:
    """Helper to match aircraft by key or model string."""
    normalized = query.upper().replace(" ", "").replace("-", "")
    for key, spec in AIRCRAFT_DB.items():
        if key.replace("-", "") == normalized or normalized in spec["model"].upper().replace(" ", "").replace("-", ""):
            return spec
    # Additional common aliases
    aliases = {
        "A321": "A321NEO",
        "321XLR": "A321XLR",
        "XLR": "A321XLR",
        "787": "B787-8",
        "7878": "B787-8",
        "7879": "B787-9",
        "737MAX": "B737-MAX8",
        "MAX8": "B737-MAX8",
        "A350": "A350-900",
        "A330": "A330-900NEO",
    }
    for alias, mapped_key in aliases.items():
        if alias in normalized:
            return AIRCRAFT_DB[mapped_key]
    return None


def get_airport_info(airport_code: str) -> Dict[str, Any]:
    """Retrieves operational specifications, coordinates, and runway capabilities for an airport.

    Use this tool whenever you need airport details such as latitude/longitude, runway lengths,
    elevation, timezone, or customs/immigration status for route evaluation.

    Args:
        airport_code: 3-letter IATA code (e.g., 'AUS', 'DUB', 'JFK'), 4-letter ICAO code ('KAUS', 'EIDW'),
                     or city name.

    Returns:
        A dictionary with airport specifications, or an error message if not found.
    """
    apt = _lookup_airport(airport_code)
    if not apt:
        return {
            "status": "error",
            "message": f"Airport code '{airport_code}' not found in database. Supported major international hubs include AUS, DUB, JFK, EWR, BOS, ORD, LAX, SFO, SEA, DFW, ATL, MIA, DEN, LHR, CDG, AMS, FRA, MAD, HND, NRT, SIN, SYD, DXB.",
        }
    return {
        "status": "success",
        "airport": apt,
    }


def calculate_route_distance(origin_code: str, destination_code: str) -> Dict[str, Any]:
    """Calculates the Great Circle distance in nautical miles, initial bearing, and estimated flight time.

    Use this tool to calculate route distances between two airports and determine baseline flight
    block times for network planning and fleet feasibility.

    Args:
        origin_code: Origin airport IATA or ICAO code (e.g., 'AUS').
        destination_code: Destination airport IATA or ICAO code (e.g., 'DUB').

    Returns:
        A dictionary with Great Circle distance (NM and km), initial bearing (degrees and cardinal),
        and estimated flight block hours.
    """
    orig = _lookup_airport(origin_code)
    dest = _lookup_airport(destination_code)

    if not orig:
        return {"status": "error", "message": f"Origin airport '{origin_code}' not found."}
    if not dest:
        return {"status": "error", "message": f"Destination airport '{destination_code}' not found."}

    lat1 = math.radians(orig["lat"])
    lon1 = math.radians(orig["lon"])
    lat2 = math.radians(dest["lat"])
    lon2 = math.radians(dest["lon"])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = math.sin(dlat / 2.0) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))

    # Earth radius in nautical miles: 3440.065 NM (6371.0 km)
    distance_nm = round(3440.065 * c)
    distance_km = round(6371.0 * c)
    distance_miles = round(distance_nm * 1.15078)

    # Initial bearing
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    initial_bearing = round((math.degrees(math.atan2(y, x)) + 360) % 360, 1)

    # Cardinal direction
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    direction_idx = int((initial_bearing + 11.25) / 22.5) % 16
    cardinal = directions[direction_idx]

    # Estimated block time assuming average cruise speed of 460 knots + 35 mins taxi/climb/descent buffer
    estimated_flight_hours = round(distance_nm / 460.0 + 0.58, 2)
    hours = int(estimated_flight_hours)
    minutes = int(round((estimated_flight_hours - hours) * 60))

    return {
        "status": "success",
        "origin": {"iata": orig["iata"], "name": orig["name"], "city": orig["city"]},
        "destination": {"iata": dest["iata"], "name": dest["name"], "city": dest["city"]},
        "great_circle_distance_nm": distance_nm,
        "great_circle_distance_km": distance_km,
        "great_circle_distance_statute_miles": distance_miles,
        "initial_bearing_degrees": initial_bearing,
        "cardinal_direction": cardinal,
        "estimated_block_time": f"{hours}h {minutes}m",
        "estimated_block_hours": estimated_flight_hours,
    }


def get_aircraft_specs(aircraft_model: str) -> Dict[str, Any]:
    """Retrieves technical specifications, range, seating capacity, and runway requirements for an aircraft.

    Use this tool to compare candidate aircraft against route distances and airport runway limitations
    to evaluate operational feasibility, passenger capacity, and fuel performance.

    Args:
        aircraft_model: Model name or identifier (e.g., 'A321XLR', 'A321neo', 'B787-8', 'B787-9', 'A350-900', '737 MAX 8').

    Returns:
        A dictionary with aircraft specifications, operational range, passenger capacity, and runway requirements.
    """
    spec = _lookup_aircraft(aircraft_model)
    if not spec:
        return {
            "status": "error",
            "message": f"Aircraft model '{aircraft_model}' not found. Supported models include A321XLR, A321neo, B787-8, B787-9, A350-900, B737-MAX8, and A330-900neo.",
        }
    return {
        "status": "success",
        "aircraft": spec,
    }


def model_route_profitability(
    origin_code: str,
    destination_code: str,
    aircraft_model: str,
    frequency_per_week: int = 7,
    avg_fare_usd: float = 650.0,
    load_factor_pct: float = 80.0,
    jet_fuel_price_per_gal: float = 2.65,
    cargo_revenue_per_flight_usd: float | None = None,
) -> Dict[str, Any]:
    """Models financial pro-forma economics, revenue, CASM, and annual EBITDA for a commercial route.

    Use this tool to calculate operating costs, revenues, operating margins, breakeven load factors,
    and annual profit projections for route business cases presented to management.

    Args:
        origin_code: Origin airport IATA code (e.g., 'AUS').
        destination_code: Destination airport IATA code (e.g., 'DUB').
        aircraft_model: Aircraft model (e.g., 'A321XLR', 'B787-8').
        frequency_per_week: Number of round-trip flights planned per week (default: 7 for daily).
        avg_fare_usd: Average one-way passenger ticket fare in USD (default: $650).
        load_factor_pct: Projected passenger load factor percentage (e.g., 80.0 for 80%).
        jet_fuel_price_per_gal: Jet-A fuel cost in USD per gallon (default: $2.65).
        cargo_revenue_per_flight_usd: Optional estimated belly cargo revenue per flight (default: auto-modeled based on widebody vs narrowbody).

    Returns:
        A dictionary with pro-forma financial metrics, CASM, RASM, breakeven load factor, and annual EBITDA.
    """
    orig = _lookup_airport(origin_code)
    dest = _lookup_airport(destination_code)
    ac = _lookup_aircraft(aircraft_model)

    if not orig:
        return {"status": "error", "message": f"Origin airport '{origin_code}' not found."}
    if not dest:
        return {"status": "error", "message": f"Destination airport '{destination_code}' not found."}
    if not ac:
        return {"status": "error", "message": f"Aircraft model '{aircraft_model}' not found."}

    # Distance and flight time
    lat1, lon1 = math.radians(orig["lat"]), math.radians(orig["lon"])
    lat2, lon2 = math.radians(dest["lat"]), math.radians(dest["lon"])
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat / 2.0) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    dist_nm = round(3440.065 * c)
    dist_statute_miles = round(dist_nm * 1.15078)
    block_hours = round(dist_nm / 460.0 + 0.58, 2)

    # Range check
    is_within_range = dist_nm <= ac["max_range_nm"]
    range_headroom_nm = ac["max_range_nm"] - dist_nm

    # Capacity
    total_seats = ac["typical_2class_seats"]
    clamped_lf = max(10.0, min(100.0, load_factor_pct))
    pax_per_flight = int(round(total_seats * (clamped_lf / 100.0)))
    annual_flights = int(frequency_per_week * 52 * 2)  # both directions

    asm_per_flight = total_seats * dist_statute_miles
    rpm_per_flight = pax_per_flight * dist_statute_miles

    # Revenues per flight
    pax_ticket_rev = pax_per_flight * avg_fare_usd
    ancillary_rev_per_pax = 40.0  # bags, seat selection, onboard
    total_ancillary_rev = pax_per_flight * ancillary_rev_per_pax

    is_widebody = "Widebody" in ac["category"]
    if cargo_revenue_per_flight_usd is not None:
        cargo_rev = cargo_revenue_per_flight_usd
    else:
        cargo_rev = 11500.0 if is_widebody else 1400.0

    total_revenue_per_flight = pax_ticket_rev + total_ancillary_rev + cargo_rev

    # Operating Costs per flight
    # 1. Fuel cost (1 gallon Jet-A = 3.04 kg)
    fuel_burn_rate_kg_hr = ac["fuel_burn_kg_per_hour"]
    total_fuel_burn_kg = fuel_burn_rate_kg_hr * block_hours
    cost_per_kg_fuel = jet_fuel_price_per_gal / 3.04
    fuel_cost = round(total_fuel_burn_kg * cost_per_kg_fuel, 2)

    # 2. Crew cost
    cockpit_hourly_rate = 480.0  # Capt + FO
    attendant_count = max(3, math.ceil(total_seats / 50))
    cabin_crew_hourly = attendant_count * 52.0
    crew_cost = round((cockpit_hourly_rate + cabin_crew_hourly) * block_hours, 2)

    # 3. Maintenance & airframe reserves
    maint_hourly = 1750.0 if is_widebody else 880.0
    maintenance_cost = round(maint_hourly * block_hours, 2)

    # 4. Landing, navigation, and passenger terminal fees
    landing_fee = 2950.0 if is_widebody else 1150.0
    nav_charges = 820.0
    pax_terminal_fee_per_pax = 24.0
    pax_handling_cost = pax_per_flight * pax_terminal_fee_per_pax
    airport_fees = round(landing_fee + nav_charges + pax_handling_cost, 2)

    # 5. Aircraft lease / ownership hourly allocation
    ownership_hourly = 1450.0 if is_widebody else 760.0
    ownership_cost = round(ownership_hourly * block_hours, 2)

    total_cost_per_flight = round(fuel_cost + crew_cost + maintenance_cost + airport_fees + ownership_cost, 2)

    # Financial KPIs
    operating_profit_per_flight = round(total_revenue_per_flight - total_cost_per_flight, 2)
    operating_margin_pct = round((operating_profit_per_flight / total_revenue_per_flight) * 100.0, 1)

    annual_revenue_usd = round(total_revenue_per_flight * annual_flights, 2)
    annual_cost_usd = round(total_cost_per_flight * annual_flights, 2)
    annual_ebitda_usd = round(operating_profit_per_flight * annual_flights, 2)

    casm_cents = round((total_cost_per_flight / asm_per_flight) * 100.0, 2)
    rasm_cents = round((total_revenue_per_flight / asm_per_flight) * 100.0, 2)

    # Breakeven Load Factor
    fixed_trip_costs = fuel_cost + crew_cost + maintenance_cost + ownership_cost + landing_fee + nav_charges - cargo_rev
    net_contrib_per_seat = avg_fare_usd + ancillary_rev_per_pax - pax_terminal_fee_per_pax
    breakeven_seats = fixed_trip_costs / max(1.0, net_contrib_per_seat)
    breakeven_load_factor_pct = round((breakeven_seats / total_seats) * 100.0, 1)

    return {
        "status": "success",
        "route": {
            "origin": f"{orig['city']} ({orig['iata']})",
            "destination": f"{dest['city']} ({dest['iata']})",
            "distance_nm": dist_nm,
            "block_hours": block_hours,
        },
        "aircraft": {
            "model": ac["model"],
            "seats": total_seats,
            "category": ac["category"],
            "range_nm": ac["max_range_nm"],
            "within_range": is_within_range,
            "range_reserve_nm": range_headroom_nm,
        },
        "operating_assumptions": {
            "frequency_per_week": frequency_per_week,
            "annual_flights": annual_flights,
            "load_factor_pct": clamped_lf,
            "passengers_per_flight": pax_per_flight,
            "avg_fare_usd": avg_fare_usd,
            "jet_fuel_price_per_gal": jet_fuel_price_per_gal,
        },
        "per_flight_finances": {
            "total_revenue_usd": round(total_revenue_per_flight, 2),
            "passenger_revenue_usd": round(pax_ticket_rev, 2),
            "ancillary_revenue_usd": round(total_ancillary_rev, 2),
            "cargo_revenue_usd": round(cargo_rev, 2),
            "total_operating_cost_usd": total_cost_per_flight,
            "cost_breakdown": {
                "fuel_cost_usd": fuel_cost,
                "crew_cost_usd": crew_cost,
                "maintenance_cost_usd": maintenance_cost,
                "airport_and_nav_fees_usd": airport_fees,
                "aircraft_ownership_usd": ownership_cost,
            },
            "net_operating_profit_usd": operating_profit_per_flight,
            "operating_margin_pct": operating_margin_pct,
        },
        "annual_executive_pro_forma": {
            "annual_revenue_usd": annual_revenue_usd,
            "annual_operating_cost_usd": annual_cost_usd,
            "annual_ebitda_contribution_usd": annual_ebitda_usd,
        },
        "airline_unit_economics": {
            "casm_cents": casm_cents,
            "rasm_cents": rasm_cents,
            "breakeven_load_factor_pct": breakeven_load_factor_pct,
        },
    }


def compare_aircraft_suitability(
    origin_code: str,
    destination_code: str,
    aircraft_model_a: str,
    aircraft_model_b: str,
    frequency_per_week: int = 7,
    avg_fare_usd: float = 650.0,
    load_factor_pct: float = 80.0,
) -> Dict[str, Any]:
    """Compares two aircraft types head-to-head for route economics, trip risk, CASM, and annual EBITDA.

    Use this tool to provide management with a comparative business case (e.g. A321XLR vs B787-8),
    identifying whether a right-sized narrowbody or high-capacity widebody is better suited for a market.

    Args:
        origin_code: Origin airport IATA code (e.g., 'AUS').
        destination_code: Destination airport IATA code (e.g., 'DUB').
        aircraft_model_a: First aircraft candidate (e.g., 'A321XLR').
        aircraft_model_b: Second aircraft candidate (e.g., 'B787-8').
        frequency_per_week: Round-trip frequency per week (default: 7).
        avg_fare_usd: Average one-way fare in USD (default: $650).
        load_factor_pct: Projected load factor percentage (default: 80.0).

    Returns:
        A comparison dictionary detailing trip costs, unit economics, annual profit variance, and an executive recommendation.
    """
    eval_a = model_route_profitability(
        origin_code, destination_code, aircraft_model_a, frequency_per_week, avg_fare_usd, load_factor_pct
    )
    eval_b = model_route_profitability(
        origin_code, destination_code, aircraft_model_b, frequency_per_week, avg_fare_usd, load_factor_pct
    )

    if eval_a.get("status") != "success":
        return eval_a
    if eval_b.get("status") != "success":
        return eval_b

    trip_cost_a = eval_a["per_flight_finances"]["total_operating_cost_usd"]
    trip_cost_b = eval_b["per_flight_finances"]["total_operating_cost_usd"]
    trip_cost_diff = round(trip_cost_b - trip_cost_a, 2)

    ebitda_a = eval_a["annual_executive_pro_forma"]["annual_ebitda_contribution_usd"]
    ebitda_b = eval_b["annual_executive_pro_forma"]["annual_ebitda_contribution_usd"]
    ebitda_diff = round(ebitda_b - ebitda_a, 2)

    casm_a = eval_a["airline_unit_economics"]["casm_cents"]
    casm_b = eval_b["airline_unit_economics"]["casm_cents"]

    be_lf_a = eval_a["airline_unit_economics"]["breakeven_load_factor_pct"]
    be_lf_b = eval_b["airline_unit_economics"]["breakeven_load_factor_pct"]

    # Formulate executive recommendation
    seats_a = eval_a["aircraft"]["seats"]
    seats_b = eval_b["aircraft"]["seats"]

    if trip_cost_a < trip_cost_b and be_lf_a <= be_lf_b:
        summary_verdict = (
            f"{eval_a['aircraft']['model']} provides lower trip risk (${trip_cost_diff:,.0f} lower cost per flight) "
            f"and a lower breakeven load factor ({be_lf_a}% vs {be_lf_b}%), making it the safer vehicle to launch and develop "
            f"this secondary market. {eval_b['aircraft']['model']} becomes attractive once seasonal demand reliably exceeds {seats_a} passengers daily."
        )
    elif ebitda_b > ebitda_a:
        summary_verdict = (
            f"{eval_b['aircraft']['model']} generates ${ebitda_diff:,.0f} higher annual EBITDA at {load_factor_pct}% load factor "
            f"due to larger seating capacity and cargo volume, but carries higher trip risk (${trip_cost_b:,.0f}/flight vs ${trip_cost_a:,.0f}/flight)."
        )
    else:
        summary_verdict = (
            f"{eval_a['aircraft']['model']} demonstrates superior overall financial profile for this route profile."
        )

    return {
        "status": "success",
        "route": eval_a["route"],
        "aircraft_comparison": {
            "candidate_a": {
                "model": eval_a["aircraft"]["model"],
                "seats": seats_a,
                "trip_cost_usd": trip_cost_a,
                "casm_cents": casm_a,
                "breakeven_load_factor_pct": be_lf_a,
                "annual_ebitda_usd": ebitda_a,
                "operating_margin_pct": eval_a["per_flight_finances"]["operating_margin_pct"],
            },
            "candidate_b": {
                "model": eval_b["aircraft"]["model"],
                "seats": seats_b,
                "trip_cost_usd": trip_cost_b,
                "casm_cents": casm_b,
                "breakeven_load_factor_pct": be_lf_b,
                "annual_ebitda_usd": ebitda_b,
                "operating_margin_pct": eval_b["per_flight_finances"]["operating_margin_pct"],
            },
            "variance_b_minus_a": {
                "trip_cost_difference_usd": trip_cost_diff,
                "annual_ebitda_difference_usd": ebitda_diff,
                "casm_difference_cents": round(casm_b - casm_a, 2),
            },
        },
        "executive_recommendation": summary_verdict,
    }
