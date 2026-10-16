#!/usr/bin/env python3
"""Builds index.json (the manifest weecounter downloads) from profiles/*.dhikr.

Header lines before the first slide are read:
  # Name           first "# " line: the profile name (else the file name)
  @id slug         unique id, never change it (else the file name)
  @version N       whole number, raise it for every change (else 1)
  @author Name
  @desc text       repeat the line for more paragraphs
"""
import json, re, sys
from pathlib import Path

SLIDE = re.compile(r"---\s*([0-9]+)")
BARE = re.compile(r"---")
profiles, ids, bad = [], set(), False

for f in sorted(Path("profiles").glob("*.dhikr")):
    text = f.read_text(encoding="utf-8-sig")
    head = {"@id": [], "@version": [], "@author": [], "@desc": []}
    name, slides = None, 0
    for ln in text.splitlines():
        s = ln.strip()
        m = SLIDE.fullmatch(s)
        if m:
            if int(m.group(1)) > 0:
                slides += 1
            continue
        if slides or BARE.fullmatch(s):
            continue
        if s.startswith("#") and len(s) > 1 and name is None:
            name = s[1:].strip()
        for k in head:
            if s.startswith(k + " "):
                head[k].append(s[len(k) + 1:].strip())
    # the header ends at the first slide; the loop above skips everything after it
    if slides == 0:
        print(f"{f}: no slides"); bad = True; continue
    pid = head["@id"][0] if head["@id"] else f.stem
    if pid in ids or not re.fullmatch(r"[\w.-]+", pid):
        print(f"{f}: id '{pid}' is not unique or has odd characters"); bad = True; continue
    ids.add(pid)
    try:
        ver = int(head["@version"][0]) if head["@version"] else 1
    except ValueError:
        print(f"{f}: @version must be a whole number"); bad = True; continue
    profiles.append({"id": pid, "name": name or f.stem, "ver": ver,
                     "author": " ".join(head["@author"]), "desc": "\n".join(head["@desc"]),
                     "slides": slides, "f": f.as_posix()})

if bad:
    sys.exit(1)
Path("index.json").write_text(json.dumps({"v": 1, "profiles": profiles}, ensure_ascii=False,
                                         indent=1) + "\n", encoding="utf-8")
print(f"{len(profiles)} profiles")
