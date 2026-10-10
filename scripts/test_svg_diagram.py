"""Generate and verify full native SVG National Standard Acupuncture Chart."""
import json
from pathlib import Path

STATIC_DIR = Path("static")
pts = json.load(open(STATIC_DIR / "fitted_points.json", encoding="utf-8"))

def get_y(y):
    if y >= 0.05:
        return 460.0 - (y - 0.05) / 5.2 * (460.0 - 75.0)
    elif y >= -1.2:
        return 460.0 + (0.05 - y) / 1.25 * (560.0 - 460.0)
    elif y >= -3.65:
        return 560.0 + (-1.2 - y) / 2.45 * (710.0 - 560.0)
    else:
        return 710.0 + (-3.65 - y) / 2.67 * (920.0 - 710.0)

def get_front_xy(p):
    x, y, z = p
    sy = get_y(y)
    if y > -1.2 and x < 1.3:
        sx_r = 280.0 + x * 36.0
        sx_l = 280.0 - x * 36.0
    elif y <= -1.2 and x < 1.3:
        sx_r = 280.0 + 20.0 + x * 22.0
        sx_l = 280.0 - 20.0 - x * 22.0
    else:
        sx_r = 280.0 + 40.0 + x * 44.0
        sx_l = 280.0 - 40.0 - x * 44.0
    return round(sx_r, 1), round(sx_l, 1), round(sy, 1)

def get_back_xy(p):
    x, y, z = p
    sy = get_y(y)
    if y > -1.2 and x < 1.3:
        sx_r = 780.0 + x * 55.0
        sx_l = 780.0 - x * 55.0
    elif y <= -1.2 and x < 1.3:
        sx_r = 780.0 + 20.0 + x * 22.0
        sx_l = 780.0 - 20.0 - x * 22.0
    else:
        sx_r = 780.0 + 40.0 + x * 44.0
        sx_l = 780.0 - 40.0 - x * 44.0
    return round(sx_r, 1), round(sx_l, 1), round(sy, 1)

def get_side_xy(p):
    x, y, z = p
    sy = get_y(y)
    if x > 1.3 and y > -1.0:
        # Raised arm
        t = (2.58 - x) / (2.58 - 1.45)
        sx = 1190.0 + t * 55.0
        sy = 45.0 + t * 215.0
    elif y <= -1.2:
        sx = 1240.0 + z * 35.0
    else:
        sx = 1270.0 + z * 50.0
    return round(sx, 1), round(sy, 1)

# Verify key points
print("Testing Front Points:")
for k in ["DU20", "YINTANG", "REN24", "REN17", "REN8", "REN3", "ST36", "SP6", "ST45"]:
    print(k, get_front_xy(pts[k]["pos"]))

print("\nTesting Back Points:")
for k in ["DU20", "DU14", "BL11", "BL23", "BL52", "BL40", "BL57", "BL60"]:
    print(k, get_back_xy(pts[k]["pos"]))

print("\nTesting Side Points:")
for k in ["GB1", "GB8", "GB14", "GB20", "GB21", "GB26", "GB30", "GB34", "GB39", "GB44", "LI1", "LI4", "LI11", "LI15"]:
    print(k, get_side_xy(pts[k]["pos"]))
