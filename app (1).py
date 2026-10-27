"""
JayZ Care - DEMONSTRATION PROTOTYPE (v0.1)
Part of the JayZ Project. Target market: Plateau State, Nigeria.

IMPORTANT
- All facilities, providers, contacts and availability are FICTIONAL sample data.
- Nothing is stored, sent, or dispatched. No real booking or emergency help happens here.
- Health content is general education only and has NOT yet been reviewed by a
  qualified medical reviewer. It is not a substitute for professional care.
"""

import random
from datetime import date, timedelta

import streamlit as st

# ---------------------------------------------------------------
# 1. PAGE SETUP AND LOOK
# ---------------------------------------------------------------
st.set_page_config(
    page_title="JayZ Care (Demo)",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="auto",
)

st.markdown(
    """
<style>
html, body, [class*="css"] { font-size: 17px; }
.stButton > button { min-height: 48px; border-radius: 10px; font-weight: 600; }
.jz-hero { background: linear-gradient(135deg, #0B6E4F, #127A8A); color: #fff;
           padding: 1.2rem 1.4rem; border-radius: 14px; margin-bottom: 1rem; }
.jz-hero h1 { color: #fff; margin: 0; font-size: 1.8rem; }
.jz-hero p { margin: .3rem 0 0; color: #EAFAF3; }
.jz-demo { display: inline-block; background: #FFF3CD; color: #5C4400;
           border: 1px solid #E0B100; padding: 2px 8px; border-radius: 6px;
           font-size: .8rem; font-weight: 700; }
.jz-emerg { background: #FDECEA; border: 2px solid #B3261E; color: #5A0F0B;
            padding: 1rem; border-radius: 12px; margin-bottom: 1rem; }
.jz-confirm { background: #FFF3CD; border: 3px dashed #B38600; color: #4A3800;
              padding: 1rem; border-radius: 12px; margin: 1rem 0; }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------
# 2. DEMONSTRATION DATA (ALL FICTIONAL)
# ---------------------------------------------------------------
PAGES = [
    "Home",
    "Health Education",
    "Find a Facility",
    "Book Appointment",
    "Emergency Help",
    "Provider Directory",
    "Guided Assistant",
    "About & Safety",
]

ARTICLES = [
    {
        "title": "Preventing malaria",
        "category": "Infectious disease",
        "summary": "Malaria is spread by the bite of infected mosquitoes. Simple steps lower the risk.",
        "points": [
            "Sleep under an insecticide-treated mosquito net every night.",
            "Young children and pregnant women are at higher risk, so protection matters most for them.",
            "If someone has a fever, get tested at a health facility promptly rather than guessing the cause.",
            "Ask a health worker at a real facility about prevention options for your situation.",
        ],
        "source_name": "WHO - Malaria fact sheet",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/malaria",
    },
    {
        "title": "Handwashing with soap",
        "category": "Hygiene",
        "summary": "Clean hands help stop the spread of many infections, including diarrhoea.",
        "points": [
            "Wash with soap and clean water, rubbing all parts of the hands.",
            "Key moments: before preparing food or eating, after using the toilet, after caring for a sick person.",
            "Keep soap and water near toilets and kitchens so handwashing is easy.",
        ],
        "source_name": "WHO - Hand hygiene",
        "source_url": "https://www.who.int/health-topics/hand-hygiene",
    },
    {
        "title": "Know your blood pressure",
        "category": "Chronic conditions",
        "summary": "High blood pressure often has no symptoms, so the only way to know is to have it measured.",
        "points": [
            "Have your blood pressure checked at a health facility or pharmacy with a trained person.",
            "Eating less salt, being active and avoiding tobacco support heart health.",
            "Do not start or stop any treatment without advice from a qualified health professional.",
        ],
        "source_name": "WHO - Hypertension fact sheet",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/hypertension",
    },
    {
        "title": "Safe drinking water",
        "category": "Water and sanitation",
        "summary": "Unsafe water is linked to diarrhoeal disease. Safe handling at home helps protect families.",
        "points": [
            "Store drinking water in a clean, covered container.",
            "Ask your local health authority which water treatment methods are recommended in your area.",
            "Seek care promptly if a child with diarrhoea cannot drink, seems very weak, or has blood in the stool.",
        ],
        "source_name": "WHO - Drinking-water fact sheet",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/drinking-water",
    },
    {
        "title": "Antenatal care during pregnancy",
        "category": "Maternal health",
        "summary": "Regular check-ups with a trained health worker help protect mother and baby.",
        "points": [
            "Attend antenatal visits at a health facility and plan where the birth will take place.",
            "Urgent warning signs: heavy bleeding, convulsions, severe headache with blurred vision, "
            "severe belly pain. Go to the nearest emergency-capable facility immediately.",
        ],
        "source_name": "WHO - Maternal mortality fact sheet",
        "source_url": "https://www.who.int/news-room/fact-sheets/detail/maternal-mortality",
    },
]

VIDEO_PLACEHOLDER = "https://www.youtube.com/@WHO"  # general WHO channel, not a specific video

FACILITIES = [
    {"name": "Demo General Hospital A", "type": "Hospital", "area": "Jos North", "services": "Outpatient, maternity, laboratory"},
    {"name": "Demo Community Clinic B", "type": "Clinic", "area": "Jos South", "services": "Outpatient, immunisation, antenatal"},
    {"name": "Demo Pharmacy C", "type": "Pharmacy", "area": "Jos North", "services": "Dispensing, blood pressure checks"},
    {"name": "Demo Health Centre D", "type": "Clinic", "area": "Bukuru", "services": "Outpatient, child health"},
    {"name": "Demo District Hospital E", "type": "Hospital", "area": "Pankshin", "services": "Outpatient, surgery, emergency"},
    {"name": "Demo Pharmacy F", "type": "Pharmacy", "area": "Barkin Ladi", "services": "Dispensing, health advice"},
    {"name": "Demo Primary Health Centre G", "type": "Clinic", "area": "Shendam", "services": "Outpatient, antenatal"},
    {"name": "Demo Referral Hospital H", "type": "Hospital", "area": "Langtang", "services": "Outpatient, laboratory, emergency"},
    {"name": "Demo Pharmacy I", "type": "Pharmacy", "area": "Bokkos", "services": "Dispensing"},
]

PROVIDERS = [
    {"name": "Dr. Demo Person One", "specialty": "General practice", "facility": "Demo General Hospital A"},
    {"name": "Dr. Demo Person Two", "specialty": "Paediatrics", "facility": "Demo Community Clinic B"},
    {"name": "Nurse Demo Person Three", "specialty": "Community nursing", "facility": "Demo Health Centre D"},
    {"name": "Dr. Demo Person Four", "specialty": "Obstetrics", "facility": "Demo District Hospital E"},
    {"name": "Pharm. Demo Person Five", "specialty": "Pharmacy", "facility": "Demo Pharmacy C"},
    {"name": "Dr. Demo Person Six", "specialty": "Internal medicine", "facility": "Demo Referral Hospital H"},
]
PROVIDER_STATUS = "🟡 DEMO RECORD - not a real person, not verified"

RED_FLAGS = [
    "Difficulty breathing or choking",
    "Chest pain or pressure",
    "Heavy bleeding that will not stop",
    "Fainting, unconsciousness, or unresponsive",
    "Seizure / convulsions",
    "Signs of stroke: face drooping, arm weakness, slurred speech",
    "Severe allergic reaction (swelling of face or throat)",
    "Pregnancy emergencies: heavy bleeding, convulsions, severe pain",
    "Poisoning, serious injury, burns or snakebite",
    "Thoughts of harming yourself or someone else",
]

# ---------------------------------------------------------------
# 3. SMALL HELPER FUNCTIONS
# ---------------------------------------------------------------
def go(page):
    """Button callback: switch page."""
    st.session_state.page = page


def demo_banner():
    st.warning(
        "⚠️ **DEMONSTRATION VERSION.** All facilities, people and contacts here are "
        "fictional sample data. Nothing is real, verified, stored or sent.",
        icon=None,
    )


def hero(title, subtitle):
    st.markdown(
        f'<div class="jz-hero"><h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )


def nav_button(label, page, key):
    st.button(label, on_click=go, args=(page,), key=key, use_container_width=True)


def search_all(query):
    q = query.lower().strip()
    arts = [a for a in ARTICLES if q in (a["title"] + a["category"] + a["summary"]).lower()]
    facs = [f for f in FACILITIES if q in (f["name"] + f["type"] + f["area"] + f["services"]).lower()]
    pros = [p for p in PROVIDERS if q in (p["name"] + p["specialty"] + p["facility"]).lower()]
    return arts, facs, pros


def facility_card(f):
    with st.container(border=True):
        st.markdown(f"**{f['name']}**  \n{f['type']} · {f['area']}, Plateau State")
        st.caption(f"Services (sample): {f['services']}")
        st.markdown('<span class="jz-demo">DEMO - not a real facility</span>', unsafe_allow_html=True)


# ---------------------------------------------------------------
# 4. PAGES
# ---------------------------------------------------------------
def page_home():
    hero("JayZ Care", "Health information and healthcare navigation for Plateau State · Demo prototype")
    demo_banner()

    st.markdown(
        '<div class="jz-emerg"><b>🚨 Emergency?</b> Do not use this app. Go to the nearest '
        "emergency facility or contact verified local emergency services right now.</div>",
        unsafe_allow_html=True,
    )
    nav_button("🚨 Emergency guidance", "Emergency Help", "home_emerg")

    st.subheader("Search")
    query = st.text_input(
        "Search topics, facilities or providers",
        placeholder="e.g. malaria, pharmacy, Jos North",
        help="Please do not type personal or medical details here.",
    )
    if query.strip():
        arts, facs, pros = search_all(query)
        st.write(f"Found {len(arts)} article(s), {len(facs)} facility(ies), {len(pros)} provider(s).")
        for a in arts:
            st.markdown(f"📚 **{a['title']}** - {a['summary']}")
        for f in facs:
            facility_card(f)
        for p in pros:
            st.markdown(f"🩺 **{p['name']}** - {p['specialty']} ({PROVIDER_STATUS})")
        if not (arts or facs or pros):
            st.info("No sample results. Try a different word.")

    st.subheader("What would you like to do?")
    tiles = [
        ("📚 Health education", "Health Education"),
        ("🏥 Find a facility", "Find a Facility"),
        ("📅 Book appointment (demo)", "Book Appointment"),
        ("🩺 Provider directory", "Provider Directory"),
        ("💬 Guided assistant", "Guided Assistant"),
        ("🔒 About & safety", "About & Safety"),
    ]
    cols = st.columns(3)
    for i, (label, page) in enumerate(tiles):
        with cols[i % 3]:
            nav_button(label, page, f"tile_{i}")


def page_education():
    hero("Health Education", "Plain-language general information")
    demo_banner()
    st.info(
        "Educational content is **not a substitute for professional medical assessment**. "
        "This content has not yet been reviewed by a qualified medical reviewer."
    )
    topic = st.selectbox("Filter by category", ["All"] + sorted({a["category"] for a in ARTICLES}))
    for a in ARTICLES:
        if topic != "All" and a["category"] != topic:
            continue
        with st.expander(f"{a['title']}  ·  {a['category']}"):
            st.write(a["summary"])
            for point in a["points"]:
                st.markdown(f"- {point}")
            st.markdown(f"**Source:** [{a['source_name']}]({a['source_url']})")
            st.markdown(f"🎥 [Watch health videos (WHO channel)]({VIDEO_PLACEHOLDER})")
            st.caption("Links should be re-checked before any public launch.")


def page_facilities():
    hero("Find a Facility", "Search sample hospitals, clinics and pharmacies")
    demo_banner()
    c1, c2, c3 = st.columns([2, 1, 1])
    text = c1.text_input("Search by name or service")
    ftype = c2.selectbox("Type", ["All", "Hospital", "Clinic", "Pharmacy"])
    area = c3.selectbox("Area", ["All"] + sorted({f["area"] for f in FACILITIES}))

    results = [
        f
        for f in FACILITIES
        if (ftype == "All" or f["type"] == ftype)
        and (area == "All" or f["area"] == area)
        and text.lower() in (f["name"] + f["services"]).lower()
    ]
    st.write(f"Showing {len(results)} sample result(s).")
    for f in results:
        facility_card(f)
    if not results:
        st.info("No sample facilities match. Try clearing a filter.")
    st.caption("No real addresses, phone numbers, opening hours or availability are shown.")


def page_booking():
    hero("Book an Appointment", "Demonstration form only")
    demo_banner()
    st.error("This form does NOT book a real appointment. Nothing is saved or sent.", icon="🚫")

    with st.form("booking_form"):
        name = st.text_input("Name or nickname (use a made-up name for this demo)")
        facility = st.selectbox("Facility (sample)", [f["name"] for f in FACILITIES])
        pref_date = st.date_input("Preferred date", value=date.today() + timedelta(days=1), min_value=date.today())
        slot = st.selectbox("Time of day", ["Morning", "Afternoon", "Evening"])
        reason = st.selectbox(
            "Type of visit (general only)",
            ["General check-up", "Child health", "Antenatal care", "Follow-up visit", "Other"],
        )
        st.caption("Do not enter symptoms, diagnoses, phone numbers or other personal health details.")
        agree = st.checkbox("I understand this is a demonstration and no real booking is made.")
        submitted = st.form_submit_button("Submit demo request", use_container_width=True)

    if submitted:
        errors = []
        if len(name.strip()) < 2:
            errors.append("Please enter a name or nickname (at least 2 characters).")
        if pref_date < date.today():
            errors.append("The date cannot be in the past.")
        if not agree:
            errors.append("Please tick the box to confirm you understand this is a demo.")
        if errors:
            for e in errors:
                st.error(e)
        else:
            ref = "DEMO-" + str(random.randint(1000, 9999))
            st.markdown(
                f'<div class="jz-confirm"><h3>DEMO ONLY - NOT A REAL BOOKING</h3>'
                f"<p>Reference <b>{ref}</b> is a made-up number. <b>{facility}</b> is a fictional "
                f"facility and has received nothing. Nothing was saved.</p>"
                f"<p>You entered: {pref_date.strftime('%A, %d %B %Y')} ({slot}) · {reason}</p></div>",
                unsafe_allow_html=True,
            )


def page_emergency():
    hero("Emergency Help", "Safety guidance · This app cannot call or dispatch help")
    st.markdown(
        '<div class="jz-emerg"><h3>🚨 If someone may be in danger, act now</h3>'
        "<p>Go to the nearest emergency-capable facility or contact <b>verified</b> local emergency "
        "services immediately. <b>Do not wait for this app or any online tool.</b> "
        "JayZ Care has not contacted anyone and cannot send help.</p></div>",
        unsafe_allow_html=True,
    )
    st.subheader("Get urgent care for signs like these")
    for r in RED_FLAGS:
        st.markdown(f"- {r}")
    st.caption("This is not a complete list. If you are worried someone is seriously unwell, treat it as urgent.")

    st.subheader("While getting help")
    st.markdown(
        "- Ask someone nearby to help you and stay with the person.\n"
        "- Follow instructions from trained emergency responders.\n"
        "- Do not give food, drink or medicine unless a health professional tells you to.\n"
        "- Bring any medicines the person already uses, if it is quick and safe to do so."
    )

    st.subheader("Verified emergency contacts")
    st.warning(
        "Placeholders only. Numbers must be confirmed with official Plateau State and "
        "Nigerian authorities before being added. No numbers are invented here."
    )
    st.table(
        {
            "Service": ["National emergency line", "Plateau State emergency service", "Nearest hospital emergency unit"],
            "Contact": ["[ADD VERIFIED NUMBER]", "[ADD VERIFIED NUMBER]", "[ADD VERIFIED NUMBER]"],
            "Verified by / date": ["[NOT VERIFIED]", "[NOT VERIFIED]", "[NOT VERIFIED]"],
        }
    )


def page_providers():
    hero("Provider Directory", "Sample records with verification labels")
    demo_banner()
    st.info(
        "Planned future labels: *Verified* (checked against the relevant Nigerian professional "
        "register by a human reviewer, with date), *Pending*, *Not verified*. "
        "Every record below is a **fictional demo record**."
    )
    spec = st.selectbox("Specialty", ["All"] + sorted({p["specialty"] for p in PROVIDERS}))
    for p in PROVIDERS:
        if spec != "All" and p["specialty"] != spec:
            continue
        with st.container(border=True):
            st.markdown(f"**{p['name']}**  \n{p['specialty']} · {p['facility']}")
            st.markdown(f"Status: {PROVIDER_STATUS}")


def assistant_reply(text):
    """Rule-based replies. Returns (message, page_to_offer or None). No AI, no storage."""
    t = text.lower()
    emergency_words = [
        "chest pain", "can't breathe", "cannot breathe", "breathing", "unconscious", "seizure",
        "convulsion", "bleeding", "stroke", "suicid", "kill myself", "poison", "snake",
        "overdose", "collapsed", "not breathing", "emergency",
    ]
    if any(w in t for w in emergency_words):
        return (
            "🚨 This could be urgent. Please go to the nearest emergency facility or contact verified "
            "local emergency services **now**. Do not wait for this app. I cannot send help.",
            "Emergency Help",
        )
    if any(w in t for w in ["book", "appointment"]):
        return "I can take you to the demo booking form. It does not make a real booking.", "Book Appointment"
    if any(w in t for w in ["hospital", "clinic", "pharmacy", "facility", "near"]):
        return "You can browse the sample facilities by type and area.", "Find a Facility"
    if any(w in t for w in ["doctor", "nurse", "provider", "specialist"]):
        return "Here is the sample provider directory (demo records only).", "Provider Directory"
    if any(w in t for w in ["malaria", "water", "pressure", "pregnan", "hygiene", "wash", "learn", "info"]):
        return "The education library has general information from WHO sources.", "Health Education"
    if any(w in t for w in ["symptom", "sick", "pain", "fever", "diagnos", "medicine", "drug", "tablet", "dose"]):
        return (
            "I'm not able to assess symptoms, diagnose, or recommend medicines. Please speak to a "
            "qualified health professional at a real facility. If it feels severe or sudden, treat "
            "it as urgent and seek emergency care.",
            "Find a Facility",
        )
    return "I'm a simple guided menu, not a clinician. Pick a topic above or type a word like 'book' or 'clinic'.", None


def page_assistant():
    hero("Guided Assistant", "A simple menu-based helper · Not a clinician · Not a live AI")
    demo_banner()
    st.info(
        "This assistant uses fixed, pre-written replies to point you to the right page. "
        "It cannot diagnose, advise on medicines or replace a health professional. "
        "Please don't type personal or medical details."
    )
    st.write("**Quick topics**")
    quick = {
        "Learn about health": "learn",
        "Find a clinic": "clinic",
        "Book (demo)": "book",
        "I have a health worry": "symptom",
        "Emergency": "emergency",
    }
    cols = st.columns(len(quick))
    chosen = None
    for col, (label, word) in zip(cols, quick.items()):
        if col.button(label, key=f"q_{word}", use_container_width=True):
            chosen = word

    typed = st.text_input("Or type a short request", placeholder="e.g. find a pharmacy")
    text = chosen or typed
    if text.strip():
        message, page = assistant_reply(text)
        with st.chat_message("assistant"):
            st.write(message)
        if page:
            nav_button(f"Go to: {page}", page, "assistant_go")


def page_about():
    hero("About & Safety", "How this prototype works and what it is not")
    st.markdown(
        """
**What this is:** a free demonstration of JayZ Care (JayZ Project) for Plateau State, Nigeria.

**What this is not:**
- Not a medical service, and not a source of diagnosis or treatment advice.
- Not connected to any real facility, provider, emergency service or booking system.
- Facilities, providers, contacts and availability are fictional demo data.

**Privacy in this prototype:** no accounts, no database, no analytics. Form entries
are not saved. Please do not enter real personal or health information.

**Needs professional review before any public launch:**
- Nigeria Data Protection Act 2023 duties (lawful basis, consent, notices, security, registration, cross-border rules)
- Health-data and telemedicine rules, and advertising or claims rules for health services
- Medical review of all educational content
- Verification process for facilities, providers and emergency contacts
- Accessibility testing, local-language support and testing on low-end phones

*This prototype makes no claim of legal or regulatory compliance.*
"""
    )


# ---------------------------------------------------------------
# 5. NAVIGATION AND MAIN
# ---------------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.title("🩺 JayZ Care")
st.sidebar.caption("Demo prototype v0.1")
st.sidebar.radio("Menu", PAGES, key="page")
st.sidebar.error("Emergency? Go to the nearest facility or call verified emergency services. Do not rely on this app.")

ROUTES = {
    "Home": page_home,
    "Health Education": page_education,
    "Find a Facility": page_facilities,
    "Book Appointment": page_booking,
    "Emergency Help": page_emergency,
    "Provider Directory": page_providers,
    "Guided Assistant": page_assistant,
    "About & Safety": page_about,
}
ROUTES[st.session_state.page]()

st.divider()
st.caption("JayZ Care · Demonstration prototype · Sample data only · Not medical advice")
