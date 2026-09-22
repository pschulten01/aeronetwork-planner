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

from app.tools import calculate_route_distance, get_aircraft_specs, get_airport_info


def test_get_airport_info():
    aus = get_airport_info("AUS")
    assert aus["status"] == "success"
    assert aus["airport"]["city"] == "Austin"
    assert aus["airport"]["longest_runway_ft"] == 12250

    dub = get_airport_info("EIDW")
    assert dub["status"] == "success"
    assert dub["airport"]["iata"] == "DUB"
    assert dub["airport"]["us_preclearance"] is True

    unknown = get_airport_info("XYZ999")
    assert unknown["status"] == "error"


def test_calculate_route_distance():
    res = calculate_route_distance("AUS", "DUB")
    assert res["status"] == "success"
    # Austin to Dublin is roughly 4,160 - 4,200 NM
    assert 4000 < res["great_circle_distance_nm"] < 4300
    assert "h " in res["estimated_block_time"]
    assert res["cardinal_direction"] in ["NE", "ENE", "NNE"]


def test_get_aircraft_specs():
    xlr = get_aircraft_specs("A321XLR")
    assert xlr["status"] == "success"
    assert xlr["aircraft"]["max_range_nm"] == 4700

    b787 = get_aircraft_specs("787-8")
    assert b787["status"] == "success"
    assert b787["aircraft"]["max_range_nm"] > 7000

    unknown = get_aircraft_specs("FlyingSaucer9000")
    assert unknown["status"] == "error"


def test_model_route_profitability():
    from app.tools import model_route_profitability

    prof = model_route_profitability(
        origin_code="AUS",
        destination_code="DUB",
        aircraft_model="A321XLR",
        frequency_per_week=7,
        avg_fare_usd=680.0,
        load_factor_pct=82.0,
    )
    assert prof["status"] == "success"
    assert prof["aircraft"]["within_range"] is True
    assert prof["per_flight_finances"]["total_revenue_usd"] > 0
    assert prof["per_flight_finances"]["total_operating_cost_usd"] > 0
    assert prof["annual_executive_pro_forma"]["annual_revenue_usd"] > 0
    assert 0 < prof["airline_unit_economics"]["breakeven_load_factor_pct"] < 100


def test_compare_aircraft_suitability():
    from app.tools import compare_aircraft_suitability

    comp = compare_aircraft_suitability(
        origin_code="AUS",
        destination_code="DUB",
        aircraft_model_a="A321XLR",
        aircraft_model_b="B787-8",
        frequency_per_week=7,
        avg_fare_usd=680.0,
        load_factor_pct=82.0,
    )
    assert comp["status"] == "success"
    assert "aircraft_comparison" in comp
    assert "executive_recommendation" in comp
    # A321XLR should have lower trip cost than B787-8
    trip_cost_xlr = comp["aircraft_comparison"]["candidate_a"]["trip_cost_usd"]
    trip_cost_787 = comp["aircraft_comparison"]["candidate_b"]["trip_cost_usd"]
    assert trip_cost_xlr < trip_cost_787
