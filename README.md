# Evaporative cooler for postharvest storage (student scale)

Agricultural and Biosystems Engineering project: a small evaporative cooling cabinet for short-term storage of fresh fruits and vegetables.

## Contents

| Path | What it is |
|------|------------|
| `docs/01-patent-landscape.md` | Patent screening (Espacenet / Google Patents / USPTO): what is free to use, what to steer clear of, and ready-made Espacenet queries to verify legal status. |
| `docs/02-design-recommendation.md` | Literature review, climate feasibility, recommended design, target spec, expected performance, thesis angles, bill of materials. |
| `tools/psychro_design.py` | Psychrometric and sizing calculator (wet-bulb, wet-bulb depression, pad outlet state, chamber temperature, water use, pad area). Standard library only. |

## Quick start

```bash
python3 tools/psychro_design.py            # Philippine climate cases
python3 tools/psychro_design.py 33 62      # your site: dry-bulb degC, RH %
python3 tools/psychro_design.py 33 62 --eff 0.75 --flow 100 --load 50 --face-vel 0.6
```

## Recommendation in one paragraph

Build a fan-assisted, single-stage direct evaporative cooling cabinet of about 0.2-0.25 m³ (25-35 kg of produce), 12 V DC, with a 60-100 mm coconut-coir pad (charcoal and jute as comparison treatments), two 120 mm exhaust fans, a small submersible pump with a drip pipe, 25-50 mm foam insulation, and an optional microcontroller that cycles the pump and fan on measured wet-bulb depression. In the Philippine dry season it delivers about 4-5 K below ambient and 88-95 % RH; in the wet season it acts mainly as a humidity chamber, which still cuts produce water loss. Avoid fabric-walled collapsible designs (Evaptainers patent), dew-point indirect stages (Coolerado family) and sump-air pre-cooling loops; everything else in this design is expired or never-patented prior art.
