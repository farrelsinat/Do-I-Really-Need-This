import streamlit as st

st.set_page_config(
    page_title="Do I Really Need This?",
    page_icon="🎟️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS: MOBILE-SAFE, HIGH CONTRAST & FRESH BOTANICAL ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Paksa latar belakang utama tetap terang pastel meski HP pakai dark mode */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background:
            radial-gradient(circle at 12% 15%, rgba(214, 235, 223, 0.78) 0%, transparent 45%),
            radial-gradient(circle at 88% 18%, rgba(232, 224, 248, 0.78) 0%, transparent 45%),
            radial-gradient(circle at 50% 92%, rgba(253, 243, 212, 0.85) 0%, transparent 50%),
            #FAF8F5 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #1F2622 !important;
    }

    /* Kontainer utama rapi & simetris di mobile maupun desktop */
    .block-container {
        max-width: 560px !important;
        padding-top: 1.75rem !important;
        padding-bottom: 2.5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* Sembunyikan menu/header bawaan Streamlit */
    #MainMenu, footer, header, [data-testid="stToolbar"] {
        visibility: hidden !important;
        display: none !important;
    }

    /* Header & Judul */
    .cute-stickers {
        text-align: center;
        font-size: 1.25rem;
        letter-spacing: 0.35rem;
        margin-bottom: 0.3rem;
        color: #1F2622 !important;
    }

    .editorial-title {
        font-family: 'Playfair Display', serif !important;
        font-size: 2.15rem;
        font-weight: 700;
        color: #1A221E !important;
        text-align: center;
        line-height: 1.15;
        margin-bottom: 0.4rem;
    }

    @media (min-width: 640px) {
        .editorial-title {
            font-size: 2.45rem;
        }
    }

    .editorial-title span.italic-sage {
        font-style: italic;
        font-weight: 600;
        color: #466E5B !important;
    }

    .editorial-subtitle {
        text-align: center;
        color: #4F5853 !important;
        font-size: 0.9rem;
        line-height: 1.55;
        margin-bottom: 1.35rem;
    }

    .editorial-subtitle strong {
        color: #1F2622 !important;
    }

    /* Kartu Utama */
    .main-card {
        background: #FFFFFF !important;
        border: 1.5px solid #E3DDD2 !important;
        border-radius: 24px;
        padding: 1.35rem 1.25rem;
        box-shadow: 0 12px 32px rgba(45, 74, 60, 0.06);
        margin-bottom: 0.85rem;
        color: #1F2622 !important;
    }

    @media (min-width: 640px) {
        .main-card {
            border-radius: 28px;
            padding: 1.75rem 1.65rem 1.45rem 1.65rem;
        }
    }

    .card-top-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 0.8rem;
    }

    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        padding: 0.26rem 0.75rem;
        border-radius: 999px;
    }

    .badge-fandom {
        background-color: #ECE7FA !important;
        color: #4E3F82 !important;
        border: 1px solid #D6CCF2 !important;
    }

    .badge-emotion {
        background-color: #FEF2CE !important;
        color: #7D5E14 !important;
        border: 1px solid #F3DF9E !important;
    }

    .badge-finance {
        background-color: #DFF0E6 !important;
        color: #2C5744 !important;
        border: 1px solid #C2DFCE !important;
    }

    .step-counter {
        font-size: 0.75rem;
        font-weight: 600;
        color: #555E59 !important;
        background: #F2EFE9 !important;
        padding: 0.22rem 0.65rem;
        border-radius: 999px;
        white-space: nowrap;
    }

    .question-text {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.25rem;
        font-weight: 600;
        color: #1A221E !important;
        line-height: 1.36;
        margin: 0;
    }

    @media (min-width: 640px) {
        .question-text {
            font-size: 1.4rem;
        }
    }

    .card-helper-text {
        font-size: 0.85rem;
        color: #5B645F !important;
        margin-top: 0.45rem;
        margin-bottom: 0;
        line-height: 1.45;
    }

    /* Styling Radio Button - kunci warna teks di semua anak elemen agar tidak hilang */
    div[data-testid="stRadio"] > label {
        display: none !important;
    }

    div[data-testid="stRadio"] > div[role="radiogroup"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 0.55rem !important;
        width: 100% !important;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        background-color: #FFFFFF !important;
        border: 1.5px solid #E3DDD2 !important;
        border-radius: 16px !important;
        padding: 0.82rem 1rem !important;
        margin: 0 !important;
        width: 100% !important;
        box-sizing: border-box !important;
        transition: all 0.18s ease !important;
        cursor: pointer;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"] * {
        color: #222925 !important;
        opacity: 1 !important;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
        background-color: #F3F8F5 !important;
        border-color: #8FB09F !important;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
        background-color: #E3F0E8 !important;
        border-color: #466E5B !important;
        box-shadow: 0 4px 12px rgba(70, 110, 91, 0.14) !important;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) * {
        color: #193629 !important;
        font-weight: 600 !important;
    }

    /* Styling Text Input */
    div[data-testid="stTextInput"] input {
        background-color: #FFFFFF !important;
        border: 1.5px solid #DCD6CA !important;
        border-radius: 16px !important;
        padding: 0.78rem 1rem !important;
        font-size: 0.95rem !important;
        color: #1F2622 !important;
        -webkit-text-fill-color: #1F2622 !important;
    }

    div[data-testid="stTextInput"] input::placeholder {
        color: #87908B !important;
        -webkit-text-fill-color: #87908B !important;
        opacity: 1 !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #466E5B !important;
        box-shadow: 0 0 0 3px rgba(70, 110, 91, 0.16) !important;
    }

    /* Tombol Navigasi */
    div.stButton > button {
        border-radius: 15px !important;
        padding: 0.65rem 1rem !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        min-height: 46px !important;
        border: 1.5px solid #DCD6CA !important;
        background-color: #FFFFFF !important;
        color: #262E2A !important;
    }

    div.stButton > button * {
        color: #262E2A !important;
    }

    div.stButton > button:hover {
        border-color: #749A87 !important;
        background-color: #F2F7F4 !important;
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #466E5B 0%, #335445 100%) !important;
        border: none !important;
        color: #FFFFFF !important;
        box-shadow: 0 8px 20px -4px rgba(51, 84, 69, 0.35) !important;
    }

    div.stButton > button[kind="primary"] * {
        color: #FFFFFF !important;
    }

    /* Progress Bar */
    div[data-testid="stProgress"] > div > div {
        background-color: #E5E0D5 !important;
        border-radius: 999px !important;
        height: 8px !important;
    }

    div[data-testid="stProgress"] > div > div > div {
        background: linear-gradient(90deg, #8B7EC8 0%, #598570 100%) !important;
        border-radius: 999px !important;
    }

    /* Kartu Result bergaya Ticket Stub */
    .ticket-card {
        background: #FFFFFF !important;
        border: 1.5px solid #E2DDD1 !important;
        border-radius: 26px;
        padding: 1.5rem 1.25rem;
        box-shadow: 0 18px 45px rgba(44, 74, 62, 0.08);
        margin-bottom: 1rem;
        color: #1F2622 !important;
    }

    @media (min-width: 640px) {
        .ticket-card {
            border-radius: 30px;
            padding: 2rem 1.8rem;
        }
    }

    .ticket-divider {
        border-top: 2px dashed #DFD9CC;
        margin: 1.3rem 0;
    }

    .concert-tag {
        display: inline-block;
        background: #F3F0E8 !important;
        color: #464D49 !important;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.3rem 0.85rem;
        border-radius: 999px;
        margin-bottom: 0.85rem;
    }

    .score-box {
        background: #F2F7F4 !important;
        border: 1px solid #D3E3DA !important;
        border-radius: 20px;
        padding: 1.1rem;
        text-align: center;
        margin-bottom: 1.15rem;
    }

    .score-caption {
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #4E6E5E !important;
        margin-bottom: 0.2rem;
    }

    .score-number {
        font-family: 'Playfair Display', serif !important;
        font-size: 2.9rem;
        font-weight: 700;
        color: #234033 !important;
        line-height: 1.05;
    }

    .score-denom {
        font-size: 1.35rem;
        font-weight: 400;
        color: #7D9186 !important;
    }

    .verdict-headline {
        font-family: 'Playfair Display', serif !important;
        font-size: 1.5rem;
        font-weight: 700;
        color: #1A221E !important;
        text-align: center;
        margin-bottom: 0.5rem;
        line-height: 1.25;
    }

    .verdict-desc {
        color: #4C5550 !important;
        font-size: 0.9rem;
        line-height: 1.6;
        text-align: center;
        margin: 0;
    }

    .verdict-desc strong {
        color: #1A221E !important;
    }

    .breakdown-heading {
        font-size: 0.74rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #67706B !important;
        margin-bottom: 0.85rem;
        text-align: center;
    }

    .cat-row {
        margin-bottom: 0.85rem;
    }

    .cat-label-row {
        display: flex;
        justify-content: space-between;
        font-size: 0.84rem;
        font-weight: 600;
        color: #27302B !important;
        margin-bottom: 0.35rem;
    }

    .cat-bar-bg {
        width: 100%;
        height: 9px;
        background-color: #EAE6DD !important;
        border-radius: 999px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# --- DATA PERTANYAAN ---
QUESTIONS = [
    {
        "id": "q1",
        "category": "Fandom",
        "icon": "🎧",
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
        "icon": "🎶",
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
        "icon": "💌",
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
        "icon": "📹",
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
        "icon": "🥹",
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
        "icon": "✈️",
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
        "icon": "✨",
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
        "icon": "🍵",
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
        "icon": "💳",
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
        "icon": "👜",
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

# --- INISIALISASI SESSION STATE ---
if "step" not in st.session_state:
    st.session_state.step = 0
if "concert_name" not in st.session_state:
    st.session_state.concert_name = ""
if "answers" not in st.session_state:
    st.session_state.answers = {}

def reset_quiz():
    st.session_state.step = 0
    st.session_state.answers = {}
    st.session_state.concert_name = ""

# --- HEADER UTAMA ---
st.markdown('<div class="cute-stickers">🎟️ 🌿 ✨ 🎧</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="editorial-title">Do I Really <span class="italic-sage">Need</span> This?</div>',
    unsafe_allow_html=True,
)

# =========================================================
# HALAMAN 0: WELCOME & INPUT NAMA KONSER / ARTIS
# =========================================================
if st.session_state.step == 0:
    st.markdown(
        '<div class="editorial-subtitle">Grab your iced matcha, take a deep breath, and let’s do a quick reality check before you hit checkout.</div>',
        unsafe_allow_html=True,
    )

    st.markdown("""
    <div class="main-card">
        <div class="card-top-row">
            <span class="badge-pill badge-finance">🌷 Ticket Reality Check</span>
            <span class="step-counter">10 Questions</span>
        </div>
        <div class="question-text">Which concert or artist are we thinking about today?</div>
        <p class="card-helper-text">
            Type the artist, band, or tour name below to personalize your result card.
        </p>
    </div>
    """, unsafe_allow_html=True)

    concert_input = st.text_input(
        "Concert or Artist Name",
        value=st.session_state.concert_name,
        placeholder="e.g., NIKI, Taylor Swift, SEVENTEEN, Wave to Earth...",
        label_visibility="collapsed"
    )

    st.write("")
    if st.button("Start Reality Check ✨", type="primary", use_container_width=True):
        st.session_state.concert_name = concert_input.strip()
        st.session_state.step = 1
        st.rerun()

# =========================================================
# HALAMAN 1 - 10: PERTANYAAN SATU PER HALAMAN
# =========================================================
elif 1 <= st.session_state.step <= len(QUESTIONS):
    idx = st.session_state.step - 1
    q = QUESTIONS[idx]
    total_q = len(QUESTIONS)

    concert_display = st.session_state.concert_name if st.session_state.concert_name else "This Concert"
    st.markdown(
        f'<div class="editorial-subtitle">Checking your vibe for <strong>{concert_display}</strong> 🫧</div>',
        unsafe_allow_html=True,
    )

    st.progress(st.session_state.step / total_q)

    st.markdown(f"""
    <div class="main-card">
        <div class="card-top-row">
            <span class="badge-pill {q['badge_class']}">{q['icon']} {q['category']}</span>
            <span class="step-counter">{st.session_state.step} / {total_q}</span>
        </div>
        <div class="question-text">{q['question']}</div>
    </div>
    """, unsafe_allow_html=True)

    option_labels = list(q["options"].keys())
    saved_answer = st.session_state.answers.get(q["id"], None)
    default_index = option_labels.index(saved_answer) if saved_answer in option_labels else None

    selected_option = st.radio(
        label=q["question"],
        options=option_labels,
        index=default_index,
        key=f"radio_{q['id']}",
        label_visibility="collapsed"
    )

    st.write("")

    col_back, col_next = st.columns([1, 1], gap="small")

    with col_back:
        if st.button("← Back", use_container_width=True):
            if selected_option is not None:
                st.session_state.answers[q["id"]] = selected_option
            st.session_state.step -= 1
            st.rerun()

    with col_next:
        next_label = "Reveal Verdict ✨" if st.session_state.step == total_q else "Next →"
        if st.button(next_label, type="primary", use_container_width=True):
            if selected_option is None:
                st.warning("Pick one answer first so we can judge fairly! 🌿")
            else:
                st.session_state.answers[q["id"]] = selected_option
                st.session_state.step += 1
                st.rerun()

# =========================================================
# HALAMAN 11: RESULT CARD
# =========================================================
else:
    total_score = 0
    max_total_score = 0

    cat_scores = {"Fandom": 0, "Emotional Attachment": 0, "Financial Safety": 0}
    cat_max = {"Fandom": 0, "Emotional Attachment": 0, "Financial Safety": 0}

    for q in QUESTIONS:
        highest = max(q["options"].values())
        max_total_score += highest
        cat_max[q["category"]] += highest

        chosen_text = st.session_state.answers.get(q["id"])
        val = q["options"].get(chosen_text, 0)
        total_score += val
        cat_scores[q["category"]] += val

    percentages = {
        cat: round((cat_scores[cat] / cat_max[cat]) * 100)
        for cat in cat_scores
    }

    concert_title = st.session_state.concert_name if st.session_state.concert_name else "This Concert"

    if percentages["Financial Safety"] < 40:
        verdict_emoji = "🛑💸"
        headline = "Step away from the checkout button."
        description = (
            f"Your heart says yes to <strong>{concert_title}</strong>, but your bank account is screaming for help. "
            "Fandom does not pay rent. Watch the fancams in HD from your bed instead."
        )
    elif total_score >= 23:
        verdict_emoji = "🎟️🥂"
        headline = "Buy the ticket. No regrets."
        description = (
            f"You're a true fan of <strong>{concert_title}</strong>, emotionally invested, and financially ready. "
            "Go scream your lungs out and enjoy every second of it!"
        )
    elif total_score >= 15:
        verdict_emoji = "🤔🍵"
        headline = "You could go, but think."
        description = (
            f"You clearly care about seeing <strong>{concert_title}</strong>. Just make sure the ticket doesn't turn into "
            "three weeks of financial suffering. Your budget has veto power—fandom does not pay rent."
        )
    else:
        verdict_emoji = "🌿🛍️"
        headline = "Save your money."
        description = (
            f"You don't actually need tickets to <strong>{concert_title}</strong>. You're probably just caught up in the hype. "
            "Treat yourself to a really nice dinner or skincare haul instead."
        )

    st.markdown(f"""
    <div class="ticket-card">
        <div style="text-align:center;">
            <span class="concert-tag">🎫 Verdict For: {concert_title}</span>
        </div>
        <div class="score-box">
            <div class="score-caption">Final Compatibility Score</div>
            <div class="score-number">
                {total_score}<span class="score-denom">/{max_total_score}</span>
            </div>
        </div>
        <div style="text-align:center; font-size:1.75rem; margin-bottom:0.35rem;">{verdict_emoji}</div>
        <div class="verdict-headline">“{headline}”</div>
        <div class="verdict-desc">{description}</div>
        <div class="ticket-divider"></div>
        <div class="breakdown-heading">✦ Breakdown By Category ✦</div>
        <div class="cat-row">
            <div class="cat-label-row">
                <span>🎧 Fandom</span>
                <span>{percentages['Fandom']}%</span>
            </div>
            <div class="cat-bar-bg">
                <div style="width:{percentages['Fandom']}%; height:100%; background:#8B7EC8; border-radius:999px;"></div>
            </div>
        </div>
        <div class="cat-row">
            <div class="cat-label-row">
                <span>🥹 Emotional Attachment</span>
                <span>{percentages['Emotional Attachment']}%</span>
            </div>
            <div class="cat-bar-bg">
                <div style="width:{percentages['Emotional Attachment']}%; height:100%; background:#D9B14A; border-radius:999px;"></div>
            </div>
        </div>
        <div class="cat-row" style="margin-bottom:0;">
            <div class="cat-label-row">
                <span>🍵 Financial Safety</span>
                <span>{percentages['Financial Safety']}%</span>
            </div>
            <div class="cat-bar-bg">
                <div style="width:{percentages['Financial Safety']}%; height:100%; background:#527966; border-radius:999px;"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_recheck, col_new = st.columns([1, 1], gap="small")
    with col_recheck:
        if st.button("← Edit Answers", use_container_width=True):
            st.session_state.step = len(QUESTIONS)
            st.rerun()
    with col_new:
        if st.button("↺ Check Another", type="primary", use_container_width=True):
            reset_quiz()
            st.rerun()