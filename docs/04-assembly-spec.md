# Assembly specification for 3D modelling (Blender handoff)

Complete dimensioned parts list for the student-scale evaporative cooling cabinet. Every part has a name, size, position, and material. Positions are the part's bounding box in the global frame unless stated as a centre.

## 1. Conventions

* **Units:** millimetres. In Blender set Scene > Units > Length = Millimeters, Unit Scale = 0.001, and model at 1 unit = 1 mm.
* **Axes:** right-handed, Z up. **X** runs left to right as seen by the operator standing in front of the door. **Y** runs from the front (door face) toward the back (pad module). **Z** runs from the floor upward. Blender's Front view (numpad 1) therefore shows the door.
* **Origin:** floor level (Z = 0, bottom of the casters), at the outside bottom-left-front corner of the main shell. The main shell occupies X 0 to 670, Y 0 to 650. Parts that protrude beyond it (rear module, electrical bay, hood, door face) have coordinates outside that range.
* **Bounding boxes** are written `X a..b, Y c..d, Z e..f`. Cylinders are given by axis, centre and diameter.
* **Naming:** `GROUP_part_variant`, e.g. `SHELL_wall_left_ply`. Blender collections follow the group letters in section 3.
* **Wall sandwich rule:** every insulated wall is three layers, outside to inside: 12 mm plywood, 50 mm EPS, 3 mm PVC liner (65 mm total). Model each wall as one block with three sub-blocks, or as one block with a single material if layer detail is not needed. Layer thicknesses are listed once here and not repeated per part.
* **Materials and colours (sRGB hex):** plywood painted white exterior `#F2F2EE`; plywood natural (interior of bay, cassette hatch underside) `#C9A46B`; EPS foam `#FFFFFF` (only visible in cut-away); PVC liner white `#FAFAFA`; aluminium angle and mesh `#B8BCC0`; galvanised hardware cloth `#9EA3A8`; coconut coir `#7A5230`; PVC pipe grey `#8E8E8E`; sump PVC sheet dark grey `#4A4A4A`; fan black `#1E1E1E`; fan guard chrome `#C8C8C8`; crates green `#2E8B57`; casters black rubber `#202020` with grey plate `#8A8A8A`; EPDM gasket black `#151515`; TFT display glass `#0B0B0B`; stainless hinges and latches `#D0D2D5`; cables black `#111111`; clear vinyl sight tube `#DDEEFF` at 40 % alpha.

## 2. Overall envelope

| Item | Value |
|------|-------|
| Main shell (insulated box) | X 0..670, Y 0..650, Z 140..1170 |
| Rear pad module | X 0..670, Y 650..785, Z 140..1170 |
| Electrical bay | X 670..820, Y 0..250, Z 820..1170 |
| Fan rain hood | X 110..560, Y 120..290, Z 1170..1230 |
| Cassette hatch lid | X 55..615, Y 652..782, Z 1170..1182 |
| Door face (closed) | X 25..645, Y -12..0, Z 165..1145 |
| Casters | Z 0..100 |
| Overall footprint including door face and bay | X 0..820, Y -12..785 |
| Overall height to top of hood | 1230 |
| Chamber interior (clear) | X 65..605, Y 65..585, Z 205..1105 (540 × 520 × 900, 0.253 m³) |
| Mass estimate, empty with water | about 62 kg |

Wall centre-plane reference: shell centre X = 335, chamber centre Y = 325.

## 3. Parts by group

### Group A: base and casters (collection `A_base`)

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `BASE_rail_front` | 40 × 40 lumber, painted | 670 × 40 × 40 | X 0..670, Y 0..40, Z 100..140 |
| `BASE_rail_back` | same | 670 × 40 × 40 | X 0..670, Y 745..785, Z 100..140 |
| `BASE_rail_left` | same | 40 × 705 × 40 | X 0..40, Y 40..745, Z 100..140 |
| `BASE_rail_right` | same | 40 × 705 × 40 | X 630..670, Y 40..745, Z 100..140 |
| `BASE_rail_mid` | cross member under the shell/rear-module joint | 590 × 40 × 40 | X 40..630, Y 630..670, Z 100..140 |
| `BASE_caster_FL` | 75 mm swivel caster with brake, 60 × 60 plate, wheel 75 dia × 25 wide | plate Z 96..100 | plate centre (50, 50), wheel axis along X at Z 37.5 |
| `BASE_caster_FR` | same | | plate centre (620, 50) |
| `BASE_caster_BL` | same | | plate centre (50, 735) |
| `BASE_caster_BR` | same | | plate centre (620, 735) |

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

Uninsulated plywood box behind the back wall. Contains the pad cassette, drip pipe, sump, pump, float switch, fill port, overflow and inlet grille. Everything in this group is designed to be wet.

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `PAD_side_left` | 12 mm plywood, painted | 12 × 135 × 1030 | X 0..12, Y 650..785, Z 140..1170 |
| `PAD_side_right` | same | | X 658..670, Y 650..785, Z 140..1170 |
| `PAD_floor` | 12 mm plywood, PVC-lined top | 646 × 135 × 12 | X 12..658, Y 650..785, Z 140..152 |
| `PAD_top` | 12 mm plywood with hatch opening | 646 × 135 × 12 | X 12..658, Y 650..785, Z 1158..1170 |
| `PAD_hatch_opening` | cut in `PAD_top` | | X 65..605, Y 662..772 |
| `PAD_hatch_lid` | 12 mm plywood lid, 10 mm foam gasket on underside, two toggle latches | 560 × 130 × 12 | X 55..615, Y 652..782, Z 1170..1182 |
| `PAD_hatch_latch_L`, `_R` | toggle latches on `PAD_side_*` exterior, keepers on lid ends | | centres (12, 717, 1160) and (658, 717, 1160) |
| `PAD_rear_upper` | 12 mm plywood rear panel, fixed, with inlet opening | 670 × 12 × 790 | X 0..670, Y 773..785, Z 380..1170 |
| `PAD_rear_lower` | 12 mm plywood rear panel, removable (4 screws) for sump access | 670 × 12 × 240 | X 0..670, Y 773..785, Z 140..380 |
| `PAD_inlet_opening` | cut in `PAD_rear_upper` | | X 75..595, Z 405..825 |
| `PAD_inlet_screen` | aluminium insect screen 1 mm mesh stapled inside the opening | 540 × 1 × 440 | X 65..605, Y 772..773, Z 395..835 |
| `PAD_inlet_louver` | external plastic louver grille (rain and sun shield) with 10 slats angled 30° down-outward | 560 × 20 × 460 | X 55..615, Y 785..805, Z 385..845 |
| `PAD_guide_left` | vertical cassette guide, PVC U-channel 100 wide (Y) × 12 deep (X), open toward the cassette | 5 × 100 × 810 | X 70..75, Y 652..752, Z 352..1162 (with side flanges X 65..75 at Y 652 and 752) |
| `PAD_guide_right` | mirror | | X 595..600, Y 652..752, Z 352..1162 |
| `PAD_cassette_stop_L`, `_R` | aluminium angle 25 × 25 × 3, 100 long, cassette rests on these | | X 75..100 and 570..595, Y 652..752, Z 402..405 (horizontal leg) with vertical leg down to Z 380 |
| `PAD_cassette_frame` | aluminium angle 20 × 20 × 2 frame, front and back rectangles joined by 75 mm spacers, forming an open box | 520 × 85 × 420 | X 75..595, Y 657..742, Z 405..825 |
| `PAD_cassette_mesh_front` | galvanised hardware cloth 12.7 mm, on chamber-facing face | 520 × 1 × 420 | Y 657..658 |
| `PAD_cassette_mesh_back` | same, on inlet-facing face | | Y 741..742 |
| `PAD_cassette_media` | coconut coir, packed 80-100 kg/m³ (model as a rough solid) | 500 × 75 × 400 | X 85..585, Y 662..737, Z 415..815 |
| `PAD_cassette_gasket` | 10 mm closed-cell foam strip on the front frame face, seals against the back wall around `SHELL_pad_opening` | ring 520 × 420 outer, 500 × 400 inner, 7 mm thick | Y 650..657 |
| `PAD_cassette_handles` | two rope or strap loops on the top frame member | | at X 150 and X 520, Z 825..860 |
| `PAD_drip_pipe` | 1/2 in PVC pipe (21.3 OD), 20 holes 2 mm dia at 25 mm pitch, holes angled 30° from -Z toward -Y so water lands on the cassette top face; left end capped, right end 90° elbow to hose. Sits just behind the cassette back face so the cassette lifts out without touching it | 520 long | axis X, centre (Y 753, Z 845), X 75..595 |
| `PAD_drip_pipe_clips` | two pipe saddle clips on `PAD_side_*` inner faces | | at X 12 and X 658, Y 753, Z 845 |
| `PAD_drip_hose` | 8 mm ID clear vinyl hose from pump to drip-pipe elbow, runs up the right side of the module between guide and side wall | | from (575, 712, 197) up to (620, 753, 845), model as a spline |
| `PAD_hose_valve` | mini ball valve 8 mm inline, flow trim | 45 long | centre (620, 712, 600) |
| `PAD_sump` | tank fabricated from 5 mm PVC sheet, open top, solvent-welded | 540 × 115 × 200 external | X 65..605, Y 655..770, Z 152..352 |
| `PAD_sump_water` | water body (for cut-away renders), working level 125 mm | 530 × 105 × 125 | X 70..600, Y 660..765, Z 157..282 |
| `PAD_pump` | 12 V submersible pump 3-5 W, 240 L/h, 60 × 45 × 40 with 8 mm barb outlet on top | | X 545..605, Y 690..735, Z 157..197 |
| `PAD_float_switch` | vertical-stem float switch, stem 80 tall, float 30 dia, switches at 40 mm water | | stem axis Z at (95, 712), Z 157..237 |
| `PAD_fill_port` | 40 mm PVC pipe through `PAD_rear_lower` and the sump rear wall, screw cap outside | 40 OD, 60 long | axis Y, centre (540, Z 320), Y 765..825 |
| `PAD_overflow` | 20 mm PVC pipe through sump rear wall and `PAD_rear_lower`, hose barb outside | 20 OD, 60 long | axis Y, centre (100, Z 300), Y 765..825 |
| `PAD_sight_tube` | 8 mm clear vinyl tube on exterior of the rear panel, between two barbs through the panel and sump rear wall | | barbs at (600, Y 765..800, Z 165) and (600, Y 765..800, Z 340); tube vertical at X 600, Y 800 |
| `PAD_sight_scale` | printed level scale 0-9 L beside the tube | 20 × 1 × 180 | X 608..628, Y 785..786, Z 160..340 |
| `PAD_gland_pump` | M16 gland in `PAD_side_right` for pump and float-switch cables | | axis X, centre (Y 700, Z 900), X 658..680 |
| `PAD_sensor_ambient` | SHT31 in a slotted 40 × 25 × 15 housing, in the inlet-side air beside the cassette | | X 610..650, Y 750..765, Z 790..815 |
| `PAD_cable_ambient` | sensor cable to `PAD_gland_pump` | | spline from (630, 758, 815) to (658, 700, 900) |

Air path through this group: ambient air enters `PAD_inlet_louver` at Y 785+, passes the screen, crosses the 31 mm gap (Y 742..773), goes through `PAD_cassette_media` from back to front (-Y), through `SHELL_pad_opening`, into the chamber.

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
| `BAY_switch_main` | 16 mm rocker switch, 12 V | | centre (745, 0, 960) |
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
| `BAY_gland_top_2` | cable entry from `PAD_gland_pump` conduit | | in `BAY_top` at (700, 120) |
| `BAY_gland_back_1` | cable from `SHELL_gland_chamber_sensor` | | in `BAY_back` at (Y 60, Z 850) via 16 mm conduit along the right wall |
| `BAY_gland_back_2` | cable from `SHELL_gland_pulp_probe` | | in `BAY_back` at (Y 90, Z 850) |
| `BAY_conduit_side` | 16 mm PVC conduit on the right wall exterior from the bay to the rear module gland | | spline: (680, 250, 900) to (680, 640, 900) to (680, 700, 900) |

### Group H: sensors inside the chamber (collection `H_sensors`)

| Name | Description | Position |
|------|-------------|----------|
| `SENS_chamber` | SHT31 in slotted housing 40 × 25 × 15, on the right liner between crate levels 1 and 2 | X 590..605, Y 313..353, Z 498..523 |
| `SENS_pad_outlet` | optional SHT31, on the back liner just above the pad opening | X 315..355, Y 570..585, Z 820..845 |
| `SENS_pulp_probe` | DS18B20 stainless probe 6 dia × 50, on 1.5 m cable, stored in `CRATE_2` | probe centre (335, 325, 600) |
| `SENS_cable_chamber` | cable from `SENS_chamber` to `SHELL_gland_chamber_sensor` | (605, 325, 510) |

### Group I: labels and finish (collection `I_labels`)

| Name | Description | Position |
|------|-------------|----------|
| `LABEL_title` | project label plate on the door | see `DOOR_label` |
| `LABEL_inlet` | "AIR INLET - KEEP CLEAR 300 mm" on the rear louver | X 200..470, Y 805, Z 850..880 |
| `LABEL_fill` | "WATER FILL 8 L" beside the fill port | X 480..600, Y 785, Z 340..360 |
| `LABEL_bay` | "12 V DC 3 A" beside the DC jack | X 680..720, Y 0, Z 875..885 |

## 4. Section views (for orientation)

Side section at X = 335, looking from +X (left is front, right is back):

```
Z
1230 ┌─hood─┐
1170 ┼──roof(65)────────────────────┬─PAD_top─┬ hatch lid
1105 │ chamber ceiling        FAN↑  │ drip pipe Z845
     │ ┌crate3 815..1045┐           │ ┌cassette┐  ← inlet air (from +Y)
     │ ├crate2 535..765 ┤           ║ │ coir   │  louver on rear panel
     │ ├crate1 255..485 ┤  pad opening 415..815 │
 205 ┼──floor(65)──────────────────┬─┴sump 152..352┴─┐
 140 ┼ base frame 100..140 ───────────────────────────┤
   0 ┴ casters ───────────────────────────────────────┘
     Y=0 door        Y=585 back liner  Y=650   Y=785
```

Plan at Z = 600 (looking down):

```
Y
785 ┌──── rear panel with louver X 75..595 ───────────┐
742 │      air gap                                     │
657 │  ┌────── cassette X 75..595 ──────┐  guides      │
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
│   ├── D2_cassette   (frame, meshes, media, gasket, handles)  ← removable, slides +Z
│   ├── D3_water      (sump, water body, pump, float, hose, valve, drip pipe, fill, overflow, sight tube)
│   └── D4_inlet      (screen, louver, ambient sensor)
├── E_fans
├── F_crates          (rails, crates, optional load)
├── G_bay
├── H_sensors
└── I_labels
```

Suggested animations or exploded views: door swing (C_door), cassette lift (D2_cassette, +420 mm in Z to clear the hatch), crate pull-out (each crate -300 mm in Y), bay lid swing (BAY_lid, hinge along its rear vertical edge at X 820, Y 250).

## 6. Interference and clearance checks

* `DOOR_plug` (X 67..603, Z 207..1103) clears the opening (X 65..605, Z 205..1105) by 2 mm per side.
* `PAD_cassette_frame` (Y 657..742) sits in the guide slot (Y 652..752) with 5 mm play each side; its front gasket compresses 2 mm against the back wall at Y 650.
* `PAD_drip_pipe` (Y 742..764 envelope, Z 834..856) sits behind the cassette back face (Y 742) and above the cassette top (Z 825), so the cassette lifts straight up through the hatch without touching the pipe. The 31 mm inlet air gap is partly occupied by the pipe over a 22 mm band; this is acceptable because the inlet opening is 440 mm tall.
* Fan holes (centres Y 205) lie over the front plenum; crates end at Y 155..495 so the fans draw from the front gap and the top of crate 3.
* `BAY_battery` (Z 829..996) sits below `BAY_pcb_plate` (Z 1000..1120) with 4 mm clearance.
* `HOOD` (X 110..560) does not overlap the hatch lid (Y 652..782) or the bay (X 670+).
* Caster swing radius 60 mm at each corner: no part below Z 100 within that radius.
* Rear louver needs 300 mm free space behind the unit for inlet air; the label says so.
