"""
Hook Analyzer Engine
Scores hooks based on viral potential using multiple signals.
"""

import re
from hooks_database import HOOK_FORMULAS, POWER_WORDS, EMOTIONAL_TRIGGERS


def analyze_hook(hook_text: str) -> dict:
    """Analyze a hook and return a detailed viral score breakdown."""
    hook_lower = hook_text.lower().strip()
    scores = {}
    tips = []
    details = []

    # 1. Length score (optimal: 8-15 words for reels, up to 20 for captions)
    word_count = len(hook_lower.split())
    if 8 <= word_count <= 15:
        scores["length"] = 1.0
        details.append(f"Word count ({word_count}) is in the sweet spot")
    elif 5 <= word_count <= 20:
        scores["length"] = 0.7
        details.append(f"Word count ({word_count}) is acceptable")
    else:
        scores["length"] = 0.3
        if word_count < 5:
            tips.append("Your hook is too short. Add more context to build curiosity.")
        else:
            tips.append("Your hook is too long. Trim it to 8-15 words for maximum impact.")
        details.append(f"Word count ({word_count}) is not optimal")

    # 2. Power words score
    power_word_count = sum(1 for word in POWER_WORDS if word in hook_lower)
    power_words_found = [w for w in POWER_WORDS if w in hook_lower]
    if power_word_count >= 3:
        scores["power_words"] = 1.0
    elif power_word_count >= 1:
        scores["power_words"] = 0.6 + (power_word_count * 0.15)
    else:
        scores["power_words"] = 0.2
        tips.append(f"Add power words like: {', '.join(POWER_WORDS[:6])}")
    details.append(f"Power words found: {power_words_found if power_words_found else 'none'}")

    # 3. Emotional trigger score
    emotions_triggered = {}
    for emotion, triggers in EMOTIONAL_TRIGGERS.items():
        found = [t for t in triggers if t in hook_lower]
        if found:
            emotions_triggered[emotion] = found

    emotion_count = len(emotions_triggered)
    if emotion_count >= 3:
        scores["emotion"] = 1.0
    elif emotion_count >= 2:
        scores["emotion"] = 0.8
    elif emotion_count >= 1:
        scores["emotion"] = 0.6
    else:
        scores["emotion"] = 0.2
        tips.append("Add emotional triggers — curiosity and urgency perform best.")
    details.append(f"Emotions triggered: {list(emotions_triggered.keys()) if emotions_triggered else 'none'}")

    # 4. Hook type pattern matching
    hook_type_matches = []
    best_match_score = 0
    for hook_type, data in HOOK_FORMULAS.items():
        for template in data["templates"]:
            # Simplify template: extract key words and check if they appear in the hook
            key_words = re.sub(r"\{[^}]+\}", " ", template.lower()).split()
            key_words = [w for w in key_words if len(w) > 3]
            if key_words:
                match_ratio = sum(1 for w in key_words if w in hook_lower) / len(key_words)
                if match_ratio >= 0.4:
                    hook_type_matches.append(data["label"])
                    best_match_score = max(best_match_score, data["score_weight"])
                    break

    if hook_type_matches:
        scores["pattern"] = best_match_score
        details.append(f"Matches hook types: {hook_type_matches}")
    else:
        scores["pattern"] = 0.4
        details.append("No strong pattern match — could be unique or needs improvement")

    # 5. Structure signals
    structure_score = 0.5
    structure_signals = []

    if hook_lower[0].isupper() or hook_text[0].isdigit():
        structure_score += 0.05
        structure_signals.append("Starts strong")

    if any(hook_lower.startswith(w) for w in ["stop", "warning", "don't", "never", "the", "why", "how", "what", "if"]):
        structure_score += 0.1
        structure_signals.append("Strong opening word")

    if "?" in hook_text:
        structure_score += 0.1
        structure_signals.append("Uses question format")

    if re.search(r"\d+", hook_text):
        structure_score += 0.1
        structure_signals.append("Contains numbers (specificity)")

    if "..." in hook_text or "—" in hook_text:
        structure_score += 0.05
        structure_signals.append("Uses suspense punctuation")

    if any(w in hook_lower for w in ["you", "your", "you're"]):
        structure_score += 0.1
        structure_signals.append("Addresses viewer directly (you/your)")
    else:
        tips.append("Use 'you/your' to speak directly to the viewer.")

    scores["structure"] = min(structure_score, 1.0)
    details.append(f"Structure signals: {structure_signals if structure_signals else 'none detected'}")

    # 6. Specificity score
    has_numbers = bool(re.search(r"\d+", hook_text))
    has_timeframe = any(w in hook_lower for w in ["days", "weeks", "months", "years", "hours", "minutes", "seconds"])
    has_money = bool(re.search(r"\$[\d,]+", hook_text)) or any(w in hook_lower for w in ["money", "income", "revenue", "$"])

    specificity = 0.3
    if has_numbers:
        specificity += 0.25
    if has_timeframe:
        specificity += 0.25
    if has_money:
        specificity += 0.2

    scores["specificity"] = min(specificity, 1.0)
    if specificity < 0.5:
        tips.append("Add specific numbers, timeframes, or amounts to increase credibility.")
    details.append(f"Specificity: numbers={has_numbers}, timeframe={has_timeframe}, money={has_money}")

    # Calculate final score (weighted average)
    weights = {
        "power_words": 0.20,
        "emotion": 0.25,
        "pattern": 0.15,
        "structure": 0.15,
        "length": 0.10,
        "specificity": 0.15,
    }

    final_score = sum(scores[k] * weights[k] for k in weights)
    final_score = round(final_score * 100)

    # Rating
    if final_score >= 80:
        rating = "VIRAL POTENTIAL"
        rating_color = "green"
    elif final_score >= 60:
        rating = "STRONG"
        rating_color = "blue"
    elif final_score >= 40:
        rating = "AVERAGE"
        rating_color = "yellow"
    else:
        rating = "NEEDS WORK"
        rating_color = "red"

    # Generate improvement suggestion
    if not tips:
        tips.append("This hook is solid! Test it and track performance.")

    return {
        "hook": hook_text,
        "score": final_score,
        "rating": rating,
        "rating_color": rating_color,
        "breakdown": {k: round(v * 100) for k, v in scores.items()},
        "emotions_triggered": emotions_triggered,
        "power_words_found": power_words_found,
        "hook_types_matched": hook_type_matches,
        "tips": tips,
        "details": details,
    }


def generate_hooks(niche: str, hook_type: str = None, count: int = 5) -> list[dict]:
    """Generate hook suggestions for a given niche."""
    import random

    niche_title = niche.title()
    results = []

    types_to_use = [hook_type] if hook_type and hook_type in HOOK_FORMULAS else list(HOOK_FORMULAS.keys())

    placeholders = {
        "topic": niche,
        "Topic": niche_title,
        "outcome": f"{niche} results",
        "common_thing": f"traditional {niche} advice",
        "unexpected_truth": "a complete myth",
        "action": f"focusing on {niche}",
        "common_action": f"basic {niche} methods",
        "thing": f"this {niche} strategy",
        "authority": f"{niche} experts",
        "percentage": str(random.choice([80, 90, 95, 97])),
        "popular_thing": f"mainstream {niche}",
        "Popular_advice": f"The most common {niche} advice",
        "Common_thing": f"Most {niche} advice",
        "popular_action": f"typical {niche} approach",
        "opinion": f"{niche} is changing faster than you think",
        "statement": f"{niche} success is simpler than gurus make it",
        "bad_situation": f"struggling with {niche}",
        "good_outcome": f"mastered {niche}",
        "start": "zero", "end": f"top 1% in {niche}",
        "timeframe": "6 months",
        "realization": f"how {niche} actually works",
        "mistake": f"one {niche} mistake",
        "advice": f"one thing about {niche}",
        "lesson": f"the truth about {niche}",
        "age": str(random.choice([22, 25, 28, 30])),
        "job": "9-5",
        "question": f"about my {niche} journey",
        "Number": str(random.choice([3, 5, 7, 10])),
        "number": str(random.choice([3, 5, 7, 10])),
        "year": "2026",
        "time": "5",
        "tools": f"{niche} tools",
        "amount": str(random.choice([50, 100, 200, 500])),
        "things": f"{niche} principles",
        "situation": f"behind in {niche}",
        "smaller_number": "2",
        "profession": f"{niche} specialist",
        "years": str(random.choice([5, 7, 10])),
        "achievement": f"built a successful {niche} brand",
        "clients": "clients",
        "impressive_feat": f"grew my {niche} audience to 100K",
        "strategy": f"{niche} framework",
        "industry": niche,
        "credential": f"has spent years in {niche}",
        "event": "it's too late",
        "prediction": f"{niche} is about to shift",
        "resource": f"{niche} guide",
        "scenario": f"you could master {niche} in 30 days",
        "simple_action": f"one {niche} habit",
        "surprising_fact": f"most {niche} success comes from one skill",
        "successful_people": f"top {niche} creators",
    }

    selected_templates = []
    for t in types_to_use:
        templates = HOOK_FORMULAS[t]["templates"]
        for tmpl in random.sample(templates, min(2, len(templates))):
            selected_templates.append((t, tmpl))

    random.shuffle(selected_templates)

    for hook_type_key, template in selected_templates[:count]:
        try:
            filled = template.format(**placeholders)
        except KeyError:
            filled = template
            for k, v in placeholders.items():
                filled = filled.replace(f"{{{k}}}", v)

        hook_data = HOOK_FORMULAS[hook_type_key]
        results.append({
            "hook": filled,
            "type": hook_data["label"],
            "viral_potential": round(hook_data["score_weight"] * 100),
        })

    return results
