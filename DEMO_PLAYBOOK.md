# ✈️ AeroNetwork Planner — Live Demo Playbook

An executive-level commercial airline network planning and fleet strategy application powered by **Google Cloud Vertex AI Agent Platform** and **Gemini 3.6 Flash**.

---

## 🎯 Executive Pitch (30-Second Elevator Pitch)
> *"Opening a new international transatlantic route is a \$40M+ gamble. If you deploy a 300-seat widebody on a secondary city pair like Austin to Dublin, you risk flying half-empty and losing millions. But if you deploy the wrong narrowbody, you won't have the range or cargo capacity.*  
> 
> *Enter **AeroNetwork Planner**: an agentic network strategy co-pilot. In seconds, it verifies airport runway constraints, calculates Great Circle flight mechanics, benchmarks candidate fleet economics (e.g. A321XLR vs. Boeing 787-8), and generates a board-ready pro-forma P&L with CASM, RASM, and EBITDA."*

---

## 🎬 2-Minute Click-by-Click Demo Flow

### 1. Launch the Live Console
* **Public Live Cloud Run URL**: [https://aeronetwork-frontend-494735752228.us-central1.run.app](https://aeronetwork-frontend-494735752228.us-central1.run.app)
* **Local Fallback URL**: [http://127.0.0.1:8080](http://127.0.0.1:8080)
* Point out the **Flight Deck Console & Live Radar**: 
  * Left panel has city-pair selectors, fleet cards, and financial sliders.
  * Right panel features a **Live Carto DarkMatter Geodesic Flight Radar** showing the Great Circle arc, glowing airport pings, an animated airplane (✈️) flying along the corridor, and a Cockpit Telemetry HUD (distance, block time, cruising altitude).

---

### 2. Scenario A: The Single Aircraft Pro-Forma (Austin ➔ Dublin)
1. **Origin Hub**: Select `Austin (AUS)`
2. **Destination**: Select `Dublin (DUB)`
3. **Candidate Aircraft**: Click `A321XLR`
4. **Levers**:
   * Set **Load Factor Slider** to `82%`
   * Set **Average Fare Slider** to `$680`
   * Set **Service Frequency** to `Daily (7x/wk)`
5. Click **"Simulate Route & Pro-Forma"**
6. **What to highlight in the output**:
   * **Physics Feasibility**: Austin's 12,250 ft runway and Dublin's 10,203 ft runway easily support the 4,021 NM flight (within the XLR's 4,700 NM envelope).
   * **Financial Pro-Forma**:
     * Gross Annual Revenue: **\$82.1M**
     * Total Operating Cost: **\$33.4M**
     * Projected Annual EBITDA: **\$48.7M (59.3% operating margin)**
     * Breakeven Load Factor: only **26.1%** (~47 passengers per flight)!

---

### 3. Scenario B: ⚔️ The Fleet Duel (A321XLR vs. Boeing 787-8)
1. Click the **⚔️ Fleet Duel** mode toggle at the top of the left panel.
2. Notice the opponent aircraft selection opens. Keep **Candidate A: A321XLR** and **Benchmark Opponent: B787-8**.
3. Click **"Simulate Route & Pro-Forma"**.
4. **Key Executive Insight**:
   * *"Notice the strategic trade-off: The A321XLR slashes trip cost by **-46.8%** (\$45.8k vs \$86.3k on the 787), drastically de-risking the route in Year 1.*
   * *However, the 787-8 unlocks **\$8.3M in cargo revenue** and higher volume EBITDA if demand exceeds 85%."*

---

### 4. Scenario C: Natural Language Sensitivity Query
1. In the bottom chat bar on the right panel, type:
   > *"What happens to our operating margin on Austin to Dublin if Jet-A fuel prices spike to $3.50 per gallon?"*
2. Hit **Ask Strategy**.
3. **What to highlight**:
   * The agent calculates the delta in fuel expense per flight leg and provides a sensitivity update on breakeven load factor and net margin in real time.

---

## 🏆 Key Architecture & Platform Highlights
* **Agent Engine**: Deployed to **Vertex AI Agent Platform (Agent Runtime)** in `us-central1`.
* **Agent-to-Agent (A2A) Protocol**: Clean HTTP streaming protocol between FastAPI proxy and cloud Reasoning Engine.
* **5 Production Tools**:
  1. `get_airport_info`: Runway dimensions, elevation, US CBP preclearance status.
  2. `calculate_route_distance`: Haversine Great Circle distance, initial bearing, flight block hours.
  3. `get_aircraft_specs`: MTOW runway needs, fuel burn, seating envelopes.
  4. `model_route_profitability`: Full P&L (Jet-A fuel, crew, reserves, CASM, RASM, EBITDA).
  5. `compare_aircraft_suitability`: Head-to-head fleet sensitivity & risk analysis.
* **Evaluation Score**: **5.0 / 5.0 (100% Quality Score)** via `agents-cli eval run` using LLM-as-a-judge against test datasets.
