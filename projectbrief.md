# My agent: AeroNetwork Planner
One-liner: A conversational agent that helps airline network planning teams evaluate and design new commercial airline routes with a catalog of aircraft fleet profiles and airport hub specifications.

Tool coverage:
- Memory: Airline business model (hub-and-spoke vs. point-to-point), primary hub airports, active fleet specifications, and evaluation criteria (e.g., minimum passenger capacity, ETOPS constraints).
- Tools: Airport data lookup (runway lengths, IATA/ICAO codes, geographic coordinates), aircraft performance lookup (max range, seating capacity, cruise speed), and great-circle distance lookup.
- Catalog/UI: Route feasibility scorecards, aircraft-to-route candidate match tables, and hub connectivity breakdown cards.
- Image gen: Stylized new route network map graphic connecting city pairs across global airspace.
- Sandbox: Block hour calculations, payload-range feasibility validation, and trip fuel / seat-mile cost calculations.

Core rails (everyone): memory, tools, eval, deploy, frontend
My stretch menu (pick later): A2UI route cards & aircraft comparison tables, Image gen route map, Code Sandbox flight time & fuel calculations
First eval question: "Evaluate opening a nonstop route between Austin (AUS) and Dublin (DUB). Can an Airbus A321XLR or Boeing 787-8 operate this nonstop, what is the great circle distance, and which aircraft is better suited for initial seasonal demand?"
