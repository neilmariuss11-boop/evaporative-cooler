# Systems, control logic, test protocol and bill of materials

Companion to `04-assembly-spec.md` (geometry) and `03-design-decisions.md` (why). This file covers what the parts do: air, water, heat, electrical, firmware behaviour, and how the unit will be tested. Numbers marked (calc) come from `tools/psychro_design.py` with the stated inputs.

## 1. Air system

**Path.** Ambient air enters the rear louver, passes the insect screen and a 31 mm gap, flows through the 75 mm coir pad from back to front, enters the chamber through the 500 × 400 mm opening in the back wall, moves forward through the vented crates and the 90 mm plenums, rises in the front plenum, and leaves through two roof fans under the rain hood, exiting sideways through the hood end slots. Once-through, no recirculation.

| Parameter | Value | Basis |
|-----------|-------|-------|
| Design airflow | 120 m³/h (0.033 m³/s) | Holds the chamber within 1.5 K of pad-outlet air at a 60 W transient load (calc) |
| Pad face area | 0.20 m² (500 × 400) | |
| Pad face velocity | 0.17 m/s | Pad literature: efficiency 80-90 % below 1 m/s |
| Air residence time in pad | about 0.45 s | 75 mm / 0.17 m/s |
| Expected saturation efficiency, coir | 75-85 % | Extrapolated from coir tests at 1-2 m/s (53-70 %) to this low velocity; **to be measured** |
| Pad pressure drop, estimated | 5-12 Pa | Loose coir at 0.17 m/s; measure with a manometer during commissioning |
| Screen, louver, crate and hood losses | 5-10 Pa | |
| Fan operating point | 2 × 60-70 m³/h at 15-20 Pa | Typical 120 mm 12 V fan: 100-110 m³/h free air, 30-40 Pa stall |
| Chamber air changes | about 470 per hour | 120 / 0.253 |

Fans are 4-pin PWM types so the ESP32 can run them at 30-100 % without a power MOSFET switching the 12 V supply; a MOSFET is still used as an on/off enable. Measure the actual fan curve against the installed pad before locking the PWM levels in firmware.

## 2. Water system

**Circuit.** Sump (8 L working) → submersible pump → 8 mm hose with trim valve → drip pipe over the cassette → coir → gravity return into the open-top sump. No drain tray: the sump covers the cassette footprint.

| Parameter | Value | Basis |
|-----------|-------|-------|
| Pump | 12 V DC submersible, 3-5 W, 240 L/h at 0 m, about 150 L/h at 0.7 m head | |
| Wetting rate needed | 1-2 L/min over 0.52 m pad width | Enough to keep coir saturated; more only splashes |
| Pump duty, DRY mode | 60 s on / 180 s off (25 %) | Coir holds water well; tune during commissioning |
| Pump duty, HUMID mode | 30 s on / 300 s off (9 %) | |
| Evaporation, dry-season afternoon | 6-8 L/day continuous (calc: 34 °C/55 % gives 8.3 L/day at 120 m³/h) | |
| Evaporation, wet season | 1.5-3.5 L/day (calc) | |
| Sump working volume | 8 L at 125 mm; overflow at 148 mm (9.6 L) | One to two days between refills |
| Low-level cut-out | float switch at 40 mm (about 2.5 L left) | Protects the pump; display shows "FILL" |
| Fill | 40 mm capped port on the rear panel; sight tube with 0-9 L scale | |

**Hygiene.** Drain and scrub the sump weekly; add 1-2 mL of household bleach (5 % NaOCl) per 8 L at each fill to slow algae and mould, which is the practice recommended in the postharvest evaporative-cooling reviews. Replace the coir when efficiency drops more than 15 % from the commissioning value or when visible mould appears; log the date. Use potable water; produce is not in contact with the water but the chamber air is.

## 3. Heat load budget

| Source | Steady, W | Transient (first 3 h after loading 30 kg at +5 K), W |
|--------|----------:|-----------------------------------------------------:|
| Wall conduction, 2.47 m² at U 0.57 W/m²K, ΔT 4 K | 6 | 6 |
| Solar on roof and side if used outdoors (white paint, shaded rear) | 0-10 | 0-10 |
| Produce respiration (tomato about 0.1 W/kg at 28 °C; pechay about 0.3 W/kg) | 3-9 | 3-9 |
| Door openings, two per day | 1 | 1 |
| Field-heat pulldown, 30 kg × 3.9 kJ/kg K × 5 K over 3 h | 0 | 54 |
| **Total** | **10-26** | **64-80** |

At 120 m³/h and a 60 W load the chamber air runs about 1.5 K above the pad outlet (calc); at the steady load about 0.5 K. So the achievable chamber condition is roughly pad-outlet plus 1 K: 28-30 °C and 88-92 % RH on a 33-34 °C dry-season afternoon, 1-2 K below ambient and 93-95 % RH in the wet season.

## 4. Electrical system

### 4.1 Power budget

| Load | Peak, W | Duty | Average, W |
|------|--------:|-----:|-----------:|
| Fan 1 + Fan 2 at 100 % | 6.0 | DRY 100 %, HUMID 40 % | 6.0 / 2.4 |
| Pump | 4.0 | 25 % / 9 % | 1.0 / 0.4 |
| ESP32, display, sensors, SD | 1.5 | 100 % | 1.5 |
| **Total** | **11.5** | | **8.5 (DRY) / 4.3 (HUMID)** |

Daily energy: about 200 Wh in DRY mode, 100 Wh in HUMID mode.

### 4.2 Options for open decision O1

| Option | Hardware | Notes |
|--------|----------|-------|
| (a) Wall adapter | 12 V 3 A regulated adapter into `BAY_jack_dc` | Simplest; lab use |
| (b) Adapter + battery | 12 V 20 Ah SLA in `BAY_battery`, 12 V 2 A charger or the adapter through a simple charge board | 1 day autonomy at 50 % depth of discharge in DRY mode, 2 days in HUMID mode |
| (c) Battery + solar | 50 W panel (about 670 × 450 mm), 10 A PWM charge controller in `BAY_charge_controller`, 20 Ah battery | Sized for 200 Wh/day at 4.5 peak-sun hours and 70 % system efficiency; a 30 W panel is enough for HUMID-mode operation only |

### 4.3 Wiring

```
                +12V bus (fused 3 A, main switch)
 DC jack ──┬─── FUSE ─── SW ───┬───────────────┬──────────────┬───────────┐
 (battery/ │                   │               │              │           │
  charger  │                   │           MOSFET_fans    MOSFET_pump   BUCK 12→5 V
  optional)│                   │               │              │           │
           │                FAN1 +12 ──────────┤           PUMP +12       5 V ── ESP32 5V
           │                FAN2 +12 ──────────┤              │           │
           │                FAN1/2 PWM ◄────── GPIO25 (25 kHz)│           ├── SHT31 amb (I2C, 3.3 V)
           │                FAN1/2 TACH ─────► GPIO26/27      │           ├── SHT31 chamber (I2C addr 0x45)
           │                                                   │           ├── SHT31 pad-out (optional, I2C mux or 2nd bus)
           │                MOSFET_fans gate ◄── GPIO32        │           ├── DS18B20 pulp (1-Wire GPIO4, 4.7 kΩ)
           │                MOSFET_pump gate ◄── GPIO33 ───────┘           ├── Float switch ─► GPIO34 (pull-up)
           │                                                               ├── TFT 2.8" SPI (GPIO18/19/23/5, DC 16, RST 17)
           │                                                               ├── microSD SPI (CS 15)
           │                                                               ├── Buttons GPIO12/13/14 (pull-up)
           │                                                               └── Status LED GPIO2
          GND ──────────────────────────────────────────────────────────────── common
```

All cables outside the bay run in 16 mm PVC conduit; entries into the chamber and the rear module use M16 glands with silicone. Keep the sensor I2C runs under 1.5 m; use shielded 4-core cable for the chamber sensor.

## 5. Control logic (firmware behaviour)

### 5.1 Inputs and derived values

* `T_amb`, `RH_amb` from the inlet-side sensor, every 10 s, 6-sample rolling median.
* `T_ch`, `RH_ch` from the chamber sensor; `T_pad` optional; `T_pulp` from the probe.
* `T_wb` computed from `T_amb`, `RH_amb` with the same relations as `tools/psychro_design.py` (Tetens saturation pressure, ASHRAE wet-bulb iteration, 20 bisection steps is enough on the ESP32).
* `WBD = T_amb - T_wb` (wet-bulb depression).
* `eta_sat = (T_amb - T_pad) / (T_amb - T_wb)` when the pad-outlet sensor is fitted; otherwise `eta_ch = (T_amb - T_ch) / WBD` as the chamber cooling efficiency.
* `water_ok` from the float switch (debounced 5 s).

### 5.2 Modes

| Mode | Entry condition | Fans | Pump | Purpose |
|------|-----------------|------|------|---------|
| DRY | WBD ≥ 3.0 K | 100 % PWM | 60 s on / 180 s off | Maximise cooling |
| HUMID | WBD < 2.5 K (0.5 K hysteresis) | 40 % PWM | 30 s on / 300 s off | Hold 90-95 % RH, save water and energy |
| SATURATED | RH_ch ≥ 97 % and T_ch ≥ T_amb - 0.5 K for 10 min | 30 % PWM | off | Air exchange only; nothing to gain from wetting |
| FILL | water_ok = false | unchanged | off | Protect the pump; display and LED alarm |
| PULLDOWN (optional) | door opened (reed switch) or T_pulp > T_ch + 3 K | 100 % | as DRY | Fast pulldown after loading |
| OFF | main switch or menu | off | off | |

Thresholds 3.0 K and 2.5 K are the initial values from the climate analysis; they are menu-adjustable and the pad-comparison experiment should confirm them.

### 5.3 Pseudo-code

```
every 10 s:
    read sensors; update medians
    T_wb = wetbulb(T_amb, RH_amb); WBD = T_amb - T_wb
    if not water_ok:              mode = FILL
    elif door_open or pulldown:   mode = PULLDOWN
    elif RH_ch >= 97 and T_ch >= T_amb - 0.5 (for 10 min): mode = SATURATED
    elif WBD >= 3.0:              mode = DRY
    elif WBD < 2.5:               mode = HUMID
    # else keep previous mode (hysteresis band)
    set fan_pwm(mode); schedule pump duty(mode)
every 60 s:
    append CSV row: timestamp, T_amb, RH_amb, T_wb, WBD, T_ch, RH_ch, T_pad, T_pulp,
                    mode, fan_pwm, pump_state, water_ok, fan1_rpm, fan2_rpm
display refresh every 2 s:
    line 1: AMB 33.1C 62%   WB 26.8
    line 2: CHM 29.4C 91%   dT 3.7
    line 3: MODE DRY  FAN 100%  PUMP ON
    line 4: WATER OK   eff 0.60  up 14:32
```

Logging is to microSD in daily CSV files; the SD card is read on a PC for analysis. No wireless in this version.

## 6. Test protocol

### 6.1 Commissioning (no produce)

1. Leak and gasket check: run fans, smoke pencil at door and hatch.
2. Fan curve: measure airflow at the hood slots with a vane anemometer at PWM 30, 40, 60, 80, 100 % with the cassette in place; record pad pressure drop with an inclined manometer across the cassette.
3. Water: verify wetting across the whole pad face after 5 min; adjust trim valve; confirm float switch trip volume.
4. Sensor check: all sensors in one bag for 30 min, agree within 0.3 K and 3 % RH; offset-correct in firmware.

### 6.2 Experiment A: pad-material comparison (no load)

* Factor: media (coir, charcoal, jute), each in its own cassette, same 75 mm thickness.
* Fixed: PWM 100 %, DRY-mode pump duty, same location and time-of-day window (13:00-16:00, dry season).
* Response: saturation efficiency (pad-outlet sensor), chamber cooling efficiency, water use per hour (sight tube), pressure drop, fan power.
* Runs: 3 days per medium, randomised order; repeat the coir run after 4 weeks of continuous wetting to measure efficiency decay and mould.
* Analysis: one-way ANOVA on daily-mean efficiency, Tukey post-hoc.

### 6.3 Experiment B: control strategy (no load)

* Treatments: continuous operation (fans 100 %, pump 25 % duty) vs adaptive control (section 5).
* Response: water use per day, energy per day (measure with a 12 V watt-meter), chamber RH and temperature profile.
* Runs: alternate days for 10 days spanning at least one rainy day.

### 6.4 Experiment C: storage trial (loaded)

Test crop is open decision O2. Default written for tomato (breaker stage) with pechay as the leafy comparison.

* Treatments: cooler vs ambient shelf (same room, same crates); optional third arm: domestic refrigerator if available (note tomato chilling injury below 10 °C).
* Sample: 3 crates × 10 kg tomato per treatment (or 2 tomato + 1 pechay), 10 tagged fruits per crate for daily scoring.
* Daily: crate weight (0.01 kg), pulp temperature, colour stage (USDA 1-6), firmness (hand or penetrometer), decay count, marketable fraction.
* Duration: until 50 % of the ambient sample is unmarketable, or 14 days.
* Metrics: cumulative weight loss %, days to colour stage 6, marketable % at day 7 and day 14, shelf-life extension in days.
* Replicate the trial twice (dry season and wet season) to show both regimes.

### 6.5 Formulas

* Saturation efficiency: `eta = (T_db,in - T_db,out) / (T_db,in - T_wb,in)`.
* Cooling capacity: `Q = rho * V * c_p * (T_db,in - T_db,out)` with rho 1.15 kg/m³, c_p 1006 J/kg K, V in m³/s.
* Water use: sump level difference × 540 × 105 mm² per mm, plus refills.
* Specific water use: L per kWh of cooling, and L per kg-day of produce.

## 7. Bill of materials

| # | Item | Spec | Qty | Est. PHP |
|---|------|------|----:|---------:|
| 1 | Marine plywood 12 mm | 4 × 8 ft sheet | 2 | 2 400 |
| 2 | Plywood 9 mm | half sheet, bay | 1 | 400 |
| 3 | EPS foam board 50 mm | 1 × 2 m | 2 | 800 |
| 4 | PVC sheet 3 mm (liner) | 1.2 × 2.4 m | 1 | 900 |
| 5 | PVC sheet 5 mm (sump) | 0.6 × 0.6 m | 1 | 300 |
| 6 | Lumber 40 × 40 | 3 m | 2 | 300 |
| 7 | Casters 75 mm, 2 swivel with brake, 2 swivel | | 4 | 600 |
| 8 | 120 mm 12 V 4-pin PWM fans | 0.25-0.35 A | 2 | 600 |
| 9 | Fan guards 120 mm | | 2 | 100 |
| 10 | 12 V submersible pump | 240 L/h | 1 | 350 |
| 11 | Float switch, vertical | | 1 | 120 |
| 12 | PVC pipe 1/2 in, elbows, cap, 40 mm port and cap, 20 mm overflow, barbs | | lot | 350 |
| 13 | Vinyl hose 8 mm ID, mini ball valve | 2 m | 1 | 150 |
| 14 | Aluminium angle 40 × 40 × 3 | 2.5 m | 1 | 450 |
| 15 | Aluminium angle 20 × 20 × 2 (cassette) | 4 m | 1 | 350 |
| 16 | Galvanised hardware cloth 12.7 mm | 1 m² | 1 | 250 |
| 17 | Aluminium insect screen | 1 m² | 1 | 150 |
| 18 | Plastic louver grille 560 × 460 | or fabricate from plywood slats | 1 | 300 |
| 19 | Coconut coir, loose | 2 kg | 1 | 150 |
| 20 | Lump charcoal (comparison) | 5 kg | 1 | 150 |
| 21 | Jute sacks (comparison) | | 3 | 90 |
| 22 | Vented plastic crates | 480 × 340 × 230 | 6 (3 cooler, 3 ambient) | 1 200 |
| 23 | EPDM D-gasket 10 mm, foam tape | 5 m | | 250 |
| 24 | Stainless hinges 75 mm, draw latches, D-handle, toggle latches | | lot | 600 |
| 25 | ESP32 DevKitC | | 1 | 350 |
| 26 | SHT31 sensor modules | | 3 | 900 |
| 27 | DS18B20 waterproof probe | | 1 | 120 |
| 28 | 2.8 in SPI TFT 320 × 240 | | 1 | 450 |
| 29 | microSD module + 8 GB card | | 1 | 250 |
| 30 | MOSFET modules, buck converter, terminal block, fuse holder, switch, jack, buttons, LED | | lot | 500 |
| 31 | 16 mm PVC conduit, M16 glands, cable | | lot | 400 |
| 32 | 12 V 3 A adapter | | 1 | 350 |
| 33 | White exterior paint, varnish, silicone, screws, PVC cement | | lot | 900 |
| | **Subtotal, option (a)** | | | **~16 500** |
| 34 | 12 V 20 Ah SLA battery (option b/c) | | 1 | 2 800 |
| 35 | 50 W PV panel + 10 A PWM controller + cable (option c) | | 1 | 3 500 |
| | **Total, option (c)** | | | **~22 800** |

Prices are 2026 Metro Manila hardware and electronics-shop estimates; expect ±30 %.

## 8. Safety and hygiene

* 12 V system, fused at 3 A; no mains inside the unit. The adapter stays outside.
* Water and electronics are separated by the insulated shell: the bay is on the dry right side, the wet module is at the back, and the only shared items are glanded cables.
* Sump water is not potable after bleach dosing; label the fill port.
* Fans are guarded; the hood slots are screened.
* Casters lock during trials so the door can be opened without the unit rolling.
* Lift the unit only by the base frame; the door and the bay are not handles.
