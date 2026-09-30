# Systems, control logic, test protocol and bill of materials

Companion to `04-assembly-spec.md` (geometry) and `03-design-decisions.md` (why). This file covers what the parts do: air, water, heat, electrical, firmware behaviour, and how the finished unit will be tested. Numbers marked (calc) come from `tools/psychro_design.py` with the stated inputs.

Design goal: get the chamber air as close as physics allows to the outside wet-bulb temperature, in a unit a vendor or farmer could actually run.

## 1. Air system

Revision: half-capacity layout, 12-17 kg in one standard crate plus one slatted shelf, chamber 540 × 520 × 590 mm (0.166 m³).

**Path.** Ambient air enters the rear louver, passes the insect screen and a 30 mm gap, flows through the 150 mm cellulose pad from back to front, enters the chamber through the 500 × 300 mm opening in the back wall, moves forward through the crate and over the shelf, rises in the front plenum, and leaves through two roof fans under the rain hood. Once-through, no recirculation.

| Parameter | Value | Basis |
|-----------|-------|-------|
| Design airflow | 100 m³/h (0.028 m³/s) | Keeps the chamber within about 1.1 K of pad-outlet air at a 35 W transient load and 0.3 K at the steady load (calc) |
| Pad | cellulose honeycomb 7090, 150 mm deep, face 500 × 300 mm (0.15 m²) | |
| Pad face velocity | 0.19 m/s | Far below the 1-2.5 m/s range of the manufacturer charts |
| Expected saturation efficiency | 90 % design value; 92-95 % likely | 150 mm 7090 pads reach the high 80s at 1 m/s and rise as velocity falls. **Measure it at commissioning** |
| Pad pressure drop | under 5 Pa | Cellulose honeycomb at this velocity |
| Screen, louver, crate and hood losses | 4-8 Pa | |
| Fan operating point | 2 × 50 m³/h at 8-12 Pa, about 65 % speed | Typical 120 mm 12 V fan: 100-110 m³/h free air, 30-40 Pa stall. Two fans kept for redundancy and even flow |
| Chamber air changes | about 600 per hour | 100 / 0.166 |

The fans are 4-pin PWM types. The ESP32 sets speed through the PWM line and a MOSFET enables or cuts their 12 V supply. With the PWM line disconnected, as in MANUAL mode, these fans run at full speed by specification; that gives about 150-180 m³/h, which is harmless.

## 2. Water system

**Circuit.** Sump (10 L working) → pump → 12 mm hose with trim valve → quick coupler → distributor pipe inside the cassette cap → jets hit the cap roof → rain onto the pad top → down the flutes → through the notched frame bottom → back into the sump. The quick coupler is unplugged to lift the cassette out.

| Parameter | Value | Basis |
|-----------|-------|-------|
| Wash rate | up to 4.5 L/min (270 L/h) | Manufacturer efficiency charts for 7090 are rated at 60 L/min per m² of pad top; top area is still 0.5 × 0.15 = 0.075 m² |
| Pump | 12 V brushless DC submersible, 300-500 L/h at 1 m head, 8-12 W | Lift from sump surface to the coupler is about 0.52 m plus hose losses |
| Flow setting | Trim valve so the whole pad face darkens evenly within 3 minutes with no dry streaks, then open 20 % more. Water must not stream off the chamber-side face | |
| Pump duty, DRY mode | 2 min on / 3 min off (40 %) default | Cellulose holds enough water to stay wet between pulses. Tune at commissioning (section 6.1) |
| Pump duty, HUMID mode | 1 min on / 9 min off | |
| Daily dry-out | pump off, fans at 50 % for 45 min once a day (default 06:00) | Standard practice for cellulose pads to control algae; chosen at the time of lowest cooling need |
| Evaporation at peak afternoon rate | 6-8 L/day in the dry season, 1.5-3.5 L/day in the wet season (calc, 100 m³/h) | Actual daily use is lower because night-time evaporation is small: expect about 4-5.5 L/day in the dry season |
| Sump working volume | 10 L at 105 mm; overflow invert at 115 mm (11 L) | Refill every 2 days in the dry season, every 3-4 days in the wet season |
| Low-level cut-out | float switch at 40 mm (about 3.8 L left) | Protects the pump; display shows "FILL" |
| Fill | 32 mm capped port on the rear panel; sight tube with a 0-11 L scale | |

**Water quality and hygiene.** Use tap water or rainwater; hard well water leaves scale on cellulose pads and cuts efficiency. Drain and scrub the sump weekly. Add 1-2 mL of household bleach (5 % sodium hypochlorite) per 10 L at each fill to slow algae. Hose the pad from the chamber side toward the inlet side once a month. A cellulose pad kept this way lasts several years. Replace it when measured saturation efficiency drops more than 10 points below the commissioning value. Produce never touches the water, but the chamber air does, so keep the water clean.

## 3. Heat load and expected performance

| Source | Steady, W | Transient (first 3 h after loading 15 kg at +5 K), W |
|--------|----------:|-----------------------------------------------------:|
| Wall conduction, 1.81 m² at U 0.57 W/m²K, ΔT 4 K | 4 | 4 |
| Solar on roof and side if used outdoors (white paint, shaded rear) | 0-7 | 0-7 |
| Produce respiration (tomato about 0.1 W/kg at 28 °C; leafy greens about 0.3 W/kg) | 2-5 | 2-5 |
| Door openings, two per day | 1 | 1 |
| Field-heat pulldown, 15 kg × 3.9 kJ/kg K × 5 K over 3 h | 0 | 27 |
| **Total** | **7-17** | **34-44** |

Expected chamber conditions (calc, 90 % pad efficiency, 100 m³/h):

| Outside air | Wet-bulb floor | Pad outlet | Chamber, steady (8 W) | Chamber, after loading (35 W) | Chamber RH |
|---|---:|---:|---:|---:|---:|
| 35 °C, 45 % | 25.1 °C | 26.1 °C | 26.3 °C | 27.1 °C | about 92 % |
| 34 °C, 55 % | 26.3 °C | 27.1 °C | 27.3 °C | 28.2 °C | about 94 % |
| 33 °C, 62 % | 26.8 °C | 27.4 °C | 27.7 °C | 28.5 °C | about 95 % |
| 31 °C, 78 % | 27.7 °C | 28.0 °C | 28.3 °C | 29.1 °C | about 97 % |
| 28 °C, 90 % | 26.6 °C | 26.8 °C | 27.0 °C | 27.9 °C | about 99 % |

Halving the capacity leaves the achievable temperatures unchanged: the steady chamber still sits within 1 K of the wet-bulb floor. Airflow, water use and power all drop by about a third.

## 4. Electrical system

### 4.1 Power budget

| Load | Peak, W | Duty DRY / HUMID | Average DRY / HUMID, W |
|------|--------:|-----------------:|-----------------------:|
| Fan 1 + Fan 2 | 6.0 | 65 % / 30 % speed | 3.0 / 1.0 |
| Pump | 10.0 | 40 % / 10 % | 4.0 / 1.0 |
| ESP32, display, sensors, SD | 1.5 | 100 % | 1.5 / 1.5 |
| **Total** | **17.5** | | **8.5 / 3.5** |

Daily energy: about 200 Wh in DRY mode, about 85 Wh in HUMID mode. Peak load current is 1.5 A; with battery charging on top, the adapter supplies up to 2.7 A, inside its 3 A rating.

### 4.2 Power supply: wall adapter with battery backup

Decided by the owner: mains adapter plus a backup battery. When mains is present the adapter runs the cooler and keeps the battery charged. During a brownout the battery takes over with no interruption.

| Part | Spec | Role |
|------|------|------|
| Wall adapter | 15 V DC, 3 A, regulated, 5.5 × 2.1 mm plug | Supplies the loads (1.5 A peak) and charges the battery (up to 1.2 A) at the same time. Stays outside the unit |
| DC-UPS / SLA charge module | 12 V lead-acid type; input 15-18 V; float 13.6-13.8 V; charge current limited to about 1.2 A (0.1 C); automatic switchover; low-voltage cut-off at about 10.8 V | Charges the battery, feeds the 12 V bus from the adapter or the battery, and disconnects the load before the battery is damaged |
| Battery | 12 V 12 Ah sealed lead-acid (SLA), 151 × 98 × 95 mm | About 72 Wh usable at 50 % depth of discharge |
| Battery fuse | 5 A blade fuse in an inline holder on the battery positive lead | Protects the battery wiring |

Bus voltage is 13.6-13.8 V on mains and 12.8 V falling to about 11 V on battery. Choose fans and pump rated for up to 13.8 V; most 12 V PC fans and brushless DC pumps are.

**Runtime on battery.**

| Mode | Average load | Runtime |
|------|-------------:|--------:|
| DRY | 8.5 W | about 8.5 h |
| DRY with battery saving (below) | 6 W | about 12 h |
| HUMID | 3.5 W | about 20 h |

**Battery saving.** When the controller sees it is running on battery and the voltage falls below 12.2 V, it caps the fans at 50 % and stretches the pump off-time by a third. Below 11.6 V it shows "LOW BATTERY" and flashes the LED. The module's own cut-off at about 10.8 V is the last line of protection.

A solar panel can be added later without redesign: a PV charge controller would feed the same battery. It is not part of this design.

### 4.3 Wiring

```
 15 V adapter ── DC jack ── DC-UPS module IN
                            DC-UPS module BAT ── 5 A fuse ── 12 V 12 Ah SLA
                            DC-UPS module OUT ── FUSE 3 A ── MAIN SW ──┬──── +12 V bus (13.8 V on mains) ─────────┐
                                                                       │                                         │
                     MODE SWITCH (3-position, 3-pole)                                                     BUCK 12→5 V ── ESP32 5V
                      AUTO: fans ← MOSFET_fans, pump ← MOSFET_pump                                               │
                      OFF:  fans and pump unpowered                                                              ├── SHT31 ambient  (I2C 0x44, bus 1)
                      MANUAL: fans ← +12 V direct (PWM open → full speed),                                       ├── SHT31 chamber  (I2C 0x45, bus 1)
                              pump ← +12 V direct                                                                ├── SHT31 pad outlet (I2C 0x44, bus 2)
                                                                                                                 ├── DS18B20 pulp probe (1-Wire GPIO4, 4.7 kΩ)
 FAN1/2 PWM  ◄── GPIO25 (25 kHz)      MOSFET_fans gate ◄── GPIO32                                                 ├── Float switch ─► GPIO34 (pull-up)
 FAN1/2 TACH ──► GPIO26 / GPIO27      MOSFET_pump gate ◄── GPIO33                                                 ├── Mode sense ─► GPIO35 (AUTO = low)
 Bus voltage ── 100 kΩ / 22 kΩ divider ──► GPIO36                                                                  ├── TFT 2.8" SPI (GPIO18/19/23/5, DC 16, RST 17)
 Adapter present ── 100 kΩ / 22 kΩ divider (from DC jack) ──► GPIO39                                               ├── microSD SPI (CS 15)
                                                                                                                 ├── Buttons GPIO12/13/14 (pull-up)
 GND ─────────────────────────────────────────────────────────────────────────────────────────────────────────── └── Status LED GPIO2
```

The controller stays powered in every mode position so it keeps logging and displaying. In MANUAL it reads the mode-sense pin, shows "MANUAL", and does not drive the MOSFETs. The float-switch pump cut-out works only in AUTO; the display still shows "FILL" in MANUAL.

All cables outside the bay run in 16 mm PVC conduit. Entries into the chamber and the rear module use M16 glands sealed with silicone. Keep I2C runs under 1.5 m and use shielded 4-core cable to the sensors.

## 5. Control logic (firmware behaviour)

### 5.1 Inputs and derived values

* `T_amb`, `RH_amb` from the inlet-side sensor, every 10 s, 6-sample rolling median.
* `T_ch`, `RH_ch` from the chamber sensor; `T_pad` from the pad-outlet sensor; `T_pulp` from the probe.
* `T_wb` computed from `T_amb`, `RH_amb` with the same relations as `tools/psychro_design.py` (Tetens saturation pressure, ASHRAE wet-bulb relation, 20 bisection steps).
* `WBD = T_amb - T_wb` (wet-bulb depression, the maximum possible cooling).
* `eta_pad = (T_amb - T_pad) / WBD`: pad saturation efficiency, shown on the display and logged. This is the headline performance number.
* `eta_ch = (T_amb - T_ch) / WBD`: chamber cooling efficiency.
* `water_ok` from the float switch (debounced 5 s).
* `V_bus` from the bus-voltage divider and `mains` from the adapter-present divider, every 10 s.

### 5.2 Modes (AUTO position)

| Mode | Entry condition | Fans | Pump | Purpose |
|------|-----------------|------|------|---------|
| DRY | WBD ≥ 3.0 K | 65 % (set at commissioning to give 100 m³/h) | 2 min on / 3 min off | Maximum cooling |
| HUMID | WBD < 2.5 K (0.5 K hysteresis) | 30 % | 1 min on / 9 min off | Hold 90-95 % RH with little water and energy |
| SATURATED | RH_ch ≥ 97 % and T_ch ≥ T_amb - 0.5 K for 10 min | 25 % | off | Air exchange only; wetting gains nothing |
| DRY-OUT | once a day at the set time, 45 min | 50 % | off | Algae control for the cellulose pad |
| FILL | water_ok = false | unchanged | off | Protect the pump; display and LED alarm |
| PULLDOWN | T_pulp > T_ch + 3 K, for example after loading | 100 % | as DRY | Fast removal of field heat |

Battery overlay, applied on top of any mode: if `mains` is false and `V_bus` < 12.2 V, fans are capped at 50 % and pump off-times are stretched by a third; below 11.6 V the display shows "LOW BATTERY" and the LED flashes.

Thresholds are menu-adjustable. Running fans with the pump off (SATURATED and DRY-OUT) is standard pad-cooler practice; see the patent note in `03-design-decisions.md`.

### 5.3 Pseudo-code

```
every 10 s:
    if mode_switch != AUTO: show "MANUAL" or "OFF"; log; return
    read sensors; update medians
    T_wb = wetbulb(T_amb, RH_amb); WBD = T_amb - T_wb
    if not water_ok:                               mode = FILL
    elif in dry_out_window:                        mode = DRY_OUT
    elif T_pulp > T_ch + 3:                        mode = PULLDOWN
    elif RH_ch >= 97 and T_ch >= T_amb - 0.5 (10 min): mode = SATURATED
    elif WBD >= 3.0:                               mode = DRY
    elif WBD < 2.5:                                mode = HUMID
    # otherwise keep the previous mode (hysteresis band)
    if not mains and V_bus < 12.2: apply battery saving
    set fan_pwm(mode); schedule pump duty(mode)
every 60 s:
    append CSV row: timestamp, T_amb, RH_amb, T_wb, WBD, T_pad, eta_pad, T_ch, RH_ch, eta_ch,
                    T_pulp, mode, switch_pos, fan_pwm, pump_state, water_ok, fan1_rpm, fan2_rpm,
                    mains, V_bus
display refresh every 2 s:
    AMB 33.1C 62%   WB 26.8
    CHM 27.6C 95%   dT 5.5
    PAD eff 91%     MODE DRY
    WATER OK        PUMP ON   MAINS / BATT 78%
```

Logging is to microSD in daily CSV files. No wireless in this version.

## 6. Test protocol

The final design is tested on its own. There is no pad-material comparison.

### 6.1 Commissioning

1. **Leaks and bypass.** Run the fans and check the door, hatch and cassette gasket with a smoke pencil or incense stick. Air must enter only through the pad.
2. **Airflow.** Measure airflow at the hood slots with a vane anemometer at 30, 50, 65, 80 and 100 % fan speed. Set the DRY-mode speed to the one that gives 100 m³/h. Measure the pad pressure drop with an inclined manometer.
3. **Wash rate.** Set the trim valve as in section 2. Record the flow with a bucket and stopwatch at the riser.
4. **Pump duty.** On a dry afternoon, run the pump continuously for 30 min, then at 2/3, 2/6 and 2/9 minutes on/off for 30 min each. Keep the longest off-time that raises the pad-outlet temperature by less than 0.2 K; write it into the DRY-mode setting.
5. **Sensors.** Place all three SHT31s in one bag for 30 min; they must agree within 0.3 K and 3 % RH. Enter offsets in firmware.
6. **Manual override.** Switch to MANUAL and confirm fans at full speed and pump running with the controller disconnected.

### 6.2 Test A: no-load performance

* Conditions: empty chamber, AUTO mode, door closed.
* Duration: 3 full days in the dry season and 3 full days in the wet season.
* Responses: pad saturation efficiency, chamber cooling efficiency, chamber temperature and RH, temperature drop below ambient, water use per day from the sight tube, energy per day with a 12 V watt-meter.
* Report: daily mean and 13:00-16:00 mean of each, plotted against wet-bulb depression. Target: pad efficiency of at least 85 % on every dry-season afternoon.

### 6.3 Test B: storage trial

The test crop is open decision O2. The default is tomato at breaker stage, with a leafy crop such as pechay as an optional second commodity.

* Treatments: cooler vs ambient shelf in the same room, same crates. Optional third arm: a domestic refrigerator (note tomato chilling injury below 10 °C).
* Sample: per treatment, one crate (8-10 kg) plus one shelf load (4-7 kg). In the crate, score 3 tagged groups of 10 fruits daily. The ambient control uses an identical crate and an identical slatted tray.
* Replication: the cooler holds one crate, so repeat the trial three times per season with fresh produce and treat each run as a replicate.
* Daily: crate weight (0.01 kg), pulp temperature, colour stage (USDA 1-6), firmness (hand scale or penetrometer), decay count, marketable fraction.
* Duration: until 50 % of the ambient sample is unmarketable, or 14 days.
* Metrics: cumulative weight loss %, days to colour stage 6, marketable % at day 7 and day 14, shelf-life extension in days.
* Run once in the dry season and once in the wet season.

### 6.4 Formulas

* Pad saturation efficiency: `eta_pad = (T_amb - T_pad) / (T_amb - T_wb)`.
* Chamber cooling efficiency: `eta_ch = (T_amb - T_ch) / (T_amb - T_wb)`.
* Cooling capacity: `Q = rho * V * c_p * (T_amb - T_pad)` with rho 1.15 kg/m³, c_p 1006 J/kg K, V in m³/s.
* Water use: sight-tube level change times 530 × 180 mm² per mm, plus refills.
* Specific water use: L per kWh of cooling and L per kg of produce per day.

## 7. Bill of materials

| # | Item | Spec | Qty | Est. PHP |
|---|------|------|----:|---------:|
| 1 | Marine plywood 12 mm | 4 × 8 ft sheet | 2 | 2,400 |
| 2 | Plywood 9 mm | half sheet, bay | 1 | 400 |
| 3 | EPS foam board 50 mm | 1 × 2 m | 2 | 800 |
| 4 | PVC sheet 3 mm (liner) | 1.2 × 2.4 m | 1 | 900 |
| 5 | PVC sheet 5 mm (sump) | 0.6 × 0.8 m | 1 | 400 |
| 6 | Lumber 40 × 40 | 3 m | 2 | 300 |
| 7 | Casters 75 mm, 2 swivel with brake, 2 swivel |  | 4 | 600 |
| 8 | 120 mm 12 V 4-pin PWM fans | 0.25-0.35 A | 2 | 600 |
| 9 | Fan guards 120 mm |  | 2 | 100 |
| 10 | Cellulose evaporative pad 7090, 150 mm | one standard sheet, cut to 500 × 300 | 1 | 2,500 |
| 11 | Aluminium sheet 1 mm (distribution cap) | 0.3 × 0.6 m | 1 | 300 |
| 12 | 12 V brushless DC submersible pump | 300-500 L/h at 1 m, 8-12 W | 1 | 900 |
| 13 | Float switch, vertical |  | 1 | 120 |
| 14 | PVC pipe 1/2 in, elbow, cap, 32 mm port and cap, 20 mm overflow, barbs |  | lot | 350 |
| 15 | Vinyl hose 12 mm ID, 1/2 in ball valve, 1/2 in hose quick coupler | 1.5 m | 1 | 450 |
| 16 | Aluminium angle 40 × 40 × 3 (crate and shelf rails) | 1.5 m | 1 | 300 |
| 17 | Aluminium angle 20 × 20 × 2 (cassette frame, shelf frame and lips) | 7 m | 1 | 650 |
| 18 | Aluminium angle 25 × 25 × 3 (cassette stops) | 0.4 m | 1 | 80 |
| 19 | PVC U-channel (cassette guides) | 0.9 m | 1 | 150 |
| 20 | Polypropylene sheet 10 mm (shelf slats) | 0.35 × 0.4 m | 1 | 350 |
| 21 | Aluminium insect screen | 1 m² | 1 | 150 |
| 22 | Plastic louver grille 560 × 360 | or fabricate from plywood slats | 1 | 250 |
| 23 | Vented plastic crates | 480 × 340 × 230 | 2 (1 cooler, 1 ambient) | 400 |
| 24 | Slatted tray for the ambient shelf control | same size as the shelf | 1 | 250 |
| 25 | EPDM D-gasket 10 mm, foam tape | 4 m |  | 200 |
| 26 | Stainless hinges 75 mm, draw latches, D-handle, toggle latches, rivets |  | lot | 650 |
| 27 | ESP32 DevKitC |  | 1 | 350 |
| 28 | SHT31 sensor modules | ambient, chamber, pad outlet | 3 | 900 |
| 29 | DS18B20 waterproof probe |  | 1 | 120 |
| 30 | 2.8 in SPI TFT 320 × 240 |  | 1 | 450 |
| 31 | microSD module + 8 GB card |  | 1 | 250 |
| 32 | MOSFET modules, buck converter, terminal block, fuse holder, main switch, jack, buttons, LED |  | lot | 500 |
| 33 | 3-position AUTO / OFF / MANUAL rocker, 10 A |  | 1 | 150 |
| 34 | 16 mm PVC conduit, M16 glands, cable |  | lot | 350 |
| 35 | 15 V 3 A adapter |  | 1 | 400 |
| 36 | 12 V 12 Ah SLA battery | 151 × 98 × 95 | 1 | 1,300 |
| 37 | 12 V DC-UPS / SLA charge module with low-voltage cut-off | 15-18 V in, ~1.2 A charge | 1 | 600 |
| 38 | Inline 5 A blade fuse holder, battery leads and terminals | | 1 | 100 |
| 39 | White exterior paint, varnish, silicone, screws, PVC cement |  | lot | 800 |
| | **Total** | | | **~20 800** |

Prices are 2026 Metro Manila hardware, poultry-supply and electronics-shop estimates; expect ±30 %. Cellulose 7090 pad is sold by poultry-house and greenhouse suppliers and online in standard sheets, commonly 600 mm wide in 1200-1800 mm lengths; one sheet makes several replacement cassettes.

## 8. Safety and hygiene

* 12 V system fused at 3 A on the bus and 5 A on the battery lead; no mains inside the unit. The adapter stays outside.
* The sealed lead-acid battery is maintenance-free and safe indoors, but keep the bay vents clear and replace the battery every 3-4 years or when runtime halves.
* Water and electronics are separated: the bay is on the dry right side, the wet module is at the back, and the only shared items are glanded cables.
* The sump water is dosed with bleach and is not potable; the fill label says so.
* Fans are guarded and the hood slots are screened.
* Casters lock during trials so the door can be opened without the unit rolling.
* Lift the unit only by the base frame; the door and the bay are not handles.
* In MANUAL mode the float-switch cut-out is bypassed, so check the sight tube daily.
