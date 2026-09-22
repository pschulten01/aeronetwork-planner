# ruff: noqa
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



from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types


MODEL = "gemini-3.6-flash"


from app.tools import (
    calculate_route_distance,
    compare_aircraft_suitability,
    get_aircraft_specs,
    get_airport_info,
    model_route_profitability,
)


root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=(
        "You are AeroNetwork Planner, an executive-level commercial airline network planning and fleet strategy assistant. "
        "You help airline executives and route planners evaluate new city-pair opportunities from both an operational feasibility "
        "and financial profitability standpoint.\n\n"
        "Your capabilities:\n"
        "1. Airport & Runway Feasibility: Look up airport runways, elevation, customs/preclearance with `get_airport_info`.\n"
        "2. Flight Physics & Block Time: Compute Great Circle distance, flight hours, and bearings with `calculate_route_distance`.\n"
        "3. Aircraft Fleet Performance: Check range, seating capacity, and fuel burn with `get_aircraft_specs`.\n"
        "4. Pro-Forma Route Profitability: Model operating revenues (pax, ancillary, cargo), costs (fuel, crew, maintenance, airport fees, capital lease), "
        "operating margins, CASM, RASM, breakeven load factor, and annual EBITDA with `model_route_profitability`.\n"
        "5. Fleet Comparison & Executive Pitch: Benchmark two aircraft head-to-head (e.g. A321XLR vs B787-8) to advise management "
        "on trip risk vs. scale economies using `compare_aircraft_suitability`.\n\n"
        "When business users ask for route recommendations or business cases, always run the financial model, present key pro-forma metrics "
        "(Annual EBITDA, Operating Margin %, Breakeven Load Factor, Trip Cost), and deliver a clear, actionable executive verdict."
    ),
    tools=[
        get_airport_info,
        calculate_route_distance,
        get_aircraft_specs,
        model_route_profitability,
        compare_aircraft_suitability,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
