FACTOR_INFO = {
    "sleep_hours": {
        "weight": -1.5,
        "reason": "Sleep deprivation raises cortisol (the stress hormone) and impairs the brain's ability to regulate emotions. Less than 6 hours of sleep is linked to measurably higher stress and anxiety.",
        "ideal_range": "7-9 hours/night"
    },
    "study_hours": {
        "weight": 2.0,
        "reason": "Extended study sessions without breaks lead to mental fatigue and academic pressure, a major contributor to student stress, especially close to exams.",
        "ideal_range": "Balanced with breaks (Pomodoro-style)"
    },
    "screen_time": {
        "weight": 1.5,
        "reason": "Excessive screen time (especially social media) is linked to sleep disruption and social comparison, both of which raise anxiety and stress.",
        "ideal_range": "Under 3-4 hours/day of non-academic use"
    },
    "social_activity": {
        "weight": -1.0,
        "reason": "Social support is a well-documented stress buffer in psychology. Interaction with friends/family releases oxytocin, which counteracts cortisol.",
        "ideal_range": "At least 1-2 hours/day"
    },
    "exercise_hours": {
        "weight": -1.2,
        "reason": "Physical activity releases endorphins and reduces cortisol levels. Regular exercise is a clinically recommended stress-management intervention.",
        "ideal_range": "30-60 minutes/day"
    },
}


def get_factor_explanation(factor_name):
    """Return the reasoning behind a given factor."""
    return FACTOR_INFO.get(factor_name, {}).get("reason", "No data available")


def get_all_explanations():
    """Return the full dictionary."""
    return FACTOR_INFO
