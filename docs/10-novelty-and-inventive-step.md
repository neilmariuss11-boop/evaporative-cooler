# Novelty and inventive step

Concept Option B - Scale. This file states what is new about the design, argues why it is not obvious, and drafts claim language. It follows the usual patent tests: novelty, inventive step (inventiveness), and industrial applicability.

Status: 1 Oct 2026. Based on a web-only search (`06-software-novelty-options.md`, `01-patent-landscape.md`); Espacenet and Google Patents full texts could not be read. Treat this as a well-argued draft, not a legal opinion. Before claiming novelty in the thesis or filing anything, have the university's Innovation and Technology Support Office (ITSO), part of IPOPHL's ITSO network, run a formal prior-art search.

## 1. Which tests apply

| Protection route in the Philippines | Novelty | Inventive step | Industrial applicability |
|-------------------------------------|:-------:|:--------------:|:------------------------:|
| Invention patent | Required | Required | Required |
| Utility model | Required | **Not required** | Required |

A utility model only needs the design to be new and usable. If the inventive-step argument below does not convince an examiner, a utility model is still possible. For a thesis or a competition, both arguments are useful.

## 2. Where the novelty is, and where it is not

**Not new (state this openly):** the cooling hardware. Wetted cellulose pad, exhaust fans, pump and sump, insulated cabinet and microcontroller control of fans and pump are all well documented. This includes PhilMech's charcoal-pad cabinets (2008), many microcontroller-controlled produce coolers since 2017, and the 2026 systematic review of intelligent evaporative cooling for postharvest storage.

**Where the novelty sits:** the "sentinel crate". The cooler weighs part of its own produce load and uses the measured weight loss to inform the operator and steer the cooling.

## 3. Closest prior art

| Ref | Document | What it discloses | What it does not disclose |
|-----|----------|-------------------|---------------------------|
| D1 | US 9,339,042 B2 and US 10,226,054 B2, "Carcass weight control" (R. W. Heston, LP Solutions LLC; filed 2012) | Wireless load cells on selected trolleys weigh meat carcasses during spray chilling. When a carcass loses weight, the solenoid valve for its spray zone opens; spraying continues until the carcass returns to its original weight. Data are logged. | Fresh produce; evaporative coolers; adding moisture to the **air** rather than spraying the product; any loss budget; learning a drying coefficient; estimating loss under other storage conditions; operator-facing shelf-life prediction |
| D2 | Microcontroller-controlled evaporative produce coolers (e.g. automated electronic evaporative cooler, 2017; AVR-based controller study) and the 2026 review in *AgriEngineering* 8(4):150 | Fans and pump controlled from air temperature and humidity sensors; logging; IoT monitoring; predictive and machine-learning control | Weighing the produce; using produce mass loss as a control or reporting variable |
| D3 | Empa physics-based digital twins (Shrivastava et al., 2022, *Nature Food*) and shelf-life apps for smallholders | Remaining shelf life computed from air-temperature data and models | Measured produce mass; on-board control; calibration from the actual batch |
| D4 | IoT tomato storage monitoring with shelf-life estimation (2026 dew-computing framework) and similar systems | Sensor-based monitoring and shelf-life estimation in storage | Weighing; controlling an evaporative cooler from mass loss |
| D5 | Evaporative cooler control patents: US 2022/0026095 (wet and dry mode control), US 10,145,572 and US 10,969,126 (precise temperature control), US 10,260,418 (pad replacement timing) | Mode switching and set-point control of evaporative coolers from air conditions and pad effectiveness | Produce mass |

D1 is the closest. It already discloses the general idea of weighing a sample of the load and adding moisture when weight is lost. Any novelty claim that says only "weight-based control" would fail against D1.

## 4. Novelty: distinguishing features

The design combines the following features. Features F1, F3 and F5 together are not found in any single document above.

| # | Feature | Closest disclosure | Difference |
|---|---------|--------------------|------------|
| F1 | A weighing device supporting a representative produce container inside an evaporative cooling chamber | D1 weighs carcasses on trolleys in a refrigerated chill room | Different product, different cooling principle, container-based sample |
| F2 | Event logic that separates sales, additions and handling (settled step changes) from water loss, and accumulates loss across segments as 1 - Π(end/start) | D1 weighs from a fixed starting weight | A retail load that is partly sold during storage still gives a true loss figure |
| F3 | In-situ learning of the batch's drying coefficient: measured mass-loss rate divided by the vapour pressure deficit at the produce surface (from a pulp-temperature probe and chamber air sensors) | D3 uses models with literature coefficients; D1 learns nothing | Each batch calibrates itself; no laboratory data per crop or variety are needed |
| F4 | Estimate of the loss the same batch would suffer in open-shelf storage, by applying the learned coefficient to ambient air conditions measured by the cooler, reported as mass (and value) saved | None found | Gives a running, batch-specific measure of the cooler's benefit |
| F5 | A weight-loss budget (crop limit and target days) turned into an allowed loss rate; the controller changes fan speed and pad wetting when the measured rate departs from it (PROTECT when too fast, ECO when well under) | D1 restores weight to the start value; D2 controls on air conditions only | The control target is a permitted loss path, not zero loss, and the actuator acts on the air, not the product |
| F6 | Projected time until the marketability limit, from current loss and rate | D3 predicts shelf life from temperature models | Prediction from the produce's own measured mass |
| F7 (pending, see section 7) | Two-layer control: the weight loop sets a target drying power, and a fast loop on air sensors holds it continuously | None found | Stronger technical effect |

**Novelty statement (draft):** an evaporative cooling storage unit for fresh produce in which a weighing device under a representative produce container measures the produce's own mass loss, the controller learns that batch's drying coefficient from the measured loss and the vapour pressure deficit at the produce surface, and uses a produce-specific weight-loss budget to adjust fan speed and pad wetting, while reporting projected days to the marketability limit and the mass saved relative to open-shelf storage.

## 5. Inventive step

### 5.1 The technical problem

Starting from D2 (an instrumented evaporative produce cooler), the problem the design solves is:

> In a humid tropical climate an evaporative cooler can lower the temperature only a little, so its main benefit is reducing produce water loss. A cooler controlled only from air temperature and humidity cannot tell whether the produce is actually losing water too fast, cannot adapt to different crops and batches, and cannot show the operator what it is achieving. Produce water loss is also too slow to measure directly for real-time control: a crate loses 10-30 g a day, about the same as a low-cost load cell drifts in a day.

### 5.2 Why the solution is not obvious

1. **D1 points the wrong way for produce.** D1 restores weight by spraying water directly onto the product until it reaches its starting weight. A person skilled in postharvest handling would not transfer that to fresh produce: free water on fruit and leafy vegetables promotes decay, and restoring the starting weight is not the goal. The design instead uses mass loss to steer the humidity of the air through the evaporative pad and fans, keeping the produce surface dry and allowing a controlled loss.
2. **The signal is too weak for D1's approach.** D1 reacts to instantaneous weight on carcasses of a few hundred kilograms losing 1-2 % in a day. A 10 kg crate losing 0.3 % a day gives a signal comparable to sensor drift. Using it directly as feedback, as D1 does, would not work. The design solves this by using weight only over 12-24 h windows to calibrate a physical coefficient, and steering through the fast air sensors. That split between a slow, produce-calibrated layer and a fast air-side layer is not suggested by D1, D2 or D3.
3. **The combination produces more than its parts.** D2 alone can control air but does not know the produce's response. D3 alone can model the produce but is not calibrated to the actual batch. Weighing alone measures, but does not control. Together, the learned coefficient lets the cooler (a) run harder only when the produce needs it, saving water and energy otherwise, (b) adapt to any crop without laboratory data, and (c) estimate its own benefit against ambient storage from the same coefficient and the ambient sensor it already has.
4. **No extra hardware beyond one load cell.** Every other input already exists on an instrumented cooler, which makes the solution economical for small units, a field where the literature stresses cost as the main barrier.

### 5.3 Weak points an examiner or panel may raise

* **"Obvious combination of D1 + D2 + known transpiration physics."** The counter-argument is points 1 and 2 above: D1 teaches away for produce, and the slow-signal problem needs the calibration split, which none of the documents suggests.
* **Displayed values are not technical.** "Days left", "kg saved" and pesos are presentations of information. Most patent offices do not count them toward inventive step. Argue inventive step on the control effect (water and energy saved while keeping loss within the budget), and treat the display as a useful feature, not the invention.
* **The current control effect is coarse.** At present the budget only switches between PROTECT, ECO and normal once an hour. An examiner could call that a routine add-on. Adopting the two-layer control (F7) makes the technical contribution clearer and harder to dismiss.
* **The search was web-only.** A formal search may find closer documents, for example in Chinese utility models on smart produce storage.

## 6. Industrial applicability

The unit is built from commercially available parts with school-shop methods, has a defined use (short-term storage of fresh produce by vendors, traders and farmers), and can be manufactured and sold. This test is met.

## 7. Recommendation

1. Present the novelty as the sentinel crate (F1-F6), and name D1 as the closest prior art with the differences in section 4.
2. Adopt the two-layer control (F7) before finalising claims; it is firmware only and makes the inventive-step argument much stronger.
3. If a filing is considered, a Philippine utility model is the realistic route; it does not need the inventive-step argument to succeed.
4. Ask the university ITSO for a formal search before the thesis states that the feature is new.

## 8. Draft claims (for discussion, not legal advice)

**Claim 1 (independent).** An evaporative cooling storage apparatus for fresh produce, comprising:
* an insulated storage chamber;
* a wetted evaporative pad through which ambient air enters the chamber;
* at least one variable-speed fan moving air through the pad and the chamber;
* a pump and a water distributor for wetting the pad;
* sensors measuring the temperature and humidity of the ambient air and of the chamber air;
* a weighing device supporting a produce container inside the chamber; and
* a controller configured to (a) determine from the weighing device a mass-loss rate of the produce over a time window, excluding step changes in mass caused by loading or removing produce; (b) compare the mass-loss rate with an allowed rate derived from a produce-specific mass-loss limit and a target storage time; and (c) adjust the fan speed, the pad wetting, or both, in response to the comparison.

**Dependent claims.**
2. The apparatus of claim 1, further comprising a produce temperature probe, wherein the controller computes a vapour pressure deficit at the produce surface and determines a batch-specific drying coefficient as the ratio of the mass-loss rate to that deficit.
3. The apparatus of claim 2, wherein the controller estimates the mass loss the produce would have suffered in ambient storage by applying the drying coefficient to a vapour pressure deficit computed from the ambient sensor, and displays the estimated mass saved.
4. The apparatus of claim 1, wherein the controller displays a projected time until the produce reaches the mass-loss limit.
5. The apparatus of claim 1, wherein the controller treats each settled step change in mass as the start of a new segment and computes the cumulative loss as one minus the product of the end-to-start mass ratios of the segments.
6. The apparatus of claim 2, wherein the controller sets a target vapour pressure deficit equal to the allowed rate divided by the drying coefficient, and continuously adjusts the fan speed to hold the measured deficit at or below the target. *(Requires adopting F7.)*
7. The apparatus of claim 1, wherein the weighing device is a single load cell beneath a platform that is free of contact with the chamber walls, with overload stops beneath the platform.
