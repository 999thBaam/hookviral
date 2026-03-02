"""
Database of proven viral hook formulas, categorized by type.
Based on research from top-performing Instagram content creators
and social media marketing data from 2024-2026.

Sources:
- Opus.pro: Instagram Reels Hook Formulas (3-second hold rate research)
- Torro.io: 100+ Best Hooks for Instagram Reels 2026
- TheDesignsFirm: 51 Viral Reel Hooks with 2026 Examples
- Vexub: 20 Viral Video Hooks That Stop the Scroll
- ContentStudio: 30+ Proven Examples from Top Creators
- Insense.pro: Must-Try Instagram Reel Hooks for 2026

Key stats:
- Average attention span: 8.25 seconds (first 3 seconds are critical)
- 3-second hold rate benchmark: 60%+ for strong hooks, 70-80% for top performers
- Reels with strong hooks outperform weak ones by 5-10x in reach
- Optimal hook length: 8-15 words for reels
"""

HOOK_FORMULAS = {
    "curiosity_gap": {
        "label": "Curiosity Gap",
        "description": "Creates an information gap that makes viewers desperate to know the answer. Exploits the brain's need to close open loops — viewers can't scroll away without resolution.",
        "score_weight": 0.95,
        "research_note": "Humans are wired to close open loops. When you present incomplete information, the brain experiences mild discomfort it needs to resolve. This is the foundation of the most effective hooks. (Source: Opus.pro)",
        "real_examples": [
            {
                "hook": "This feels illegal to know",
                "performance": "One of the most shared hook formats in 2025. Consistently drives 70%+ 3-second hold rates across niches.",
                "source": "Torro.io / Multiple top creators",
            },
            {
                "hook": "I wasn't going to share this but...",
                "performance": "Confession-style curiosity hooks generate 2-3x more saves than direct hooks.",
                "source": "ContentStudio — Top creator analysis",
            },
            {
                "hook": "Nobody is talking about this TikTok strategy...",
                "performance": "Gap-based openers consistently rank in top 10% for watch time retention.",
                "source": "Opus.pro — Hook formula research",
            },
            {
                "hook": "I almost quit my job until I discovered this one thing...",
                "performance": "Unfinished story hooks drive the highest average watch time among all hook types.",
                "source": "Vexub — Viral Video Hooks 2026",
            },
        ],
        "templates": [
            "Nobody talks about {topic} but it changed my {outcome}",
            "I found out why {common_thing} is actually {unexpected_truth}",
            "The real reason {topic} doesn't work for you",
            "What happens when you {action} for 30 days straight",
            "I tested {thing} so you don't have to. Here's what happened",
            "The {topic} trick that {authority} don't want you to know",
            "Stop {common_action} — do this instead",
            "This {topic} hack feels illegal to know",
            "I've been doing {thing} wrong my entire life",
            "Why {percentage}% of people fail at {topic}",
            "The dark side of {popular_thing} nobody mentions",
            "I accidentally discovered the secret to {outcome}",
        ],
    },
    "contrarian": {
        "label": "Contrarian / Hot Take",
        "description": "Goes against common belief. Challenges the viewer's existing knowledge and forces them to stay to find out why. Triggers engagement through disagreement, comments, and shares.",
        "score_weight": 0.90,
        "research_note": "Starting a Reel with a statement that challenges common beliefs immediately stops the scroll. Brands love this format because it sparks conversation and saves, both of which boost reach. (Source: Torro.io)",
        "real_examples": [
            {
                "hook": "Everyone tells you to post daily on Instagram, but I grew to 100K posting twice a week",
                "performance": "Contrarian hooks with specific numbers achieve 80%+ 3-second hold rates. The specificity makes the contrarian claim believable.",
                "source": "Opus.pro — Hook Formula Research",
            },
            {
                "hook": "You're wasting your money on Facebook ads",
                "performance": "Bold contrarian statements in the marketing niche consistently drive 3-5x more comments than neutral hooks.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
            {
                "hook": "Unpopular Opinion: High follower counts are vanity metrics",
                "performance": "Unpopular opinion format is one of the most-used viral structures in 2025-2026.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
            {
                "hook": "Everything you know about keyword research is wrong",
                "performance": "The 'everything you know is wrong' format consistently ranks in top 5 hook styles for saves and shares.",
                "source": "Vexub — Viral Video Hooks 2026",
            },
        ],
        "templates": [
            "{Popular_advice} is the worst advice I've ever heard",
            "Unpopular opinion: {topic} is completely overrated",
            "{Common_thing} is a scam. Here's proof",
            "I stopped {common_action} and everything changed",
            "Everyone is wrong about {topic}",
            "{Popular_thing} is actually ruining your {outcome}",
            "Hot take: {opinion}",
            "I'm going to get hate for this but {statement}",
            "The {topic} industry doesn't want you to see this",
            "Controversial but {topic} is not what you think",
        ],
    },
    "story": {
        "label": "Story Hook",
        "description": "Opens with a compelling personal narrative. Story hooks achieve the highest average watch time because humans are hardwired for narrative. The vulnerability + outcome format builds trust and curiosity simultaneously.",
        "score_weight": 0.92,
        "research_note": "Story-based hooks have the highest completion rates. The brain processes stories differently — it activates empathy, making viewers feel personally invested in the outcome. (Source: Vexub, ContentStudio)",
        "real_examples": [
            {
                "hook": "I wasted $5,000 on Instagram ads before learning this one targeting trick",
                "performance": "Mistake hooks combining vulnerability with specific dollar amounts get 2-4x more engagement than generic story hooks.",
                "source": "Opus.pro — Mistake Hook Formula",
            },
            {
                "hook": "How I hit 10K followers in 60 days without paid ads",
                "performance": "Time-based story hooks drive urgency. The specific timeframe increases credibility and 3-second hold rates by 40%.",
                "source": "Opus.pro — Time-Based Hook Formula",
            },
            {
                "hook": "Here's how I completely failed at influencer marketing",
                "performance": "Failure stories outperform success stories for engagement. Vulnerability drives 3x more comments.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
            {
                "hook": "The story of how one simple landing page change increased conversions by 50%",
                "performance": "Specific result stories drive high save rates — viewers bookmark for later reference.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
        ],
        "templates": [
            "3 years ago I was {bad_situation}. Today I {good_outcome}",
            "I went from {start} to {end} in {timeframe}. Here's how",
            "The moment I realized {realization} everything changed",
            "I lost everything because of {mistake}. Don't repeat this",
            "A stranger told me {advice} and it was the best advice ever",
            "This one decision made me {outcome} in {timeframe}",
            "I was {age} when I figured out {lesson}",
            "My biggest failure taught me {lesson}",
            "I quit my {job} to {action}. {timeframe} later...",
            "Someone asked me {question}. My answer surprised them",
        ],
    },
    "listicle": {
        "label": "Listicle / Number",
        "description": "Numbered lists signal clear, digestible value. They set expectations upfront (viewer knows exactly what they'll get) and drive the highest save rates because viewers bookmark them for later.",
        "score_weight": 0.85,
        "research_note": "Numbered list hooks with specific outcomes doubled engagement compared to vague lists. '5 Reels mistakes killing your reach' outperforms '5 Reels tips' because it implies loss aversion. (Source: Opus.pro)",
        "real_examples": [
            {
                "hook": "5 Reels mistakes killing your reach",
                "performance": "Negative-framed listicles (mistakes, things to avoid) get 40% more clicks than positive-framed ones (tips, tricks).",
                "source": "Opus.pro — Numbered List Hook Formula",
            },
            {
                "hook": "3 caption formulas that doubled my engagement",
                "performance": "Listicles with specific outcome metrics (doubled, tripled, 10x) drive higher 3-second hold rates.",
                "source": "Opus.pro — Numbered List Hook Formula",
            },
            {
                "hook": "7 things I know at 33 that I wish I knew at 23",
                "performance": "Generated significantly more engagement than standard listicle formats. The age-wisdom format is highly shareable.",
                "source": "ContentStudio — @growwithcolby",
            },
            {
                "hook": "My top 5 free keyword research tools",
                "performance": "Tool recommendation listicles drive the highest save rates across all listicle subtypes.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
        ],
        "templates": [
            "{Number} {topic} mistakes that are costing you {outcome}",
            "{Number} things I wish I knew before {action}",
            "Top {number} {topic} tips that actually work in {year}",
            "{Number} {topic} hacks under {time} minutes",
            "{Number} free {tools} that replaced my ${amount}/month subscriptions",
            "Save this: {number} {topic} rules to live by",
            "{Number} signs you're {situation} (and how to fix it)",
            "The only {number} {things} you need for {outcome}",
            "{Number} {topic} trends to watch in {year}",
            "I tried {number} {things}. Only {smaller_number} were worth it",
        ],
    },
    "authority": {
        "label": "Authority / Proof",
        "description": "Establishes credibility in the first 3 seconds. By leading with credentials, specific numbers, or proven results, viewers immediately trust the content is worth watching.",
        "score_weight": 0.88,
        "research_note": "Authority hooks work because they answer the viewer's subconscious question: 'Why should I listen to you?' Leading with credentials or proof eliminates this friction immediately. (Source: Vexub, TheDesignsFirm)",
        "real_examples": [
            {
                "hook": "As a dermatologist with 15 years of experience, here's what I actually recommend",
                "performance": "Credential-led hooks in health/finance niches achieve 75%+ 3-second hold rates. Professional authority stops the scroll instantly.",
                "source": "Vexub — Authority Hook Analysis",
            },
            {
                "hook": "This strategy helped 500 of my clients double their revenue",
                "performance": "Social proof openers with specific client numbers drive high trust and engagement.",
                "source": "Vexub — Social Proof Opener",
            },
            {
                "hook": "After running a SEO company for 10 years, the biggest lesson I learned",
                "performance": "Long-tenure authority claims drive curiosity — viewers want to know what the lesson is.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
            {
                "hook": "The exact framework I use to write blog posts that rank on Google's first page",
                "performance": "Framework reveals from authorities drive the highest save rates in B2B/marketing niches.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
        ],
        "templates": [
            "As a {profession} with {years} years of experience, here's the truth about {topic}",
            "I've {achievement} and this is what I learned",
            "After working with {number}+ {clients}, I noticed this pattern",
            "I've spent ${amount} on {topic} so you don't have to",
            "After {number} hours of research, here's what actually works",
            "I {impressive_feat}. Here's my exact {strategy}",
            "My {topic} went from {start} to {end}. The strategy is simple",
            "{Number} years in {industry} taught me one thing",
            "I've helped {number}+ people {outcome}. The secret is {hook}",
            "Coming from someone who {credential}: {statement}",
        ],
    },
    "fear_urgency": {
        "label": "Fear / Urgency",
        "description": "Triggers loss aversion — the psychological principle that people fear losing something more than they desire gaining something equivalent. Creates FOMO and drives immediate action.",
        "score_weight": 0.87,
        "research_note": "Fear-based hooks trigger loss aversion, one of the strongest psychological motivators. Combined with urgency (time pressure), these hooks drive the highest click-through and share rates. (Source: Vexub, Torro.io)",
        "real_examples": [
            {
                "hook": "Everyone is doing this except you",
                "performance": "FOMO hooks drive 2-3x more shares than value-promise hooks. The exclusion trigger is powerful.",
                "source": "Vexub — FOMO Hook Analysis",
            },
            {
                "hook": "It's 2026 and you're still not using a CRM system?",
                "performance": "Year-shaming hooks create urgency by implying the viewer is behind. High comment engagement due to defensiveness.",
                "source": "TheDesignsFirm — Trend-Based Hooks",
            },
            {
                "hook": "Stop making this mistake with your Instagram — it's killing your reach",
                "performance": "Warning/mistake hooks in the social media niche drive 50% higher save rates than tip-based hooks.",
                "source": "Vexub — Mistake Warning Hook",
            },
            {
                "hook": "Red flags to look for in your marketing agency",
                "performance": "Red flag hooks drive high watch time — viewers are anxious to check if they're affected.",
                "source": "Torro.io — Warning Hook Category",
            },
        ],
        "templates": [
            "If you're not doing {action} in {year}, you're falling behind",
            "This {thing} is about to change everything. Are you ready?",
            "You're losing {outcome} every day you ignore {topic}",
            "Warning: {topic} is not what it used to be",
            "{Thing} is dying. Here's what's replacing it",
            "Last chance to {action} before {event}",
            "The {topic} bubble is about to burst",
            "Most people won't see this coming: {prediction}",
            "If you {action}, stop immediately. Here's why",
            "The clock is ticking on {topic}. Here's what to do now",
        ],
    },
    "value_promise": {
        "label": "Value Promise",
        "description": "Promises clear, specific value upfront. These hooks work because they immediately answer 'What's in it for me?' — the viewer knows exactly what they'll gain by watching.",
        "score_weight": 0.86,
        "research_note": "When the opening line promises something valuable, viewers stay through the key moments of your Reel, boosting average watch time — a major ranking factor in Instagram's algorithm. (Source: Insense.pro, Torro.io)",
        "real_examples": [
            {
                "hook": "How to get more website traffic without paid ads",
                "performance": "How-to hooks with a pain point removal ('without paid ads') outperform simple how-to hooks by 60%.",
                "source": "TheDesignsFirm — Solution/How-To Hooks",
            },
            {
                "hook": "A little-known AI tool that will change how you write social media copy",
                "performance": "Tool reveal hooks drive the highest save-to-view ratio — viewers bookmark to try later.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
            {
                "hook": "Save this for later: the complete guide to email marketing",
                "performance": "'Save this' as an opening CTA increases actual save rates by 30-40% compared to end-of-video CTAs.",
                "source": "Torro.io — Benefit-Focused Hooks",
            },
            {
                "hook": "This free tool does what I used to pay $200/month for",
                "performance": "Money-saving tool reveals are among the most shared hook formats. The specific dollar amount adds credibility.",
                "source": "Vexub — Tool Reveal Hook",
            },
        ],
        "templates": [
            "Save this for later: the complete guide to {topic}",
            "The only {topic} tutorial you'll ever need",
            "How to {outcome} in {timeframe} (step by step)",
            "Free {resource} that will {outcome} (link in bio)",
            "The exact {strategy} I used to {outcome}",
            "Here's your {topic} cheat sheet",
            "Copy my exact {thing} for {outcome}",
            "Steal my {topic} template (it's free)",
            "The simplest way to {outcome} — explained in {time}",
            "Watch this before you {action}. It'll save you {time/money}",
        ],
    },
    "question": {
        "label": "Question Hook",
        "description": "Engages the brain automatically — when asked a question, the human brain compulsively tries to answer it. This involuntary mental engagement keeps viewers watching to compare their answer.",
        "score_weight": 0.83,
        "research_note": "Question hooks pique interest by suggesting there's something the viewer doesn't know yet. Starting a Reel with 'Did you know...?' or 'Does this sound like you?' plants a question in the viewer's mind that they need answered. (Source: Torro.io, Insense.pro)",
        "real_examples": [
            {
                "hook": "Are you using Instagram's algorithm against yourself?",
                "performance": "Self-referential question hooks drive high engagement because viewers immediately self-assess.",
                "source": "Opus.pro — Question Hook Formula",
            },
            {
                "hook": "What if everything you know about Reels is wrong?",
                "performance": "Paradigm-challenging questions drive the highest comment rates among question hooks — viewers debate in comments.",
                "source": "Opus.pro — Question Hook Formula",
            },
            {
                "hook": "Does this sound like you?",
                "performance": "Relatability questions like 'Stop scrolling if this sounds like you' consistently rank in top hooks for 3-second hold rate.",
                "source": "Torro.io — Question-Based Hooks",
            },
            {
                "hook": "Do you know the #1 reason why social media campaigns fail on ROI?",
                "performance": "Numbered ranking questions (#1 reason, biggest mistake) create a stronger curiosity gap than open questions.",
                "source": "TheDesignsFirm — 51 Viral Reel Hooks",
            },
        ],
        "templates": [
            "What would you do if {scenario}?",
            "Can you actually {outcome} by just {simple_action}?",
            "Why does nobody talk about {topic}?",
            "Is {popular_thing} actually worth it in {year}?",
            "What's the worst {topic} advice you've ever received?",
            "Did you know that {surprising_fact}?",
            "Are you making this {topic} mistake?",
            "What if everything you knew about {topic} was wrong?",
            "Want to know the fastest way to {outcome}?",
            "How do {successful_people} {action} so easily?",
        ],
    },
}

NICHES = [
    "fitness", "finance", "marketing", "tech", "cooking",
    "travel", "fashion", "beauty", "productivity", "mindset",
    "business", "real estate", "crypto", "health", "parenting",
    "photography", "music", "gaming", "education", "self-improvement",
    "ai & tools", "side hustles", "motivation", "relationships", "career",
]

POWER_WORDS = [
    "secret", "proven", "free", "instant", "guaranteed", "exclusive",
    "shocking", "hack", "ultimate", "insane", "brutal", "deadly",
    "powerful", "hidden", "banned", "illegal", "truth", "exposed",
    "genius", "underrated", "game-changer", "life-changing", "viral",
    "simple", "easy", "fast", "overnight", "effortless", "no one",
    "everyone", "stop", "never", "always", "warning", "mistake",
    "finally", "actually", "literally", "seriously", "honestly",
]

EMOTIONAL_TRIGGERS = {
    "curiosity": ["secret", "hidden", "truth", "exposed", "real reason", "nobody", "actually", "find out"],
    "fear": ["warning", "mistake", "stop", "never", "losing", "dying", "falling behind", "dangerous"],
    "greed": ["free", "money", "income", "passive", "rich", "profit", "cash", "earn", "revenue"],
    "urgency": ["now", "today", "hurry", "last chance", "before", "limited", "running out", "immediately"],
    "social_proof": ["everyone", "million", "thousands", "viral", "trending", "top", "best", "proven"],
    "aspiration": ["dream", "freedom", "success", "lifestyle", "achieve", "transform", "level up", "upgrade"],
}
