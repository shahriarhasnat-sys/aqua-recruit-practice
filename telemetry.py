def depth_status(age_s):
    if age_s is None:
        return "NO DATA"
    elif age_s < 2:
        return "LIVE"
    else:
        return "STALE"