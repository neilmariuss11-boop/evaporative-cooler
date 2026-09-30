# Assembly specification for 3D modelling (Blender handoff)

Complete dimensioned parts list for the student-scale evaporative cooling cabinet. Every part has a name, size, position, and material. Positions are the part's bounding box in the global frame unless stated as a centre.

## 1. Conventions

* **Units:** millimetres. In Blender set Scene > Units > Length = Millimeters, Unit Scale = 0.001, and model at 1 unit = 1 mm.
* **Axes:** right-handed, Z up. **X** runs left to right as seen by the operator standing in front of the door. **Y** runs from the front (door face) toward the back (pad module). **Z** runs from the floor upward. Blender's Front view (numpad 1) therefore shows the door.
* **Origin:** floor level (Z = 0, bottom of the casters), at the outside bottom-left-front corner of the main shell. The main shell occupies X 0 to 670, Y 0 to 650. Parts that protrude beyond it (rear module, electrical bay, hood, door face) have coordinates outside that range.
* **Bounding boxes** are written `X a..b, Y c..d, Z e..f`. Cylinders are given by axis, centre and diameter.
* **Naming:** `GROUP_part_variant`, e.g. `SHELL_wall_left_ply`. Blender collections follow the group letters in section 3.
* **Wall sandwich rule:** every insulated wall is three layers, outside to inside: 12 mm plywood, 50 mm EPS, 3 mm PVC liner (65 mm total). Model each wall as one block with three sub-blocks, or as one block with a single material if layer detail is not needed. Layer thicknesses are listed once here and not repeated per part.
* **Materials and colours (sRGB hex):** plywood painted white exterior `#F2F2EE`; plywood natural (interior of bay, cassette hatch underside) `#C9A46B`; EPS foam `#FFFFFF` (only visible in cut-away); PVC liner white `#FAFAFA`; aluminium angle and mesh `#B8BCC0`; galvanised hardware cloth `#9EA3A8`; cellulose pad kraft brown `#A9743A` (flutes darker `#7E5424`); PVC pipe grey `#8E8E8E`; sump PVC sheet dark grey `#4A4A4A`; fan black `#1E1E1E`; fan guard chrome `#C8C8C8`; crates green `#2E8B57`; casters black rubber `#202020` with grey plate `#8A8A8A`; EPDM gasket black `#151515`; TFT display glass `#0B0B0B`; stainless hinges and latches `#D0D2D5`; cables black `#111111`; clear vinyl sight tube `#DDEEFF` at 40 % alpha.

## 2. Overall envelope

| Item | Value |
|------|-------|
| Main shell (insulated box) | X 0..670, Y 0..650, Z 140..1170 |
| Rear pad module | X 0..670, Y 650..860, Z 140..1170 |
| Electrical bay | X 670..820, Y 0..250, Z 820..1170 |
| Fan rain hood | X 110..560, Y 120..290, Z 1170..1230 |
| Cassette hatch lid | X 55..615, Y 640..830, Z 1170..1182 |
| Door face (closed) | X 25..645, Y -12..0, Z 165..1145 |
| Casters | Z 0..100 |
| Overall footprint including door face, bay and rear louver | X 0..820, Y -12..880 |
| Overall height to top of hood | 1230 |
| Chamber interior (clear) | X 65..605, Y 65..585, Z 205..1105 (540 × 520 × 900, 0.253 m³) |
| Mass estimate, with 12 L of water, no produce | about 66 kg |

Wall centre-plane reference: shell centre X = 335, chamber centre Y = 325.

## 3. Parts by group

### Group A: base and casters (collection `A_base`)

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `BASE_rail_front` | 40 × 40 lumber, painted | 670 × 40 × 40 | X 0..670, Y 0..40, Z 100..140 |
| `BASE_rail_back` | same | 670 × 40 × 40 | X 0..670, Y 820..860, Z 100..140 |
| `BASE_rail_left` | same | 40 × 780 × 40 | X 0..40, Y 40..820, Z 100..140 |
| `BASE_rail_right` | same | 40 × 780 × 40 | X 630..670, Y 40..820, Z 100..140 |
| `BASE_rail_mid` | cross member under the shell/rear-module joint | 590 × 40 × 40 | X 40..630, Y 630..670, Z 100..140 |
| `BASE_caster_FL` | 75 mm swivel caster with brake, 60 × 60 plate, wheel 75 dia × 25 wide | plate Z 96..100 | plate centre (50, 50), wheel axis along X at Z 37.5 |
| `BASE_caster_FR` | same | | plate centre (620, 50) |
| `BASE_caster_BL` | same | | plate centre (50, 810) |
| `BASE_caster_BR` | same | | plate centre (620, 810) |

### Group B: insulated shell (collection `B_shell`)

All walls follow the sandwich rule. Extents are the full 65 mm sandwich.

| Name | Description | Position |
|------|-------------|----------|
| `SHELL_floor` | insulated floor | X 0..670, Y 0..650, Z 140..205 |
| `SHELL_roof` | insulated roof, with two fan holes and cable holes (see Group E) | X 0..670, Y 0..650, Z 1105..1170 |
| `SHELL_wall_left` | | X 0..65, Y 0..650, Z 205..1105 |
| `SHELL_wall_right` | | X 605..670, Y 0..650, Z 205..1105 |
| `SHELL_wall_back` | insulated back wall with the pad opening | X 65..605, Y 585..650, Z 205..1105 |
| `SHELL_pad_opening` | rectangular cut through `SHELL_wall_back`, lined with 3 mm PVC on its four faces | X 85..585, Y 585..650, Z 415..815 (500 wide × 400 high) |
| `SHELL_door_opening` | the front of the chamber is entirely open; the 65 mm ring formed by floor, roof and side walls is the door frame face at Y 0 | X 65..605, Z 205..1105 |
| `SHELL_gasket_door` | EPDM D-profile 10 × 10 mm, glued to the frame face at Y 0, ring centred 20 mm outside the opening edge | ring outer X 35..635, Z 175..1135; ring inner X 55..615, Z 195..1115; Y -10..0 |
| `SHELL_floor_drain` | 20 mm PVC tank fitting through the floor, with 12 mm hose stub below | axis Z, centre (335, 560), Z 130..210 |
| `SHELL_gland_chamber_sensor` | M16 cable gland through right wall | axis X, centre (Y 325, Z 510), X 605..680 |
| `SHELL_gland_pulp_probe` | M16 cable gland through right wall | axis X, centre (Y 400, Z 700), X 605..680 |
| `SHELL_hole_fan_1` | round hole through roof | axis Z, centre (185, 205), dia 118 |
| `SHELL_hole_fan_2` | round hole through roof | axis Z, centre (485, 205), dia 118 |

### Group C: door (collection `C_door`)

Plug-type insulated door, hinged on the left, opens toward -Y.

| Name | Description | Size | Position (closed) |
|------|-------------|------|-------------------|
| `DOOR_face` | 12 mm plywood, painted white outside | 620 × 12 × 980 | X 25..645, Y -12..0, Z 165..1145 |
| `DOOR_plug` | 50 mm EPS + 3 mm PVC liner on the inner face and the four edges | 536 × 53 × 896 | X 67..603, Y 0..53, Z 207..1103 |
| `DOOR_hinge_1` | stainless butt hinge 75 × 50, knuckle axis vertical at X 25, Y -6 | | Z 330..405 |
| `DOOR_hinge_2` | same | | Z 905..980 |
| `DOOR_latch_1` | draw latch (toggle), body on door face, keeper on right wall exterior | body 60 × 20 × 25 | body centre (630, -12, 370), keeper on X 670 face at Y 0..30 |
| `DOOR_latch_2` | same | | body centre (630, -12, 940) |
| `DOOR_handle` | D-handle stainless, 120 long | | axis Z, centre (600, -35), Z 590..710 |
| `DOOR_label` | printed label plate 100 × 40 | | X 285..385, Y -13..-12, Z 1080..1120 |

Hinge line: X = 25, Y = -6. Rotate `C_door` about this line by up to 120° to open. The door face overlaps the frame by 40 mm on all sides and compresses `SHELL_gasket_door`.

### Group D: rear pad module (collection `D_padmodule`)

Uninsulated plywood box behind the back wall. Contains the pad cassette with its own water distributor, the sump, pump, float switch, fill port, overflow and inlet grille. Everything in this group is designed to be wet.

**Pad.** 150 mm deep cellulose honeycomb, type 7090 (7 mm flute height, flutes crossing at 45° and 15°), the same commodity pad used in poultry houses and greenhouses. It is rigid and self-supporting, so the cassette needs no mesh. Install it so the steep 45° flutes slope **downward toward the air-inlet face** (+Y side); this drains water toward the incoming air and keeps droplets out of the chamber. In the model, show the flutes on the two large faces as a crossed diagonal texture at 45° and 15°, or as a bump map.

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `PAD_side_left` | 12 mm plywood, painted | 12 × 210 × 1030 | X 0..12, Y 650..860, Z 140..1170 |
| `PAD_side_right` | same | | X 658..670, Y 650..860, Z 140..1170 |
| `PAD_floor` | 12 mm plywood, PVC-lined top | 646 × 210 × 12 | X 12..658, Y 650..860, Z 140..152 |
| `PAD_top_side_L` | 12 mm plywood strip, part of the top frame around the hatch | 53 × 210 × 12 | X 12..65, Y 650..860, Z 1158..1170 |
| `PAD_top_side_R` | same | | X 605..658, Y 650..860, Z 1158..1170 |
| `PAD_top_rear` | 12 mm plywood strip | 540 × 38 × 12 | X 65..605, Y 822..860, Z 1158..1170 |
| `PAD_hatch_opening` | open area bounded by the shell back wall and the three top strips | | X 65..605, Y 650..822 |
| `PAD_hatch_lid` | 12 mm plywood lid, 10 mm foam gasket on underside; overlaps the shell roof by 10 mm at the front and the top strips at the sides and rear | 560 × 190 × 12 | X 55..615, Y 640..830, Z 1170..1182 |
| `PAD_hatch_latch_L`, `_R` | toggle latches on `PAD_side_*` exterior, keepers on lid ends | | centres (12, 735, 1160) and (658, 735, 1160) |
| `PAD_rear_upper` | 12 mm plywood rear panel, fixed, with inlet opening | 670 × 12 × 790 | X 0..670, Y 848..860, Z 380..1170 |
| `PAD_rear_lower` | 12 mm plywood rear panel, removable (4 screws) for sump access | 670 × 12 × 240 | X 0..670, Y 848..860, Z 140..380 |
| `PAD_inlet_opening` | cut in `PAD_rear_upper` | | X 75..595, Z 405..825 |
| `PAD_inlet_screen` | aluminium insect screen 1 mm mesh stapled inside the opening | 540 × 1 × 440 | X 65..605, Y 847..848, Z 395..835 |
| `PAD_inlet_louver` | external plastic louver grille (rain and sun shield) with 10 slats angled 30° down-outward | 560 × 20 × 460 | X 55..615, Y 860..880, Z 385..845 |
| `PAD_guide_left` | vertical cassette guide, PVC U-channel 170 wide (Y) × 12 deep (X), open toward the cassette | 5 × 170 × 518 | web X 70..75, Y 652..822, Z 352..870; side flanges X 65..75 at Y 652 and Y 822 |
| `PAD_guide_right` | mirror | | web X 595..600, Y 652..822, Z 352..870 |
| `PAD_cassette_stop_L`, `_R` | aluminium angle 25 × 25 × 3, 170 long, the cassette rests on these | | X 75..100 and X 570..595, Y 652..822, horizontal leg Z 402..405, vertical leg down to Z 380 |
| `PAD_cassette_frame` | aluminium angle 20 × 20 × 2: two 520 × 420 rectangles (front and back faces) joined at the corners by four 160 mm spacers. The bottom members are notched every 50 mm so water drains straight down | 520 × 160 × 420 | X 75..595, Y 657..817, Z 405..825 |
| `PAD_cassette_media` | cellulose 7090 block, cut from a standard sheet with a fine saw | 500 × 150 × 400 | X 85..585, Y 662..812, Z 415..815 |
| `PAD_cassette_gasket` | 10 mm closed-cell foam strip on the front frame face, seals against the back wall around `SHELL_pad_opening` so no air bypasses the pad | ring 520 × 420 outer, 500 × 400 inner, 7 mm thick | X 75..595, Y 650..657, Z 405..825 |
| `PAD_cassette_cap` | water distribution cap: 1 mm aluminium sheet folded into an inverted U that covers the whole pad top; open underneath; riveted to the frame | 520 × 160 × 45 | X 75..595, Y 657..817, Z 820..865 |
| `PAD_distributor_pipe` | 1/2 in PVC pipe (21.3 OD) inside the cap, 20 holes of 2.5 mm at 25 mm pitch facing **up** (+Z). Water jets hit the cap roof and rain evenly onto the full pad top. Left end capped, right end has a 90° elbow turning up through the cap top | 500 long | axis X, centre (Y 737, Z 840), X 85..585 |
| `PAD_distributor_riser` | 1/2 in PVC stub from the elbow up through the cap top | 21.3 OD × 40 | axis Z, centre (570, 737), Z 850..890 |
| `PAD_quick_coupler` | 1/2 in garden-hose quick coupler, male half on the riser, female half on the hose; unplug before lifting the cassette | 30 dia × 45 | axis Z, centre (570, 737), Z 890..935 |
| `PAD_cassette_handles` | two strap loops riveted to the cap top | | at X 150 and X 450, Y 737, Z 865..900 |
| `PAD_hose` | 12 mm ID clear vinyl hose, pump to quick coupler. Runs up the right side of the module between the guide and the side wall, then over the guide top | | spline (585, 782, 210) → (630, 800, 400) → (630, 800, 950) → (570, 737, 950) → (570, 737, 935) |
| `PAD_hose_valve` | 1/2 in inline ball valve, flow trim | 60 long | centre (630, 800, 600), axis Z |
| `PAD_sump` | tank fabricated from 5 mm PVC sheet, open top, solvent-welded; covers the whole cassette footprint so no drip tray is needed | 540 × 190 × 200 external | X 65..605, Y 655..845, Z 152..352 |
| `PAD_sump_water` | water body (for cut-away renders), working level 125 mm | 530 × 180 × 125 | X 70..600, Y 660..840, Z 157..282 |
| `PAD_pump` | 12 V brushless DC submersible pump, 300-500 L/h at 1 m head, 8-12 W, about 70 × 50 × 55, 1/2 in outlet on top | | X 535..595, Y 760..810, Z 157..212 |
| `PAD_float_switch` | vertical-stem float switch, stem 80 tall, float 30 dia, switches at 40 mm water | | stem axis Z at (95, 750), Z 157..237 |
| `PAD_fill_port` | 40 mm PVC pipe through `PAD_rear_lower` and the sump rear wall, screw cap outside | 40 OD, 45 long | axis Y, centre (X 470, Z 320), Y 835..880 |
| `PAD_overflow` | 20 mm PVC pipe through the sump rear wall and `PAD_rear_lower`, hose barb outside; sets the maximum level at 148 mm | 20 OD, 45 long | axis Y, centre (X 110, Z 300), Y 835..880 |
| `PAD_sight_tube` | 8 mm clear vinyl tube on the exterior of the rear panel, between two barbs through the panel and the sump rear wall | | barbs at (560, Y 835..875, Z 165) and (560, Y 835..875, Z 340); tube vertical at X 560, Y 875 |
| `PAD_sight_scale` | printed level scale 0-14 L beside the tube | 20 × 1 × 180 | X 568..588, Y 860..861, Z 160..340 |
| `PAD_gland_pump` | M16 gland in `PAD_side_right` for pump, float-switch and ambient-sensor cables | | axis X, centre (Y 830, Z 1000), X 658..680 |
| `PAD_sensor_ambient` | SHT31 in a slotted 40 × 25 × 15 housing, in the inlet air behind the pad, shielded from splash by the cap overhang | | X 610..650, Y 825..840, Z 880..905 |
| `PAD_cable_ambient` | sensor cable to `PAD_gland_pump` | | spline (630, 832, 905) → (658, 830, 1000) |

Air path through this group: ambient air enters `PAD_inlet_louver` at Y 880, passes the screen at Y 848, crosses the 30 mm gap (Y 817..847), goes through `PAD_cassette_media` from back to front (-Y), through `SHELL_pad_opening`, into the chamber.

Water path: sump → pump → hose → valve → quick coupler → distributor pipe → jets hit the cap → rain onto the pad top → down through the flutes → notched frame bottom → back into the sump.

### Group E: roof fans and hood (collection `E_fans`)

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `FAN_1` | 120 × 120 × 25 mm 12 V DC 4-pin PWM axial fan, exhausting +Z | | X 125..245, Y 145..265, Z 1170..1195 |
| `FAN_2` | same | | X 425..545, Y 145..265, Z 1170..1195 |
| `FAN_1_guard`, `FAN_2_guard` | chrome wire finger guard 120 | 120 dia × 5 | Z 1195..1200, centred on each fan |
| `FAN_1_screen`, `FAN_2_screen` | insect screen disc under the roof hole, held by a 130 mm ring | 130 dia × 2 | Z 1103..1105 |
| `HOOD_top` | 12 mm plywood | 450 × 170 × 12 | X 110..560, Y 120..290, Z 1218..1230 |
| `HOOD_front` | 12 mm plywood | 450 × 12 × 48 | X 110..560, Y 120..132, Z 1170..1218 |
| `HOOD_back` | 12 mm plywood | 450 × 12 × 48 | X 110..560, Y 278..290, Z 1170..1218 |
| `HOOD_end_left` | 12 mm plywood with a 120 × 30 slot covered by insect screen, air leaves here | 12 × 146 × 48 | X 110..122, Y 132..278, Z 1170..1218 |
| `HOOD_end_right` | same, mirror | | X 548..560, Y 132..278, Z 1170..1218 |
| `HOOD_slot_L`, `HOOD_slot_R` | 120 × 30 openings in the end plates | | Y 145..265, Z 1180..1210 |
| `FAN_conduit` | 16 mm PVC conduit from the hood's right end to the bay's top, carries two 4-wire fan cables | | spline: (560, 205, 1176) to (690, 200, 1170) to bay interior |

Fan flow is upward through the roof holes into the hood and out sideways through the two end slots. The hood keeps rain and direct sun off the fans.

### Group F: crate rails and crates (collection `F_crates`)

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `RAIL_L1_left` | aluminium angle 40 × 40 × 3, horizontal leg inward (+X), vertical leg down against the liner | 340 long | X 65..105 (horizontal leg), Y 155..495, horizontal leg Z 252..255, vertical leg X 65..68, Z 215..255 |
| `RAIL_L1_right` | mirror | | X 565..605, vertical leg X 602..605 |
| `RAIL_L2_left`, `RAIL_L2_right` | same, level 2 | | horizontal leg Z 532..535, vertical leg Z 495..535 |
| `RAIL_L3_left`, `RAIL_L3_right` | same, level 3 | | horizontal leg Z 812..815, vertical leg Z 775..815 |
| `CRATE_1` | generic vented plastic crate, external 480 × 340 × 230, walls 4 mm, slotted sides, bottom grid; model with about 40 % open area | | X 95..575, Y 155..495, Z 255..485 |
| `CRATE_2` | same | | Z 535..765 |
| `CRATE_3` | same | | Z 815..1045 |
| `CRATE_x_load` | optional produce (generic 60 mm spheres, 10 kg per crate), fill to 100 mm depth | | inside each crate |

Clearances: 50 mm between crate top and next rail, 60 mm above crate 3 to the roof liner, 90 mm plenum in front of the crates (Y 65..155) and 90 mm behind (Y 495..585). The crate width may be 480-500 mm; rails bear 10-20 mm each side.

### Group G: electrical bay (collection `G_bay`)

Plywood box (9 mm) screwed to the right wall exterior. Display and buttons on the front face (Y 0 plane), hinged lid on the right face (X 820 plane), ventilation slots top and bottom with mesh.

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `BAY_back` | 9 mm ply, against the shell right wall | 9 × 250 × 350 | X 670..679, Y 0..250, Z 820..1170 |
| `BAY_front` | 9 mm ply with display and button cut-outs | 141 × 9 × 350 | X 679..820, Y 0..9, Z 820..1170 |
| `BAY_rear` | 9 mm ply | 141 × 9 × 350 | X 679..820, Y 241..250, Z 820..1170 |
| `BAY_bottom` | 9 mm ply with 4 vent slots 60 × 8 and screen | 141 × 232 × 9 | X 679..820, Y 9..241, Z 820..829 |
| `BAY_top` | 9 mm ply with 4 vent slots 60 × 8 and screen, and cable entry holes | 141 × 232 × 9 | X 679..820, Y 9..241, Z 1161..1170 |
| `BAY_lid` | 9 mm ply, hinged along its rear vertical edge, magnetic catch at front | 9 × 250 × 350 | X 811..820, Y 0..250, Z 820..1170 (closed) |
| `BAY_display` | 2.8 in TFT (320 × 240), active area 58 × 43, bezel 70 × 50 | | centre (745, 0, 1080), flush in `BAY_front` |
| `BAY_button_1..3` | 12 mm momentary pushbuttons (menu, up, down) | | centres (715, 0, 1010), (745, 0, 1010), (775, 0, 1010) |
| `BAY_led_status` | 5 mm bicolour LED | | centre (800, 0, 1080) |
| `BAY_switch_main` | 16 mm rocker switch, 12 V, ON/OFF | | centre (775, 0, 960) |
| `BAY_switch_mode` | 3-position rocker, AUTO / OFF / MANUAL, 12 V 10 A. MANUAL powers the fans at full speed and the pump directly, bypassing the controller, so the cooler keeps working if the electronics fail | 22 × 30 | centre (715, 0, 960) |
| `BAY_jack_dc` | 5.5 × 2.1 mm panel-mount DC barrel jack | | centre (700, 0, 900) on `BAY_front` |
| `BAY_fuse` | panel-mount 5 × 20 fuse holder, 3 A | | centre (790, 0, 900) on `BAY_front` |
| `BAY_socket_probe` | 3.5 mm jack for the pulp-temperature probe | | centre (745, 0, 900) |
| `BAY_pcb_plate` | 3 mm acrylic plate on 10 mm standoffs, carries the boards below | 120 × 200 × 3 | X 689..692, Y 25..225, Z 1000..1120 (mounted vertically against `BAY_back`, plate plane X) |
| `BAY_esp32` | ESP32 DevKitC, 55 × 28 × 12 | | on plate, centre (Y 70, Z 1090) |
| `BAY_buck_5v` | 12 V to 5 V buck module 43 × 21 × 14 | | on plate, centre (Y 70, Z 1030) |
| `BAY_mosfet_pump` | MOSFET module 33 × 24 × 12 | | on plate, centre (Y 140, Z 1090) |
| `BAY_mosfet_fans` | same (fan enable), PWM goes direct from ESP32 | | on plate, centre (Y 140, Z 1050) |
| `BAY_sd_module` | microSD module 40 × 24 × 10 | | on plate, centre (Y 200, Z 1090) |
| `BAY_terminal_block` | 12-way barrier terminal 12 × 80 × 15 | | on plate, centre (Y 140, Z 1010) |
| `BAY_battery` | reserved: 12 V 20 Ah SLA, 181 × 77 × 167 (open decision O1) | | X 700..777, Y 30..211, Z 829..996 |
| `BAY_charge_controller` | reserved: 10 A PWM solar charge controller 130 × 70 × 30, mounted on the inside of `BAY_lid` (open decision O1) | | X 780..810, Y 60..190, Z 900..1030 |
| `BAY_gland_top_1` | cable entry from `FAN_conduit` | | in `BAY_top` at (700, 200) |
| `BAY_gland_top_2` | cable entry from the `PAD_gland_pump` conduit | | in `BAY_top` at (700, 120) |
| `BAY_gland_back_1` | cable from `SHELL_gland_chamber_sensor` | | in `BAY_back` at (Y 60, Z 850) via 16 mm conduit along the right wall |
| `BAY_gland_back_2` | cable from `SHELL_gland_pulp_probe` | | in `BAY_back` at (Y 90, Z 850) |
| `BAY_conduit_side` | 16 mm PVC conduit on the right wall exterior from the bay top to the rear module gland | | spline: (700, 120, 1175) → (700, 250, 1175) → (680, 640, 1000) → (680, 830, 1000) |

### Group H: sensors inside the chamber (collection `H_sensors`)

| Name | Description | Position |
|------|-------------|----------|
| `SENS_chamber` | SHT31 in slotted housing 40 × 25 × 15, on the right liner between crate levels 1 and 2 | X 590..605, Y 313..353, Z 498..523 |
| `SENS_pad_outlet` | SHT31 in slotted housing, on the back liner just above the pad opening; measures pad-outlet air for the efficiency reading | X 315..355, Y 570..585, Z 820..845 |
| `SENS_pulp_probe` | DS18B20 stainless probe 6 dia × 50, on 1.5 m cable, stored in `CRATE_2` | probe centre (335, 325, 600) |
| `SENS_cable_chamber` | cable from `SENS_chamber` to `SHELL_gland_chamber_sensor` | (605, 325, 510) |

### Group I: labels and finish (collection `I_labels`)

| Name | Description | Position |
|------|-------------|----------|
| `LABEL_title` | project label plate on the door | see `DOOR_label` |
| `LABEL_inlet` | "AIR INLET - KEEP CLEAR 300 mm" above the rear louver | X 200..470, Y 860, Z 850..880 |
| `LABEL_fill` | "WATER FILL 12 L - NOT POTABLE" above the fill port | X 400..540, Y 860, Z 345..365 |
| `LABEL_bay` | "12 V DC 3 A" beside the DC jack | X 680..720, Y 0, Z 875..885 |
| `LABEL_mode` | "AUTO / OFF / MANUAL" under the mode switch | X 695..735, Y 0, Z 935..945 |

## 4. Section views (for orientation)

Side section at X = 335, looking from +X (left is front, right is back):

```
Z
1230 ┌─hood─┐
1182 │      │                        ┌──hatch lid Y 640..830──┐
1170 ┼──roof(65)────────────────────┼┴────────────────────────┴┐
1105 │ chamber ceiling   FAN↑       │  cap + distributor Z 820..865
     │ ┌crate3 815..1045┐           │ ┌────────────────┐ gap │← inlet air
     │ ├crate2 535..765 ┤  opening  ║ │ cellulose 7090 │ 30  │  louver Y 860..880
     │ ├crate1 255..485 ┤  415..815 ║ │ 150 deep       │     │
 405 │                              │ └────────────────┘     │
 352 │                              │ ┌──sump 152..352──────┐│
 205 ┼──floor(65)───────────────────┤ │ water 125 mm, 12 L  ││
 140 ┼ base frame 100..140 ─────────┴─┴─────────────────────┴┤
   0 ┴ casters ──────────────────────────────────────────────┘
     Y=0 door        Y=585 liner  Y=650  657  817   848 860
```

Plan at Z = 600 (looking down):

```
Y
880 ┌──── louver X 55..615 ───────────────────────────┐
860 ├──── rear panel ─────────────────────────────────┤
847 │      air gap                               hose │
817 │  ┌────── cassette X 75..595, 160 deep ──┐  ●     │
657 │  └──────────────────────────────────────┘ guides │
650 ├──back wall (65) with opening X 85..585──────────┤
585 │  chamber                                        │
495 │   ┌──────── crate X 95..575 ────────┐  SENS ●   │   ┌ bay X 670..820 (Z 820+)
155 │   └──────────────────────────────────┘          │   └ Y 0..250
 65 │  front plenum                                   │
  0 ├──────────── door (X 25..645 face) ──────────────┤
    X=0                                            X=670
```

## 5. Blender collection hierarchy

```
EvapCooler
├── A_base
├── B_shell
├── C_door            (pivot: hinge line X=25, Y=-6, axis Z)
├── D_padmodule
│   ├── D1_box        (sides, floor, top, rear panels, guides, hatch)
│   ├── D2_cassette   (frame, media, gasket, cap, distributor pipe, riser, coupler half, handles)  ← removable, slides +Z
│   ├── D3_water      (sump, water body, pump, float, hose, valve, fill, overflow, sight tube)
│   └── D4_inlet      (screen, louver, ambient sensor)
├── E_fans
├── F_crates          (rails, crates, optional load)
├── G_bay
├── H_sensors
└── I_labels
```

Suggested animations or exploded views: door swing (C_door), cassette lift (D2_cassette, +820 mm in Z to clear the hatch, after unplugging the quick coupler), crate pull-out (each crate -300 mm in Y), bay lid swing (BAY_lid, hinge along its rear vertical edge at X 820, Y 250).

## 6. Interference and clearance checks

* `DOOR_plug` (X 67..603, Z 207..1103) clears the opening (X 65..605, Z 205..1105) by 2 mm per side.
* `PAD_cassette_frame` (Y 657..817) sits in the guide slot (Y 652..822) with 5 mm play each side; its front gasket compresses 2 mm against the back wall at Y 650.
* The cassette with cap, riser and coupler (Z 405..935) lifts straight up through the hatch opening (X 65..605, Y 650..822). The hose is unplugged first; it crosses above the guide tops (Z 870) at Z 950.
* `PAD_cassette_media` (Z 415..815) exactly matches `SHELL_pad_opening` (Z 415..815, X 85..585), so the whole pad face is used and no air bypasses it.
* `PAD_pump` (X 535..595, Y 760..810) sits under the cassette's rear right corner, clear of the float switch (X 95) and the fill port (X 450..490).
* Fan holes (centres Y 205) lie over the front plenum; crates end at Y 155..495 so the fans draw from the front gap and the top of crate 3.
* `BAY_battery` (Z 829..996) sits below `BAY_pcb_plate` (Z 1000..1120) with 4 mm clearance.
* `HOOD` (X 110..560, Y 120..290) does not overlap the hatch lid (Y 640..830) or the bay (X 670+).
* `BAY_switch_mode` (centre X 715) and `BAY_switch_main` (centre X 775) sit side by side above the jack row at Z 900 with 30 mm between centres of adjacent parts.
* Caster swing radius 60 mm at each corner: no part below Z 100 within that radius.
* Rear louver needs 300 mm free space behind the unit for inlet air; the label says so.
