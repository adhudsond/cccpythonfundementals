# log_analyzer.py
# Project: Log File Analyzer
# - Create sample log file (20+ entries)
# - Parse entries (timestamp | level | event_type | message)
# - Count INFO/WARNING/ERROR
# - Find most common error types
# - Write summary report to CSV (with timestamps + statistics)

import csv

LOG_FILE = "app.log"
SUMMARY_CSV = "log_summary.csv"

# ------------------------------------------------------------
# 1) Create a sample log file (20+ entries)
# Format: YYYY-MM-DD HH:MM:SS | LEVEL | TYPE | MESSAGE
# ------------------------------------------------------------
sample_logs = [
    "2026-02-25 08:00:01 | INFO | STARTUP | Service boot sequence initiated",
    "2026-02-25 08:00:05 | INFO | CONFIG | Loaded configuration successfully",
    "2026-02-25 08:01:12 | WARNING | DEPRECATED | Using deprecated config key 'lr'",
    "2026-02-25 08:02:20 | INFO | AUTH | User login succeeded",
    "2026-02-25 08:03:10 | ERROR | FILE_NOT_FOUND | data.csv not found",
    "2026-02-25 08:03:25 | INFO | RETRY | Retrying file load",
    "2026-02-25 08:03:40 | ERROR | FILE_NOT_FOUND | data.csv not found",
    "2026-02-25 08:04:15 | WARNING | SLOW_IO | Disk read latency high",
    "2026-02-25 08:05:02 | INFO | TRAINING | Training started",
    "2026-02-25 08:05:30 | INFO | METRICS | loss=0.92 acc=0.61",
    "2026-02-25 08:06:02 | ERROR | API_TIMEOUT | GET /features timed out",
    "2026-02-25 08:06:20 | WARNING | API_RETRY | Retrying external API request",
    "2026-02-25 08:06:45 | ERROR | API_TIMEOUT | GET /features timed out",
    "2026-02-25 08:07:10 | INFO | METRICS | loss=0.74 acc=0.70",
    "2026-02-25 08:07:42 | ERROR | VALUE_ERROR | Invalid value in column 'age'",
    "2026-02-25 08:08:05 | INFO | CLEANUP | Temporary files removed",
    "2026-02-25 08:08:33 | WARNING | MEMORY | Memory usage above threshold",
    "2026-02-25 08:09:01 | INFO | METRICS | loss=0.58 acc=0.79",
    "2026-02-25 08:10:10 | ERROR | PERMISSION_DENIED | Cannot write to output directory",
    "2026-02-25 08:10:45 | INFO | TRAINING | Training finished",
    "2026-02-25 08:11:00 | INFO | SHUTDOWN | Service shut down cleanly",
    "2026-02-25 08:11:15 | WARNING | CLOCK_SKEW | System clock drift detected",
]

with open(LOG_FILE, "w") as f:
    for line in sample_logs:
        f.write(line + "\n")

# ------------------------------------------------------------
# 2) Read and parse log entries
# ------------------------------------------------------------
entries = []
with open(LOG_FILE, "r") as f:
    for raw in f:
        raw = raw.strip()
        if not raw:
            continue

        parts = [p.strip() for p in raw.split("|")]
        if len(parts) < 4:
            # Skip malformed line safely
            continue

        timestamp, level, event_type, message = parts[0], parts[1], parts[2], parts[3]
        entries.append({
            "timestamp": timestamp,
            "level": level,
            "type": event_type,
            "message": message
        })

# ------------------------------------------------------------
# 3) Count errors, warnings, info
# ------------------------------------------------------------
level_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
for e in entries:
    lvl = e["level"].upper()
    if lvl in level_counts:
        level_counts[lvl] += 1

# ------------------------------------------------------------
# 4) Find most common error types
# ------------------------------------------------------------
error_type_counts = {}
for e in entries:
    if e["level"].upper() == "ERROR":
        t = e["type"]
        error_type_counts[t] = error_type_counts.get(t, 0) + 1

sorted_error_types = sorted(error_type_counts.items(), key=lambda item: (-item[1], item[0]))

# Time window (first/last timestamp)
first_ts = entries[0]["timestamp"] if entries else "N/A"
last_ts = entries[-1]["timestamp"] if entries else "N/A"

total_entries = len(entries)
total_errors = level_counts["ERROR"]
total_warnings = level_counts["WARNING"]
total_info = level_counts["INFO"]

error_rate = (total_errors / total_entries) * 100 if total_entries else 0

# ------------------------------------------------------------
# 5) Write summary report to CSV (timestamps + statistics)
# ------------------------------------------------------------
with open(SUMMARY_CSV, "w", newline="") as f:
    writer = csv.writer(f)

    # Header section
    writer.writerow(["Log Summary Report"])
    writer.writerow(["Log file", LOG_FILE])
    writer.writerow(["Start time", first_ts])
    writer.writerow(["End time", last_ts])
    writer.writerow(["Total entries", total_entries])
    writer.writerow(["INFO count", total_info])
    writer.writerow(["WARNING count", total_warnings])
    writer.writerow(["ERROR count", total_errors])
    writer.writerow(["Error rate (%)", f"{error_rate:.2f}"])
    writer.writerow([])

    # Error type breakdown
    writer.writerow(["Error Type Breakdown"])
    writer.writerow(["error_type", "count"])
    for err_type, count in sorted_error_types:
        writer.writerow([err_type, count])

# ------------------------------------------------------------
# 6) Print summary report
# ------------------------------------------------------------
print("=" * 72)
print("LOG ANALYZER REPORT")
print("=" * 72)
print(f"Log file:      {LOG_FILE}")
print(f"Time window:   {first_ts}  →  {last_ts}")
print(f"Total entries: {total_entries}")
print("-" * 72)
print(f"INFO:          {total_info}")
print(f"WARNING:       {total_warnings}")
print(f"ERROR:         {total_errors}")
print(f"Error rate:    {error_rate:.2f}%")
print("-" * 72)

print("Most common ERROR types:")
if sorted_error_types:
    top_n = 5
    for err_type, count in sorted_error_types[:top_n]:
        print(f"  {err_type:<18} {count}")
else:
    print("  None")

print("-" * 72)
print(f"Summary CSV written to: {SUMMARY_CSV}")
print("=" * 72)