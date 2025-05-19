# Lost Ark PvP Mobility Calculator
# See README.md for usage instructions

import math
from typing import List, Dict

def calculate_uses_per_sec(cooldown: float) -> float:
    return 1 / cooldown

def calculate_mobility_score(uses_per_sec: float, distance: float, flexibility: float) -> float:
    return uses_per_sec * distance * flexibility

def calculate_base_score(skills: List[Dict]) -> float:
    return sum(skill['mobility_score'] for skill in skills)

def calculate_weighted_score(base_score: float, number_of_skills: int) -> float:
    return base_score * math.sqrt(number_of_skills)

def normalize_scores(weighted_scores: Dict[str, float]) -> Dict[str, float]:
    max_score = max(weighted_scores.values())
    return {cls: (score / max_score) * 100 for cls, score in weighted_scores.items()}

def evaluate_class(skills: List[Dict]) -> Dict[str, float]:
    for skill in skills:
        skill['uses_per_sec'] = calculate_uses_per_sec(skill['cooldown'])
        skill['mobility_score'] = calculate_mobility_score(
            skill['uses_per_sec'], skill['distance'], skill['flexibility']
        )

    base_score = calculate_base_score(skills)
    weighted_score = calculate_weighted_score(base_score, len(skills))

    return {
        'base_score': base_score,
        'weighted_score': weighted_score,
        'skills': skills
    }

# Example usage
gunslinger_skills = [
    {'name': 'Dexterous Shot', 'distance': 12, 'cooldown': 6, 'flexibility': 0.45},
    {'name': 'Quick Step', 'distance': 8, 'cooldown': 10, 'flexibility': 0.95},
    {'name': 'Somersault Shot', 'distance': 10, 'cooldown': 6, 'flexibility': 0.70},
    {'name': 'Peacekeeper', 'distance': 6, 'cooldown': 12, 'flexibility': 0.50},
    {'name': 'Death Fire', 'distance': 6, 'cooldown': 24, 'flexibility': 0.80},
]

berserker_skills = [
    {'name': 'Shoulder Charge (1)', 'distance': 11, 'cooldown': 12, 'flexibility': 0.90},
    {'name': 'Shoulder Charge (2)', 'distance': 11, 'cooldown': 12, 'flexibility': 0.90},
    {'name': 'Diving Slash', 'distance': 10, 'cooldown': 16, 'flexibility': 0.65},
]

gunslinger_results = evaluate_class(gunslinger_skills)
berserker_results = evaluate_class(berserker_skills)

weighted_scores = {
    'Gunslinger': gunslinger_results['weighted_score'],
    'Berserker': berserker_results['weighted_score'],
}

normalized = normalize_scores(weighted_scores)

print("Normalized Mobility Scores (0-100):")
for cls, score in normalized.items():
    print(f"{cls}: {score:.2f}")
