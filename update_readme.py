import os
from datetime import datetime, timezone

REPO = os.environ.get("GITHUB_REPOSITORY", "your-username/your-repo")
BRANCH = "main"
BASE_RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

def build_table(directory):
    files = sorted(f for f in os.listdir(directory) if f.endswith(".txt"))
    rows = []
    for fname in files:
        code = fname.replace(".txt", "")
        count = sum(1 for line in open(f"{directory}/{fname}", encoding="utf-8") if line.strip())
        raw_url = f"{BASE_RAW}/{directory}/{fname}"
        rows.append(f"| {code} | {count} | [raw]({raw_url}) |")
    return "\n".join(rows)

table_all = build_table("regions")
table_443 = build_table("regions_443")
updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

readme = f"""# IP List by Region

自動從 [all.txt](https://zip.cm.edu.kg/all.txt) 抓取並按國家代碼分類，每日更新。

## 全部 Port

| 國家代碼 | 條目數 | Raw URL |
|----------|--------|---------|
{table_all}

## 僅 443 Port

| 國家代碼 | 條目數 | Raw URL |
|----------|--------|---------|
{table_443}

---
*最後更新：{updated}*
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md updated")
