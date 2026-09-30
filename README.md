# Evaporative cooler for postharvest storage (student scale)

Agricultural and Biosystems Engineering project: a small evaporative cooling cabinet for short-term storage of fresh fruits and vegetables.

## Contents

| Path | What it is |
|------|------------|
| `docs/01-patent-landscape.md` | Patent screening (Espacenet / Google Patents / USPTO): what is free to use, what to steer clear of, and ready-made Espacenet queries to verify legal status. |
| `docs/02-design-recommendation.md` | Literature review, climate feasibility, recommended design, target spec, expected performance, thesis angles, bill of materials. |
| `docs/03-design-decisions.md` | Decision log: every design choice, its rationale (research, novelty, patent avoidance), and the two open decisions. |
| `docs/04-assembly-spec.md` | Full dimensioned parts list and positions for 3D modelling (Blender handoff): axes, naming, materials, every part's bounding box, section views, collection hierarchy, clearance checks. |
| `docs/05-systems-and-protocol.md` | Air, water, heat, electrical and control design; firmware behaviour; test protocol; bill of materials; safety. |
| `docs/06-software-novelty-options.md` | Software-based novelty options with prior-art screening; the weight-loss budget with a sentinel crate is recommended. |
| `tools/psychro_design.py` | Psychrometric and sizing calculator (wet-bulb, wet-bulb depression, pad outlet state, chamber temperature, water use, pad area). Standard library only. |

## Quick start

```bash
python3 tools/psychro_design.py            # Philippine climate cases
python3 tools/psychro_design.py 33 62      # your site: dry-bulb degC, RH %
python3 tools/psychro_design.py 33 62 --eff 0.75 --flow 100 --load 50 --face-vel 0.6
```

## Design at a glance

Insulated plywood and EPS cabinet with a 540 × 520 × 590 mm chamber (0.166 m³) holding 12-17 kg of produce: one standard vented crate on aluminium rails and a slatted shelf above it, behind a front plug door. A 500 × 300 × 150 mm cellulose honeycomb pad (type 7090) sits in a lift-out cassette on the back wall, with its own water distributor, over a 10 L sump and pump. Two 120 mm PWM exhaust fans in the roof pull 100 m³/h through the pad and across the produce. An ESP32 controller with an external display switches between DRY and HUMID modes on measured wet-bulb depression and logs everything; an AUTO / OFF / MANUAL switch keeps the cooler running if the electronics fail. Overall 820 × 892 × 920 mm on four casters.

Priority: application and cooling efficiency, not novelty. Expected pad saturation efficiency is about 90 %, which puts the chamber within about 1 K of the outside wet-bulb temperature, the physical limit for any evaporative cooler.

Open decisions (see `docs/03-design-decisions.md` section 4): power source (adapter, battery, or solar) and test crop.
