"""
HookViral - Complete Instagram Viral Toolkit
Analyze hooks, discover trending songs, study viral reels, and master the algorithm.
"""

from flask import Flask, render_template, request, jsonify
from analyzer import analyze_hook, generate_hooks
from hooks_database import HOOK_FORMULAS, NICHES
from trending import generate_trending_hooks
from ab_test import compare_hooks
from viral_data import (
    TRENDING_SONGS, VIRAL_REELS, ALGORITHM_DATA,
    fetch_live_trending_songs, get_viral_strategy,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        hook_types=HOOK_FORMULAS,
        niches=NICHES,
        trending_songs=TRENDING_SONGS,
        viral_reels=VIRAL_REELS,
        algorithm=ALGORITHM_DATA,
    )


@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json()
    hook_text = data.get("hook", "").strip()
    if not hook_text:
        return jsonify({"error": "Please enter a hook to analyze"}), 400
    return jsonify(analyze_hook(hook_text))


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json()
    niche = data.get("niche", "marketing")
    hook_type = data.get("hook_type")
    count = min(int(data.get("count", 10)), 20)
    return jsonify({"hooks": generate_hooks(niche, hook_type, count)})


@app.route("/api/trending", methods=["POST"])
def api_trending():
    data = request.get_json()
    niche = data.get("niche")
    count = min(int(data.get("count", 10)), 20)
    return jsonify(generate_trending_hooks(niche, count))


@app.route("/api/ab-test", methods=["POST"])
def api_ab_test():
    data = request.get_json()
    hook_a = data.get("hook_a", "").strip()
    hook_b = data.get("hook_b", "").strip()
    if not hook_a or not hook_b:
        return jsonify({"error": "Please enter both hooks to compare"}), 400
    return jsonify(compare_hooks(hook_a, hook_b))


@app.route("/api/songs", methods=["GET"])
def api_songs():
    songs = fetch_live_trending_songs()
    return jsonify({"songs": songs})


@app.route("/api/strategy", methods=["POST"])
def api_strategy():
    data = request.get_json()
    niche = data.get("niche")
    return jsonify(get_viral_strategy(niche))


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(debug=debug, host="0.0.0.0", port=port)
