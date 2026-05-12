import os
from collections import defaultdict

with open("all.txt", "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

groups = defaultdict(list)
groups_443 = defaultdict(list)

for line in lines:
    line = line.strip()
    if not line:
        continue
    region = line.split("#", 1)[1].upper() if "#" in line else "UNKNOWN"
    groups[region].append(line)

    # 篩選 443 port：格式為 IP:PORT#REGION
    part = line.split("#")[0]  # 取 IP:PORT 部分
    if part.endswith(":443"):
        groups_443[region].append(line)

os.makedirs("regions", exist_ok=True)
os.makedirs("regions_443", exist_ok=True)

for region, entries in groups.items():
    with open(f"regions/{region}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(entries))
    print(f"regions/{region}.txt — {len(entries)} 條")

for region, entries in groups_443.items():
    with open(f"regions_443/{region}.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(entries))
    print(f"regions_443/{region}.txt — {len(entries)} 條 (443 only)")
