# Blender handoff: evaporative cooler, concept "Option B - Scale"

Brief for whoever builds the 3D model, human or AI. Read this first, then work from `04-assembly-spec.md`, which is the single source of truth for every dimension. If this file and the spec ever disagree, the spec wins; report the conflict.

Branch: `option-b-scale`. Date: 30 Sep 2026.

## 1. What you are modelling

A small evaporative cooling cabinet for storing fresh fruit and vegetables, about the size of a bedside cabinet on wheels: 820 mm wide including the side electrical box, 892 mm deep including the rear louver, 920 mm tall.

* A white-painted, insulated plywood box on four casters, with a front door.
* Inside: one green market crate standing on a small weighing platform, and a slatted shelf above it.
* Behind the back wall: a wet module with a brown honeycomb cooling pad in a lift-out cassette, a water tank and a pump, closed by a louvered rear panel.
* On the roof: two fans under a small plywood rain hood.
* On the right side: a plywood electrical box with a small screen, buttons and switches on its front face.

Air enters through the rear louver, passes through the wet pad, crosses the produce, and leaves through the roof fans. Section 1 of `05-systems-and-protocol.md` explains the air and water paths if you need them for arrows or annotations.

**What is new in this concept** compared with earlier drafts, so you don't carry over old geometry:

| Feature | This concept |
|---------|--------------|
| Capacity | Half size: one crate plus a shelf, chamber 540 × 520 × 590 mm |
| Pad | 150 mm deep cellulose honeycomb, 500 × 300 mm face, in a cassette with a water-distribution cap on top |
| Power | Wall adapter plus a battery inside the electrical box |
| Scale | The crate stands on a platform carried by one load cell bolted to the floor. There are **no** lower crate rails |
| Controller | ESP32-S3 board; external display page for the produce's weight |

## 2. Files to use

| File | Use it for |
|------|------------|
| `04-assembly-spec.md` | Every part: name, size, position, material colour. Sections 4 to 6 give section views, the collection tree and the clearance rules |
| `03-design-decisions.md` | Why parts are where they are, if a choice looks odd |
| `05-systems-and-protocol.md` | Display contents (sections 5.3 and 5.4), air and water paths |
| This file | Build order, modelling methods, renders, deliverables, checks |

## 3. Setup

1. New file. Scene > Units: Metric, Length = Millimeters, Unit Scale = 0.001. Model at 1 Blender unit = 1 mm.
2. Axes as in the spec: X left to right facing the door, Y from the door (front) toward the back, Z up. Front view (numpad 1) looks at the door. Origin at floor level, outside bottom-left-front corner of the main shell.
3. Create the collection tree exactly as in spec section 5, including the sub-collections of `D_padmodule` and `F_storage`.
4. Name every object exactly as its spec name (for example `SCALE_loadcell`). Parts written as ranges such as `SCALE_stop_1..4` become separate objects `SCALE_stop_1` to `SCALE_stop_4`. Parts written `NAME_L`, `_R` become `NAME_L` and `NAME_R`.
5. Create the materials listed in spec section 1 as Principled BSDF materials, one per colour, named after what they are (`plywood_white`, `cellulose_pad`, `crate_green`, and so on).

## 4. How to read and build a spec row

* **Bounding box** `X a..b, Y c..d, Z e..f`: add a cube, set its dimensions to (b-a, d-c, f-e) and its location to the box centre ((a+b)/2, (c+d)/2, (e+f)/2). Apply scale afterwards.
* **Cylinder** "axis X, centre (Y y, Z z), X a..b": cylinder of the stated diameter, rotated to the axis, spanning a..b along it.
* **Spline** "(x1, y1, z1) → (x2, y2, z2) → ...": a curve through those points with a bevel depth of half the stated diameter (hose 12 mm ID: use 16 mm outer; cables 5 mm).
* **Centre-only parts** such as switches, buttons and board modules: place the part's centre at the given point; its size is in the Size or Description column. For parts on `BAY_front` the given Y is the panel's outer face (Y 0); the part protrudes toward -Y.
* **Holes and openings** (`SHELL_pad_opening`, `SHELL_hole_fan_*`, `PAD_inlet_opening`, `PAD_hatch_opening`, `HOOD_slot_*`): cut them with a Boolean difference, then apply it.
* **Insulated walls**: either three stacked blocks per wall (12 mm plywood, 50 mm EPS, 3 mm PVC liner) or one block with the plywood material outside. Use three layers only if you will render the cut-away in section 6.

## 5. Build order

Build in this order so each part has something to sit on, and check the overall size after steps 2 and 4.

1. `A_base`: frame and casters.
2. `B_shell`: floor with the HDPE hardpoint, walls, roof; cut the pad opening and fan holes. **Check:** shell outside is 670 × 650 × 720 mm (Z 140..860).
3. `C_door`: set the object origin of every door part on the hinge line (X 25, Y -6), parent them to an empty called `DOOR_pivot` at that line, and rotate the empty to open the door.
4. `D_padmodule`: box, guides and stops, then the cassette (frame, media, cap, pipe, riser, coupler), then the sump, water, pump, float, hose, valve, fill, overflow, sight tube, then the screen, louver and ambient sensor. **Check:** the rear louver's back face is at Y 880 and the hatch lid top at Z 872.
5. `E_fans`: fans, guards, screens, hood, conduit.
6. `F_storage`: in sub-collection order `F1_scale`, `F2_crate`, `F3_shelf`.
7. `G_bay`: panels, then front-panel parts, then internals (plate, boards, battery, charge module, fuse).
8. `H_sensors`, then `I_labels`.

## 6. Modelling guidance for the tricky parts

| Part | How to model it |
|------|-----------------|
| `PAD_cassette_media` (cellulose pad) | A box with a crossed diagonal texture on the two 500 × 300 faces: lines at 45° and 15°, 7 mm apart, darker brown in the grooves. The steep 45° lines slope **down toward the back** (+Y face). A bump or normal map is enough; do not model individual flutes |
| `CRATE_1` | Box shell with 4 mm walls; array of rectangular slots on the four sides (about 40 % open) and a grid bottom. Rounded vertical corners, radius 15 mm. Any generic vented market crate of the stated outer size is acceptable |
| `SHELF_slats` | 11 separate thin boxes, or one box with an Array modifier: count 11, relative offset along X so slat 1 is X 95..125 and the pitch is 45 mm |
| `SCALE_loadcell` | Box 150 × 40 × 40 with a round through-hole of about 20 mm dia along Y in the middle (typical single-point cell shape), black potting on the top face, cable leaving the fixed (left, lower X) end |
| `SCALE_platform` and edges | Thin plate with three 15 mm-high edge strips on the left, right and back; the **front edge is open** so the crate can slide in |
| `SCALE_stop_1..4` | Small off-white block with a vertical screw on top ending 0.5 mm below the platform rib |
| `PAD_cassette_frame` | Model as the 12 edges of the 520 × 160 × 320 box using 20 × 20 × 2 L-profile (a Screw or Solidify on an edge mesh works) plus a few notches on the bottom edges |
| `PAD_inlet_louver`, `HOOD` slots | Slats as an Array of thin boxes tilted 30° outward-down |
| `PAD_sump_water`, sight tube | Glass-like water material (transmission 0.9, IOR 1.33); sight tube clear vinyl |
| Hoses and cables | Curves with bevel. Make the load-cell and pulp-probe cables visibly slack (a sag between points) |
| `BAY_display` | Emissive image texture of the screen. Use the "page 2" layout in `05-systems-and-protocol.md` section 5.4 for the hero render (produce weight, days left, kg saved); page 1 layout is in section 5.3. White or green text on black |
| Labels | Text objects converted to mesh, 0.2 mm raised, or image textures on thin planes |

Level of detail: required for every part listed in the spec. Screws, rivets and wire colours are optional. Keep the model under about 500 k triangles.

## 7. Rigging and animation

Set these pivots and make these actions (keyframes at frame 1 closed, frame 60 open or moved):

| Action | Object(s) | Motion |
|--------|-----------|--------|
| Door open | `DOOR_pivot` | Rotate about Z up to 120°, door swinging toward -Y |
| Cassette lift | `D2_cassette` parts, parented to an empty | +540 mm in Z (after hiding or detaching the hose end at the coupler) |
| Crate out | `F2_crate` | +15 mm in Z, then -300 mm in Y |
| Shelf out | `F3_shelf` without the rails | -300 mm in Y |
| Bay lid open | `BAY_lid` | Rotate about the vertical line X 820, Y 250 |
| Exploded view | all | A separate scene or a shape of the above combined, plus the hood lifted +100 mm |

## 8. Renders to deliver

Resolution 2400 × 1600 PNG, neutral grey studio background, soft three-point lighting, same camera lens (50 mm) for all except the close-ups.

1. **Hero front three-quarter**, door closed, from front-left above, display lit with page 2.
2. **Front, door open**, showing the crate on the scale platform and the shelf with produce.
3. **Rear three-quarter**, showing the louver, fill port, sight tube and hatch.
4. **Side cut-away** at X = 335 (Boolean or clipping), showing the air path with arrows: louver → pad → crate and shelf → fans → hood slots. Add water-path arrows in blue.
5. **Scale close-up**: crate lifted and platform, load cell, stops and hardpoint visible (hide the floor liner locally or use a cut-away).
6. **Cassette lifted** out of the hatch with the coupler unplugged.
7. **Electrical bay close-up**, lid open, showing battery, board plate, charge module and display.
8. **Orthographic views**: front, right side, top and back, with overall dimensions (820, 892, 920) annotated.

## 9. Deliverables

* `cooler_option_b_scale.blend`, with packed textures, collections and names as specified.
* The 8 renders in section 8.
* A short `deviations.md` listing every place you departed from the spec and why, plus any spec conflicts you found.

## 10. Acceptance checklist

* [ ] Overall bounding box of the whole model is X 0..820, Y -12..880, Z 0..920, except the door handle and latches, which stand out to about Y -47.
* [ ] Chamber clear interior is 540 × 520 × 590 mm.
* [ ] Every object name matches the spec, and every spec part exists.
* [ ] No part intersects another, except the intended ones: the pad inside its cassette frame, the cap riveted over the frame top, the pump and water inside the sump, the HDPE hardpoint replacing floor insulation, and cut openings.
* [ ] **Scale isolation**: the platform, crate and load cell touch nothing except each other and the bottom spacer. Gaps from spec section 6 are visible: 19 mm platform to side walls, 33 mm crate top to shelf rails, 0.5 mm platform ribs to overload screws.
* [ ] Pad media exactly fills the 500 × 300 mm opening in the back wall (X 85..585, Z 360..660).
* [ ] The cassette lift animation passes through the hatch without intersecting anything.
* [ ] The door plug clears the opening by 2 mm per side and the door swings without hitting the bay.
* [ ] Front-panel items on the bay do not overlap one another.

## 11. Open item and assumptions

* **Test crop is not decided.** Fill the crate with generic round fruit (tomato-sized, red-orange) and the shelf with leafy bundles, or leave both empty in at least one render.
* The crate, casters, fans, load cell and boards are generic catalogue parts. Match the outer dimensions in the spec; styling details are free.
* If a dimension looks impossible, for example two parts that must touch but don't, follow the spec, flag it in `deviations.md`, and do not redesign.
