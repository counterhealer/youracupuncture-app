import fitz
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

wm_dir = r"C:\Users\lingh\OneDrive\桌面\TCM\Royal TCM\WM-02 Diagnostics"
tcm_dir = r"C:\Users\lingh\OneDrive\桌面\TCM\Royal TCM\TCM-10 Traumatology"

print("--- WM-02 Diagnostics Summary ---")
for f in os.listdir(wm_dir):
    if f.endswith(".pdf") and not f.startswith("."):
        doc = fitz.open(os.path.join(wm_dir, f))
        print(f"{f}: {len(doc)} pages")
        text = ""
        for i in range(min(3, len(doc))):
            text += doc[i].get_text()[:200] + "\n"
        print("  Sample snippet:", text[:150].replace('\n', ' '))

print("\n--- TCM-10 Traumatology Summary ---")
for f in os.listdir(tcm_dir):
    if f.endswith(".pdf") and not f.startswith("."):
        doc = fitz.open(os.path.join(tcm_dir, f))
        print(f"{f}: {len(doc)} pages")
