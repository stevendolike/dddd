import os
from collections import defaultdict

# 直接讀本地文件，不再重新下載
with open("all.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

groups = defaultdict(list)

for line in lines:
    line = line.strip()
    if not line:
        continue
    region = line.split("#", 1)[1].upper() if "#" in line else "UNKNOWN"
    groups[region].append(line)

os.makedirs("regions", exist_ok=True)

for region, entries in groups.items():
    with open(f"regions/{region}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(entries))
    print(f"regions/{region}.txt — {len(entries)} 條")
