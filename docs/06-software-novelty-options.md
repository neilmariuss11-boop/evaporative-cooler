# Device-level novelty through software: search results and options

Status: ideation and screening search, 30 Sep 2026. **Option 1 was chosen** and is in the design as concept Option B - Scale: geometry in `04-assembly-spec.md` group F, firmware in `05-systems-and-protocol.md` section 5.4. Final cost of the scale is about PHP 2,600 with a sealed load cell, not the PHP 600-900 first estimated below.

Goal set by the owner: a device-level novelty that is mostly software, so it adds little cost, and that serves the application rather than knowledge for its own sake.

## 1. Already taken: do not claim these

| Idea | Prior art found |
|------|-----------------|
| Switching modes on measured wet-bulb depression | Microcontroller produce coolers since 2017; US 2022/0026095 (wet and dry mode control); 2026 systematic review of intelligent evaporative cooling |
| Pump pulsing tuned by outlet-air temperature | 2021 study on controlling pump run and off times; 2025 regenerative cooler pump-cycling study |
| Alert when the pad needs replacing, from measured pad effectiveness | US 10,260,418 (media replacement timing from effectiveness). Also a patent risk: avoid |
| Forecasting ambient temperature to pre-cool the chamber | 2023 machine-learning pre-cooling study cited in the 2026 review |
| Shelf-life digital twin of the fruit | Empa (Defraeye group): physics-based twins delivered through a smartphone app for smallholders |
| IoT shelf-life monitoring of stored tomato | 2026 dew-computing tomato storage framework; several Arduino/ESP32 monitoring systems |
| Gas or multispectral freshness sensing | ML gas-sensor shelf-life estimators; multispectral ripening framework |
| Load-cell feedback to control product weight loss | US 9,339,042 and US 10,226,054 (carcass weight control) weigh selected carcasses and spray water until each returns to its starting weight. This is the **closest prior art**: the general idea of weighing a sample and adding moisture is taken. The sentinel crate differs in product, cooling principle, control target and learning; see `10-novelty-and-inventive-step.md` |

## 2. What looks open

The 2026 review notes that produce-specific vapour-pressure-deficit management needs multi-objective control that simple set-point controllers cannot provide. No system found makes **the produce's own measured weight loss** the controlled variable in an evaporative cooler. That is the gap the options below use.

Why weight loss: in a humid tropical climate the cooler can only take a few degrees off, so its main benefit is cutting water loss. Water loss is also money: produce is sold by the kilogram, and shrivelling makes it unsellable. Tomato is commonly given a marketability limit of about 7 % weight loss and leafy greens about 3-5 % (classic postharvest tables; confirm the figures for your chosen crop).

## 3. Options

### Option 1 (chosen): weight-loss budget control with a sentinel crate

**Hardware added.** The cooler's one standard crate becomes the "sentinel" and sits on a weighing platform: a single-point aluminium bar load cell (20-30 kg) with an HX711 amplifier. The amplifier lives in the dry electrical bay; the load cell is coated for humidity. Cost about PHP 600-900.

**What the software does.**
1. **Detects batches automatically.** A step change of more than 2 kg on the sentinel starts a new batch and records the starting mass. Removing produce for sale is detected the same way and re-baselines.
2. **Measures transpiration live.** Every 10 minutes it computes the filtered mass-loss rate, with drift correction from the chamber temperature.
3. **Calibrates itself to the batch.** It computes the driving force, the vapour pressure deficit at the produce surface: saturation pressure at pulp temperature minus the chamber vapour pressure. It then fits the batch's own transpiration coefficient, loss rate divided by that deficit. Every crop, variety and maturity gets its own value, learned on the spot instead of taken from a table.
4. **Manages a budget.** The operator picks the crop and the target storage days on the menu. The controller computes the allowed loss rate as the remaining margin to the crop limit divided by the days left. If the batch is losing weight faster, it escalates: full fans, longer wetting, shorter dry-out. If it is comfortably under budget, it backs off to save water and energy.
5. **Shows what matters to a vendor.** The display gives weight lost so far, projected days until the marketability limit, and **kilograms saved versus open-shelf storage**. The last figure comes from the same fitted coefficient applied to the ambient conditions the unit already measures. With a price entered, it shows pesos saved.

**Novelty statement (draft).** A small evaporative produce cooler whose controller manages a produce weight-loss budget. A load-cell sentinel crate measures transpiration in real time and self-calibrates a vapour-pressure-deficit model for the loaded batch. The controller adjusts fans and wetting to meet the budget with minimum water and energy, and reports projected days to the marketability limit and the weight saved against ambient storage.

**Why it serves the application.** It turns the cooler's hardest-to-see benefit in humid weather into a number a vendor understands. It also stops wasting water and fan energy when the produce doesn't need it.

**Risks.**
* Condensation on produce adds apparent weight. The SATURATED mode already prevents saturated air, and a step filter rejects sudden gains.
* Handling the sentinel crate disturbs the reading. Batch detection re-baselines on any step change.
* Load cells drift with temperature and humidity. Use temperature compensation, a coated cell, and a daily zero check when the crate is lifted.
* The sentinel is the crate, which holds most of the load; the shelf produce is not weighed by the cooler. During trials, weigh the shelf produce daily by hand to show whether the crate represents it.

### Option 2: software-only weight-loss budget ("virtual sentinel")

Same budget logic and display, but the transpiration coefficient comes from literature values per crop instead of a load cell. It costs nothing, but it is less accurate and weaker as novelty, because model-based shelf-life estimation is close to the Empa digital-twin work. It can be the fallback if the load cell proves unreliable.

### Option 3 (add-on): on-site suitability report

After a week of logging, the unit reports the local mean wet-bulb depression, the expected shelf-life gain for the chosen crop, and the hours when running it matters most. This is an on-device version of the published deployment maps. It is useful and cheap, but weak alone as novelty. It combines well with Option 1.

### Option 4 (add-on): sell-first advisor

Per-crate timers started by a button, ranking crates by accumulated heat and dryness exposure so the vendor sells the most at-risk crate first. This is first-expired-first-out, common in cold chains, so it is weak as novelty. It is a convenience feature only.

## 4. Before claiming novelty

The search behind this file used web-search results only; Espacenet and Google Patents are blocked in the environment where it was done. Before the group writes a novelty claim, run these searches in Google Scholar, Espacenet and the IPOPHL database:

```
("load cell" OR "weighing" OR "mass loss") AND ("evaporative cool*") AND (fruit* OR vegetable* OR produce)
("weight loss" OR "transpiration") AND ("control" OR "controller") AND ("evaporative cool*" OR "storage chamber") AND produce
("vapour pressure deficit" OR "vapor pressure deficit") AND ("evaporative cool*") AND (storage OR postharvest)
("shelf life" AND "load cell") AND (storage OR cooler)
```

Also read the independent claims of US 10,226,054 (carcass weight control), US 12,209,768 (systems and methods for evaporative cooling control) and US 12,474,070 (direct evaporative cooling with fan and water optimization) to confirm none covers a weight-based produce budget.
