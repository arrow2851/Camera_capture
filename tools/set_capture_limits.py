"""Apply v1.2 capture limits to Android source after zoom patch; fail on unexpected source."""
from pathlib import Path

source = Path("app/src/main/java/com/example/dscintervalcamera/MainActivity.java")
text = source.read_text(encoding="utf-8")
replacements = [
    ("interval < 2 || interval > 600", "interval < 1 || interval > 600"),
    ("count < 1 || count > 2000", "count < 1 || count > 3000"),
    ("interval 2–600 sec, photos 1–2000", "interval 1–600 sec, photos 1–3000"),
    ('"Seconds between photos"', '"Seconds between photos (1–600)"'),
    ('"Number of photos"', '"Number of photos (1–3000)"'),
]
for old, new in replacements:
    if old not in text and new not in text:
        raise SystemExit(f"Missing expected Android source fragment: {old}")
    text = text.replace(old, new)

note_old = "Keep this app in the foreground while recording."
note_new = (
    "Keep this app in the foreground while recording. "
    "A 3,000-photo run can last 50 minutes at 1 second and use several GB."
)
if note_old in text and "A 3,000-photo run" not in text:
    text = text.replace(note_old, note_new)
source.write_text(text, encoding="utf-8")
assert "interval < 1 || interval > 600" in text
assert "count < 1 || count > 3000" in text
assert "interval 1–600 sec, photos 1–3000" in text
print("Android limits updated: up to 3,000 photos, minimum 1 second.")
