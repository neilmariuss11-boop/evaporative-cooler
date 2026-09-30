#!/usr/bin/env python3
"""
Psychrometric and sizing calculator for a small direct evaporative cooling cabinet.

Usage:
    python3 tools/psychro_design.py                 # runs the built-in Philippine climate cases
    python3 tools/psychro_design.py 33 60           # dry-bulb [degC] and RH [%] of your site
    python3 tools/psychro_design.py 33 60 --eff 0.8 --flow 120 --load 60

Formulas: Tetens/Magnus saturation pressure, ASHRAE humidity-ratio and
wet-bulb relations, adiabatic (constant-enthalpy) saturation for the pad.
Standard atmospheric pressure is assumed unless --pressure is given (kPa).
Only the Python standard library is used.
"""
import argparse
import math

RHO_AIR = 1.15      # kg/m3, warm humid air (approx.)
CP_AIR = 1.006      # kJ/kg.K
H_FG = 2501.0       # kJ/kg latent heat of water at 0 degC


def p_ws(t_c):
    """Saturation vapour pressure [kPa] (Tetens)."""
    return 0.61078 * math.exp(17.27 * t_c / (t_c + 237.3))


def humidity_ratio(t_c, rh_pct, p_kpa):
    pw = rh_pct / 100.0 * p_ws(t_c)
    return 0.622 * pw / (p_kpa - pw)


def enthalpy(t_c, w):
    """Moist air enthalpy [kJ/kg dry air]."""
    return CP_AIR * t_c + w * (H_FG + 1.86 * t_c)


def wet_bulb(t_c, rh_pct, p_kpa):
    """Thermodynamic wet-bulb temperature [degC] by bisection (ASHRAE eq.)."""
    w = humidity_ratio(t_c, rh_pct, p_kpa)
    lo, hi = -20.0, t_c
    for _ in range(80):
        twb = 0.5 * (lo + hi)
        ws = humidity_ratio(twb, 100.0, p_kpa)
        w_calc = ((H_FG - 2.326 * twb) * ws - CP_AIR * (t_c - twb)) / (
            H_FG + 1.86 * t_c - 4.186 * twb)
        if w_calc > w:
            hi = twb
        else:
            lo = twb
    return 0.5 * (lo + hi)


def pad_outlet(t_c, rh_pct, eff, p_kpa):
    """State of air leaving a direct evaporative pad of saturation efficiency eff."""
    twb = wet_bulb(t_c, rh_pct, p_kpa)
    t_out = t_c - eff * (t_c - twb)
    w_in = humidity_ratio(t_c, rh_pct, p_kpa)
    h = enthalpy(t_c, w_in)
    w_out = (h - CP_AIR * t_out) / (H_FG + 1.86 * t_out)
    rh_out = 100.0 * (w_out * p_kpa / (0.622 + w_out)) / p_ws(t_out)
    return twb, t_out, w_in, w_out, min(rh_out, 100.0)


def size(t_c, rh_pct, eff, flow_m3h, load_w, face_vel, p_kpa):
    twb, t_out, w_in, w_out, rh_out = pad_outlet(t_c, rh_pct, eff, p_kpa)
    m_air = flow_m3h / 3600.0 * RHO_AIR                       # kg/s
    water_kg_s = m_air * (w_out - w_in)
    water_l_day = water_kg_s * 3600 * 24
    # chamber air temperature rise above pad outlet caused by heat load
    dt_chamber = load_w / 1000.0 / (m_air * CP_AIR) if m_air > 0 else float("nan")
    pad_area = flow_m3h / 3600.0 / face_vel                    # m2
    return dict(
        twb=twb, wbd=t_c - twb, t_out=t_out, rh_out=rh_out,
        t_chamber=t_out + dt_chamber, dt_chamber=dt_chamber,
        water_l_day=water_l_day, water_l_h=water_l_day / 24.0,
        pad_area_m2=pad_area,
    )


def report(label, t_c, rh_pct, args):
    r = size(t_c, rh_pct, args.eff, args.flow, args.load, args.face_vel, args.pressure)
    print(f"{label:<34} {t_c:5.1f} {rh_pct:4.0f} {r['twb']:6.1f} {r['wbd']:5.1f} "
          f"{r['t_out']:6.1f} {r['rh_out']:5.0f} {r['t_chamber']:7.1f} "
          f"{r['water_l_day']:6.1f} {r['pad_area_m2']*1e4:7.0f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("t", nargs="?", type=float, help="dry-bulb temperature, degC")
    ap.add_argument("rh", nargs="?", type=float, help="relative humidity, %")
    ap.add_argument("--eff", type=float, default=0.80, help="pad saturation efficiency (0-1), default 0.80")
    ap.add_argument("--flow", type=float, default=120.0, help="airflow through pad, m3/h, default 120")
    ap.add_argument("--load", type=float, default=60.0, help="chamber heat load, W, default 60")
    ap.add_argument("--face-vel", type=float, default=0.6, help="pad face velocity, m/s, default 0.6")
    ap.add_argument("--pressure", type=float, default=101.325, help="atmospheric pressure, kPa")
    args = ap.parse_args()

    print(f"Assumptions: pad efficiency {args.eff:.2f}, airflow {args.flow:.0f} m3/h, "
          f"heat load {args.load:.0f} W, face velocity {args.face_vel:.1f} m/s, P {args.pressure:.1f} kPa\n")
    hdr = f"{'case':<34} {'Tdb':>5} {'RH':>4} {'Twb':>6} {'WBD':>5} {'Tout':>6} {'RHout':>5} {'Tchamb':>7} {'L/day':>6} {'pad cm2':>7}"
    print(hdr)
    print("-" * len(hdr))

    if args.t is not None and args.rh is not None:
        report("user site", args.t, args.rh, args)
        return

    cases = [
        # label, dry-bulb degC, RH %  (typical, not station-certified values)
        ("Lowland PH, Apr-May 2 pm (hot/dry)", 34.0, 55.0),
        ("Lowland PH, Mar-May 2 pm (typical)", 33.0, 62.0),
        ("Lowland PH, dry-season morning",     28.0, 78.0),
        ("Lowland PH, wet season afternoon",   31.0, 78.0),
        ("Lowland PH, wet season, rainy day",  28.0, 90.0),
        ("Highland (Benguet) afternoon",       24.0, 70.0),
        ("Semi-arid reference (for contrast)", 35.0, 30.0),
    ]
    for label, t, rh in cases:
        report(label, t, rh, args)
    print("\nTdb/Twb: dry/wet-bulb temp; WBD: wet-bulb depression = maximum possible drop;")
    print("Tout: pad outlet air; Tchamb: chamber air after absorbing the heat load;")
    print("L/day: water evaporated at continuous operation; pad cm2: pad face area needed.")


if __name__ == "__main__":
    main()
