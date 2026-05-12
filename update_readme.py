import os
from datetime import datetime, timezone

REPO = os.environ.get("GITHUB_REPOSITORY", "your-username/your-repo")
BRANCH = "main"
BASE_RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/regions"

region_files = sorted(f for f in os.listdir("regions") if f.endswith(".txt"))

rows = []
for fname in region_files:
    code = fname.replace(".txt", "")
    count = sum(1 for line in open(f"regions/{fname}", encoding="utf-8") if line.strip())
    raw_url = f"{BASE_RAW}/{fname}"
    rows.append(f"| {code} | {count} | [raw]({raw_url}) |")

table = "\n".join(rows)
updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

readme = f"""# IP List by Region

自動從 [all.txt](https://zip.cm.edu.kg/all.txt) 抓取並按國家代碼分類，每日更新。

## 地區列表

| 國家代碼 | 條目數 | Raw URL |
|----------|--------|---------|
{table}

---
*最後更新：{updated}*
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md updated")
