"""
Viral Reels Data Engine
Curated database of trending songs, viral reels, algorithm insights,
and best practices — all backed by real data.

Sources:
- Dash Social: Trending Instagram Reels Songs (Feb/Mar 2026)
- Loopex Digital: Instagram Reels Statistics 2026
- Buffer: Best Time to Post on Instagram (9.6M posts analyzed)
- Later.com: Top Instagram Reels Trends 2026
- SocialPilot: Instagram Reels Trends 2026
"""

import requests
import re
import random
from datetime import datetime, timezone

HEADERS = {"User-Agent": "HookViral/1.0"}

# ─── TRENDING SONGS DATABASE ─────────────────────────────────────────────────

TRENDING_SONGS = [
    {
        "title": "End of Beginning",
        "artist": "Djo",
        "reels_count": "1.5M+ Reels",
        "vibe": "Nostalgic, Cinematic",
        "best_for": ["Travel recaps", "City montages", "Nostalgia content", "Before/after transformations"],
        "tip": "Save your most impactful visual for the lyric drop. The audio builds steadily — time your hook to it.",
        "trending_since": "Jan 2026",
        "status": "hot",
    },
    {
        "title": "Aperture",
        "artist": "Harry Styles",
        "reels_count": "111K+ Reels",
        "vibe": "Upbeat, Fun",
        "best_for": ["Brand personality showcases", "'We belong together' trend", "Product highlights", "Team intros"],
        "tip": "Use fast cuts synced to the beat. This track works best with the 'things that go together' format.",
        "trending_since": "Feb 2026",
        "status": "rising",
    },
    {
        "title": "DtMF (Piano Version)",
        "artist": "Bad Bunny",
        "reels_count": "117K+ Reels",
        "vibe": "Calm, Romantic",
        "best_for": ["Clothing showcases", "Dreamy interiors", "Makeup tutorials", "Tranquil travel"],
        "tip": "Soft, mellow energy. Perfect for aesthetic content — let visuals breathe, don't over-edit.",
        "trending_since": "Feb 2026",
        "status": "rising",
    },
    {
        "title": "Lush Life",
        "artist": "Zara Larsson",
        "reels_count": "202K+ Reels",
        "vibe": "Confident, Feel-Good",
        "best_for": ["Glow-ups", "Outfit transitions", "Confidence content", "Day-in-the-life"],
        "tip": "High energy track — match it with bold transitions and confident body language.",
        "trending_since": "Jan 2026",
        "status": "hot",
    },
    {
        "title": "All The Things She Said",
        "artist": "t.A.T.u",
        "reels_count": "47K+ Reels",
        "vibe": "Intense, Energetic",
        "best_for": ["Sports content", "Gym/fitness", "Health transformations", "Intense lifestyle"],
        "tip": "The intensity of this track matches high-energy content. Great for workout montages.",
        "trending_since": "Jan 2026",
        "status": "steady",
    },
    {
        "title": "Arizona Dreaming (Remastered)",
        "artist": "Various Artists",
        "reels_count": "313K+ Reels",
        "vibe": "Light, Dreamy",
        "best_for": ["Lifestyle content", "Aesthetic vlogs", "Cozy content", "Food/cooking"],
        "tip": "Pairs well with warm-toned visuals. Light and fun — don't overthink the edit.",
        "trending_since": "Jan 2026",
        "status": "hot",
    },
    {
        "title": "Give Me Everything",
        "artist": "Pitbull ft. Ne-Yo",
        "reels_count": "150K+ Reels",
        "vibe": "Party, Elegant",
        "best_for": ["Event recaps", "Black-and-white edits", "Vintage lifestyle", "Bridgerton aesthetic"],
        "tip": "The Bridgerton comeback. Use elegant, vintage-style visuals with slow-motion cuts.",
        "trending_since": "Feb 2026",
        "status": "rising",
    },
    {
        "title": "Vogue",
        "artist": "Madonna",
        "reels_count": "200K+ Reels",
        "vibe": "Fashion, Confident",
        "best_for": ["Outfit transitions", "Walk-in reveals", "Fashion content", "Confident struts"],
        "tip": "This is THE fashion track right now. Sharp transitions synced to the beat are key.",
        "trending_since": "Feb 2026",
        "status": "hot",
    },
    {
        "title": "Pretty Little Baby",
        "artist": "Various",
        "reels_count": "1.5M+ Reels",
        "vibe": "Cute, Wholesome",
        "best_for": ["Pet content", "Baby content", "Couple content", "Wholesome moments"],
        "tip": "One of the most-used audios. Works for any 'cute' content. Simple format wins.",
        "trending_since": "Dec 2025",
        "status": "mega",
    },
    {
        "title": "DAISIES",
        "artist": "Justin Bieber",
        "reels_count": "90K+ Reels",
        "vibe": "Chill, Laid-back",
        "best_for": ["Cooking videos", "Cozy travel clips", "Outfit checks", "Morning routines"],
        "tip": "Chill vibe that works for lifestyle content. Don't rush the edits — let it breathe.",
        "trending_since": "Feb 2026",
        "status": "rising",
    },
]


# ─── VIRAL REELS SHOWCASE ────────────────────────────────────────────────────

VIRAL_REELS = [
    {
        "creator": "Deepika Padukone x Hilton Hotels",
        "views": "1.9B views",
        "hook_used": "Celebrity collaboration + luxury lifestyle reveal",
        "why_viral": "Massive celebrity reach + brand partnership + aspirational content. The most-viewed Reel of all time.",
        "category": "Brand Collaboration",
        "niche": "Travel / Luxury",
        "takeaway": "Collaborations with high-reach accounts can 100x your views. Even micro-influencer collabs boost reach significantly.",
    },
    {
        "creator": "@khloekardashian",
        "views": "400M+ views",
        "hook_used": "Behind-the-scenes family moment — raw, unscripted authenticity",
        "why_viral": "Highly polished videos are losing relevance. Raw, relatable, real content wins. Audiences connect with human moments.",
        "category": "Authenticity",
        "niche": "Lifestyle / Celebrity",
        "takeaway": "You don't need production quality — you need authenticity. Film real moments, not scripted content.",
    },
    {
        "creator": "@zachking",
        "views": "300M+ views",
        "hook_used": "Visual illusion in the first frame — 'Wait... what just happened?'",
        "why_viral": "Jump cuts in the first 3 seconds boost virality by 72%. The brain can't look away from visual magic.",
        "category": "Visual Hook",
        "niche": "Entertainment / Magic",
        "takeaway": "Your first frame matters more than anything. Create a visual that makes people think 'wait, what?' and they'll watch till the end.",
    },
    {
        "creator": "@lfrankl (fitness creator)",
        "views": "50M+ views",
        "hook_used": "'I did [extreme challenge] for 30 days. Here's what happened to my body.'",
        "why_viral": "Transformation + timeframe + curiosity gap. The '30 day challenge' format consistently goes viral in fitness.",
        "category": "Transformation",
        "niche": "Fitness / Health",
        "takeaway": "The 30-day challenge format works in ANY niche. Document a transformation with a clear before/after.",
    },
    {
        "creator": "@cookingwithayeh",
        "views": "80M+ views",
        "hook_used": "'You've been making [food] wrong your entire life. Try this instead.'",
        "why_viral": "Contrarian hook + practical value. People save food hacks to try later, boosting algorithmic reach.",
        "category": "Contrarian + Value",
        "niche": "Cooking / Food",
        "takeaway": "'You've been doing X wrong' is one of the highest-performing hook formulas. Saves drive reach more than likes.",
    },
    {
        "creator": "@garyvee",
        "views": "40M+ views",
        "hook_used": "'The harsh truth nobody wants to hear about [topic]'",
        "why_viral": "Authority + contrarian + emotional trigger. Bold statements from credible sources drive massive comment engagement.",
        "category": "Authority + Contrarian",
        "niche": "Business / Motivation",
        "takeaway": "If you have expertise, lead with bold claims. Comments (even angry ones) signal engagement to the algorithm.",
    },
    {
        "creator": "@thekoreanvegan",
        "views": "30M+ views",
        "hook_used": "Storytelling voiceover over calming cooking visuals",
        "why_viral": "Story hooks have the highest completion rates. Combining narrative with ASMR-like visuals = maximum watch time.",
        "category": "Story Hook",
        "niche": "Cooking / Storytelling",
        "takeaway": "Story-based content gets watched to the end. High completion rate = algorithm boost = viral reach.",
    },
    {
        "creator": "@mrnigelng",
        "views": "100M+ views",
        "hook_used": "'Rating [thing] out of 10' with exaggerated reactions",
        "why_viral": "Review/rating format is inherently engaging — viewers mentally rate along with you. Exaggerated reactions drive shares.",
        "category": "Engagement Format",
        "niche": "Food / Comedy",
        "takeaway": "The rating format works in any niche. 'Rating X out of 10' gets viewers invested in your verdict.",
    },
]


# ─── ALGORITHM & STRATEGY DATA ───────────────────────────────────────────────

ALGORITHM_DATA = {
    "key_stats": [
        {"stat": "140-200B", "label": "Daily Reel views globally", "source": "Loopex Digital 2026"},
        {"stat": "50%", "label": "of time on Instagram is spent on Reels", "source": "Instagram 2026"},
        {"stat": "55%", "label": "of Reel views come from non-followers", "source": "Loopex Digital 2026"},
        {"stat": "72%", "label": "more likely to go viral with hook in first 3s", "source": "Loopex Digital 2026"},
        {"stat": "42%", "label": "higher engagement with trending audio", "source": "Loopex Digital 2026"},
        {"stat": "30.81%", "label": "average reach rate (2x higher than photos)", "source": "Loopex Digital 2026"},
    ],
    "ranking_factors": [
        {"factor": "Watch Time", "weight": "Highest", "detail": "How long people watch your Reel. #1 ranking signal in 2026."},
        {"factor": "Sends/Shares", "weight": "Very High", "detail": "Sends are 3-5x more valuable than likes for reaching new audiences."},
        {"factor": "Likes per Reach", "weight": "High", "detail": "Ratio of likes to total views. Quality engagement over vanity metrics."},
        {"factor": "Saves", "weight": "High", "detail": "Saves signal high-value content. Algorithm boosts saved content significantly."},
        {"factor": "Comments", "weight": "Medium-High", "detail": "Comments show active engagement. Longer comments weighted more."},
        {"factor": "Original Content", "weight": "Medium", "detail": "Aggregators/reposters saw 60-80% reach drops. Original content gets priority."},
    ],
    "best_posting_times": {
        "best_days": ["Tuesday", "Wednesday"],
        "peak_hours": ["7-9 AM", "11 AM-1 PM", "7-9 PM"],
        "worst_time": "Late night (11 PM - 5 AM)",
        "source": "Buffer analysis of 9.6M posts (2026)",
        "tip": "Post when your specific audience is active. Check Instagram Insights for your data.",
    },
    "optimal_format": {
        "length": "60-90 seconds for highest engagement",
        "hashtags": "3-5 relevant hashtags (not 30)",
        "captions": "Keywords in captions drive 30% more reach than hashtags alone",
        "aspect_ratio": "9:16 vertical (1080x1920)",
        "text_on_screen": "Add text overlay — 80% of Reels are watched without sound",
    },
    "viral_benchmarks": {
        "under_10k_followers": "50K-100K views = viral",
        "10k_to_100k_followers": "250K-500K views = viral",
        "over_100k_followers": "1M+ views = viral",
        "average_reel_metrics": "243 likes, 8 comments, 28 saves per Reel",
    },
}


# ─── LIVE TRENDING SONGS FETCHER ─────────────────────────────────────────────

def fetch_live_trending_songs() -> list[dict]:
    """Attempt to fetch current trending songs from web sources."""
    songs = list(TRENDING_SONGS)  # Start with curated database

    # Try to supplement with live data from Reddit music communities
    try:
        resp = requests.get(
            "https://www.reddit.com/r/InstagramReels/hot.json",
            headers=HEADERS,
            params={"limit": 10},
            timeout=8,
        )
        if resp.status_code == 200:
            children = resp.json().get("data", {}).get("children", [])
            for child in children:
                title = child["data"].get("title", "")
                if any(word in title.lower() for word in ["song", "audio", "music", "sound", "trending"]):
                    songs.append({
                        "title": title[:60],
                        "artist": "Community Pick",
                        "reels_count": "Trending",
                        "vibe": "Various",
                        "best_for": ["Check the original post for usage ideas"],
                        "tip": "Community-sourced trending audio — act fast before it peaks.",
                        "trending_since": "This week",
                        "status": "rising",
                    })
    except Exception:
        pass

    return songs


def get_viral_strategy(niche: str = None) -> dict:
    """Get a complete viral strategy for a given niche."""
    strategy = {
        "algorithm": ALGORITHM_DATA,
        "trending_songs": TRENDING_SONGS[:6],
        "viral_reels": VIRAL_REELS,
    }

    if niche:
        # Filter viral reels by niche relevance
        niche_lower = niche.lower()
        relevant_reels = [r for r in VIRAL_REELS if niche_lower in r.get("niche", "").lower()]
        if relevant_reels:
            strategy["niche_reels"] = relevant_reels

    return strategy
