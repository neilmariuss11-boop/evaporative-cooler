# Patent landscape: small evaporative coolers for fresh produce

Status: screening-level search, 30 Sep 2026.
Purpose: identify designs and claimed features that a small, student-scale evaporative cooler for postharvest storage should steer clear of, and confirm which building blocks are free to use.

## How this search was done, and its limits

Espacenet (`worldwide.espacenet.com`) and Google Patents (`patents.google.com`) could not be opened from this session because the environment's network policy blocks both hosts. The results below come from web-search snippets of those databases plus the USPTO full-text server, which was reachable. That means:

* Publication numbers, titles, applicants and the gist of the main claim are reliable.
* Full claim text and current legal status (in force, lapsed, expired) were **not** read directly. Before the design is finalised, each entry marked "verify" must be opened in Espacenet and its INPADOC legal status checked. Ready-made Espacenet queries are at the end of this file.

## Two different questions the search answers

1. **Freedom to operate.** A patent only restricts making, using or selling in the country where it was granted and is still in force. For a project built and used in the Philippines, only Philippine patents and utility models (IPOPHL) and PCT applications that entered the Philippine national phase matter. Foreign patents that were never filed in the Philippines do not restrict you.
2. **Novelty of your own design.** If the thesis claims a "new" design, or if you later file a Philippine utility model, everything published anywhere counts as prior art: granted patents, expired patents, applications, journal papers, PhilMech bulletins and student theses.

Most of the entries below matter for question 2, not question 1.

## Building blocks that are free to use

The basic direct evaporative cooler (wetted pad, fan pulling ambient air through the pad, pump and sump recirculating water, insulated storage chamber) has been in the patent literature since the 1900s and every foundational patent is long expired. Examples found: US1293005 (1919, food cooler), US1551709 (1925, evaporation refrigerator), US2913883 (1959), US2966046 (1960, combined evaporative cooler and ice box), US3324786 (1967, grape field cooler with excelsior pads). A student cabinet built from a commodity fan, aquarium pump, natural-fibre pad and an insulated box infringes nothing.

The same holds for the classic passive designs: the pot-in-pot or zeer (used since antiquity, popularised by Mohammed Bah Abba in the 1990s, never patented in a way that survives), the IARI brick Zero Energy Cool Chamber (Roy and Khurdiya, 1983-85, published openly), the Kenyan charcoal cooler, and the MIT D-Lab forced-air brick chamber, which MIT explicitly chose not to patent and released as an open design.

## Patents and applications to steer clear of

Listed from most to least relevant to a small produce cooler. "Term" is the nominal expiry assuming maintenance fees are paid (US: 20 years from filing; CN utility model: 10 years from filing).

| No. | Publication | Applicant / title | What is claimed (gist) | Term | Relevance to us |
|----|-------------|-------------------|------------------------|------|-----------------|
| 1 | US 10,907,878 B2 (also US 2019/0219321 A1) | Evaptainers LLC, "Electricity free portable evaporative cooling device" | A collapsible housing whose walls combine an insulative layer and an evaporative surface built from an inner fabric layer plus a membrane fabric layer; deployable between collapsed and expanded states; door for access. | to ~2039 (verify) | **High.** Do not build a collapsible or soft-walled cooler whose walls are a wicking-fabric/membrane laminate. Rigid walls with a separate pad are outside these claims. |
| 2 | CN 211430869 U | "Non-refrigeration type fresh-keeping device" (utility model, 2020) | Small non-refrigerated fresh-keeping box; details not read. | to ~2030 (verify) | **Medium.** Chinese utility model only; no effect in the Philippines, but read the claims before claiming novelty for any box-with-humidifier layout. |
| 3 | CN 116772497 A | "Fruit and vegetable refrigeration fresh-keeping device" (application, 2023) | Refrigerated chamber plus a wet-film humidifier with water tray and adjacent fan for humidity control. | pending | Low. Combines mechanical refrigeration with evaporative humidification. Avoid pairing a compressor or Peltier stage with a wet-film humidifier if you want clear separation. |
| 4 | US 9,310,134 | "Wetting of evaporative cooler pads" (2016) | Specific pad-wetting distribution arrangement. | to ~2033 (verify) | Low-medium. Use a plain perforated drip pipe or gravity trough over the pad, which is decades-old prior art, and do not copy any unusual distributor geometry. |
| 5 | US 2014/0174116 A1, WO 2015/199676 A1 | "Evaporation cooler and pad" | Internal fan blowing already-cooled, humidified air over the sump surface before water goes to the pads, to pre-cool the water. | check grant status | Low-medium. Do not add a sump-air pre-cooling loop. |
| 6 | US 10,113,758 and US 10,830,463 | Rex A. Eiserer, "Evaporative cooler" | Residential/portable swamp-cooler construction details. | to ~2036 (verify) | Low. Building-cooling product; check only if you copy any specific cabinet or louvre construction. |
| 7 | US 11,604,000 | "Evaporative cooler" (2023 grant) | Not read. | to ~2040 (verify) | Low, but open it in Espacenet: it is a recent US grant with our exact title. |
| 8 | US 10,759,589 | "Container for storing moisture level-sensitive products" (priority AT 2015) | Container with humidity-regulating construction for moisture-sensitive goods. | to ~2036 | Low. Not an evaporative cooler; noted because "humidity-controlled produce container" claims overlap the humidity side of our design. |
| 9 | IN 201931002973 (application) | Saptkrishi Scientific, "Sabjikothi / Preservator" | Isolated chamber with high-humidity, sterile microclimate; 20 W; IoT control. | pending | Low in the Philippines; **medium for novelty** if you add ozone/UV sterilisation or IoT control to a humid chamber. |
| 10 | Maisotsenko / Coolerado family, e.g. US 6,581,402; US 6,705,096; US 7,197,887; US 8,613,839; US 10,739,079; US 12,504,181 | Dew-point (M-cycle) indirect evaporative coolers | Plate heat-exchanger arrangements where part of the product air is diverted to the wet channels to approach the dew point. | many expired, newer ones in force to ~2040 | **High if you go indirect/two-stage.** A single-stage direct cooler is unaffected. If a two-stage (indirect + direct) unit is chosen, use a plain cross-flow indirect stage with a separate scavenger fan and no regenerative dew-point channel. |
| 11 | JP H06-14702 A | Method for cooling produce in a cold, humid state | Process claim, 1994. | expired | Prior art only. |
| 12 | CN 203810830 U, CN 2342600 Y, CN 2855946 Y | Chinese automatic cold store / wet-curtain preserving equipment | Wet curtain plus mechanical refrigeration. | expired | Prior art only. |
| 13 | Wakati (Arne Pauwels, Belgium) | Solar-ventilated humidity tent, 3 W PV fan, ~150 kg | Commercial product; no patent number located in this search. | unknown | **Verify on Espacenet by applicant name "Pauwels" and "Wakati".** Do not copy the tent-plus-ultrasonic/evaporative humidifier layout without checking. |

### Features to avoid, in one list

* Collapsible or fabric-walled housings where the wall itself is the evaporator (Evaptainers).
* Multilayer wicking fabric plus vapour-permeable membrane laminates as walls (Evaptainers "PhaseTek").
* Dew-point / M-cycle regenerative indirect stages (Coolerado family).
* Pre-cooling the sump water with recirculated chamber air (US 2014/0174116).
* Novel pad-wetting distributors beyond a drip pipe, trough or spray bar (US 9,310,134).
* Sealed humid chamber combined with sterilisation and IoT control marketed as a "preservator" (Sabjikothi, for novelty only).
* Any compressor or Peltier stage combined with a wet-film humidifier (CN 116772497 A, for novelty only).

## Philippine prior art (matters for novelty, and possibly for IPOPHL utility models)

* Acedo, A. L. (1997). Two simple evaporative coolers using **jute bag** and **rice husk** pads. Philippine Technology Journal 22(4): 71-75 (also indexed in HERDIN).
* PhilMech (2008 onward): display-type (50-80 kg) and cabinet-type (240-400 kg) evaporative coolers with a **charcoal pad**, water reservoir, submersible pump, fan and storage chamber; tested on eggplant, ampalaya, tomato, cucumber, calamansi, pepper, beans, cabbage and pechay.
* UPLB OVCRE listing: "Evaporative cooling pad for high-humidity storage of fruits and vegetables".
* UPLB undergraduate thesis: two-stage evaporative cooler for short-term tomato storage (UKDR etd-undergrad/222).
* UP Mindanao: brick-walled evaporative cooler, 61.8 % marketable fruit after 49 days vs 23.3 % ambient.
* Central Philippine University repository: evaporative cooler for agricultural produce.

Whether PhilMech or UPLB registered any of these as IPOPHL utility models was not determinable from here. Search IPOPHL's database (via WIPO Patentscope, country filter PH) for applicant "PhilMech", "Philippine Center for Postharvest Development and Mechanization", "University of the Philippines" with keywords "evaporative".

## Ready-made Espacenet queries

Open `https://worldwide.espacenet.com/patent/search` and paste one query at a time into the Advanced search box.

```
# 1. Title/abstract: evaporative + produce storage
(ta="evaporative cooler" OR ta="evaporative cooling") AND ta=(vegetable* OR fruit* OR produce OR perishable*)

# 2. Classification approach (more complete than keywords)
cpc=F25D7/00 AND ta=(vegetable* OR fruit* OR produce)          # refrigerators using evaporation, no vapour recovery
cpc=A23B7/04 AND ta=(evaporat*)                                 # preserving fruit/veg by cooling
cpc=F24F5/0035 AND ta=(storage OR container OR cabinet)         # direct evaporative cooling apparatus
cpc=F24F6/04 AND ta=(fruit* OR vegetable*)                      # evaporative humidifiers
cpc=B65D81/18 AND ta=(evaporat*)                                # containers with cooling means

# 3. Named risks to check legal status
pn=US10907878 OR pn=US2019219321 OR pn=CN211430869U OR pn=US11604000 OR pn=US9310134 OR pn=US10830463 OR pn=US10113758 OR pn=WO2015199676
pa=Evaptainers OR pa=Saptkrishi OR pa=Wakati OR pa=Pauwels

# 4. Philippine filings only
ctr=PH AND ta=(evaporat* AND (cool* OR chamber OR storage))
```

For each hit: open the record, click "Legal status" (INPADOC), and note whether it is in force and in which countries.

## Sources consulted

* USPTO full text: US 10,907,878; US 2019/0219321 A1 (Evaptainers).
* Google Patents index entries: US7014174B2, US20140174116A1, WO2015199676A1, US9310134, CN116772497A, CN211430869U, CN203810830U, CN2342600Y, CN2855946Y, JPH0614702A, US6581402B2, US6705096B2, US10739079, US12504181, US10759589, US1293005A, US1551709A, US2913883, US2966046A, US3324786A.
* MIT News (19 Jul 2023): D-Lab chose not to patent the forced-air evaporative cooling chamber and published it open-source.
* AGNIi / Saptkrishi: Indian application 201931002973.
* PhilMech news release "Evaporative coolers prolong shelf-life of veggies" (2008); HERDIN record for Acedo (1997).
* Engineering for Change product pages: Evaptainers EV-8, Wakati One, Zeer pot, Evaporative cooling chambers.
