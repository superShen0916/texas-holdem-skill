#!/usr/bin/env python3
"""复核 reference/ 里的每一个数字。

本库所有数值都由这张表给出，agent 直接信任它们。所以每个数字都必须能
被独立重算出来。这个脚本把文档里声称的值和公式算出的真值逐格比对，
任何一格对不上就非零退出。

用法：python3 scripts/verify_tables.py
"""

from math import comb

FAIL = 0


def check(label, claimed, actual, tol=0.05):
    """claimed / actual 都是百分比数值。tol 单位是百分点。"""
    global FAIL
    ok = abs(claimed - actual) <= tol
    if not ok:
        FAIL += 1
    mark = "ok  " if ok else "FAIL"
    print(f"  [{mark}] {label:<34} 文档={claimed:>7} 实算={actual:>8.4f}")


def fmt(x):
    return round(x, 1)


# ---------------------------------------------------------------- 底池赔率
print("\n== reference/pot-odds.md :: 跟注所需胜率 (公式 b/(1+2b)) ==")
# (下注倍数, 文档声称的百分比)
CALL = [
    (0.25, 16.7), (1 / 3, 20.0), (0.5, 25.0), (2 / 3, 28.6),
    (0.75, 30.0), (1.0, 33.3), (1.5, 37.5), (2.0, 40.0),
]
for b, claimed in CALL:
    check(f"下注 {b:.4g}x 池", claimed, 100 * b / (1 + 2 * b))

print("\n== reference/pot-odds.md :: 诈唬所需弃牌率 (公式 b/(1+b)) ==")
BLUFF = [
    (0.25, 20.0), (1 / 3, 25.0), (0.5, 33.3), (2 / 3, 40.0),
    (0.75, 42.9), (1.0, 50.0), (1.5, 60.0), (2.0, 66.7),
]
for b, claimed in BLUFF:
    check(f"下注 {b:.4g}x 池", claimed, 100 * b / (1 + b))

# -------------------------------------------------------------------- MDF
print("\n== reference/mdf.md :: MDF (公式 1/(1+b)) 与 Alpha ==")
MDF = [
    (0.25, 80.0, 20.0), (1 / 3, 75.0, 25.0), (0.5, 66.7, 33.3),
    (2 / 3, 60.0, 40.0), (0.75, 57.1, 42.9), (1.0, 50.0, 50.0),
    (1.5, 40.0, 60.0), (2.0, 33.3, 66.7),
]
for b, mdf_c, alpha_c in MDF:
    check(f"下注 {b:.4g}x 池 MDF    ", mdf_c, 100 / (1 + b))
    check(f"下注 {b:.4g}x 池 Alpha  ", alpha_c, 100 * b / (1 + b))

# ------------------------------------------------------------------ 权益
print("\n== reference/equity.md :: 听牌胜率 (两街 1-(47-o)(46-o)/(47*46), 一街 o/46) ==")
# (出牌数, 两街%, 一街%)
OUTS = [
    (1, 4.3, 2.2), (4, 16.5, 8.7), (5, 20.4, 10.9), (6, 24.1, 13.0),
    (7, 27.8, 15.2), (8, 31.5, 17.4), (9, 35.0, 19.6), (10, 38.4, 21.7),
    (11, 41.7, 23.9), (12, 45.0, 26.1), (14, 51.2, 30.4), (15, 54.1, 32.6),
]
for o, two_c, one_c in OUTS:
    two = 100 * (1 - (47 - o) * (46 - o) / (47 * 46))
    one = 100 * o / 46
    check(f"{o:>2} 出牌 · 两街", two_c, two, tol=0.06)
    check(f"{o:>2} 出牌 · 一街", one_c, one, tol=0.06)

# --------------------------------------------------------------- 组合数
print("\n== reference/combinatorics.md :: 组合数 ==")
COMBOS = [
    ("全部手牌 C(52,2)", 1326, comb(52, 2)),
    ("对子 C(4,2)", 6, comb(4, 2)),
    ("指定同花 4x1", 4, 4),
    ("指定不同花 4x3", 12, 12),
    ("非对子 4+12", 16, 16),
    ("持一张 A 后 AA", 3, comb(3, 2)),
    ("持一张 A 后 AK", 12, 3 * 4),
    ("持 AK 后 AK", 9, 3 * 3),
    ("QQ+,AK 合计", 34, 3 * 6 + 16),
    ("持 AK 后合计", 21, 3 + 3 + 6 + 9),
]
for label, claimed, actual in COMBOS:
    ok = claimed == actual
    if not ok:
        FAIL += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label:<24} 文档={claimed:>6} 实算={actual:>6}")

# --------------------------------------------------------------- SPR 几何
print("\n== reference/spr.md :: 底池几何 (逐街按当前底池比例下注) ==")


def spr_to_allin(streets):
    """streets 是每街下注占当前底池的比例。返回打光所需 SPR。"""
    pot, committed = 1.0, 0.0
    for f in streets:
        committed += f * pot
        pot += 2 * f * pot
    return committed


GEOM = [
    ("翻牌一次满池", [1.0], 1.0),
    ("三街 1/3", [1 / 3] * 3, 1.8),
    ("两街 2/3", [2 / 3] * 2, 2.2),
    ("翻牌 1/2 → 转牌满池", [0.5, 1.0], 2.5),
    ("两街 3/4", [0.75] * 2, 2.6),
    ("三街 1/2", [0.5] * 3, 3.5),
    ("两街满池", [1.0] * 2, 4.0),
    ("三街 2/3", [2 / 3] * 3, 5.9),
    ("三街 3/4", [0.75] * 3, 7.3),
    ("三街满池", [1.0] * 3, 13.0),
]
for label, streets, claimed in GEOM:
    check(label, claimed, spr_to_allin(streets), tol=0.06)

# ------------------------------------------------------------------ 汇总
print()
if FAIL:
    print(f"✗ {FAIL} 处对不上")
    raise SystemExit(1)
print("✓ 全部数字复核通过")
