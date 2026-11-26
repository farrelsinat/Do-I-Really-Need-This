import streamlit as st

st.set_page_config(
    page_title="Do I Really Need This?",
    page_icon="✨",
    layout="centered"
)

# Gaya visual Soft Editorial / Botanical Pastel (non-pink)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,500&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');

    .stApp {
        background:
            radial-gradient(at 0% 0%, rgba(216, 232, 222, 0.6) 0px, transparent 50%),
            radial-gradient(at 100% 10%, rgba(232, 226, 245, 0.6) 0px, transparent 50%),
            radial-gradient(at 50% 100%, rgba(252, 243, 214, 0.65) 0px, transparent 50%),
            #FAF8F5;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #2D312E;
    }

    .editorial-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #1F2923;
        text-align: center;
        margin-bottom: 0.25rem;
    }

    .editorial-title span.italic-sage {
        font-style: italic;
        font-weight: 500;
        color: #527966;
    }

    .editorial-subtitle {
        text-align: center;
        color: #636B66;
        font-size: 0.95rem;
        margin-bottom: 2rem;
    }

    .badge-pill {
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        margin-bottom: 0.4rem;
    }

    .badge-fandom {
        background-color: #ECE8F8;
        color: #5B4E8A;
    }

    .badge-emotion {
        background-color: #FDF3D7;
        color: #8A6D22;
    }

    .badge-finance {
        background-color: #E4F0E8;
        color: #3B6351;
    }

    .result-card {
        background: rgba(255, 255, 255, 0.88);
        border: 1px solid #E6E2D8;
        border-radius: 28px;
        padding: 2rem;
        box-shadow: 0 18px 45px rgba(44, 74, 62, 0.07);
        margin-top: 1rem;
    }

    .score-box {
        background-color: #F7F9F7;
        border: 1px solid #E1EAE4;
        border-radius: 20px;
        padding: 1.25rem;
        text-align: center;
        margin-bottom: 1.5rem;
    }

    .score-number {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 700;
        color: #2C4A3E;
        line-height: 1.1;
    }

    .verdict-headline {
        font-family: 'Playfair Display', serif;
        font-size: 1.65rem;
        font-weight: 700;
        color: #1F2923;
        text-align: center;
        margin-bottom: 0.6rem;
    }

    .verdict-desc {
        color: #5C645F;
        font-size: 0.92rem;
        line-height: 1.6;
        text-align: center;
        margin-bottom: 1.5rem;
    }

    div[data-testid="stRadio"] > div {
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid #E6E2D8;
        border-radius: 20px;
        padding: 0.9rem 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

QUESTIONS = [
    {
        "id": "q1",
        "category": "Fandom",
        "badge_class": "badge-fandom",
        "question": "How long have you been a fan?",
        "options": {
            "Since they debut": 3,
            "1 - 3 years": 2,
            "Just a few months": 1,
            "I only know 1 viral song": 0,
        },
    },
    {
        "id": "q2",
        "category": "Fandom",
        "badge_class": "badge-fandom",
        "question": "Can you recognize their song in 5 seconds?",
        "options": {
            "Yes, even the B-sides": 3,
            "Some of it (mostly title tracks)": 2,
            "Only the chorus": 1,
            "No": 0,
        },
    },
    {
        "id": "q3",
        "category": "Fandom",
        "badge_class": "badge-fandom",
        "question": "Do you know the members' names and inside jokes?",
        "options": {
            "By heart, yes": 3,
            "Most of them": 2,
            "Only the main vocalist/frontman": 1,
            "Not really": 0,
        },
    },
    {
        "id": "q4",
        "category": "Fandom",
        "badge_class": "badge-fandom",
        "question": "Have you watched their live concert videos on YouTube?",
        "options": {
            "Countless times, I know the fanchants": 3,
            "A few times": 2,
            "Once or twice": 1,
            "Never": 0,
        },
    },
    {
        "id": "q5",
        "category": "Emotional Attachment",
        "badge_class": "badge-emotion",
        "question": "How would you feel if you skip this concert and see clips on social media?",
        "options": {
            "Devastated, pure regret for months": 3,
            "Pretty sad (FOMO hits hard)": 2,
            "A bit jealous, then move on": 1,
            "Totally fine": 0,
        },
    },
    {
        "id": "q6",
        "category": "Emotional Attachment",
        "badge_class": "badge-emotion",
        "question": "How likely are they to tour in your city again soon?",
        "options": {
            "Almost zero / Once in a lifetime": 3,
            "Maybe in 2-3 years": 2,
            "They come here pretty often": 1,
            "No idea": 0,
        },
    },
    {
        "id": "q7",
        "category": "Emotional Attachment",
        "badge_class": "badge-emotion",
        "question": "Are you going for the music or just for Instagram stories?",
        "options": {
            "100% the live music experience": 3,
            "Mostly music, partly the hype": 2,
            "50/50": 1,
            "Honestly, just the clout": 0,
        },
    },
    {
        "id": "q8",
        "category": "Financial Safety",
        "badge_class": "badge-finance",
        "question": "Can you afford the ticket without putting essentials at risk?",
        "options": {
            "Yes, easily": 3,
            "Maybe, need to cut back on coffee/eating out": 2,
            "No, rent/bills will suffer": 0,
        },
    },
    {
        "id": "q9",
        "category": "Financial Safety",
        "badge_class": "badge-finance",
        "question": "How are you paying for this ticket?",
        "options": {
            "Dedicated concert/fun savings": 3,
            "This month's paycheck": 2,
            "Paylater / Credit card debt / Borrowing": 0,
        },
    },
    {
        "id": "q10",
        "category": "Financial Safety",
        "badge_class": "badge-finance",
        "question": "Did you factor in transport, food, and outfit costs?",
        "options": {
            "Yes, all budgeted": 3,
            "Roughly estimated": 2,
            "Wait... there are extra costs?": 1,
            "I'll figure it out later": 0,
        },
    },
]

st.markdown(
    '<div class="editorial-title">Do I Really <span class="italic-sage">Need</span> This?</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="editorial-subtitle">Take a deep breath, grab your iced matcha, and answer 10 honest questions before checkout.</div>',
    unsafe_allow_html=True,
)

if "submitted" not in st.session_state:
    st.session_state.submitted = False

with st.form("survey_form"):
    selected_scores = {}

    for idx, q in enumerate(QUESTIONS, start=1):
        st.markdown(
            f'<span class="badge-pill {q["badge_class"]}">{q["category"]}</span>',
            unsafe_allow_html=True,
        )
        option_labels = list(q["options"].keys())
        choice = st.radio(
            f"{idx}. {q['question']}",
            options=option_labels,
            index=None,
            key=q["id"],
        )
        selected_scores[q["id"]] = q["options"][choice] if choice is not None else None

    submitted = st.form_submit_button("Reveal My Verdict ✨", use_container_width=True)

if submitted:
    if any(val is None for val in selected_scores.values()):
        st.warning("Please answer all 10 questions before revealing your verdict.")
    else:
        st.session_state.submitted = True
        st.session_state.scores = selected_scores

if st.session_state.submitted and "scores" in st.session_state:
    scores = st.session_state.scores
    total_score = 0
    max_total_score = 0

    cat_scores = {"Fandom": 0, "Emotional Attachment": 0, "Financial Safety": 0}
    cat_max = {"Fandom": 0, "Emotional Attachment": 0, "Financial Safety": 0}

    for q in QUESTIONS:
        highest = max(q["options"].values())
        max_total_score += highest
        cat_max[q["category"]] += highest

        val = scores[q["id"]]
        total_score += val
        cat_scores[q["category"]] += val

    percentages = {
        cat: round((cat_scores[cat] / cat_max[cat]) * 100)
        for cat in cat_scores
    }

    if percentages["Financial Safety"] < 40:
        headline = "Step away from the checkout button."
        description = (
            "Your heart says yes, your bank account is screaming for help. "
            "Fandom does not pay rent. Watch the fancams in HD from your bed instead."
        )
    elif total_score >= 23:
        headline = "Buy the ticket. No regrets."
        description = (
            "You're a true fan, emotionally invested, and financially ready. "
            "Go scream your lungs out and enjoy every second of it."
        )
    elif total_score >= 15:
        headline = "You could go, but think."
        description = (
            "You clearly care about this concert. Just make sure the ticket doesn't turn into "
            "three weeks of financial suffering. Your budget has veto power. Fandom does not pay rent."
        )
    else:
        headline = "Save your money."
        description = (
            "You don't actually need this. You're probably just caught up in the hype. "
            "Treat yourself to a really nice dinner instead."
        )

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="score-box">
            <div style="font-size:0.75rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;color:#688275;">Your Score</div>
            <div class="score-number">{total_score}<span style="font-size:1.4rem;font-weight:400;color:#94A69C;">/{max_total_score}</span></div>
        </div>
        <div class="verdict-headline">“{headline}”</div>
        <div class="verdict-desc">{description}</div>
        """,
        unsafe_allow_html=True,
    )

    for cat, pct in percentages.items():
        st.markdown(f"**{cat}** — `{pct}%`")
        st.progress(pct / 100)

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("↺ Take It Again", use_container_width=True):
        st.session_state.submitted = False
        st.rerun()