# Evaporative cooler for postharvest storage (student scale)

Concept on this branch: **Option B - Scale** (wall adapter with backup battery, sentinel-crate scale). The Blender handoff is `docs/07-blender-handoff.md`.

Agricultural and Biosystems Engineering project: a small evaporative cooling cabinet for short-term storage of fresh fruits and vegetables.

## Contents

| Path | What it is |
|------|------------|
| `docs/01-patent-landscape.md` | Patent screening (Espacenet / Google Patents / USPTO): what is free to use, what to steer clear of, and ready-made Espacenet queries to verify legal status. |
| `docs/02-design-recommendation.md` | Literature review, climate feasibility, recommended design, target spec, expected performance, thesis angles, bill of materials. |
| `docs/03-design-decisions.md` | Decision log: every design choice, its rationale (research, novelty, patent avoidance), and the two open decisions. |
| `docs/04-assembly-spec.md` | Full dimensioned parts list and positions for 3D modelling (Blender handoff): axes, naming, materials, every part's bounding box, section views, collection hierarchy, clearance checks. |
| `docs/05-systems-and-protocol.md` | Air, water, heat, electrical and control design; firmware behaviour; test protocol; bill of materials; safety. |
| `docs/06-software-novelty-options.md` | Software-based novelty options with prior-art screening; the sentinel crate (Option 1) was chosen. |
| `docs/08-literature-synthesis.md` | Synthesis of related literature behind each design decision, with pad-media decision matrix, economics and reference list for the RRL. |
| `docs/09-materials-and-components.md` | Every part with its material or spec, why it was chosen, rejected alternatives, quantity and cost; material rules for the humid, wet environment. |
| `docs/07-blender-handoff.md` | Brief for the 3D modeller: what to build, in what order, how, and what to deliver back. |
| `tools/psychro_design.py` | Psychrometric and sizing calculator (wet-bulb, wet-bulb depression, pad outlet state, chamber temperature, water use, pad area). Standard library only. |

## Quick start

```bash
python3 tools/psychro_design.py            # Philippine climate cases
python3 tools/psychro_design.py 33 62      # your site: dry-bulb degC, RH %
python3 tools/psychro_design.py 33 62 --eff 0.75 --flow 100 --load 50 --face-vel 0.6
```

## Design at a glance

Insulated plywood and EPS cabinet with a 540 × 520 × 590 mm chamber (0.166 m³) holding 12-17 kg of produce: one standard vented crate on a built-in weighing platform and a slatted shelf above it on aluminium rails, behind a front plug door. A 500 × 300 × 150 mm cellulose honeycomb pad (type 7090) sits in a lift-out cassette on the back wall, with its own water distributor, over a 10 L sump and pump. Two 120 mm PWM exhaust fans in the roof pull 100 m³/h through the pad and across the produce. An ESP32-S3 controller with an external display switches between DRY and HUMID modes on measured wet-bulb depression and logs everything; an AUTO / OFF / MANUAL switch keeps the cooler running if the electronics fail. The crate stands on a built-in scale, so the cooler measures its own produce's weight loss and shows the days left and the kilograms saved versus shelf storage. Overall 820 × 892 × 920 mm on four casters.

Priority: application and cooling efficiency, not novelty. Expected pad saturation efficiency is about 90 %, which puts the chamber within about 1 K of the outside wet-bulb temperature, the physical limit for any evaporative cooler.

Power: 15 V wall adapter with a 12 V 12 Ah backup battery that takes over during brownouts.

Open decision (see `docs/03-design-decisions.md` section 4): test crop.
