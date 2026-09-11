#!/usr/bin/env python3
"""检查所有 markdown 文件里的内部链接是否有效。

知识库靠链接把 agent 从入口带到具体规则。链接一断，路由就断，agent 只能
凭记忆瞎编。所以每次改动都要跑这个。

用法：python3 scripts/check_links.py
"""

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r"\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "#", "mailto:")

broken = []
total = 0

for path in sorted(glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)):
    rel = os.path.relpath(path, ROOT)
    if rel.startswith(".git"):
        continue
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    for m in LINK.finditer(text):
        target = m.group(1).strip()
        if target.startswith(SKIP_PREFIXES):
            continue
        target = target.split("#")[0]
        if not target:
            continue
        total += 1
        resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(resolved):
            broken.append(f"{rel} -> {target}")

print(f"检查了 {total} 条内部链接")
if broken:
    print(f"✗ {len(broken)} 条失效：")
    for b in broken:
        print(f"  {b}")
    sys.exit(1)
print("✓ 全部有效")
