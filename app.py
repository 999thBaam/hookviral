"""
Instagram Hook Analyzer - Web App
Analyze and generate viral hooks for Instagram content.
"""

from flask import Flask, render_template, request, jsonify
from analyzer import analyze_hook, generate_hooks
from hooks_database import HOOK_FORMULAS, NICHES
from trending import generate_trending_hooks
from ab_test import compare_hooks

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        hook_types=HOOK_FORMULAS,
        niches=NICHES,
    )


@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    data = request.get_json()
    hook_text = data.get("hook", "").strip()
    if not hook_text:
        return jsonify({"error": "Please enter a hook to analyze"}), 400
    result = analyze_hook(hook_text)
    return jsonify(result)


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json()
    niche = data.get("niche", "marketing")
    hook_type = data.get("hook_type")
    count = min(int(data.get("count", 10)), 20)
    results = generate_hooks(niche, hook_type, count)
    return jsonify({"hooks": results})


@app.route("/api/trending", methods=["POST"])
def api_trending():
    data = request.get_json()
    niche = data.get("niche")
    count = min(int(data.get("count", 10)), 20)
    results = generate_trending_hooks(niche, count)
    return jsonify(results)


@app.route("/api/ab-test", methods=["POST"])
def api_ab_test():
    data = request.get_json()
    hook_a = data.get("hook_a", "").strip()
    hook_b = data.get("hook_b", "").strip()
    if not hook_a or not hook_b:
        return jsonify({"error": "Please enter both hooks to compare"}), 400
    result = compare_hooks(hook_a, hook_b)
    return jsonify(result)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    debug = os.environ.get("FLASK_ENV") != "production"
    app.run(debug=debug, host="0.0.0.0", port=port)
