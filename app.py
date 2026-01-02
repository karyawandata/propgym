import calendar
from datetime import date

from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    site = {
        "brand": "brand gym anda",
        "slogan_main": "FITNESS CENTER TERLENGKAP DI KOTA ANDA",
        "slogan_motivation": "ingat Gym, ingat GYM ANDA",
        "address": "Alamat Anda",
        "maps_url": "https://maps.app.goo.gl/He6CFkAndq5do9wD6",
        "wa_number_e164": "6281111",
    }

    pricing = [
        {
            "name": "Basic",
            "price": "Rp 399.000 / bulan",
            "tag": "Start Strong",
            "features": [
                "Akses gym reguler",
                "Area strength + cardio",
                "Kelas Aerobic/Zumba (jadwal tertentu)",
                "Program starter untuk pemula",
                "Support basic via admin",
            ],
        },
        {
            "name": "Plus",
            "price": "Rp 649.000 / bulan",
            "tag": "Recommended",
            "features": [
                "Semua benefit Basic",
                "Program terarah (update bulanan)",
                "Priority booking kelas",
                "Progress check lebih rutin",
                "Bonus: 1x konsultasi coach / bulan",
            ],
        },
        {
            "name": "VIP",
            "price": "Rp 1.199.000 / bulan",
            "tag": "Executive",
            "features": [
                "Semua benefit Plus",
                "Priority support & booking",
                "Body composition & review lebih sering",
                "Diskon PT / bonus PT session",
                "Benefit eksklusif (jika tersedia)",
            ],
        },
    ]

    membership_plans = {
        "contract": [
            {
                "name": "GOAL 12",
                "tag": "Kontrak",
                "desc": "Komitmen 12 bulan, bayar bulanan.",
                "features": [
                    "Tanpa biaya admin",
                    "Full akses ke seluruh fasilitas",
                    "Bayar bulanan tanpa ribet",
                    "Bawa teman untuk free trial",
                ],
            },
            {
                "name": "FLEX 4",
                "tag": "Kontrak",
                "desc": "Komitmen 4 bulan, bayar bulanan.",
                "features": [
                    "Tanpa biaya admin",
                    "Full akses ke seluruh fasilitas",
                    "Bayar bulanan tanpa ribet",
                    "Bawa teman untuk free trial",
                ],
            },
            {
                "name": "NOMAD GOAL 12",
                "tag": "Nomad",
                "desc": "Komitmen 12 bulan, bayar bulanan.",
                "features": [
                    "Tanpa biaya admin",
                    "Full akses ke seluruh fasilitas",
                    "Bayar bulanan tanpa ribet",
                    "Akses ke seluruh klub",
                ],
            },
        ],
    }

    trainers = [
        {
            "name": "Coach Andi",
            "cert": "Certified Personal Trainer",
            "bio": "Fokus bantu pemula mulai latihan dengan teknik yang benar, aman, dan konsisten.",
            "photo": "https://images.unsplash.com/photo-1550345332-09e3ac987658?auto=format&fit=crop&w=900&q=80",
            "specialties": ["Fat loss", "Strength", "Beginner guidance"],
        },
        {
            "name": "Coach Rina",
            "cert": "Certified Fitness Coach",
            "bio": "Pendekatan latihan yang fun dan terarah untuk body shaping & kebiasaan hidup sehat.",
            "photo": "https://images.unsplash.com/photo-1594737625785-a6cbdabd333c?auto=format&fit=crop&w=900&q=80",
            "specialties": ["Body shaping", "Mobility", "Lifestyle habit"],
        },
        {
            "name": "Coach Dimas",
            "cert": "Strength & Conditioning",
            "bio": "Spesialis strength & hypertrophy. Cocok buat kamu yang ngejar progres dan performa.",
            "photo": "https://images.unsplash.com/photo-1599058917212-d750089bc07e?auto=format&fit=crop&w=900&q=80",
            "specialties": ["Hypertrophy", "Performance", "Technique"],
        },
    ]

    facilities = [
        {
            "title": "Peralatan lengkap",
            "desc": "Cardio, strength, dan functional training tersedia dan terawat.",
            "icon": "ALAT",
            "img": "https://images.unsplash.com/photo-1571902943202-507ec2618e8f?auto=format&fit=crop&w=1200&q=80",
        },
        {
            "title": "Area sauna",
            "desc": "Recovery lebih nyaman setelah latihan intens.",
            "icon": "SAUNA",
            "img": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80",
        },
        {
            "title": "Ruang kelas",
            "desc": "Kelas eksklusif dengan jadwal rutin untuk variasi latihan.",
            "icon": "KELAS",
            "img": "https://images.unsplash.com/photo-1517836357463-d25dfeac3438?auto=format&fit=crop&w=1200&q=80",
        },
        {
            "title": "Wi‑Fi gratis",
            "desc": "Tetap terkoneksi selama latihan di area gym.",
            "icon": "WIFI",
            "img": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80",
        },
    ]

    testimonials = [
        {
            "name": "Rizky",
            "role": "Member 6 bulan",
            "quote": "Tempatnya bersih dan alatnya lengkap. Enak buat latihan fokus, apalagi jam pagi.",
        },
        {
            "name": "Nadia",
            "role": "Beginner",
            "quote": "Aku baru mulai gym dan dibantu coach buat teknik dasar. Jadi lebih pede dan konsisten.",
        },
        {
            "name": "Fajar",
            "role": "Bulking",
            "quote": "Programnya jelas dan progress kerasa. Admin juga responsif kalau tanya jadwal.",
        },
    ]

    class_catalog = [
        {
            "category": "Strength & Conditioning",
            "name": "HYROX",
            "desc": "Latihan interval untuk stamina, power, dan performa.",
        },
        {
            "category": "Cardio / Combat",
            "name": "BODYCOMBAT",
            "desc": "Cardio combat seru untuk bakar kalori dan improve endurance.",
        },
        {
            "category": "Mind & Body",
            "name": "YOGA",
            "desc": "Mobility, breathwork, dan recovery untuk tubuh lebih seimbang.",
        },
        {
            "category": "Mind & Body",
            "name": "BODYBALANCE",
            "desc": "Gabungan yoga/pilates untuk strength, posture, dan fleksibilitas.",
        },
        {
            "category": "HIIT",
            "name": "HIIT X",
            "desc": "Sesi HIIT singkat untuk hasil maksimal.",
        },
        {
            "category": "Dance",
            "name": "ZUMBA",
            "desc": "Dance cardio fun untuk mood booster dan konsistensi.",
        },
    ]

    def build_schedule_events(year: int, month: int):
        cal = calendar.Calendar(firstweekday=0)
        events_by_day: dict[int, list[dict]] = {}

        for d in cal.itermonthdates(year, month):
            if d.month != month:
                continue

            weekday = d.weekday()  # Mon=0
            day_events: list[dict] = []

            if weekday in (1, 3):
                day_events.append({"title": "Zumba", "time": "18:30"})

            if weekday in (0, 2, 4):
                day_events.append({"title": "Aerobic", "time": "07:00"})

            if weekday == 5:
                day_events.append({"title": "MMA", "time": "19:30"})

            if day_events:
                events_by_day[d.day] = day_events

        return events_by_day

    def build_month_calendar(year: int, month: int, events_by_day: dict[int, list[dict]]):
        weeks = []
        for week in calendar.monthcalendar(year, month):
            row = []
            for day in week:
                row.append(
                    {
                        "day": day if day != 0 else None,
                        "events": events_by_day.get(day, []) if day != 0 else [],
                    }
                )
            weeks.append(row)
        return weeks

    def wa_link(text: str) -> str:
        text_encoded = (
            text.replace(" ", "%20")
            .replace("\n", "%0A")
            .replace("&", "%26")
            .replace("?", "%3F")
        )
        return f"https://wa.me/{site['wa_number_e164']}?text={text_encoded}"

    @app.get("/")
    def home():
        return render_template(
            "home.html",
            site=site,
            pricing=pricing,
            membership_plans=membership_plans,
            trainers=trainers,
            facilities=facilities,
            class_catalog=class_catalog,
            testimonials=testimonials,
            wa_link=wa_link,
        )

    @app.get("/facilities")
    def facilities_page():
        return render_template(
            "facilities.html",
            site=site,
            facilities=facilities,
            wa_link=wa_link,
        )

    @app.get("/pricing")
    def pricing_page():
        return render_template(
            "pricing.html",
            site=site,
            pricing=pricing,
            wa_link=wa_link,
        )

    @app.get("/personaltrainer")
    def personal_trainer_page():
        return render_template(
            "personaltrainer.html",
            site=site,
            trainers=trainers,
            wa_link=wa_link,
        )

    @app.route("/contact", methods=["GET", "POST"])
    def contact_page():
        submitted = False
        form_data = {}

        if request.method == "POST":
            submitted = True
            form_data = {
                "name": request.form.get("name", ""),
                "phone": request.form.get("phone", ""),
                "package": request.form.get("package", ""),
                "message": request.form.get("message", ""),
            }

        return render_template(
            "contact.html",
            site=site,
            pricing=pricing,
            submitted=submitted,
            form_data=form_data,
            wa_link=wa_link,
        )

    @app.get("/schedule")
    def schedule_page():
        today = date.today()
        year = today.year
        month = today.month

        month_names_id = [
            "Januari",
            "Februari",
            "Maret",
            "April",
            "Mei",
            "Juni",
            "Juli",
            "Agustus",
            "September",
            "Oktober",
            "November",
            "Desember",
        ]

        events_by_day = build_schedule_events(year, month)
        weeks = build_month_calendar(year, month, events_by_day)

        return render_template(
            "schedule.html",
            site=site,
            wa_link=wa_link,
            year=year,
            month=month,
            month_label=month_names_id[month - 1],
            weeks=weeks,
        )

    return app


if __name__ == "__main__":
    create_app().run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
    
    
