# Design decisions and rationale

Decision log for the student-scale evaporative cooling cabinet. Each entry states the decision, why it was taken (research result, novelty, or patent avoidance), and what it rules out. Read this before `04-assembly-spec.md`; that file only gives geometry.

Status: decided with the project owner on 30 Sep 2026, except the items in section 3.

## 1. Decisions taken with the owner

| # | Decision | Choice | Why |
|---|----------|--------|-----|
| D1 | Capacity | 25-35 kg of produce, three vented plastic crates, chamber 0.54 × 0.52 × 0.90 m (0.25 m³ gross) | Enough produce for 7-14 day shelf-life trials with replicates, still fits a lab bench and a tricycle sidecar. Matches the "small student scale" brief; PhilMech's smallest unit is 50-80 kg. |
| D2 | Loading | Front hinged plug door, crates on side rails | Crates can be lifted out daily for weighing and swapped with the ambient control. Top-loading keeps humid air in but makes weighing awkward. |
| D3 | Walls | 12 mm marine plywood outside, 50 mm EPS core, 3 mm PVC liner inside | School-shop fabrication, PHP-level cost, U about 0.57 W/m²K, keeps steady wall gain under 10 W. Rigid walls also keep the design clear of the Evaptainers fabric-wall claims (US 10,907,878). |
| D4 | Pad position | Pad on the back wall, exhaust fans in the roof at the front | Classic cross-flow layout (PhilMech, Nigerian and Ethiopian active coolers). Fans at the front, not above the pad, so air must cross the crate stack instead of short-circuiting from pad to fan. |
| D5 | Controller | ESP32 with ambient and chamber T/RH sensors, float switch, MOSFET-switched pump and PWM fans, SD logging, external display | Main novelty lever for a humid climate: fan and pump duty follow the measured wet-bulb depression, which saves water and avoids pointless fan running when the air is near saturation. Also gives the thesis its data logger for free. |
| D6 | Base | Four 75 mm locking casters | Unit moves between lab, weighing station and field without two people carrying 60-70 kg. |
| D7 | Pad media | Coconut coir, 75 mm, in a slide-out mesh cassette | Locally abundant, light, cheap to replace when mould appears. Literature puts coir at 53-70 % saturation efficiency at HVAC velocities and above 80 % at the low face velocity used here. The cassette lets charcoal and jute be swapped in for the pad-comparison experiment. |
| D8 | Inspection | No window. Display on the outside of the electrical bay | A window adds heat gain and a leak path; the owner asked for an external display instead. The 2.8 in TFT on the bay's front face shows ambient and chamber T/RH, temperature drop, mode, water level and alarms, so the door stays shut. Feasible without any override. |
| D9 | Model detail | Full assembly, every part dimensioned and positioned | For the Blender handoff. |

## 2. Decisions taken by the designer (owner may override)

| # | Decision | Choice | Why |
|---|----------|--------|-----|
| E1 | Single-stage direct cooling only | No indirect or dew-point stage | A two-stage unit gains 1-3 K in humid air but doubles parts and sits next to the Coolerado/Maisotsenko patent family. Left as a stretch goal in the docs. |
| E2 | Large pad, low face velocity | Pad face 500 × 400 mm (0.20 m²), 75 mm thick, design airflow 120 m³/h, face velocity about 0.17 m/s | Pad studies show saturation efficiency falling from 80-90 % below 1 m/s to 50-60 % at 2-3 m/s. Low velocity also keeps pressure drop under about 10 Pa, which is all a 120 mm axial fan can push. |
| E3 | Pull-through fans | Two 120 mm 12 V 4-pin PWM fans exhausting through the roof under a rain hood | Fans stay on the dry side; the chamber runs at slight negative pressure so the only inlet is the pad. Two small fans give redundancy and finer duty control than one large fan. |
| E4 | Once-through air, no recirculation | Inlet only through the pad, outlet only through the fans | Recirculating chamber air saturates the pad inlet and kills cooling. Also avoids the sump-air pre-cooling loop claimed in US 2014/0174116. |
| E5 | Water distribution | 1/2 in PVC drip pipe, 20 holes of 2 mm at 25 mm pitch, gravity return straight into an open-top sump under the cassette | Century-old prior art, nothing to infringe, no drain tray needed because the sump covers the whole cassette footprint. Keeps clear of the distributor claimed in US 9,310,134. |
| E6 | Sump | Fabricated 540 × 115 × 200 mm PVC-sheet tank, 8 L working, float switch low-level cut-out, overflow, external fill port and sight tube | Calculated evaporation is 3-8 L/day in the dry season, so 8 L gives one to two days between refills. |
| E7 | Cassette loading | Cassette drops in through a gasketed hatch in the roof of the rear module | Swapping media takes two minutes and does not disturb the chamber or door. |
| E8 | Electrical bay on the right side wall, outside the insulation | 150 × 250 × 350 mm plywood box with the display on its front face | Electronics stay dry and away from the wet rear module; display is beside the door where the operator stands. |
| E9 | Modular 12 V power | 12 V bus with a barrel-jack input, fuse and main switch; space reserved for a 12 V 20 Ah battery and a PWM solar charge controller | Owner has not chosen between adapter, battery and PV. This bay accepts all three without redesign. See section 3. |
| E10 | Crate rails | 40 × 40 × 3 mm aluminium angle, three levels, 280 mm pitch | Fits generic 480-500 mm wide vented crates with 10-20 mm bearing each side; 50 mm air gap between crate levels. |
| E11 | Exterior finish | White exterior paint, varnished edges | White cuts solar gain if the unit is used outdoors; the roof is the main solar receiver. |
| E12 | Sensor placement | Ambient sensor in the rear module inlet air, chamber sensor at mid-height between crate levels 1 and 2, optional pad-outlet sensor at the pad opening | Ambient must be the actual pad inlet air. Chamber sensor sits in the produce zone, not in the pad-outlet plenum, so the reported temperature drop is honest. |
| E13 | No sterilisation, no ozone or UV, no IoT cloud | Local logging only | Keeps the design clear of the Sabjikothi application and keeps the thesis focused. A Wi-Fi dashboard can be added later without geometry changes. |

## 3. Open decisions (owner to confirm)

| # | Item | Options | Effect on the model | Default used until decided |
|---|------|---------|---------------------|----------------------------|
| O1 | Power source | (a) 12 V 3 A wall adapter; (b) adapter plus 12 V 20 Ah battery for autonomy; (c) battery plus 50 W solar panel on a separate stand or a roof bracket | (a) and (b) change nothing outside the bay. (c) adds a 50 W panel (about 670 × 450 × 25 mm) either free-standing or on a tilted bracket over the roof; the bracket would sit behind the fan hood. | (b): bay is modelled with the battery and charge-controller footprints present, panel not modelled. |
| O2 | Test crop | Tomato plus pechay; tomato only; other | Only the crate contents in renders and the storage protocol in `05-systems-and-protocol.md`. No geometry change. | Crates modelled empty or with generic round fruit. |

## 4. How the design relates to the research and to novelty

* **Climate reality.** Calculations in `02-design-recommendation.md` show 6-8 K of wet-bulb depression on Philippine dry-season afternoons and 1-3 K in the wet season. The controller's two modes exist because of this: DRY mode maximises cooling, HUMID mode keeps the chamber at 90-95 % RH with minimum water and fan energy. No published small cooler switches behaviour on measured wet-bulb depression; that is the thesis's main claim to novelty, together with the pad-material durability comparison.
* **Efficiency.** Large pad, low face velocity and once-through airflow are what the pad literature says gives the highest saturation efficiency; the fans are sized for airflow, not for pressure.
* **Freedom to operate.** Every claimed-feature risk listed in `01-patent-landscape.md` is avoided by construction: rigid walls, single stage, plain drip pipe, no sump-air loop, no fabric evaporator wall, no sterilisation.
* **Honest prior art.** PhilMech (2008) built charcoal-pad cabinets of 50-400 kg; Acedo (1997) built jute and rice-husk coolers; the UPLB thesis built a two-stage unit. This design is smaller, instrumented, climate-adaptive and swappable-media, and the thesis should say exactly that.
