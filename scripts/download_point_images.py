# -*- coding: utf-8 -*-
"""Download all 361 clinical point images from acupuntura.com into static/atlas_images."""
import os
import re
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
IMAGES_DIR = os.path.join(STATIC_DIR, "atlas_images")
os.makedirs(IMAGES_DIR, exist_ok=True)

with open(os.path.join(STATIC_DIR, "atlas_points_all.json"), "r", encoding="utf-8") as f:
    pts = json.load(f)

# Find points with image paths
targets = []
for p in pts:
    img_path = p.get("image")
    if img_path:
        # e.g. "/atlas-images/LU/LU1.jpg"
        clean_path = img_path.lstrip("/")
        remote_url = f"https://acupuntura.com/{clean_path}"
        # local path
        local_rel = img_path.replace("/atlas-images/", "")
        local_dest = os.path.join(IMAGES_DIR, local_rel)
        targets.append((p.get("id"), remote_url, local_dest))

print(f"Total images to download: {len(targets)}")

def download_image(item):
    pid, url, dest = item
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        return pid, True, "cached"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
            with open(dest, "wb") as f_out:
                f_out.write(content)
        return pid, True, "downloaded"
    except Exception as e:
        return pid, False, str(e)

completed = 0
failed = 0
with ThreadPoolExecutor(max_workers=16) as executor:
    futures = [executor.submit(download_image, t) for t in targets]
    for fut in as_completed(futures):
        pid, success, msg = fut.result()
        if success:
            completed += 1
        else:
            failed += 1
            print(f"Failed {pid}: {msg}")

print(f"Finished! Successfully fetched: {completed}, Failed: {failed}")
