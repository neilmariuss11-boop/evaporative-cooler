# Design decisions and rationale

Decision log for the student-scale evaporative cooling cabinet. Each entry states the decision, why it was taken (research result, efficiency, practicality or patent avoidance), and what it rules out. Read this before `04-assembly-spec.md`; that file only gives geometry.

Status: decided with the project owner on 30 Sep 2026, revised twice the same day (cellulose pad; then half capacity). One item remains open (section 4).

## 1. Project priority

**Application and cooling efficiency come first; novelty is not a goal.** The owner's group wants a unit that performs as close as possible to the physical limit and could be used by a vendor or farmer, not a new device made for its own sake. Every choice below follows from that.

The physical limit is the outside wet-bulb temperature. In lowland Philippines it is about 25 to 27 °C for most of the year, so no evaporative cooler can go colder than that (see `02-design-recommendation.md`). "High efficiency" here means getting the chamber air as close to that floor as possible, measured as saturation efficiency.

## 2. Decisions taken with the owner

| # | Decision | Choice | Why |
|---|----------|--------|-----|
| D1 | Capacity | **12-17 kg**: one standard vented crate (8-10 kg) plus one slatted shelf for loose produce (4-7 kg); chamber 0.54 × 0.52 × 0.59 m (0.166 m³ gross) | Owner halved the earlier 25-35 kg, three-crate layout. The standard crate keeps market compatibility; the shelf takes leafy or loose produce. Storage trials get their replicates from repeated runs instead of extra crates. |
| D2 | Loading | Front hinged plug door; crate and shelf on side rails | The crate and the shelf lift out daily for weighing and swap with the ambient control. |
| D3 | Walls | 12 mm marine plywood outside, 50 mm EPS core, 3 mm PVC liner inside | School-shop fabrication, low cost, U about 0.57 W/m²K, steady wall gain under 10 W. Rigid walls also keep the design clear of the Evaptainers fabric-wall claims (US 10,907,878). |
| D4 | Pad position | Pad on the back wall, exhaust fans in the roof at the front | Classic cross-flow layout. Fans sit at the front, not above the pad, so air must cross the crate stack instead of short-circuiting from pad to fan. |
| D5 | Controller | ESP32 with ambient, chamber and pad-outlet T/RH sensors, float switch, MOSFET-switched pump and PWM fans, SD logging, external display | Saves water and energy in humid weather, protects the pump, and logs every minute, which gives the group continuous proof of performance. |
| D6 | Base | Four 75 mm locking casters | The unit moves between lab, weighing station and field without two people carrying about 50 kg. |
| D7 | Pad media | **Cellulose honeycomb 7090, 150 mm deep** (replaces coconut coir) | Highest practical efficiency: 150 mm cellulose reaches the high 80s % at 1 m/s and above 90 % at this design's 0.2 m/s, against 50-70 % for coir. Rigid, low pressure drop, lasts years with cleaning instead of weeks, and it is a commodity item sold by Philippine poultry and greenhouse suppliers. |
| D8 | Inspection | No window. Display on the outside of the electrical bay | A window adds heat gain and a leak path. The 2.8 in display beside the door shows ambient and chamber conditions, temperature drop, pad efficiency, mode and water level. |
| D9 | Model detail | Full assembly, every part dimensioned and positioned | For the Blender handoff. |
| D10 | Efficiency definition | Get as close to the wet-bulb limit as possible, single stage | A two-stage unit would add 1.5-2 K on dry afternoons but doubles parts and cost and sits near the dew-point cooler patents. Not worth it for a practical unit. |
| D11 | Testing scope | Test only the final design: commissioning, no-load performance in both seasons, storage trial | No pad-material comparison. |
| D12 | Electronics fallback | Keep the controller, add a 3-position AUTO / OFF / MANUAL switch | If the electronics fail, MANUAL runs the fans at full speed and the pump continuously, so the cooler keeps working. Essential for a unit meant for real use. |
| D13 | Power | 15 V wall adapter plus a 12 V 12 Ah sealed lead-acid battery through a DC-UPS charge module | Mains runs the cooler and charges the battery; brownouts switch to the battery without interruption, for about 8-12 h of cooling or 20 h in humid weather. No solar. |

## 3. Decisions taken by the designer (owner may override)

| # | Decision | Choice | Why |
|---|----------|--------|-----|
| E1 | Large pad face, low face velocity | Pad face 500 × 300 mm (0.15 m²), 150 mm deep, design airflow 100 m³/h, face velocity 0.19 m/s | Saturation efficiency rises as velocity falls and as depth grows. The pad height was cut from 400 to 300 mm to fit the shorter back wall while keeping the face velocity low. Pressure drop stays under 5 Pa. |
| E2 | Airflow 100 m³/h | Scaled with the halved heat load | Keeps the chamber within about 1.1 K of pad-outlet air after loading and 0.3 K at steady load, the same margins as the full-size design, with a third less water and fan energy. The two fans run at about 65 % speed. |
| E3 | Pull-through fans | Two 120 mm 12 V 4-pin PWM fans exhausting through the roof under a rain hood | Fans stay dry; the chamber runs at slight negative pressure so the only inlet is the pad. Two fans give redundancy and finer control. |
| E4 | Once-through air, no recirculation | Inlet only through the pad, outlet only through the fans | Recirculating chamber air would raise the pad-inlet humidity and kill cooling. It also avoids the sump-air pre-cooling loop claimed in US 2014/0174116. |
| E5 | Water distribution built into the cassette | Pipe with upward jets under a full-width aluminium cap, fed through a hose quick coupler | Cellulose pads need even wetting across their full 150 mm depth. The cap method is standard in commercial pad systems. Building it into the cassette lets the whole assembly lift out after unplugging one coupler. |
| E6 | Pump sized to the pad | 12 V brushless DC, 300-500 L/h at 1 m head, 8-12 W, run in pulses | The manufacturer's efficiency data assume a wash rate of about 4.5 L/min for this pad size. Pulsing (2 min on / 3 min off by default, tuned at commissioning) keeps the pad wet at 40 % of the pump energy. |
| E7 | Sump 10 L | 540 × 190 × 160 mm PVC tank under the whole cassette footprint | About two dry-season days of evaporation. No separate drip tray needed. |
| E8 | Daily dry-out | 45 min with pump off and fans at 60 %, default 06:00 | Standard practice for cellulose pads to stop algae; scheduled when the cooling need is lowest. |
| E9 | Cassette through a roof hatch | Cassette lifts straight up through a gasketed hatch | Pad cleaning and replacement take minutes and do not disturb the chamber or door. |
| E10 | Electrical bay on the right side wall | 150 × 250 × 350 mm plywood box, display on its front face | Electronics stay dry and away from the wet module; display is beside the door where the operator stands. |
| E11 | Power layout | 12 V bus behind a DC-UPS module, 3 A bus fuse, main switch and mode switch; battery in the bay | Implements D13. |
| E12 | Rails and shelf | 40 × 40 × 3 mm aluminium angle at two levels: the crate on the lower pair, a slatted polypropylene shelf with front and back lips on the upper pair | Fits common 480-500 mm vented crates. Slats run front to back so the air sweeps along them. |
| E13 | White exterior | White paint, varnished edges | Cuts solar heat gain when the unit is used outdoors. |
| E14 | Three sensors | Ambient in the inlet air, pad outlet at the pad opening, chamber at mid-height between crate levels 1 and 2 | Pad efficiency needs inlet and pad-outlet readings. Chamber efficiency needs a reading in the produce zone, so the reported temperature drop is honest. |
| E15 | No sterilisation, UV, ozone or cloud connection | Local logging only | Keeps the unit simple and clear of the Sabjikothi application. Wi-Fi can be added later without geometry changes. |

## 4. Open decisions (owner to confirm)

| # | Item | Options | Effect on the model | Default used until decided |
|---|------|---------|---------------------|----------------------------|
| O2 | Test crop | Tomato in the crate plus a leafy crop on the shelf; tomato only; other | Only the crate and shelf contents in renders and the storage protocol in `05-systems-and-protocol.md`. | Crate and shelf modelled empty or with generic produce. |

## 5. Positioning: what the unit is, and what it is not

**Not a new invention as built.** A software-based novelty is under consideration; see `06-software-novelty-options.md`. An earlier draft of this log claimed that switching modes on measured wet-bulb depression was new. A later search found close prior art: microcontroller-controlled produce coolers published since at least 2017, a 2026 systematic review of intelligent evaporative cooling for postharvest storage, and US patents on evaporative cooler control. That claim is withdrawn.

**What the group can honestly claim:**
* **Performance near the physical limit.** A target pad saturation efficiency of 85-95 %, against 50-70 % for the natural-fibre pads used in most published student and extension coolers, including coir and jute.
* **A practical unit.** Commodity parts, a pad that lasts years, a 12 V supply, a manual fallback, two-day water autonomy in the dry season, and one-person handling on casters.
* **Proof, not claims.** Continuous logging of ambient, pad-outlet and chamber conditions, water and energy, over both seasons, plus a storage trial against ambient.
* **Credit where due.** PhilMech built charcoal-pad cabinets of 50-400 kg in 2008; Acedo built jute and rice-husk coolers in 1997. The group's unit is smaller, more efficient and fully instrumented.

## 6. Patent check on the final design

Every claimed-feature risk in `01-patent-landscape.md` is avoided by construction: rigid walls, single stage, plain drip distribution under a cap, no sump-air loop, no fabric evaporator wall, no sterilisation. Buying and using a commercial cellulose pad does not infringe anything; the original CELdek patents are decades old and the 7090 pad is a generic commodity.

**One item to verify.** US 2022/0026095, "Evaporative cooler wet and dry mode control", and US 10,145,572 and US 10,969,126, "Direct evaporative cooling system with precise temperature control", are close to the controller's behaviour. The first appears to cover a hybrid unit with a cooling coil downstream, which this design does not have. Running fans with the pump off, as in the SATURATED and DRY-OUT modes, is standard pad-cooler practice recommended by pad manufacturers. Open all three in Espacenet, read the independent claims, and check whether any is in force in the Philippines.
