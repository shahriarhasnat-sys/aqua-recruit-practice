from telemetry import depth_status

assert depth_status(None) == "NO DATA"
assert depth_status(1.9) == "LIVE"
assert depth_status(2.0) == "STALE"
assert depth_status(3.0) == "STALE"

print("all tests pass")