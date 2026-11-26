from flask import Flask, render_template, request

app = Flask(__name__)

# Daftar 10 pertanyaan dengan kategori dan skor masing-masing
QUESTIONS = [
    # --- Kategori: Fandom ---
    {
        "id": "q1",
        "category": "Fandom",
        "question": "How long have you been a fan?",
        "options": [
            {"text": "Since they debut", "score": 3},
            {"text": "1 - 3 years", "score": 2},
            {"text": "Just a few months", "score": 1},
            {"text": "I only know 1 viral song", "score": 0}
        ]
    },
    {
        "id": "q2",
        "category": "Fandom",
        "question": "Can you recognize their song in 5 seconds?",
        "options": [
            {"text": "Yes, even the B-sides", "score": 3},
            {"text": "Some of it (mostly title tracks)", "score": 2},
            {"text": "Only the chorus", "score": 1},
            {"text": "No", "score": 0}
        ]
    },
    {
        "id": "q3",
        "category": "Fandom",
        "question": "Do you know the members' names and inside jokes?",
        "options": [
            {"text": "By heart, yes", "score": 3},
            {"text": "Most of them", "score": 2},
            {"text": "Only the main vocalist/frontman", "score": 1},
            {"text": "Not really", "score": 0}
        ]
    },
    {
        "id": "q4",
        "category": "Fandom",
        "question": "Have you watched their live concert videos on YouTube?",
        "options": [
            {"text": "Countless times, I know the fanchants", "score": 3},
            {"text": "A few times", "score": 2},
            {"text": "Once or twice", "score": 1},
            {"text": "Never", "score": 0}
        ]
    },

    # --- Kategori: Emotional Attachment ---
    {
        "id": "q5",
        "category": "Emotional Attachment",
        "question": "How would you feel if you skip this concert and see clips on social media?",
        "options": [
            {"text": "Devastated, pure regret for months", "score": 3},
            {"text": "Pretty sad (FOMO hits hard)", "score": 2},
            {"text": "A bit jealous, then move on", "score": 1},
            {"text": "Totally fine", "score": 0}
        ]
    },
    {
        "id": "q6",
        "category": "Emotional Attachment",
        "question": "How likely are they to tour in your city again soon?",
        "options": [
            {"text": "Almost zero / Once in a lifetime", "score": 3},
            {"text": "Maybe in 2-3 years", "score": 2},
            {"text": "They come here pretty often", "score": 1},
            {"text": "No idea", "score": 0}
        ]
    },
    {
        "id": "q7",
        "category": "Emotional Attachment",
        "question": "Are you going for the music or just for Instagram stories?",
        "options": [
            {"text": "100% the live music experience", "score": 3},
            {"text": "Mostly music, partly the hype", "score": 2},
            {"text": "50/50", "score": 1},
            {"text": "Honestly, just the clout", "score": 0}
        ]
    },

    # --- Kategori: Financial Safety ---
    {
        "id": "q8",
        "category": "Financial Safety",
        "question": "Can you afford the ticket without putting essentials at risk?",
        "options": [
            {"text": "Yes, easily", "score": 3},
            {"text": "Maybe, need to cut back on coffee/eating out", "score": 2},
            {"text": "No, rent/bills will suffer", "score": 0}
        ]
    },
    {
        "id": "q9",
        "category": "Financial Safety",
        "question": "How are you paying for this ticket?",
        "options": [
            {"text": "Dedicated concert/fun savings", "score": 3},
            {"text": "This month's paycheck", "score": 2},
            {"text": "Paylater / Credit card debt / Borrowing", "score": 0}
        ]
    },
    {
        "id": "q10",
        "category": "Financial Safety",
        "question": "Did you factor in transport, food, and outfit costs?",
        "options": [
            {"text": "Yes, all budgeted", "score": 3},
            {"text": "Roughly estimated", "score": 2},
            {"text": "Wait... there are extra costs?", "score": 1},
            {"text": "I'll figure it out later", "score": 0}
        ]
    }
]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", questions=QUESTIONS)

@app.route("/result", methods=["POST"])
def result():
    total_score = 0
    max_total_score = 0

    # Penampung skor per kategori
    cat_scores = {"Fandom": 0, "Emotional Attachment": 0, "Financial Safety": 0}
    cat_max = {"Fandom": 0, "Emotional Attachment": 0, "Financial Safety": 0}

    for q in QUESTIONS:
        # Hitung skor maksimal yang mungkin didapat
        highest_option = max(opt["score"] for opt in q["options"])
        max_total_score += highest_option
        cat_max[q["category"]] += highest_option

        # Ambil jawaban user dari form
        user_answer = int(request.form.get(q["id"], 0))
        total_score += user_answer
        cat_scores[q["category"]] += user_answer

    # Hitung persentase tiap kategori
    percentages = {
        cat: round((cat_scores[cat] / cat_max[cat]) * 100)
        for cat in cat_scores
    }

    # Logika Penentuan Verdict (Bisa disesuaikan!)
    # Jika Financial Safety terlalu rendah (< 40%), langsung beri peringatan keras
    if percentages["Financial Safety"] < 40:
        headline = "Step away from the checkout button."
        description = "Your heart says yes, your bank account is screaming for help. Fandom does not pay rent. Watch the fancams in HD from your bed instead."
    elif total_score >= 23:
        headline = "Buy the ticket. No regrets."
        description = "You're a true fan, emotionally invested, and financially ready. Go scream your lungs out and enjoy every second of it."
    elif total_score >= 15:
        headline = "You could go, but think."
        description = "You clearly care about this concert. Just make sure the ticket doesn't turn into three weeks of financial suffering. Your budget has veto power. Fandom does not pay rent."
    else:
        headline = "Save your money."
        description = "You don't actually need this. You're probably just caught up in the hype. Treat yourself to a really nice dinner instead."

    return render_template(
        "result.html",
        total_score=total_score,
        max_total_score=max_total_score,
        headline=headline,
        description=description,
        percentages=percentages
    )

if __name__ == "__main__":
    app.run(debug=True)