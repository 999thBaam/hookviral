"""
A/B Testing Engine
Compares two hooks head-to-head and picks a winner with detailed reasoning.
"""

from analyzer import analyze_hook


def compare_hooks(hook_a: str, hook_b: str) -> dict:
    """
    Compare two hooks and return detailed A/B comparison.
    """
    result_a = analyze_hook(hook_a)
    result_b = analyze_hook(hook_b)

    score_a = result_a["score"]
    score_b = result_b["score"]

    # Determine winner
    diff = abs(score_a - score_b)
    if diff <= 5:
        verdict = "TIE"
        verdict_detail = "Both hooks are very close in viral potential. Test both and let your audience decide."
    elif score_a > score_b:
        verdict = "A"
        verdict_detail = f"Hook A scores {diff} points higher. It has stronger viral potential."
    else:
        verdict = "B"
        verdict_detail = f"Hook B scores {diff} points higher. It has stronger viral potential."

    # Category-by-category comparison
    categories = ["power_words", "emotion", "pattern", "structure", "length", "specificity"]
    category_labels = {
        "power_words": "Power Words",
        "emotion": "Emotional Triggers",
        "pattern": "Hook Pattern",
        "structure": "Structure & Flow",
        "length": "Optimal Length",
        "specificity": "Specificity",
    }

    comparison = []
    a_wins = 0
    b_wins = 0
    for cat in categories:
        val_a = result_a["breakdown"].get(cat, 0)
        val_b = result_b["breakdown"].get(cat, 0)
        if val_a > val_b:
            cat_winner = "A"
            a_wins += 1
        elif val_b > val_a:
            cat_winner = "B"
            b_wins += 1
        else:
            cat_winner = "TIE"

        comparison.append({
            "category": category_labels.get(cat, cat),
            "key": cat,
            "score_a": val_a,
            "score_b": val_b,
            "winner": cat_winner,
        })

    # Strengths and weaknesses
    strengths_a = []
    strengths_b = []
    for c in comparison:
        if c["winner"] == "A" and c["score_a"] >= 70:
            strengths_a.append(c["category"])
        if c["winner"] == "B" and c["score_b"] >= 70:
            strengths_b.append(c["category"])

    # Improvement recommendations
    recommendations = []
    if verdict == "A":
        weak_cats = [c for c in comparison if c["winner"] == "B"]
        if weak_cats:
            recommendations.append(
                f"Hook A could improve in: {', '.join(c['category'] for c in weak_cats)}"
            )
        recommendations.extend(result_a["tips"][:2])
    elif verdict == "B":
        weak_cats = [c for c in comparison if c["winner"] == "A"]
        if weak_cats:
            recommendations.append(
                f"Hook B could improve in: {', '.join(c['category'] for c in weak_cats)}"
            )
        recommendations.extend(result_b["tips"][:2])
    else:
        recommendations.append("Try combining the best elements of both hooks.")
        if result_a["tips"]:
            recommendations.append(f"Hook A tip: {result_a['tips'][0]}")
        if result_b["tips"]:
            recommendations.append(f"Hook B tip: {result_b['tips'][0]}")

    # Generate a combined "best of both" suggestion
    best_elements = []
    for c in comparison:
        if c["winner"] == "A" and c["score_a"] >= 60:
            best_elements.append(f"{c['category']} from Hook A")
        elif c["winner"] == "B" and c["score_b"] >= 60:
            best_elements.append(f"{c['category']} from Hook B")

    return {
        "hook_a": {
            "text": hook_a,
            "score": score_a,
            "rating": result_a["rating"],
            "rating_color": result_a["rating_color"],
            "breakdown": result_a["breakdown"],
            "emotions": list(result_a["emotions_triggered"].keys()),
            "strengths": strengths_a,
        },
        "hook_b": {
            "text": hook_b,
            "score": score_b,
            "rating": result_b["rating"],
            "rating_color": result_b["rating_color"],
            "breakdown": result_b["breakdown"],
            "emotions": list(result_b["emotions_triggered"].keys()),
            "strengths": strengths_b,
        },
        "verdict": verdict,
        "verdict_detail": verdict_detail,
        "category_wins": {"A": a_wins, "B": b_wins, "TIE": 6 - a_wins - b_wins},
        "comparison": comparison,
        "recommendations": recommendations,
        "best_elements": best_elements,
    }
