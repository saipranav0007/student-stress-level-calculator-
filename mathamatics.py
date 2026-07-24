# Weights for each factor (direction + magnitude explained in core_subject/stress_rules.py)
WEIGHTS = {
    "sleep_hours": -1.5,
    "study_hours": 2.0,
    "screen_time": 1.5,
    "social_activity": -1.0,
    "exercise_hours": -1.2
}

# Max realistic value for each factor, used for normalization
MAX_VALUES = {
    "sleep_hours": 12,
    "study_hours": 12,
    "screen_time": 12,
    "social_activity": 12,
    "exercise_hours": 12
}


def normalize(value, max_value):
    """Scales a raw value to a 0-1 range."""
    return min(value / max_value, 1.0)


def calculate_stress_score(sleep_hours, study_hours, screen_time, social_activity, exercise_hours):
    """Combines all 5 factors into a single stress score (0-100)."""
    raw_inputs = {
        "sleep_hours": sleep_hours,
        "study_hours": study_hours,
        "screen_time": screen_time,
        "social_activity": social_activity,
        "exercise_hours": exercise_hours
    }

    weighted_total = 0
    for factor, value in raw_inputs.items():
        norm_value = normalize(value, MAX_VALUES[factor])
        weighted_total += norm_value * WEIGHTS[factor]

    # Rescale weighted_total to a 0-100 range
    min_possible = -3.7
    max_possible = 3.5
    score = ((weighted_total - min_possible) / (max_possible - min_possible)) * 100
    score = max(0, min(100, score))  # keep within 0-100

    return round(score, 2)


def classify_stress(score):
    """Turns the numeric score into a Low/Medium/High label."""
    if score < 35:
        return "Low"
    elif score < 65:
        return "Medium"
    else:
        return "High"
    if __name__ == "__main__":
        test_score = calculate_stress_score(7, 4, 3, 2, 1)
        print("Score:", test_score)
        print("Category:", classify_stress(test_score))
        