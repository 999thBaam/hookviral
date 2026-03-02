"""
Trending Topics Engine
Fetches real-time trending topics from multiple sources
and generates hooks around current trends.
"""

import re
import random
import requests
from datetime import datetime, timezone

HEADERS = {
    "User-Agent": "HookViral/1.0 (TrendAnalyzer)"
}


def fetch_reddit_trending() -> list[dict]:
    """Fetch trending topics from Reddit's popular posts."""
    topics = []
    try:
        resp = requests.get(
            "https://www.reddit.com/r/popular.json",
            headers=HEADERS,
            params={"limit": 25},
            timeout=10,
        )
        resp.raise_for_status()
        children = resp.json().get("data", {}).get("children", [])
        for child in children:
            post = child["data"]
            topics.append({
                "title": post.get("title", ""),
                "subreddit": post.get("subreddit", ""),
                "score": post.get("score", 0),
                "url": f"https://reddit.com{post.get('permalink', '')}",
            })
    except Exception:
        pass
    return topics


def fetch_google_trends_topics() -> list[dict]:
    """Fetch daily trending searches from Google Trends RSS."""
    topics = []
    try:
        resp = requests.get(
            "https://trends.google.com/trending/rss?geo=US",
            headers=HEADERS,
            timeout=10,
        )
        resp.raise_for_status()
        # Parse XML manually — extract titles between <title> tags
        titles = re.findall(r"<title>(.+?)</title>", resp.text)
        for title in titles[1:26]:  # skip the feed title
            topics.append({
                "title": title.strip(),
                "source": "Google Trends",
                "score": 0,
            })
    except Exception:
        pass
    return topics


def extract_trending_keywords(topics: list[dict]) -> list[str]:
    """Extract the most common meaningful keywords from trending topics."""
    stop_words = {
        "the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
        "have", "has", "had", "do", "does", "did", "will", "would", "could",
        "should", "may", "might", "shall", "can", "to", "of", "in", "for",
        "on", "with", "at", "by", "from", "as", "into", "about", "like",
        "through", "after", "over", "between", "out", "up", "off", "down",
        "and", "but", "or", "nor", "not", "no", "so", "if", "than", "too",
        "very", "just", "that", "this", "it", "its", "my", "your", "his",
        "her", "our", "their", "what", "which", "who", "whom", "how", "when",
        "where", "why", "all", "each", "every", "both", "few", "more", "most",
        "other", "some", "such", "only", "own", "same", "then", "now", "here",
        "there", "also", "new", "old", "get", "got", "vs", "via", "per",
    }

    word_counts = {}
    for topic in topics:
        words = re.findall(r"[a-zA-Z]+", topic["title"].lower())
        for word in words:
            if word not in stop_words and len(word) > 2:
                word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return [w[0] for w in sorted_words[:20]]


TREND_HOOK_TEMPLATES = [
    "Everyone is talking about {topic} right now — here's what you need to know",
    "{topic} is trending and nobody is taking advantage of it yet",
    "The {topic} situation just changed everything. Here's why it matters to you",
    "I predicted the {topic} trend 6 months ago. Here's what's coming next",
    "How to use the {topic} trend to grow your brand right now",
    "Stop scrolling — the {topic} news affects you more than you think",
    "{topic} went viral today. Here's the lesson most people are missing",
    "3 ways to capitalize on the {topic} trend before everyone else does",
    "The real story behind {topic} that no one is reporting",
    "If you're ignoring {topic}, you're leaving money on the table",
    "I spent 5 hours researching {topic} so you don't have to",
    "Hot take: {topic} is going to change {niche} forever",
    "The {topic} trend proves what I've been saying all along",
    "Why {topic} matters for content creators right now",
    "{topic} broke the internet today. Here's my honest take",
]


def generate_trending_hooks(niche: str = None, count: int = 10) -> dict:
    """
    Fetch real-time trends and generate hooks around them.
    Returns trends data + generated hooks.
    """
    # Fetch from multiple sources in parallel (sequentially for simplicity)
    reddit_topics = fetch_reddit_trending()
    google_topics = fetch_google_trends_topics()

    all_topics = reddit_topics + google_topics
    keywords = extract_trending_keywords(all_topics)

    # Build trending summary
    trending_items = []
    seen_titles = set()
    for topic in all_topics[:15]:
        title = topic["title"][:80]
        if title.lower() not in seen_titles:
            seen_titles.add(title.lower())
            trending_items.append({
                "title": title,
                "source": topic.get("subreddit", topic.get("source", "Web")),
                "score": topic.get("score", 0),
            })

    # Generate hooks around trending topics
    hooks = []
    selected_topics = random.sample(all_topics, min(count * 2, len(all_topics))) if all_topics else []

    for topic in selected_topics:
        if len(hooks) >= count:
            break

        topic_text = topic["title"]

        # Extract a clean, short topic phrase (2-4 key words)
        # For Google Trends, topics are already short keywords
        if topic.get("source") == "Google Trends":
            short_topic = topic_text.strip()
        else:
            # For Reddit, extract the most meaningful noun phrase
            words = topic_text.split()
            # Remove common filler starts
            skip_starts = {"my", "i", "the", "a", "an", "this", "so", "just", "what", "how", "why"}
            clean_words = []
            started = False
            for w in words:
                if not started and w.lower() in skip_starts:
                    continue
                started = True
                clean_words.append(w)
                if len(clean_words) >= 4:
                    break
            short_topic = " ".join(clean_words) if clean_words else " ".join(words[:3])

        # Capitalize nicely
        short_topic = short_topic.strip(".,!?:;")

        template = random.choice(TREND_HOOK_TEMPLATES)
        niche_text = niche if niche else "your industry"

        hook = template.format(topic=short_topic, niche=niche_text)

        hooks.append({
            "hook": hook,
            "based_on": topic_text[:60],
            "source": topic.get("subreddit", topic.get("source", "Web")),
            "type": "Trending",
        })

    return {
        "trending_topics": trending_items[:10],
        "trending_keywords": keywords[:10],
        "hooks": hooks[:count],
        "fetched_at": datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "sources_count": {
            "reddit": len(reddit_topics),
            "google_trends": len(google_topics),
        },
    }
