"""One-off data fix for Tier 0 of the improvement roadmap.

- Repairs two corrupt Github URL values
- Normalizes http:// -> https:// and strips trailing slashes on github.com URLs
- Replaces null Speakers with []
- Collapses straggler track names into the 20 canonical ones

Only files whose content changes are rewritten, preserving each file's
existing indent / trailing-newline style.
"""
import glob
import json

TRACK_MAP = {
    "Malware": "Malware Defense",
    "Threat Hunting and Incident Response": "Data Forensics/Incident Response",
    "Digital Forensics": "Data Forensics/Incident Response",
    "Internet of Things": "Internet Of Things",
    "Network": "Network Defense",
    "Risks": "Vulnerability Assessment",
    "Privacy": "Vulnerability Assessment",
}

URL_FIXES = {
    "nuhttps://github.com/netxms/netxmsll": "https://github.com/netxms/netxms",
    "Qiling Framework: Deep Dive Into Obfuscated Binary Analysis": "https://github.com/qilingframework/qiling",
}


def dump_like(data, raw):
    """Serialize `data` in the same style `raw` was written in."""
    for indent in (2, 4):
        for nl in ("", "\n"):
            if json.dumps(json.loads(raw), indent=indent, ensure_ascii=False) + nl == raw:
                return json.dumps(data, indent=indent, ensure_ascii=False) + nl
    return json.dumps(data, indent=2, ensure_ascii=False) + ("\n" if raw.endswith("\n") else "")


def fix(tool):
    changed = False

    url = tool.get("Github URL")
    if isinstance(url, str):
        new = URL_FIXES.get(url, url).strip()
        if new.startswith("http://github.com"):
            new = "https://" + new[len("http://"):]
        if new.startswith("https://github.com/") and new.endswith("/"):
            new = new.rstrip("/")
        if new != url:
            tool["Github URL"] = new
            changed = True

    if tool.get("Speakers") is None and "Speakers" in tool:
        tool["Speakers"] = []
        changed = True

    tracks = tool.get("Tracks")
    if isinstance(tracks, list):
        seen, new_tracks = set(), []
        for t in tracks:
            t = TRACK_MAP.get(t, t)
            if t not in seen:
                seen.add(t)
                new_tracks.append(t)
        if new_tracks != tracks:
            tool["Tracks"] = new_tracks
            changed = True

    return changed


def main():
    touched = 0
    for path in sorted(glob.glob("tools/*/*/*.json")):
        with open(path, encoding="utf-8") as f:
            raw = f.read()
        data = json.loads(raw)
        if fix(data):
            with open(path, "w", encoding="utf-8") as f:
                f.write(dump_like(data, raw))
            touched += 1
            print(f"fixed {path}")
    print(f"\n{touched} files updated")


if __name__ == "__main__":
    main()
