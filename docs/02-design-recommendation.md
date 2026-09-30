# Design recommendation: student-scale evaporative cooler for postharvest storage

Status: literature review and engineering recommendation, 30 Sep 2026. Numbers marked "calc" come from `tools/psychro_design.py` in this repo.

Assumed context: an Agricultural and Biosystems Engineering student project in the Philippines (lowland, humid tropical climate). If the site is different, rerun the calculator with local dry-bulb temperature and relative humidity; the conclusions about climate below change with the site, the hardware recommendation mostly does not.

## 1. What the literature says

### 1.1 The physics sets a hard ceiling

A direct evaporative cooler can never cool air below the ambient wet-bulb temperature. The useful number for any site is the wet-bulb depression (dry-bulb minus wet-bulb). Defraeye and colleagues (Frontiers in Food Science and Technology, 2023) built design charts and maps from exactly this quantity and concluded that passive evaporative coolers add up to about 7 days of postharvest life where the depression is large, and that deploying them where it is small makes farmers lose trust in the technology.

Calculated wet-bulb depression for typical Philippine conditions (calc, standard pressure):

| Condition | Dry-bulb | RH | Wet-bulb | Max possible drop |
|-----------|---------:|---:|---------:|------------------:|
| Lowland, April-May, 2 pm, hot day | 34 °C | 55 % | 26.3 °C | 7.7 K |
| Lowland, March-May, 2 pm, typical | 33 °C | 62 % | 26.8 °C | 6.2 K |
| Lowland, dry-season morning | 28 °C | 78 % | 24.9 °C | 3.1 K |
| Lowland, wet-season afternoon | 31 °C | 78 % | 27.7 °C | 3.3 K |
| Lowland, rainy day | 28 °C | 90 % | 26.6 °C | 1.4 K |
| Highland (Benguet) afternoon | 24 °C | 70 % | 20.1 °C | 3.9 K |
| Semi-arid reference (Sahel-type) | 35 °C | 30 % | 21.5 °C | 13.5 K |

The takeaway: in the Philippines the temperature benefit is real only in dry-season afternoons (6 to 8 K available, about 5 to 6 K delivered by a good pad). In the wet season the cooler is mainly a **humidifier**. That is still worth having: for leafy and thin-skinned produce, water loss (transpiration) is the dominant cause of quality loss, and holding 85-95 % RH cuts weight loss several-fold even at ambient temperature (PhilMech reports 3-4 extra days of freshness; the Ethiopian and Nigerian active-cooler studies report 5-10 K drops and RH 85-95 %). Frame the thesis objective as "temperature reduction and humidity control", not "refrigeration".

### 1.2 Performance of the design families

| Family | Typical size | Reported temperature drop | Cooling / saturation efficiency | Notes |
|--------|-------------:|--------------------------:|-------------------------------:|-------|
| Pot-in-pot (zeer) | 10-60 L | 3-8 K in dry climates; ~2 K in humid | n/a (passive) | Cheapest; MIT D-Lab Mali evaluation; heat-and-mass model by MIT JWAFS 2020. Poor in humid air. |
| Brick ZECC (Roy & Khurdiya, IARI) | 100-200 kg | 6-10 K, RH ~90 % | 87-89 % reported (India) | Tomato shelf life 6 to 15 days (JIRCAS); UP Mindanao brick cooler 61.8 % marketable after 49 days vs 23.3 %. Static, heavy. |
| Charcoal cooler / charcoal blanket | 0.06-0.5 m³ | ~5 K (Empa lab), 70 % daytime efficiency in Kenya field trials; losses cut up to 45 % | 70-88 % | Locally available in PH; PhilMech already uses charcoal pads. |
| Active direct cooler (fan + pump + pad + cabinet) | 0.2-1 m³ | 5-10 K in tropical trials | 77-98 % with good pads | Best air distribution and most controllable; the family used by PhilMech, Nigeria (SPECSS, Ethiopia (South Gondar, 2025). |
| Two-stage (indirect + direct) | 0.3 m³ and up | 1-3 K more than direct in humid air | 88-96 % reported | UPLB undergraduate thesis did this for tomato. More parts, more patent exposure (see landscape file). |

### 1.3 Pad materials (cooling/saturation efficiency at comparable face velocity)

* Commercial CELdek cellulose: 78-80 %, benchmark.
* Jute (tossa): 62 % at 2.4 m/s; up to 93 % in a hexagonal low-velocity cooler; highest mould degradation over time.
* Coconut coir: 53-70 % depending on packing density and velocity; widely available in the Philippines; a 2008 study built a sustainable coir pad specifically for produce coolers.
* Charcoal (lump, 20-40 mm): 87-91 %; heavy but cheap; PhilMech's choice.
* Luffa: 55 % but best durability; jute-luffa blends improve both water retention and airflow.
* Wood wool / shavings: 74-92 %.
* Rice husk (Acedo 1997): works, low cost, compacts and rots faster.

Face velocity matters more than the material: below about 1 m/s most fibrous pads reach 70-90 %; at 2-3 m/s they fall to 50-60 %. Design for 0.5-0.8 m/s.

## 2. Recommended design

**A fan-assisted, single-stage direct evaporative cooling cabinet, 12 V DC, with a locally sourced natural-fibre pad, insulated rigid chamber, and a simple duty-cycle controller.**

Why this and not the alternatives:

* Pot-in-pot: not enough engineering content for an ABE thesis and near-useless in humid air.
* Brick ZECC: proven but too large and static for "student scale", and there is little left to investigate.
* Two-stage: better numbers on paper but doubles the parts count and brings you close to the Coolerado/M-cycle patent family. Keep it as a stretch goal only if the direct unit is finished early.
* Fabric-walled portable: directly on top of the Evaptainers patent. Avoid.

### 2.1 Target specification

| Item | Value | Basis |
|------|-------|-------|
| Storage volume | 0.20-0.25 m³ (inside about 0.55 × 0.55 × 0.75 m) | 25-35 kg tomato in 2-3 plastic crates; fits a lab bench and a tricycle |
| Test crop | Tomato (breaker stage), plus one leafy crop (pechay) for the humidity case | Standard in the ZECC and PhilMech literature, easy to score |
| Design airflow | 90-120 m³/h once-through (not recirculated) | Enough to hold the chamber within ~1.5 K of pad-outlet air at a 60 W load (calc) |
| Fans | 2 × 120 mm 12 V DC axial (nominal 100-150 m³/h each, ~2-3 W) mounted as exhaust, pulling air through the pad | Pull-through keeps the fan dry and gives even face velocity |
| Pad | 60-100 mm thick, face area ≥ 0.05 m² (e.g. 0.30 × 0.20 m), in a removable galvanised-mesh frame | Face velocity 0.5-0.7 m/s (calc); thicker pad raises efficiency but also pressure drop, which small axial fans handle poorly beyond 100 mm |
| Pad media | Coconut coir as the primary treatment; charcoal and jute as comparison treatments | See section 1.3 |
| Water system | 12 V submersible pump 2-4 W, 200-300 L/h, PVC drip pipe with 2 mm holes at 25 mm pitch over the pad, gravity return to a 10-15 L sump | Drip pipe and sump are century-old prior art |
| Water use | 3-8 L/day continuous in the dry season (calc); refill every 2 days | |
| Chamber walls | 12 mm marine plywood or 0.5 mm GI sheet outside, 25-50 mm EPS or PU foam, food-safe plastic sheet inside; sloped drip floor | Keeps wall heat gain under 20-30 W |
| Air path | Inlet through the pad on one side, fans on the opposite top, slatted crate shelves so air passes through the produce, small outlet louvre | Avoid dead zones |
| Power | 12 V, total 8-12 W; run from a 20-30 W PV panel with a 12 V 7-12 Ah battery, or a bench supply in the lab | Off-grid demonstration; also lets you test the "solar-powered" case that Nigerian and Ethiopian studies report |
| Control (optional, recommended) | Arduino/ESP32 with 2 DHT22 or SHT31 sensors (ambient and chamber), a float switch, and a MOSFET for the pump. Pump runs 30 s every 5 min; fan runs continuously in the dry season and at reduced duty when ambient RH > 85 % | Cheap, gives you data logging for free, and is the main "novelty" lever in a humid climate |
| Instrumentation | Ambient and chamber T/RH loggers, produce pulp temperature probe, water meter or graduated sump, kitchen balance for weight loss, colour chart and firmness scoring | Standard ABE test protocol |

### 2.2 Performance you can expect (calc, 80 % pad efficiency, 120 m³/h, 60 W load)

| Ambient | Pad outlet | Chamber air | Chamber RH |
|---------|-----------:|------------:|-----------:|
| 34 °C / 55 % | 27.9 °C | 29.4 °C | ~88 % |
| 33 °C / 62 % | 28.0 °C | 29.6 °C | ~90 % |
| 28 °C / 78 % | 25.5 °C | 27.1 °C | ~95 % |
| 31 °C / 78 % | 28.4 °C | 29.9 °C | ~95 % |

So: 4-5 K below ambient on a dry-season afternoon, 1-2 K in the wet season, and 88-95 % RH throughout. Insulation and a heat load below 60 W are what keep the chamber close to the pad outlet; skimping on insulation costs more than a better pad gains.

### 2.3 What makes it a defensible thesis, not a copy

Pick one or two of these as the research question; all sit on free-to-use prior art:

1. **Pad comparison with local agricultural residues** at the same face velocity: coir vs charcoal vs jute (or abaca), measuring saturation efficiency, pressure drop and efficiency decay over 4-6 weeks (mould). The durability angle is thin in the literature.
2. **Humid-climate control strategy**: fan and pump duty cycling based on measured wet-bulb depression, and its effect on water use and chamber RH. The "intelligent evaporative cooling" systematic review (Preprints, Jan 2026) shows this space is active but not crowded, and the Sabjikothi application is the only IP found near it.
3. **Load-side validation**: pulp-temperature cooling curves, weight loss and marketable fraction of tomato and pechay over 7-14 days, cooler vs ambient vs (if available) a domestic refrigerator.
4. **Solar sizing**: energy audit of the 12 V system across a full dry-season day, PV and battery sizing for autonomy.

Two things to state explicitly in the thesis so the novelty claim is honest: PhilMech built charcoal-pad cabinets of 50-400 kg in 2008, and Acedo built jute and rice-husk coolers in 1997. Your contribution is the scale, the instrumentation and control, and the comparative data, not the concept.

### 2.4 Build sequence

1. Build the chamber and pad frame; measure fan curve against pad pressure drop with a manometer.
2. No-load test: 48 h runs per pad material, log ambient and chamber T/RH, compute saturation efficiency and water use.
3. Add crates of tomato; run 7-14 day storage trials with ambient control.
4. Add the controller and repeat one no-load and one loaded run to quantify water saved.
5. Optional: solar and battery autonomy test.

## 3. Bill of materials (indicative, Philippine market)

| Item | Qty | Approx. PHP |
|------|----:|------------:|
| Marine plywood 12 mm, 4 × 8 ft | 1 | 1 200 |
| EPS foam 50 mm or PU board | 2 m² | 800 |
| 120 mm 12 V DC fans | 2 | 500 |
| 12 V submersible pump 3 W | 1 | 350 |
| PVC 1/2 in pipe, fittings, drip pipe | lot | 300 |
| Galvanised mesh for pad frame | 1 m² | 250 |
| Coconut coir (bulk), charcoal 5 kg, jute sacks | lot | 400 |
| Plastic crates | 3 | 600 |
| ESP32 + 2 × SHT31/DHT22 + MOSFET + float switch | 1 set | 1 200 |
| 12 V 7 Ah SLA battery + 30 W PV panel + PWM controller | 1 set | 3 500 |
| Hinges, silicone, food-grade liner, paint | lot | 700 |
| **Total** | | **~9 800** |

Without the solar kit, about PHP 6 300.

## 4. Sources

Journal and institutional sources used for the numbers above (full citations to be added to the thesis reference list):

* Defraeye T. et al. (2023). Passive evaporative coolers for postharvest storage of fruit and vegetables: where to best deploy them and how well do they perform. Frontiers in Food Science and Technology 3:1100181.
* Defraeye T., Schudel S., Shrivastava C., Motmans T., Umani K., Crenna E., Shoji K., Onwude D. (2024). The charcoal cooling blanket. Biosystems Engineering 238:128-142.
* Evaluation of the passive evaporative cooling blanket for fruits and vegetables in Kenya (Energy for Sustainable Development, 2025).
* Verploegen E., Rinker P., Ognakossan K.E. (2018). Evaporative Cooling Best Practices Guide. MIT D-Lab.
* MIT News (2023). Open-source forced-air evaporative cooling chamber.
* MIT JWAFS (2020). A heat and mass transport model of clay pot evaporative coolers for vegetable storage. Int. J. Heat Mass Transfer.
* Roy S.K., Khurdiya D.S. (1983-85). Zero energy cool chamber, IARI; JIRCAS JARQ 46(3):257 on tomato and eggplant.
* Basediya A.L., Samuel D.V.K., Beera V. (2013). Evaporative cooling system for storage of fruits and vegetables: a review. J. Food Sci. Technol. 50(3):429-442.
* Lufu R. et al. (2025). Evaporative cooling systems for perishables in Sub-Saharan Africa: a review. J. Food Process Engineering.
* Assessment of a solar-powered evaporative cooler for rural storage, South Gondar, Ethiopia (Int. J. Refrigeration, 2025).
* Comparison on cooling efficiency of cooling pad materials (jute, luffa, date palm, activated-carbon foam), 2018; Performance analysis of a sustainable coconut-coir pad, Int. J. Sustainable Engineering, 2008; wood wool vs CELdek vs khus pads.
* Acedo A.L. (1997). Improving quality and shelf-life of vegetables and fruits by evaporative cooling storage. Philippine Technology Journal 22(4):71-75.
* PhilMech (2008). Evaporative coolers prolong shelf-life of veggies (charcoal-pad display and cabinet coolers).
* UPLB UKDR etd-undergrad/222: two-stage evaporative cooler for tomato; UP Mindanao brick-walled evaporative cooler study.
* PAGASA (1991-2020 climatological normals; national mean RH 71 % in March to 85 % in September; May warmest month).
