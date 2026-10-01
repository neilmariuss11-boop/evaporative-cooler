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

**A fan-assisted, single-stage direct evaporative cooling cabinet, 12 V DC, with a 150 mm cellulose honeycomb pad, insulated rigid chamber, and a controller with a manual fallback.** The detailed design is in `03-design-decisions.md` (why), `04-assembly-spec.md` (geometry) and `05-systems-and-protocol.md` (systems, tests, bill of materials). This section only summarises it.

The first draft of this file recommended coconut coir and a research-oriented pad comparison. The project owner has since set the priority as application and cooling efficiency rather than novelty, so the pad changed to cellulose and the comparison was dropped.

Why this family and not the alternatives:

* Pot-in-pot: near-useless in humid air and too small for meaningful trials.
* Brick ZECC: proven but large, heavy and static.
* Two-stage (indirect plus direct): 1.5-2 K colder on dry afternoons, but double the parts and close to the dew-point cooler patent family.
* Fabric-walled portable: directly on top of the Evaptainers patent.
* Natural-fibre pads (coir, jute, charcoal): cheap, but 50-70 % efficient for coir and jute, and they need replacing within weeks.

### 2.1 Key numbers

| Item | Value |
|------|-------|
| Storage | 1 standard crate plus 1 slatted shelf, 12-17 kg, chamber 540 × 520 × 590 mm |
| Pad | cellulose 7090, 500 × 300 × 150 mm, face velocity 0.19 m/s |
| Airflow | 100 m³/h, two 120 mm 12 V PWM exhaust fans at about 65 % speed |
| Expected pad saturation efficiency | 90 % design value, 92-95 % likely |
| Chamber on a 33-34 °C dry-season afternoon | about 27.3-27.7 °C, 94-95 % RH (steady load) |
| Chamber on a wet-season afternoon | about 28.3 °C, 97 % RH |
| Water | 10 L sump, about 4-5.5 L/day in the dry season |
| Power | 15 V wall adapter plus 12 V 12 Ah backup battery; about 200 Wh/day in the dry season, 8-12 h on battery |
| Overall size | 820 × 892 × 920 mm on casters |
| Novelty feature | Sentinel crate: built-in scale under the crate tracks the produce's own weight loss |
| Cost | about PHP 24 500 including the backup battery and the scale |

### 2.2 How to present it

The group's case rests on efficiency and proof, not novelty: saturation efficiency near the physical limit, measured continuously over both seasons, plus a storage trial against ambient. Report efficiency, not only temperature drop, because efficiency removes the effect of the weather on test day and makes results comparable with other units.

## 3. Sources

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
