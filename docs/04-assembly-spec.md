# Assembly specification for 3D modelling (Blender handoff)

Complete dimensioned parts list for the student-scale evaporative cooling cabinet. Every part has a name, size, position, and material. Positions are the part's bounding box in the global frame unless stated as a centre.

Revision: concept **Option B - Scale**. Half-capacity layout (12-17 kg in one standard crate plus one slatted shelf), wall adapter with backup battery, and the crate standing on a built-in weighing platform (the "sentinel crate") so the cooler can measure the produce's own weight loss.

## 1. Conventions

* **Units:** millimetres. In Blender set Scene > Units > Length = Millimeters, Unit Scale = 0.001, and model at 1 unit = 1 mm.
* **Axes:** right-handed, Z up. **X** runs left to right as seen by the operator standing in front of the door. **Y** runs from the front (door face) toward the back (pad module). **Z** runs from the floor upward. Blender's Front view (numpad 1) therefore shows the door.
* **Origin:** floor level (Z = 0, bottom of the casters), at the outside bottom-left-front corner of the main shell. The main shell occupies X 0 to 670, Y 0 to 650. Parts that protrude beyond it (rear module, electrical bay, hood, door face) have coordinates outside that range.
* **Bounding boxes** are written `X a..b, Y c..d, Z e..f`. Cylinders are given by axis, centre and diameter.
* **Naming:** `GROUP_part_variant`. Blender collections follow the group letters in section 3.
* **Wall sandwich rule:** every insulated wall is three layers, outside to inside: 12 mm plywood, 50 mm EPS, 3 mm PVC liner (65 mm total). Model each wall as one block with three sub-blocks, or as one block with a single material if layer detail is not needed.
* **Materials and colours (sRGB hex):** plywood painted white exterior `#F2F2EE`; plywood natural (interior of bay) `#C9A46B`; EPS foam `#FFFFFF` (only visible in cut-away); PVC liner white `#FAFAFA`; aluminium angle and sheet `#B8BCC0`; load cell anodised silver `#C0C4C8` with a black potting face `#1A1A1A`; HDPE hardpoint and stops off-white `#EDEBE4`; rubber overload-stop tips black `#202020`; cellulose pad kraft brown `#A9743A` (flutes darker `#7E5424`); PVC pipe grey `#8E8E8E`; sump PVC sheet dark grey `#4A4A4A`; fan black `#1E1E1E`; fan guard chrome `#C8C8C8`; crate green `#2E8B57`; shelf slats polypropylene white `#E8E8E8`; casters black rubber `#202020` with grey plate `#8A8A8A`; EPDM gasket black `#151515`; TFT display glass `#0B0B0B`; stainless hinges and latches `#D0D2D5`; cables black `#111111`; clear vinyl hose and sight tube `#DDEEFF` at 40 % alpha.

## 2. Overall envelope

| Item | Value |
|------|-------|
| Main shell (insulated box) | X 0..670, Y 0..650, Z 140..860 |
| Rear pad module | X 0..670, Y 650..860, Z 140..860 |
| Electrical bay | X 670..820, Y 0..250, Z 510..860 |
| Fan rain hood | X 110..560, Y 120..290, Z 860..920 |
| Cassette hatch lid | X 55..615, Y 640..830, Z 860..872 |
| Door face (closed) | X 25..645, Y -12..0, Z 165..835 |
| Casters | Z 0..100 |
| Overall footprint including door face, bay and rear louver | X 0..820, Y -12..880 |
| Overall height to top of hood | 920 |
| Chamber interior (clear) | X 65..605, Y 65..585, Z 205..795 (540 × 520 × 590, 0.166 m³) |
| Capacity | one standard crate (8-10 kg) plus one shelf of loose produce (4-7 kg): 12-17 kg |
| Mass estimate, with 10 L of water and the battery, no produce | about 53 kg |

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
| `SHELL_roof` | insulated roof, with two fan holes (see Group E) | X 0..670, Y 0..650, Z 795..860 |
| `SHELL_wall_left` | | X 0..65, Y 0..650, Z 205..795 |
| `SHELL_wall_right` | | X 605..670, Y 0..650, Z 205..795 |
| `SHELL_wall_back` | insulated back wall with the pad opening | X 65..605, Y 585..650, Z 205..795 |
| `SHELL_pad_opening` | rectangular cut through `SHELL_wall_back`, lined with 3 mm PVC on its four faces | X 85..585, Y 585..650, Z 360..660 (500 wide × 300 high) |
| `SHELL_door_opening` | the front of the chamber is entirely open; the 65 mm ring formed by floor, roof and side walls is the door frame face at Y 0 | X 65..605, Z 205..795 |
| `SHELL_gasket_door` | EPDM D-profile 10 × 10 mm, glued to the frame face at Y 0, ring centred 20 mm outside the opening edge | ring outer X 35..635, Z 175..825; ring inner X 55..615, Z 195..805; Y -10..0 |
| `SHELL_hardpoint` | HDPE block set into the floor in place of the EPS, under the load cell, so the scale bolts to something solid. The PVC liner runs over it; the two bolt holes are sealed with silicone | X 240..430, Y 290..360, Z 152..202 |
| `SHELL_floor_drain` | 20 mm PVC tank fitting through the floor, with 12 mm hose stub below | axis Z, centre (335, 560), Z 130..210 |
| `SHELL_gland_chamber_sensor` | M16 cable gland through the right wall, exiting directly inside the electrical bay | axis X, centre (Y 120, Z 530), X 605..690 |
| `SHELL_gland_pulp_probe` | M16 cable gland through the right wall, exiting directly inside the electrical bay | axis X, centre (Y 200, Z 560), X 605..690 |
| `SHELL_gland_loadcell` | M16 cable gland through the right wall for the load-cell cable, exiting directly inside the electrical bay | axis X, centre (Y 230, Z 590), X 605..690 |
| `SHELL_hole_fan_1` | round hole through roof | axis Z, centre (185, 205), dia 118 |
| `SHELL_hole_fan_2` | round hole through roof | axis Z, centre (485, 205), dia 118 |

### Group C: door (collection `C_door`)

Plug-type insulated door, hinged on the left, opens toward -Y.

| Name | Description | Size | Position (closed) |
|------|-------------|------|-------------------|
| `DOOR_face` | 12 mm plywood, painted white outside | 620 × 12 × 670 | X 25..645, Y -12..0, Z 165..835 |
| `DOOR_plug` | 50 mm EPS + 3 mm PVC liner on the inner face and the four edges | 536 × 53 × 586 | X 67..603, Y 0..53, Z 207..793 |
| `DOOR_hinge_1` | stainless butt hinge 75 × 50, knuckle axis vertical at X 25, Y -6 | | Z 280..355 |
| `DOOR_hinge_2` | same | | Z 645..720 |
| `DOOR_latch_1` | draw latch (toggle), body on door face, keeper on right wall exterior | body 60 × 20 × 25 | body centre (630, -12, 320), keeper on X 670 face at Y 0..30 |
| `DOOR_latch_2` | same | | body centre (630, -12, 680) |
| `DOOR_handle` | D-handle stainless, 120 long | | axis Z, centre (600, -35), Z 440..560 |
| `DOOR_label` | printed label plate 100 × 40 | | X 285..385, Y -13..-12, Z 775..815 |

Hinge line: X = 25, Y = -6. Rotate `C_door` about this line by up to 120° to open. The door face overlaps the frame by 40 mm on all sides and compresses `SHELL_gasket_door`.

### Group D: rear pad module (collection `D_padmodule`)

Uninsulated plywood box behind the back wall. Contains the pad cassette with its own water distributor, the sump, pump, float switch, fill port, overflow and inlet grille. Everything in this group is designed to be wet.

**Pad.** 150 mm deep cellulose honeycomb, type 7090 (7 mm flute height, flutes crossing at 45° and 15°), the same commodity pad used in poultry houses and greenhouses. It is rigid and self-supporting, so the cassette needs no mesh. Install it so the steep 45° flutes slope **downward toward the air-inlet face** (+Y side); this drains water toward the incoming air and keeps droplets out of the chamber. In the model, show the flutes on the two large faces as a crossed diagonal texture at 45° and 15°, or as a bump map.

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `PAD_side_left` | 12 mm plywood, painted; butts against the rear panels | 12 × 198 × 720 | X 0..12, Y 650..848, Z 140..860 |
| `PAD_side_right` | same | | X 658..670, Y 650..848, Z 140..860 |
| `PAD_floor` | 12 mm plywood, PVC-lined top | 646 × 198 × 12 | X 12..658, Y 650..848, Z 140..152 |
| `PAD_top_side_L` | 12 mm plywood strip, part of the top frame around the hatch | 53 × 198 × 12 | X 12..65, Y 650..848, Z 848..860 |
| `PAD_top_side_R` | same | | X 605..658, Y 650..848, Z 848..860 |
| `PAD_top_rear` | 12 mm plywood strip | 540 × 26 × 12 | X 65..605, Y 822..848, Z 848..860 |
| `PAD_hatch_opening` | open area bounded by the shell back wall and the three top strips | | X 65..605, Y 650..822 |
| `PAD_hatch_lid` | 12 mm plywood lid, 10 mm foam gasket on underside; overlaps the shell roof by 10 mm at the front and the top strips at the sides and rear | 560 × 190 × 12 | X 55..615, Y 640..830, Z 860..872 |
| `PAD_hatch_latch_L`, `_R` | toggle latches on `PAD_side_*` exterior, keepers on lid ends | | centres (12, 735, 850) and (658, 735, 850) |
| `PAD_rear_upper` | 12 mm plywood rear panel, fixed, with inlet opening | 670 × 12 × 540 | X 0..670, Y 848..860, Z 320..860 |
| `PAD_rear_lower` | 12 mm plywood rear panel, removable (4 screws) for sump access | 670 × 12 × 180 | X 0..670, Y 848..860, Z 140..320 |
| `PAD_inlet_opening` | cut in `PAD_rear_upper` | | X 75..595, Z 350..670 |
| `PAD_inlet_screen` | aluminium insect screen 1 mm mesh stapled inside the opening | 540 × 1 × 340 | X 65..605, Y 847..848, Z 340..680 |
| `PAD_inlet_louver` | external plastic louver grille (rain and sun shield) with 8 slats angled 30° down-outward | 560 × 20 × 360 | X 55..615, Y 860..880, Z 330..690 |
| `PAD_guide_left` | vertical cassette guide, PVC U-channel 170 wide (Y) × 12 deep (X), open toward the cassette | 5 × 170 × 403 | web X 70..75, Y 652..822, Z 312..715; side flanges X 65..75 at Y 652 and Y 822 |
| `PAD_guide_right` | mirror | | web X 595..600, Y 652..822, Z 312..715 |
| `PAD_cassette_stop_L`, `_R` | aluminium angle 25 × 25 × 3, 170 long, the cassette rests on these | | X 75..100 and X 570..595, Y 652..822, horizontal leg Z 347..350, vertical leg down to Z 325 |
| `PAD_cassette_frame` | aluminium angle 20 × 20 × 2: two 520 × 320 rectangles (front and back faces) joined at the corners by four 160 mm spacers. The bottom members are notched every 50 mm so water drains straight down | 520 × 160 × 320 | X 75..595, Y 657..817, Z 350..670 |
| `PAD_cassette_media` | cellulose 7090 block, cut from a standard sheet with a fine saw | 500 × 150 × 300 | X 85..585, Y 662..812, Z 360..660 |
| `PAD_cassette_gasket` | 10 mm closed-cell foam strip on the front frame face, seals against the back wall around `SHELL_pad_opening` so no air bypasses the pad | ring 520 × 320 outer, 500 × 300 inner, 7 mm thick | X 75..595, Y 650..657, Z 350..670 |
| `PAD_cassette_cap` | water distribution cap: 1 mm aluminium sheet folded into an inverted U that covers the whole pad top; open underneath; riveted to the frame | 520 × 160 × 45 | X 75..595, Y 657..817, Z 665..710 |
| `PAD_distributor_pipe` | 1/2 in PVC pipe (21.3 OD) inside the cap, 20 holes of 2.5 mm at 25 mm pitch facing **up** (+Z). Water jets hit the cap roof and rain evenly onto the full pad top. Left end capped, right end has a 90° elbow turning up through the cap top | 500 long | axis X, centre (Y 737, Z 685), X 85..585 |
| `PAD_distributor_riser` | 1/2 in PVC stub from the elbow up through the cap top | 21.3 OD × 40 | axis Z, centre (570, 737), Z 695..735 |
| `PAD_quick_coupler` | 1/2 in garden-hose quick coupler, male half on the riser, female half on the hose; unplug before lifting the cassette | 30 dia × 45 | axis Z, centre (570, 737), Z 735..780 |
| `PAD_cassette_handles` | two strap loops riveted to the cap top | | at X 150 and X 450, Y 737, Z 710..745 |
| `PAD_hose` | 12 mm ID clear vinyl hose, pump to quick coupler. Runs up the right side of the module between the guide and the side wall, then over the guide top | | spline (585, 782, 212) → (630, 800, 350) → (630, 800, 800) → (570, 737, 800) → (570, 737, 780) |
| `PAD_hose_valve` | 1/2 in inline ball valve, flow trim | 60 long | centre (630, 800, 500), axis Z |
| `PAD_sump` | tank fabricated from 5 mm PVC sheet, open top, solvent-welded; covers the whole cassette footprint so no drip tray is needed | 540 × 190 × 160 external | X 65..605, Y 655..845, Z 152..312 |
| `PAD_sump_water` | water body (for cut-away renders), working level 105 mm | 530 × 180 × 105 | X 70..600, Y 660..840, Z 157..262 |
| `PAD_pump` | 12 V brushless DC submersible pump, 300-500 L/h at 1 m head, 8-12 W, about 70 × 50 × 55, 1/2 in outlet on top | | X 535..595, Y 760..810, Z 157..212 |
| `PAD_float_switch` | vertical-stem float switch, stem 80 tall, float 30 dia, switches at 40 mm water | | stem axis Z at (95, 750), Z 157..237 |
| `PAD_fill_port` | 32 mm PVC pipe through `PAD_rear_lower` and the sump rear wall, screw cap outside | 32 OD, 45 long | axis Y, centre (X 470, Z 290), Y 835..880 |
| `PAD_overflow` | 20 mm PVC pipe through the sump rear wall and `PAD_rear_lower`, hose barb outside; its invert at Z 272 sets the maximum level (115 mm, 11 L) | 20 OD, 45 long | axis Y, centre (X 110, Z 282), Y 835..880 |
| `PAD_sight_tube` | 8 mm clear vinyl tube on the exterior of the rear panel, between two barbs through the panel and the sump rear wall | | barbs at (560, Y 835..875, Z 165) and (560, Y 835..875, Z 300); tube vertical at X 560, Y 875 |
| `PAD_sight_scale` | printed level scale 0-11 L beside the tube | 20 × 1 × 140 | X 568..588, Y 860..861, Z 160..300 |
| `PAD_gland_pump` | M16 gland in `PAD_side_right` for pump, float-switch and ambient-sensor cables | | axis X, centre (Y 830, Z 780), X 658..680 |
| `PAD_sensor_ambient` | SHT31 in a slotted 40 × 25 × 15 housing, in the inlet air behind the pad, above the inlet opening and clear of splash | | X 610..650, Y 825..840, Z 720..745 |
| `PAD_cable_ambient` | sensor cable to `PAD_gland_pump` | | spline (630, 832, 745) → (658, 830, 780) |

Air path through this group: ambient air enters `PAD_inlet_louver` at Y 880, passes the screen at Y 848, crosses the 30 mm gap (Y 817..847), goes through `PAD_cassette_media` from back to front (-Y), through `SHELL_pad_opening`, into the chamber.

Water path: sump → pump → hose → valve → quick coupler → distributor pipe → jets hit the cap → rain onto the pad top → down through the flutes → notched frame bottom → back into the sump.

### Group E: roof fans and hood (collection `E_fans`)

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `FAN_1` | 120 × 120 × 25 mm 12 V DC 4-pin PWM axial fan, exhausting +Z | | X 125..245, Y 145..265, Z 860..885 |
| `FAN_2` | same | | X 425..545, Y 145..265, Z 860..885 |
| `FAN_1_guard`, `FAN_2_guard` | chrome wire finger guard 120 | 120 dia × 5 | Z 885..890, centred on each fan |
| `FAN_1_screen`, `FAN_2_screen` | insect screen disc under the roof hole, held by a 130 mm ring | 130 dia × 2 | Z 793..795 |
| `HOOD_top` | 12 mm plywood | 450 × 170 × 12 | X 110..560, Y 120..290, Z 908..920 |
| `HOOD_front` | 12 mm plywood | 450 × 12 × 48 | X 110..560, Y 120..132, Z 860..908 |
| `HOOD_back` | 12 mm plywood | 450 × 12 × 48 | X 110..560, Y 278..290, Z 860..908 |
| `HOOD_end_left` | 12 mm plywood with a 120 × 30 slot covered by insect screen, air leaves here | 12 × 146 × 48 | X 110..122, Y 132..278, Z 860..908 |
| `HOOD_end_right` | same, mirror | | X 548..560, Y 132..278, Z 860..908 |
| `HOOD_slot_L`, `HOOD_slot_R` | 120 × 30 openings in the end plates | | Y 145..265, Z 870..900 |
| `FAN_conduit` | 16 mm PVC conduit from the hood's right end to the bay's top, carries two 4-wire fan cables | | spline: (560, 205, 866) → (700, 200, 866) → down into `BAY_top` at (700, 200, 860) |

Fan flow is upward through the roof holes into the hood and out sideways through the two end slots. The hood keeps rain and direct sun off the fans.

### Group F: crate, scale, shelf and rails (collection `F_storage`)

**Weighing platform (the sentinel crate).** The crate no longer rests on rails. It stands on a platform carried by one single-point load cell bolted to the floor hardpoint. Nothing else may touch the platform or the crate, or the scale will read wrong: keep every gap listed in section 6.

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `SCALE_spacer_bottom` | aluminium spacer block under the fixed end of the load cell, bolted through the liner into `SHELL_hardpoint` with two M6 bolts | 60 × 40 × 10 | X 260..320, Y 305..345, Z 205..215 |
| `SCALE_loadcell` | single-point aluminium load cell, 30 kg capacity, IP66 potted, accuracy class C3, rated for a 400 × 400 mm platform; four M6 holes on each end face. Long axis along X. Left end (fixed) bolted down, right end (live) bolted up | 150 × 40 × 40 | X 260..410, Y 305..345, Z 215..255 |
| `SCALE_spacer_top` | aluminium spacer block on the live end, between the load cell and the platform | 60 × 40 × 10 | X 350..410, Y 305..345, Z 255..265 |
| `SCALE_platform` | 4 mm aluminium plate | 496 × 350 × 4 | X 87..583, Y 150..500, Z 265..269 |
| `SCALE_rib_front`, `SCALE_rib_back` | aluminium angle 20 × 20 × 2 riveted under the platform, stiffening it along X | 460 long | X 105..565; Y 170..190 and Y 460..480; Z 245..265 |
| `SCALE_edge_left`, `SCALE_edge_right` | aluminium flat bar 20 × 3 riveted to the platform edge, standing 15 mm above the plate; keeps the crate from sliding sideways | 3 × 350 × 20 | X 84..87 and X 583..586; Y 150..500; Z 264..284 |
| `SCALE_edge_back` | same, along the back edge | 502 × 3 × 20 | X 84..586, Y 500..503, Z 264..284 |
| `SCALE_stop_1..4` | overload stops: HDPE block on the floor with an M8 nylon-tipped screw set 0.5 mm under the platform ribs; they catch the platform if the crate is dropped in, so the load cell is not bent | block 30 × 20 × 30, screw to Z 244.5 | block centres (130, 180), (540, 180), (130, 470), (540, 470); Z 205..235 block, 235..244.5 screw |
| `SCALE_cable` | 4-core shielded load-cell cable, 1.2 m, leaving the load cell's fixed end with a slack loop, clipped to the floor liner and then up the right liner to `SHELL_gland_loadcell` | 5 dia | spline (260, 325, 235) → (240, 380, 210) → (598, 380, 210) → (598, 230, 400) → (605, 230, 590) |
| `CRATE_1` | standard vented plastic crate, external 480 × 340 × 230, walls 4 mm, slotted sides, bottom grid; model with about 40 % open area. Holds 8-10 kg. Stands on `SCALE_platform` | | X 95..575, Y 155..495, Z 269..499 |
| `CRATE_1_load` | optional produce (generic 60 mm spheres), fill to 170 mm depth | | inside the crate |
| `RAIL_L2_left` | aluminium angle 40 × 40 × 3, horizontal leg inward (+X), vertical leg down against the liner; carries the shelf | 340 long | horizontal leg X 65..105, Y 155..495, Z 532..535; vertical leg X 65..68, Z 495..535 |
| `RAIL_L2_right` | mirror | | horizontal leg X 565..605, Z 532..535; vertical leg X 602..605, Z 495..535 |
| `SHELF_frame` | aluminium angle 20 × 20 × 2 rectangle resting on the rails | 480 × 340 × 20 | X 95..575, Y 155..495, Z 535..555 |
| `SHELF_slats` | 11 polypropylene slats 30 wide × 10 thick × 340 long, running front to back (along Y), 15 mm gaps, riveted on top of the frame | | X 95..575 (first slat X 95..125, pitch 45), Y 155..495, Z 555..565 |
| `SHELF_lip_front`, `SHELF_lip_back` | aluminium angle 20 × 20 × 2 along the front and back edges, stops loose produce rolling off | 480 long | Y 155..157 and Y 493..495, Z 565..585 |
| `SHELF_load` | optional loose produce, one layer up to 150 mm (e.g. leafy bundles or fruit), 4-7 kg. Not weighed by the scale | | X 100..570, Y 160..490, Z 565..715 |

Clearances: 33 mm between the crate top (Z 499) and the shelf rails (Z 532), 80 mm between the top of the shelf load and the roof liner, 90 mm plenum in front of the crate (Y 65..155) and 85 mm behind the platform (Y 500..585). The pad opening (Z 360..660) spans the upper half of the crate and the shelf zone. The old lower crate rails are removed: the crate slides in over the open front edge of the platform.

### Group G: electrical bay (collection `G_bay`)

Plywood box (9 mm) screwed to the right wall exterior. Display and buttons on the front face (Y 0 plane), hinged lid on the right face (X 820 plane), ventilation slots top and bottom with mesh.

| Name | Description | Size | Position |
|------|-------------|------|----------|
| `BAY_back` | 9 mm ply, against the shell right wall | 9 × 250 × 350 | X 670..679, Y 0..250, Z 510..860 |
| `BAY_front` | 9 mm ply with display, switch and button cut-outs | 132 × 9 × 350 | X 679..811, Y 0..9, Z 510..860 |
| `BAY_rear` | 9 mm ply | 132 × 9 × 350 | X 679..811, Y 241..250, Z 510..860 |
| `BAY_bottom` | 9 mm ply with 4 vent slots 60 × 8 and screen | 132 × 232 × 9 | X 679..811, Y 9..241, Z 510..519 |
| `BAY_top` | 9 mm ply with 4 vent slots 60 × 8 and screen, and cable entry holes | 132 × 232 × 9 | X 679..811, Y 9..241, Z 851..860 |
| `BAY_lid` | 9 mm ply, hinged along its rear vertical edge, magnetic catch at front | 9 × 250 × 350 | X 811..820, Y 0..250, Z 510..860 (closed) |
| `BAY_display` | 2.8 in TFT (320 × 240), active area 58 × 43, bezel 70 × 50 | | centre (745, 0, 800), flush in `BAY_front` |
| `BAY_led_status` | 5 mm bicolour LED | | centre (800, 0, 800) |
| `BAY_button_1..3` | 12 mm momentary pushbuttons (menu, up, down) | | centres (715, 0, 740), (745, 0, 740), (775, 0, 740) |
| `BAY_switch_mode` | 3-position rocker, AUTO / OFF / MANUAL, 12 V 10 A. MANUAL powers the fans at full speed and the pump directly, bypassing the controller | 22 × 30 | centre (715, 0, 690) |
| `BAY_switch_main` | 16 mm rocker switch, 12 V, ON/OFF | | centre (775, 0, 690) |
| `BAY_jack_dc` | 5.5 × 2.1 mm panel-mount DC barrel jack | | centre (700, 0, 630) |
| `BAY_fuse` | panel-mount 5 × 20 fuse holder, 3 A | | centre (790, 0, 630) |
| `BAY_pcb_plate` | 3 mm acrylic plate on 10 mm standoffs against `BAY_back`, plate plane vertical | 120 × 200 × 3 | X 689..692, Y 25..225, Z 700..820 |
| `BAY_esp32` | ESP32-S3-DevKitC-1 (replaces the classic ESP32 because the scale needs two more pins), 69 × 26 × 12 | | on plate, centre (Y 70, Z 790), long side along Y |
| `BAY_buck_5v` | 12 V to 5 V buck module 43 × 21 × 14 | | on plate, centre (Y 70, Z 730) |
| `BAY_mosfet_pump` | MOSFET module 33 × 24 × 12 | | on plate, centre (Y 140, Z 790) |
| `BAY_mosfet_fans` | same (fan enable); PWM goes direct from the ESP32 | | on plate, centre (Y 140, Z 750) |
| `BAY_sd_module` | microSD module 40 × 24 × 10 | | on plate, centre (Y 200, Z 790) |
| `BAY_terminal_block` | 12-way barrier terminal 12 × 80 × 15 | | on plate, centre (Y 140, Z 715) |
| `BAY_hx711` | HX711 load-cell amplifier board 34 × 21 × 4, in a small shielded tin 40 × 28 × 10, as close to the load-cell gland as possible | | on plate, centre (Y 200, Z 740) |
| `BAY_battery` | 12 V 12 Ah sealed lead-acid battery, 151 × 98 × 95, held by a strap to `BAY_bottom` | | X 700..798, Y 40..191, Z 519..614 |
| `BAY_dcups_module` | 12 V DC-UPS / battery charge module, about 110 × 60 × 25, on standoffs on the inside of `BAY_lid` | | X 786..811, Y 70..180, Z 625..685 |
| `BAY_fuse_battery` | inline 5 A blade fuse holder on the battery positive lead | 40 × 15 × 12 | X 720..760, Y 195..210, Z 620..632 |
| `BAY_gland_top_1` | cable entry from `FAN_conduit` | | in `BAY_top` at (700, 200) |
| `BAY_gland_top_2` | cable entry from `BAY_conduit_side` (pump, float switch, ambient sensor) | | in `BAY_top` at (700, 120) |
| `BAY_back_hole_1`, `_2`, `_3` | 20 mm holes in `BAY_back` aligned with the three chamber glands, so sensor and load-cell cables pass straight from the chamber into the bay | | (Y 120, Z 530), (Y 200, Z 560) and (Y 230, Z 590) |
| `BAY_conduit_side` | 16 mm PVC conduit on the right wall exterior from the bay top to the rear module gland | | spline: (700, 120, 865) → (700, 250, 865) → (680, 640, 780) → (680, 830, 780) |

Power: a 15 V wall adapter plugs into `BAY_jack_dc`; the DC-UPS module runs the cooler from it and keeps `BAY_battery` charged, switching to the battery during brownouts. See `05-systems-and-protocol.md` section 4.2.

### Group H: sensors inside the chamber (collection `H_sensors`)

| Name | Description | Position |
|------|-------------|----------|
| `SENS_chamber` | SHT31 in slotted housing 40 × 25 × 15, on the right liner in the front plenum, level with the gap between the crate top and the shelf. This is the air leaving the produce, the honest chamber reading | X 590..605, Y 100..140, Z 518..543 |
| `SENS_pad_outlet` | SHT31 in slotted housing, on the back liner just above the pad opening; measures pad-outlet air for the efficiency reading | X 315..355, Y 570..585, Z 665..690 |
| `SENS_pulp_probe` | DS18B20 stainless probe 6 dia × 50, on a 1.5 m cable from `SHELL_gland_pulp_probe`, pushed into a fruit in `CRATE_1`. The cable is clipped to the right liner and hangs in a slack loop into the crate so it does not pull on the weighed crate | probe centre (335, 325, 414) |
| `SENS_cable_chamber` | short cable from `SENS_chamber` to `SHELL_gland_chamber_sensor` | (605, 120, 530) |

### Group I: labels and finish (collection `I_labels`)

| Name | Description | Position |
|------|-------------|----------|
| `LABEL_title` | project label plate on the door | see `DOOR_label` |
| `LABEL_inlet` | "AIR INLET - KEEP CLEAR 300 mm" above the rear louver | X 200..470, Y 860, Z 700..730 |
| `LABEL_fill` | "WATER FILL 10 L - NOT POTABLE" above the fill port | X 400..540, Y 860, Z 305..318 |
| `LABEL_bay` | "15 V DC 3 A IN" beside the DC jack | X 680..720, Y 0, Z 605..615 |
| `LABEL_mode` | "AUTO / OFF / MANUAL" under the mode switch | X 695..735, Y 0, Z 665..675 |

## 4. Section views (for orientation)

Side section at X = 335, looking from +X (left is front, right is back):

```
Z
 920 ┌─hood─┐
 872 │      │                        ┌──hatch lid Y 640..830──┐
 860 ┼──roof(65)────────────────────┼┴────────────────────────┴┐
 795 │ chamber ceiling   FAN↑       │  cap + distributor Z 665..710
     │  shelf load 565..715         │ ┌────────────────┐ gap │← inlet air
     │ ═shelf 535..565═   opening   ║ │ cellulose 7090 │ 30  │  louver Y 860..880
     │ ┌crate 269..499┐   360..660  ║ │ 150 deep       │     │
 350 │ │              │             │ └────────────────┘     │
 265 │ ╞platform══════╡             │                        │
 215 │   [load cell]                │                        │
 312 │                              │ ┌──sump 152..312──────┐│
 205 ┼──floor(65)───────────────────┤ │ water 105 mm, 10 L  ││
 140 ┼ base frame 100..140 ─────────┴─┴─────────────────────┴┤
   0 ┴ casters ──────────────────────────────────────────────┘
     Y=0 door        Y=585 liner  Y=650  657  817   848 860
```

Plan at Z = 400 (looking down; the load cell under the platform is shown for reference):

```
Y
880 ┌──── louver X 55..615 ───────────────────────────┐
860 ├──── rear panel ─────────────────────────────────┤
847 │      air gap                               hose │
817 │  ┌────── cassette X 75..595, 160 deep ──┐  ●     │
657 │  └──────────────────────────────────────┘ guides │
650 ├──back wall (65) with opening X 85..585──────────┤
585 │  chamber                                        │
500 │  ┌─────── platform X 87..583 ─────────┐         │   ┌ bay X 670..820 (Z 510..860)
495 │  │┌──────── crate X 95..575 ────────┐ │         │   │
325 │  ││   load cell X 260..410 (below)   │ │         │   │
155 │  │└──────────────────────────────────┘ │         │   └ Y 0..250
150 │  └────────────────────────────────────┘         │
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
│   ├── D1_box        (sides, floor, top strips, rear panels, guides, stops, hatch)
│   ├── D2_cassette   (frame, media, gasket, cap, distributor pipe, riser, coupler half, handles)  ← removable, slides +Z
│   ├── D3_water      (sump, water body, pump, float, hose, valve, fill, overflow, sight tube)
│   └── D4_inlet      (screen, louver, ambient sensor)
├── E_fans
├── F_storage
│   ├── F1_scale      (hardpoint is in B_shell; spacers, load cell, platform, ribs, edges, stops, cable)
│   ├── F2_crate      (crate, optional load)  ← sits on the platform
│   └── F3_shelf      (rails, frame, slats, lips, optional load)
├── G_bay
├── H_sensors
└── I_labels
```

Suggested animations or exploded views: door swing (C_door), cassette lift (D2_cassette, +540 mm in Z to clear the hatch, after unplugging the quick coupler), crate pull-out (lift +15 mm to clear the platform edges, then -300 mm in Y), shelf pull-out (-300 mm in Y), bay lid swing (BAY_lid, hinge along its rear vertical edge at X 820, Y 250).

## 6. Interference and clearance checks

* `DOOR_plug` (X 67..603, Z 207..793) clears the opening (X 65..605, Z 205..795) by 2 mm per side.
* `PAD_cassette_frame` (Y 657..817) sits in the guide slot (Y 652..822) with 5 mm play each side; its front gasket compresses 2 mm against the back wall at Y 650.
* `PAD_cassette_media` (X 85..585, Z 360..660) exactly matches `SHELL_pad_opening`, so the whole pad face is used and no air bypasses it.
* The cassette assembly (Z 350..780 including the coupler) lifts straight up through the hatch opening (X 65..605, Y 650..822). The hose is unplugged first; it crosses above the guide tops (Z 715) at Z 800, below the hatch underside (Z 848).
* The cassette stops (Z 325..350) sit above the sump top (Z 312), leaving a 38 mm drop for drain water under the cassette bottom (Z 350).
* `PAD_pump` (X 535..595, Y 760..810) sits under the cassette's rear right corner, clear of the float switch (X 95) and the fill port (X 454..486).
* `PAD_fill_port` (Z 274..306) and `PAD_overflow` (Z 272..292) both sit inside the sump wall height (up to Z 312) and inside `PAD_rear_lower` (Z 140..320).
* Fan holes (centres Y 205) lie over the front plenum and the front of the shelf zone; air must cross the crate and shelf to reach them.
* `SENS_chamber` (Y 100..140) sits in the front plenum, forward of the rails (which start at Y 155) and of the crate and shelf, so it clears both. Its gland (Y 120, Z 530) and the pulp-probe gland (Y 200, Z 560) exit inside the bay footprint (Y 0..250, Z 510..860).
* `BAY_battery` (Z 519..614) sits below `BAY_pcb_plate` (Z 700..820). `BAY_dcups_module` on the lid (X 786..811, Z 625..685) sits above the battery's top (Z 614), so the lid closes without touching it. `BAY_fuse_battery` (Z 620..632) sits beside the battery top at Y 195..210, behind the battery (Y 40..191).
* `HOOD` (X 110..560, Y 120..290) does not overlap the hatch lid (Y 640..830) or the bay (X 670+).
* Front-panel parts on `BAY_front` sit in rows at Z 800, 740, 690 and 630, at least 50 mm apart vertically and 30 mm apart horizontally.
* **Scale isolation (critical).** Nothing may touch the platform or the crate except the load cell. Gaps: platform edge strips (X 84..586) to the side liners (X 65 and 605) 19 mm; back edge strip (Y 503) to the back liner (Y 585) 82 mm; crate top (Z 499) to the shelf rails (Z 532) 33 mm; platform ribs (Z 245) to the overload-stop screws (Z 244.5) 0.5 mm; platform underside (Z 265) to the chamber sensor and cables: no contact. The pulp-probe and load-cell cables hang in slack loops.
* `SCALE_loadcell` (X 260..410, Y 305..345) sits on its bottom spacer at the fixed end only (X 260..320); the live end (X 350..410) is free underneath, with 10 mm clearance to the liner, so it can deflect.
* `SCALE_stop_1..4` sit under the ribs (Y 170..190 and 460..480) and clear the load cell (Y 305..345).
* `SHELL_hardpoint` (X 240..430, Y 290..360) spans the bottom spacer and stays clear of the floor drain (centre Y 560).
* Caster swing radius 60 mm at each corner: no part below Z 100 within that radius.
* Rear louver needs 300 mm free space behind the unit for inlet air; the label says so.
