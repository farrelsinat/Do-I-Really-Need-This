import streamlit as st

st.set_page_config(
    page_title="Do I Really Need This?",
    page_icon="🎟️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS: FRESH, GIRLY BOTANICAL & SYMMETRIC ALIGNMENT ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,500;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Latar belakang pastel segar & lembut */
    .stApp {
        background:
            radial-gradient(circle at 12% 15%, rgba(214, 235, 223, 0.75) 0%, transparent 42%),
            radial-gradient(circle at 88% 18%, rgba(232, 224, 248, 0.75) 0%, transparent 42%),
            radial-gradient(circle at 50% 92%, rgba(253, 243, 212, 0.8) 0%, transparent 48%),
            #FAF8F5;
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #262B28;
    }

    /* Merapikan kontainer utama agar sejajar simetris kanan-kiri */
    .block-container {
        max-width: 560px !important;
        padding-top: 2.5rem !important;
        padding-bottom: 3rem !important;
        padding-left: 1.25rem !important;
        padding-right: 1.25rem !important;
    }

    /* Sembunyikan menu/header bawaan Streamlit agar bersih */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* Header & Judul */
    .cute-stickers {
        text-align: center;
        font-size: 1.35rem;
        letter-spacing: 0.45rem;
        margin-bottom: 0.35rem;
        opacity: 0.9;
    }

    .editorial-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.45rem;
        font-weight: 700;
        color: #1D2621;
        text-align: center;
        line-height: 1.15;
        margin-bottom: 0.4rem;
    }

    .editorial-title span.italic-sage {
        font-style: italic;
        font-weight: 600;
        color: #4D7763;
    }

    .editorial-subtitle {
        text-align: center;
        color: #636B66;
        font-size: 0.92rem;
        line-height: 1.55;
        margin-bottom: 1.6rem;
    }

    /* Kartu Utama (Welcome & Pertanyaan) */
    .main-card {
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(12px);
        border: 1.5px solid #E5E0D5;
        border-radius: 28px;
        padding: 1.75rem 1.65rem 1.4rem 1.65rem;
        box-shadow: 0 16px 40px rgba(45, 74, 60, 0.06);
        margin-bottom: 1rem;
    }

    /* Baris atas kartu pertanyaan (Badge kiri, Nomor kanan) */
    .card-top-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.85rem;
    }

    .badge-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        padding: 0.28rem 0.8rem;
        border-radius: 999px;
    }

    .badge-fandom {
        background-color: #EDE8FA;
        color: #5A4B8C;
        border: 1px solid #DDD4F5;
    }

    .badge-emotion {
        background-color: #FEF4D6;
        color: #8C6B1D;
        border: 1px solid #F7E5B2;
    }

    .badge-finance {
        background-color: #E3F2E9;
        color: #35614D;
        border: 1px solid #C9E3D3;
    }

    .step-counter {
        font-size: 0.78rem;
        font-weight: 600;
        color: #8B948E;
        background: #F4F2EC;
        padding: 0.22rem 0.65rem;
        border-radius: 999px;
    }

    .question-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #1D2621;
        line-height: 1.38;
        margin-bottom: 0.25rem;
    }

    /* Styling Radio Button menjadi kartu pilihan yang rapi & sejajar */
    div[data-testid="stRadio"] > label {
        display: none !important;
    }

    div[data-testid="stRadio"] > div {
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
        width: 100%;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"] {
        background-color: #FCFBF8 !important;
        border: 1.5px solid #E8E3D9 !important;
        border-radius: 18px !important;
        padding: 0.85rem 1.1rem !important;
        margin: 0 !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
        cursor: pointer;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
        background-color: #F2F7F4 !important;
        border-color: #9BB8A8 !important;
        transform: translateY(-1px);
    }

    /* Warna saat opsi dipilih */
    div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
        background-color: #E7F2EC !important;
        border-color: #527966 !important;
        box-shadow: 0 4px 12px rgba(82, 121, 102, 0.14) !important;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"] p {
        font-size: 0.92rem !important;
        color: #363D39 !important;
        font-weight: 500 !important;
    }

    div[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) p {
        color: #1F3B2E !important;
        font-weight: 600 !important;
    }

    /* Styling Text Input nama konser */
    div[data-testid="stTextInput"] input {
        background-color: #FCFBF8 !important;
        border: 1.5px solid #DFD9CE !important;
        border-radius: 16px !important;
        padding: 0.75rem 1rem !important;
        font-size: 0.95rem !important;
        color: #262B28 !important;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: #527966 !important;
        box-shadow: 0 0 0 3px rgba(82, 121, 102, 0.15) !important;
    }

    /* Styling Tombol Navigasi agar sejajar & pill-shaped */
    div.stButton > button {
        border-radius: 16px !important;
        padding: 0.65rem 1.25rem !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        transition: all 0.2s ease !important;
        border: 1.5px solid #DFD9CE !important;
        background-color: #FFFFFF !important;
        color: #3A423E !important;
    }

    div.stButton > button:hover {
        border-color: #7FA391 !important;
        background-color: #F4F8F6 !important;
        color: #233D31 !important;
    }

    /* Tombol Primary (Next / Reveal) */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #476E5B 0%, #355747 100%) !important;
        color: #FAF8F5 !important;
        border: none !important;
        box-shadow: 0 8px 20px -4px rgba(53, 87, 71, 0.35) !important;
    }

    div.stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #3C604F 0%, #2B483A 100%) !important;
        transform: translateY(-1px);
    }

    /* Styling Progress Bar */
    div[data-testid="stProgress"] > div > div {
        background-color: #E6E2D8 !important;
        border-radius: 999px !important;
        height: 8px !important;
    }

    div[data-testid="stProgress"] > div > div > div {
        background: linear-gradient(90deg, #8B7EC8 0%, #689680 100%) !important;
        border-radius: 999px !important;
    }

    /* Kartu Result bergaya Ticket Stub */
    .ticket-card {
        background: rgba(255, 255, 255, 0.92);
        border: 1.5px solid #E4DFD3;
        border-radius: 30px;
        padding: 2rem 1.8rem;
        box-shadow: 0 20px 50px rgba(44, 74, 62, 0.08);
        position: relative;
        margin-bottom: 1.2rem;
    }

    .ticket-divider {
        border-top: 2px dashed #DFD9CC;
        margin: 1.4rem -1.8rem;
        position: relative;
    }

    .concert-tag {
        display: inline-block;
        background: #F4F1EA;
        color: #5C584F;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        margin-bottom: 0.9rem;
    }

    .score-box {
        background: linear-gradient(180deg, #F5F9F6 0%, #EDF4F0 100%);
        border: 1px solid #D7E6DD;
        border-radius: 22px;
        padding: 1.15rem;
        text-align: center;
        margin-bottom: 1.25rem;
    }

    .score-number {
        font-family: 'Playfair Display', serif;
        font-size: 3.1rem;
        font-weight: 700;
        color: #294739;
        line-height: 1.05;
    }

    .verdict-headline {
        font-family: 'Playfair Display', serif;
        font-size: 1.65rem;
        font-weight: 700;
        color: #1D2621;
        text-align: center;
        margin-bottom: 0.55rem;
        line-height: 1.25;
    }

    .verdict-desc {
        color: #5B635E;
        font-size: 0.92rem;
        line-height: 1.6;
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
        color: #3E4742;
        margin-bottom: 0.35rem;
    }

    .cat-bar-bg {
        width: 100%;
        height: 9px;
        background-color: #EAE6DD;
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
# step 0 = Halaman Awal (Input Nama Konser)
# step 1..10 = Pertanyaan 1 sampai 10
# step 11 = Halaman Hasil
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
            <span class="step-counter">10 Quick Questions</span>
        </div>
        <div class="question-text">Which concert or artist are we thinking about today?</div>
        <p style="font-size:0.86rem; color:#6D7570; margin-top:0.35rem; margin-bottom:0;">
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

    # Progress bar atas
    st.progress(st.session_state.step / total_q)

    # Kartu Pertanyaan
    st.markdown(f"""
    <div class="main-card">
        <div class="card-top-row">
            <span class="badge-pill {q['badge_class']}">{q['icon']} {q['category']}</span>
            <span class="step-counter">Question {st.session_state.step} of {total_q}</span>
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

    # Tombol Back & Next sejajar simetris kanan-kiri
    col_back, col_next = st.columns([1, 1], gap="medium")

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

    # Penentuan Verdict
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
            <div style="font-size:0.72rem; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:#648072; margin-bottom:0.2rem;">
                Final Compatibility Score
            </div>
            <div class="score-number">
                {total_score}<span style="font-size:1.45rem; font-weight:400; color:#92A49A;">/{max_total_score}</span>
            </div>
        </div>
        <div style="text-align:center; font-size:1.8rem; margin-bottom:0.35rem;">{verdict_emoji}</div>
        <div class="verdict-headline">“{headline}”</div>
        <div class="verdict-desc">{description}</div>
        <div class="ticket-divider"></div>
        <div style="font-size:0.75rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase; color:#868E89; margin-bottom:0.9rem; text-align:center;">
            ✦ Breakdown By Category ✦
        </div>
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

    col_recheck, col_new = st.columns([1, 1], gap="medium")
    with col_recheck:
        if st.button("← Edit Answers", use_container_width=True):
            st.session_state.step = len(QUESTIONS)
            st.rerun()
    with col_new:
        if st.button("↺ Check Another Concert", type="primary", use_container_width=True):
            reset_quiz()
            st.rerun()