# Synthesis of related literature behind the design

How the evidence led to the design of concept Option B - Scale: a small, active, single-stage evaporative cooling cabinet with a 150 mm cellulose honeycomb pad, a 12-17 kg chamber, a battery-backed 12 V supply, and a built-in scale under the produce crate.

Status: 1 Oct 2026. Written for the project's Review of Related Literature (RRL) and design-rationale chapters.

## How to use this document

* Each section takes one design question, summarises what the literature says, states the decision, and notes the economic side.
* Numbers marked (calc) come from this project's psychrometric calculator (`tools/psychro_design.py`), not from the literature.
* Sources were gathered through web search of journal pages, patent records and Philippine institutional sites; most were read as abstracts or summaries, not full text. Every citation marked **[verify]** needs its full text or full bibliographic details checked before it goes into the thesis. The reference list in section 12 shows what is still missing.
* Costs are 2026 Metro Manila estimates from `05-systems-and-protocol.md` section 7, ±30 %. Where an economic figure rests on an assumption, the assumption is stated.

## 1. The problem: postharvest loss and why evaporative cooling

Fresh fruits and vegetables keep respiring and losing water after harvest, and both processes speed up with temperature. Reviews of low-cost storage agree that evaporative cooling is the most economical way to lower temperature and raise humidity where refrigeration is unaffordable or unreliable (Basediya et al., 2013; Ndukwu & Manuwa, 2014 [verify]; Lufu et al., 2025 [verify]). Reported product temperature reductions are typically 3-10 °C, with relative humidity of 70-100 % inside the cooler (Ndukwu & Manuwa, 2014 [verify]).

Field results show the effect on losses:
* A passive cooling blanket tested in Kenya ran at about 70 % daytime cooling efficiency and cut postharvest losses by up to 45 % (Energy for Sustainable Development, 2025 [verify authors]).
* A brick-walled evaporative cooler studied at the University of the Philippines Mindanao kept 61.8 % of fruit marketable after 49 days, against 23.3 % at ambient [verify source].
* Zero-energy cool chambers roughly doubled tomato shelf life in South Asian trials (Islam & Morimoto, 2012 [verify]).

Philippine work goes back decades. Acedo (1997) built simple coolers with jute-bag and rice-husk pads. PhilMech (2008) developed charcoal-pad display coolers of 50-80 kg and cabinet coolers of 240-400 kg that kept vegetables fresh for 3-4 extra days.

**Design consequence:** an evaporative cooler is the right technology class for a low-cost student unit in the Philippines. The open questions were which type, which pad, what size, and how to make it stand out.

## 2. Climate limit: what an evaporative cooler can achieve in the Philippines

No direct evaporative cooler can cool air below the ambient wet-bulb temperature. The useful measure for a site is the wet-bulb depression, the gap between dry-bulb and wet-bulb temperature. Defraeye et al. (2023) built design charts and maps from this quantity and found passive coolers add up to about 7 days of postharvest life where the depression is large. They warned that deploying coolers where cooling potential is small makes users lose trust in the technology. MIT D-Lab's best-practice guide gives the same advice: assess the local climate before choosing evaporative cooling (Verploegen et al., 2018).

Philippine conditions are humid. National mean relative humidity ranges from about 71 % in March to 85 % in September, and May is the warmest month (PAGASA, 1991-2020 normals). The project's calculations translate that into cooling potential:

| Condition | Wet-bulb depression (calc) |
|-----------|---------------------------:|
| Hot dry-season afternoon, 34 °C and 55 % | 7.7 K |
| Typical dry-season afternoon, 33 °C and 62 % | 6.2 K |
| Wet-season afternoon, 31 °C and 78 % | 3.3 K |
| Rainy day, 28 °C and 90 % | 1.4 K |

The literature on what drives quality loss makes humidity as important as temperature in this climate. Water loss depends on the vapour pressure deficit between produce and air, and lowering it sharply reduces transpiration (Zhang et al., 2017 [verify], greenhouse tomato). Wakati, a commercial produce tent, is built entirely on this point: it keeps produce in near-saturated air rather than cooling it (Wakati product reports, 2015).

**Design consequences:**
* The cooler is framed as "temperature reduction and humidity control", not refrigeration. In the wet season it works mainly as a humidity chamber.
* "High efficiency" is defined as getting as close as possible to the wet-bulb floor, measured as saturation efficiency, because absolute temperature depends on the weather on test day.
* The controller distinguishes dry and humid weather, because the benefit of running fans and pump changes with the depression.

## 3. Choice of cooler type

| Type | Evidence | Strengths | Weaknesses for this project |
|------|----------|-----------|-----------------------------|
| Pot-in-pot (zeer) | Long traditional use; heat and mass transport modelled by MIT (2020); evaluated in Mali by MIT D-Lab (2018) | Cheapest, no power | Small; performance collapses in humid air; little engineering content |
| Brick zero-energy cool chamber | Roy & Khurdiya, IARI (1983-85); temperature drops of 6-10 °C and efficiencies near 88-89 % reported in India [verify]; UP Mindanao brick cooler result above | Proven, no power | Heavy and static; results come mostly from drier climates |
| Charcoal cooler or charcoal blanket | Defraeye et al. (2024): about 5 °C below ambient in the lab, scalable, local materials; Kenya field trials 2025 | Cheap, scalable | Passive airflow gives modest, weather-dependent results |
| Active direct cooler (fan, pump, pad, cabinet) | Cooling efficiencies of 63-98 % reported across tropical studies [verify individual studies]; PhilMech cabinets; solar-powered versions in Nigeria and Ethiopia (2025) | Controllable airflow, highest efficiency per size, can be instrumented | Needs power, pump and fan |
| Two-stage (indirect plus direct) | Reported efficiencies of 88-96 % (Heliyon, 2020 [verify]); UPLB undergraduate thesis on a two-stage tomato cooler | 1.5-2 K colder than single-stage on dry afternoons (calc) | Twice the parts; under 1 K gain in the wet season (calc) |
| Dew-point (Maisotsenko-cycle) indirect | Coolerado patent family, US 6,581,402 onward | Coldest evaporative option, approaching the dew point | Hard to build in a school shop; patented |

**Decision:** active, single-stage direct cooler. It gives the highest efficiency that can be built, measured and controlled at student scale, which matched the owner's priority of application over novelty. The two-stage option was rejected because its gain is small in humid weather, it costs a second fan and a heat exchanger, and it sits next to the dew-point patents.

**Economics:** a single-stage active cabinet costs about PHP 23,400 complete, including the battery and the scale (section 10). A two-stage unit would add a second fan, a fabricated plate heat exchanger and extra ducting, which is roughly PHP 2,000-4,000 more by this project's estimate, for a gain of about 1 K in the wet season.

## 4. Pad media: why cellulose honeycomb instead of coconut coir or other local fibres

This was the most consequential decision, and the most open to debate, so the evidence is set out in full.

### 4.1 What the studies report

| Medium | Reported performance | Durability findings | Source |
|--------|---------------------|---------------------|--------|
| Cellulose honeycomb (CELdek 7090 type) | Benchmark material. About 78-80 % saturation efficiency at typical air speeds in comparison studies; manufacturer curves for 150 mm depth give the high 80s % at about 1 m/s, rising at lower speeds | Rigid, resin-impregnated; lasts years with cleaning; efficiency falls with age and scaling | Munters product sheet [verify values]; cellulose-pad ageing tested in a wind tunnel (Franco-Salas et al., 2019 [verify]); water-flow effects on cellulose pads (Franco et al., 2010 [verify]) |
| Coconut coir | 53.6 % cooling efficiency at optimal wettability, slightly below CELdek 7090 (Cogent Engineering, 2024 [verify]); about 50 % for a coir-based pad against 47 % for a commercial paper pad in one test (Engineering Proceedings, 2025 [verify]); 53.5 % mean saturation effectiveness against 64 % for cedar and teak in another comparison [verify source] | No long-term mould or degradation study found | Int. J. Sustainable Engineering (2008) [verify authors] |
| Jute | 62.1 % at 2.4 m/s, the best of three local fibres tested | **Fastest deterioration** of the three | Al-Sulaiman (2002) |
| Luffa | 55.1 % at 2.4 m/s; one study reports 78.5 %, above CELdek's 75.6 % under the same conditions | **Most durable**, highest mould resistance of the three | Al-Sulaiman (2002); Modern Applied Science (2012) [verify] |
| Date palm fibre | 38.9 % at 2.4 m/s | | Al-Sulaiman (2002) |
| Lump charcoal | Charcoal-pad chambers reduced temperature 6.0-10.2 °C at about 87.8 % efficiency [verify]; a charcoal-pad cooler ran 3-5 °C below ambient at about 85 % RH | Durable if kept clean; sheds fines | Innspub tomato study [verify]; Ndukwu & Manuwa (2014) [verify]; PhilMech (2008) |
| Rice straw, banana midrib, ramie, pineapple leaf fibre | Rice straw 63-77 % (Darwesh et al. [verify]); banana midrib and ramie about 45 %; pineapple leaf fibre up to 85 % wet-bulb effectiveness in an indirect cooler | Not studied long term | Heliyon (2022) [verify]; banana/ramie study [verify] |

Two findings from this literature shaped the decision more than any single number:

1. **Air speed matters more than material.** Most natural-fibre results were measured at 1-2.5 m/s, where efficiency drops sharply. At low face velocity, under about 0.5 m/s, most wetted media reach much higher values. This design runs at 0.19 m/s, so any medium would perform better here than in the published tests. The ranking between media is less certain than the published numbers suggest.
2. **Durability separates the media more than initial efficiency does.** Jute starts high and degrades fastest. Luffa starts lower and lasts. Natural fibres in general mould and compact in continuously wet, warm conditions. Cellulose pads are made to run wet for years.

### 4.2 Effect on the cooler's performance

Using the efficiency each medium can plausibly reach at this design's low air speed:

| Medium (assumed efficiency) | Pad outlet, 34 °C / 55 % | Chamber, 34 °C / 55 % | Chamber RH |
|-----------------------------|-------------------------:|----------------------:|-----------:|
| Coconut coir (65 %) | 29.0 °C | 29.3 °C | 81 % |
| Lump charcoal (85 %) | 27.5 °C | 27.7 °C | 91 % |
| Cellulose 7090 (90 %) | 27.1 °C | 27.3 °C | 94 % |

(calc; airflow 100 m³/h, steady load 8 W)

Cellulose keeps the chamber about 2 K cooler and 13 percentage points more humid than coir. Respiration rate roughly doubles to triples for every 10 K rise (Q10 of 2-3; Kader, 2002 [verify]), which works out to about 7-12 % faster respiration for each extra kelvin. The 2 K difference therefore means roughly 15-25 % faster deterioration with coir, plus faster water loss from the drier air.

### 4.3 Economic comparison

| Medium | Upfront cost per pad | Expected life | Annual media cost | Notes |
|--------|---------------------:|---------------|------------------:|-------|
| Cellulose 7090 | about PHP 500 (one PHP 2,500 sheet, 600 × 1,500 mm, cuts into five 500 × 300 pads) | 2-3 years with cleaning (assumed from manufacturer guidance) | PHP 170-250 | Spare pads come from the same sheet |
| Coconut coir | about PHP 150 per fill | 4-8 weeks before mould or compaction (assumption; no published long-term data) | PHP 1,000-2,000, plus refill labour | Cheapest to start, dearest to run |
| Lump charcoal | about PHP 150 per 5 kg | Long if washed | PHP 300-600 (washing losses, replacement of fines) | Wet cassette weighs roughly 10 kg against about 2-3 kg for cellulose (project estimate) |
| Jute | about PHP 90 per set | Weeks (fastest degradation) | PHP 800-1,500 | |

Over a three-year life, cellulose costs less in media than coir or jute despite the higher first cost. It also avoids the labour and downtime of frequent repacking, which matters for a unit meant to be used by vendors.

### 4.4 Decision matrix

Scores from 1 (worst) to 5 (best), weighted by the project's priorities: efficiency first, then durability and cost.

| Criterion (weight) | Cellulose 7090 | Lump charcoal | Luffa | Jute | Coconut coir |
|--------------------|---:|---:|---:|---:|---:|
| Cooling efficiency (30 %) | 5 | 4 | 3 | 3 | 2 |
| Durability and maintenance (20 %) | 5 | 4 | 4 | 1 | 2 |
| Annual cost (15 %) | 4 | 4 | 3 | 3 | 3 |
| Upfront cost (10 %) | 2 | 5 | 4 | 5 | 5 |
| Availability in the Philippines (10 %) | 4 | 5 | 3 | 5 | 5 |
| Low air resistance, fan energy (10 %) | 5 | 3 | 4 | 4 | 3 |
| Hygiene and handling (5 %) | 4 | 2 | 3 | 2 | 2 |
| **Weighted score** | **4.40** | **4.00** | **3.40** | **3.05** | **2.85** |

**Sensitivity:** if upfront cost is weighted as heavily as efficiency (30 % each, durability 10 %), lump charcoal comes first (4.20) and cellulose falls to 3.80. Charcoal is therefore the credible alternative, and the thesis should say so. Cellulose was kept because the owner's stated priority was efficiency and practical use, and because charcoal is heavy, sheds dust into the sump and pump, and is what PhilMech already used in 2008.

**Decision:** cellulose honeycomb 7090, 150 mm deep, sized for a low face velocity of 0.19 m/s.

## 5. Pad geometry, airflow and water distribution

* **Depth and face velocity.** Saturation efficiency rises with pad depth and falls with air speed (Munters product data [verify]; review of optimal pad operation, Renewable and Sustainable Energy Reviews, 2021 [verify]). Decision: 150 mm depth, 500 × 300 mm face, 100 m³/h, giving 0.19 m/s and under 5 Pa pressure drop. This lets two small 12 V fans do the job.
* **Wetting rate.** Cellulose pad studies show efficiency rises with water flow up to a point, then falls when excess water films the pad face (Franco et al., 2010 [verify]). Decision: a trim valve set at commissioning until the whole face is wet with no streaming. A distribution cap spreads water across the full 150 mm depth, the method used in commercial pad systems.
* **Intermittent wetting.** Pulsing the pump can lower outlet temperature and save energy compared with continuous wetting (Int. Comm. Heat Mass Transfer, 2021 [verify]). A regenerative cooler study cut pump power by 32.3 % with a 2 minutes on, 60 minutes off cycle (Int. J. Refrigeration, 2025 [verify]). Decision: pulsed wetting, 2 minutes on and 3 minutes off by default, tuned at commissioning.
* **Pull-through, once-through air.** Fans exhaust from the chamber so the pad is the only air inlet, and no chamber air is recirculated to the pad. Recirculation would raise pad-inlet humidity, and one form of it is patented (US 2014/0174116).

## 6. Chamber size, layout and insulation

* **Size.** PhilMech's smallest cooler holds 50-80 kg. The owner set the student unit at half of a first 25-35 kg concept: 12-17 kg in one standard market crate plus a shelf. That is enough produce for storage trials when repeated three times per season.
* **Insulation.** Every watt of heat leaking in raises the chamber above the pad-outlet temperature. 50 mm EPS limits steady wall gain to about 4 W, so the chamber stays within 0.3 K of the pad outlet at steady load (calc).
* **Rigid walls.** Fabric-walled evaporative containers are covered by the Evaptainers patent (US 10,907,878). The rigid plywood and EPS cabinet avoids it and is easier to build.

## 7. Control, instrumentation and the manual override

Microcontroller-controlled produce coolers are well established. Examples include an automated electronic evaporative cooler (2017) and an AVR-based temperature and humidity controller [verify]. A 2026 systematic review of intelligent evaporative cooling for postharvest storage covers sensing, control and machine-learning approaches (AgriEngineering 8(4):150 [verify authors]). The same review identifies maintenance access, and the ability of farmers to diagnose faults without expert help, as a key deployment problem.

**Decisions:**
* Three temperature and humidity sensors (ambient, pad outlet, chamber) so that pad efficiency and chamber efficiency can be measured continuously, the numbers the project competes on.
* Mode switching on wet-bulb depression, presented as good practice, not as novelty, because similar control exists in the literature and in patents (US 2022/0026095; US 10,145,572).
* An AUTO / OFF / MANUAL switch, in direct response to the maintenance problem raised in the review: if the electronics fail, the cooler still runs.

## 8. Power supply

The literature on off-grid coolers favours solar (Nigeria; Ethiopia, 2025). For this unit the owner chose a wall adapter with a backup battery. The cooler averages about 8.5 W in dry weather (calc). A 12 V 12 Ah battery carries it for 8-12 hours through brownouts, at much lower cost than the 80 W solar array the same load would need. Energy cost on mains is about 73 kWh a year, roughly PHP 900 at an assumed PHP 12 per kWh.

## 9. The novelty: a cooler that weighs its own produce

The screening search (`06-software-novelty-options.md`) found that most software ideas for evaporative coolers already exist:
* weather-adaptive control;
* pump pulsing;
* pad-replacement alerts (patented in US 10,260,418);
* forecast-based pre-cooling;
* shelf-life digital twins delivered by smartphone (Shrivastava et al., 2022);
* IoT tomato shelf-life monitoring (2026).

The search found no evaporative produce cooler that uses the measured weight of its own produce. The closest analogue is load-cell control of spray chilling for meat carcasses (US 10,226,054).

The supporting literature:
* Water loss is a main cause of lost marketability. Commonly cited limits are about 7 % weight loss for tomato and 3-5 % for leafy greens (Robinson et al., 1975 [verify]).
* Water loss is driven by the vapour pressure deficit (Zhang et al., 2017 [verify]).
* Produce is sold by weight, so every gram of water lost is money lost.

**Decision:** a single sealed 30 kg load cell under the crate (the "sentinel crate"). The controller fits each batch's drying rate, shows weight lost, days left and kilograms saved versus shelf storage, and adjusts its effort to a weight-loss budget.

**Economics:** the scale adds about PHP 2,600, about 11 % of the unit cost. A sealed load cell was chosen over a PHP 300 unsealed one because the chamber stays at 90-95 % humidity.

## 10. Overall economics

Cost by subsystem, from the bill of materials:

| Subsystem | Approx. PHP | Share |
|-----------|------------:|------:|
| Cabinet, insulation, door, base and casters | 6,250 | 27 % |
| Pad, cassette, water system | 5,900 | 25 % |
| Fans, hood, louver, screens | 1,100 | 5 % |
| Controller, sensors, display, wiring | 3,170 | 14 % |
| Power: adapter, battery, charge module | 2,400 | 10 % |
| Sentinel-crate scale | 2,600 | 11 % |
| Crates, shelf, finishing | 2,000 | 9 % |
| **Total** | **about 23,400** | 100 % (shares rounded) |

An illustrative payback, with every input an assumption to be replaced by trial data:
* 15 kg per batch, 5-day batches, about 70 batches a year;
* produce worth PHP 80 per kg;
* the cooler saves 20 % of each batch from spoilage. This is in line with the 45 % loss reduction in Kenya and the 38-point marketability gain at UP Mindanao.

That gives about PHP 240 per batch, or PHP 16,800 a year, against running costs under PHP 1,500 a year for power and pads. Payback would be about one and a half years. Weight-loss savings alone (about 3 % of 15 kg per batch) would be worth only about PHP 2,500 a year. The economic case therefore rests on reducing spoilage, which the storage trial must measure.

## 11. Gaps and limitations of this synthesis

* Most sources were read as abstracts or search summaries. The **[verify]** items need full-text checking, especially the numbers in sections 4.1 and 5.
* No published study measures coconut coir or cellulose pads over months of continuous use in a humid tropical climate. The durability ranking relies on related fibres and manufacturer guidance.
* Pad efficiencies in section 4.2 are assumed values at this design's low air speed. The commissioning test will replace them with measurements.
* The novelty search was web-only. Espacenet, Google Scholar and the IPOPHL database must be searched with the queries in `06-software-novelty-options.md` before a novelty claim is made.
* The payback estimate in section 10 is illustrative; the storage trial supplies the real numbers.

## 12. References

Citations marked [verify] are incomplete or were not read in full.

* Acedo, A. L. (1997). Improving quality and shelf-life of vegetables and fruits by evaporative cooling storage. *Philippine Technology Journal*, 22(4), 71-75.
* Al-Sulaiman, F. (2002). Evaluation of the performance of local fibers in evaporative cooling. *Energy Conversion and Management*, 43(16), 2267-2273. [verify volume and pages]
* Basediya, A. L., Samuel, D. V. K., & Beera, V. (2013). Evaporative cooling system for storage of fruits and vegetables: a review. *Journal of Food Science and Technology*, 50(3), 429-442.
* Defraeye, T., et al. (2023). Passive evaporative coolers for postharvest storage of fruit and vegetables: where to best deploy them and how well do they perform. *Frontiers in Food Science and Technology*, 3, 1100181. [verify author list]
* Defraeye, T., Schudel, S., Shrivastava, C., Motmans, T., Umani, K., Crenna, E., Shoji, K., & Onwude, D. (2024). The charcoal cooling blanket: a scalable, simple, self-supporting evaporative cooling device for preserving fresh foods. *Biosystems Engineering*, 238, 128-142.
* Enhancing postharvest storage in low- and middle-income countries: evaluation of the passive evaporative cooling blanket for fruits and vegetables. (2025). *Energy for Sustainable Development*. [verify authors, volume]
* Franco, A., Valera, D. L., Madueño, A., & Peña, A. (2010). Influence of water and air flow on the performance of cellulose evaporative cooling pads used in Mediterranean greenhouses. *Transactions of the ASABE*, 53(2), 565-576. [verify]
* Franco-Salas, A., et al. (2019). Refrigeration capacity and effect of ageing on the operation of cellulose evaporative cooling pads, by wind tunnel analysis. PMC6926749. [verify journal and authors]
* Increasing evaporative cooler efficiency by controlling water pump run and off times. (2021). *International Communications in Heat and Mass Transfer*. [verify authors, volume]
* Intelligent evaporative cooling systems for post-harvest fruit and vegetable preservation: a systematic literature review. (2026). *AgriEngineering*, 8(4), 150. [verify authors]
* Islam, M. P., & Morimoto, T. (2012). Zero energy cool chamber for extending the shelf-life of tomato and eggplant. *Japan Agricultural Research Quarterly*, 46(3), 257-267. [verify]
* Kader, A. A. (Ed.). (2002). *Postharvest Technology of Horticultural Crops* (3rd ed.). University of California ANR Publication 3311. [verify Q10 figures]
* Lufu, R., et al. (2025). Evaporative cooling systems for perishables in Sub-Saharan Africa: a review. *Journal of Food Process Engineering*. [verify]
* MIT D-Lab. (2018). Evaluation of low-cost evaporative cooling devices in Mali. MIT News, 20 June 2018.
* MIT News. (2023). Addressing food insecurity in arid regions with an open-source evaporative cooling chamber design. 19 July 2023.
* Munters. CELdek 7090-15 evaporative cooling pad, product sheet. [verify efficiency values]
* Ndukwu, M. C., & Manuwa, S. I. (2014). Review of research and application of evaporative cooling in preservation of fresh agricultural produce. *International Journal of Agricultural and Biological Engineering*, 7(5), 85-102. [verify]
* PAGASA. Climatological normals 1991-2020 and Climate of the Philippines.
* Performance analysis of a new sustainable evaporative cooling pad made from coconut coir. (2008). *International Journal of Sustainable Engineering*. [verify authors]
* A comparative study of performance and energy efficiency in evaporative cooling: assessing different configurations of organic packings. (2024). *Cogent Engineering*, 11(1). [verify authors]
* Development and performance analysis of coconut coir waste-based recycle papers for cooling pad applications. (2025). *Engineering Proceedings*, 84, 18. [verify]
* Performance evaluation of an indirect air cooling system combined with evaporative cooling. (2020). *Heliyon*. [verify authors]
* Development of indirect evaporative cooler based on a finned heat pipe with a natural-fiber cooling pad. (2022). *Heliyon*. [verify authors]
* Experimental optimization of a regenerative indirect evaporative cooler: effects of working air ratio, pump control strategy, water temperature, and ambient conditions. (2025). *International Journal of Refrigeration*. [verify]
* Optimal operation of evaporative cooling pads: a review. (2021). *Renewable and Sustainable Energy Reviews*. [verify authors]
* PhilMech. (2008). Evaporative coolers prolong shelf-life of veggies. Philippine Center for Postharvest Development and Mechanization news release.
* Robinson, J. E., Browne, K. M., & Burton, W. G. (1975). Storage characteristics of some vegetables and soft fruits. *Annals of Applied Biology*, 81, 399-408. [verify weight-loss limits]
* Roy, S. K., & Khurdiya, D. S. (1983-1985). Zero energy cool chamber. Indian Agricultural Research Institute, New Delhi. [verify original publication]
* Shrivastava, C., Berry, T., Cronje, P., Schudel, S., & Defraeye, T. (2022). Digital twins enable the quantification of the trade-offs in maintaining citrus quality and marketability in the refrigerated supply chain. *Nature Food*, 3, 413-427. [verify]
* Verploegen, E., Rinker, P., & Ognakossan, K. E. (2018). *Evaporative Cooling Best Practices Guide*. MIT D-Lab.
* Zhang, D., et al. (2017). Vapour pressure deficit control in relation to water transport and water productivity in greenhouse tomato production during summer. *Scientific Reports*, 7, 43461. [verify author list]
* Patents: US 10,907,878 B2 (Evaptainers); US 6,581,402 B2 and related Maisotsenko-cycle patents (Coolerado); US 2014/0174116 A1; US 2022/0026095 A1; US 10,145,572 B2; US 10,260,418; US 10,226,054. Full list and Espacenet queries in `01-patent-landscape.md`.
* Unverified institutional sources: University of the Philippines Mindanao brick-walled evaporative cooler study; UPLB undergraduate thesis on a two-stage evaporative cooler for tomato (UKDR etd-undergrad/222); Wakati product reports (2015).
