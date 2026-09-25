"""Streamlit portfolio application.

Run with ``streamlit run portfolio.py``.
Keep the requirements minimal: add ``streamlit`` to requirements.txt.
The app is suitable for GitHub and Python hosting.

To update the site after deployment, edit PROFILE or PROJECTS, commit the
change, and redeploy.
"""

import streamlit as st
from pathlib import Path


# Page setup and lightweight responsive styling
st.set_page_config(
    page_title="Mayank Rathi | Portfolio",
    page_icon=" ",
    layout="wide"
)

st.markdown(
"""
<style>
.stApp {
    background: #ffffff;
    color: #111827;
}

.hero {
    padding: 4rem 0 2rem;
}

.hero h1 {
    font-size: clamp(2.8rem, 7vw, 5.8rem);
    line-height: 1;
    color: #f8fafc;
}

.hero p, .muted {
    color: #64784b;
    font-size: 1.1rem;
}


/* =========================
   PROJECT CARDS
   ========================= */

.card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 18px;
    padding: 1.6rem;
    min-height: 210px;
    margin-bottom: 1rem;

    display: flex;
    flex-direction: column;
    justify-content: space-between;

    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-4px);
    border-color: #cbd5e1;
    box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
}

.card h3 {
    color: #0f172a;
    margin-bottom: 0.8rem;
}

.card p {
    color: #334155;
    line-height: 1.6;
}

.card small {
    color: #64748b;
}


/* =========================
   ALL LINK BUTTONS
   ========================= */

div[data-testid="stLinkButton"] a {
    border-radius: 10px !important;
    font-weight: 600 !important;

    padding: 0.65rem 1.1rem !important;

    background: #111827 !important;
    color: #ffffff !important;

    border: 1px solid #111827 !important;

    transition: all 0.2s ease !important;
}


/* Hover effect */

div[data-testid="stLinkButton"] a:hover {
    background: #2563eb !important;
    border-color: #2563eb !important;

    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(37, 99, 235, 0.20);
}


/* Project buttons */

div[data-testid="stLinkButton"] {
    margin-top: -0.4rem;
}


/* Contact buttons */

div[data-testid="stLinkButton"] a {
    width: 100%;
    text-align: center;
}


/* Normal links */

a {
    color: #2563eb !important;
}

</style>
""",
unsafe_allow_html=True
)


# Edit this single data section to update the deployed portfolio
PROFILE = {
    "name": "Mayank Rathi",
    # Short one-line hook shown right under your name.
    "role": "CSE student building toward a career in cybersecurity.",
    # Slightly longer version shown in the About section.
    "bio": (
        "First-year Computer Science Engineering student with a focus on "
        "cybersecurity. Currently learning Python, C, and the fundamentals "
        "of how systems work, and building hands-on projects as I go."
    ),
    # Real skill/interest tags -- keep this honest and specific.
    # Swap in real ones as you learn them, e.g. "networking basics",
    # "Linux", "Wireshark", "CTFs".
    "focus_areas": [
        "Python",
        "C",
        "Streamlit",
        "problem solving",
        "web security",
        "networking fundamentals",
        "Data structures and algorithms",
    ],
    "email": "mayankrathinp@gmail.com",
    "github": "https://github.com/Mayank-Rathi-create",
    "linkedin": "https://www.linkedin.com/in/mayank-rathi-555007427/",
    "Instagram": "https://www.instagram.com/mayank_rathi11/",
    "discord": "https://discord.com/channels/@mayankrathi0719",
}

# Keep this list to real, finished (or in-progress) work only.
# Drop placeholder cards like "working on more projects" -- an empty
# slot makes the whole section look unfinished. Add a card only when
# there's something behind the link.
PROJECTS = [
    {
        "title": "Portfolio website",
        "description": "This site, built with Streamlit and Python.",
        "stack": "Python, Streamlit",
        "url": "https://mayank-portfolio.streamlit.app/"
    },
    {
        "title": "Number guessing game",
        "description": "A simple interactive Python game that narrows down a hidden number using guess-and-check logic.",
        "stack": "Python",
        "url": "https://github.com/Mayank-Rathi-create/number_guess.git"
    },

    # Example of what to add next -- uncomment and fill in once built.
    # A small security-flavored project (port scanner, Caesar cipher
    # tool, password strength checker, a CTF writeup) will do far more
    # for this page than a second beginner exercise.
    # {
    #     "title": "Basic port scanner",
    #     "description": "A command-line tool that scans a host for open TCP ports using Python sockets.",
    #     "stack": "Python, sockets",
    #     "url": "https://github.com/Mayank-Rathi-create/port-scanner"
    # },
]

# Add blog/update entries here. Each item can be a short note about what
# you're learning, building, or doing lately.
BLOGS = [
    {
        "title": "Learning Computer Networking Basics",
        "date": "September 2026",
        "excerpt": "I am currently learning the basics of computer networking and exploring the fundamentals of cybersecurity.",
        "tags": ["Networking", "Cybersecurity"],
    },
    {
        "title": "Learning C and C++ Language",
        "date": "September 2026",
        "excerpt": "I am currently learning the C and C++ programming languages and exploring their applications in system-level programming.",
        "tags": ["C", "C++", "Programming"],
    },
]


if "projects" not in st.session_state:
    st.session_state.projects = [project.copy() for project in PROJECTS]

if "blogs" not in st.session_state:
    st.session_state.blogs = [blog.copy() for blog in BLOGS]


# ============================================================
# HERO SECTION
# ============================================================

st.markdown('<div class="hero">', unsafe_allow_html=True)

st.caption("PORTFOLIO / 2026")

hero_text, hero_photo = st.columns([4, 1])

with hero_text:
    st.markdown(f"# Hi, I'm {PROFILE['name']}.")

# Photo section: only turn this back on with a natural, casual photo --
# a formal ID-style headshot reads as a document photo, not a personal
# site photo. It's fine to leave this off entirely.
# with hero_photo:
#     st.image(
#         str(Path(__file__).parent / "assets" / "profile.jpg"),
#         width=180,
#     )

st.markdown(f"### {PROFILE['role']}")

st.write("Get in touch or explore my work below.")


# Profile buttons
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.link_button(
        "Email",
        f"mailto:{PROFILE['email']}"
    )

with col2:
    st.link_button(
        "GitHub",
        PROFILE["github"]
    )

with col3:
    st.link_button(
        "LinkedIn",
        PROFILE["linkedin"]
    )

with col4:
    st.link_button(
        "Instagram",
        PROFILE["Instagram"]
    )
with col5:
    st.link_button(
        "Discord",
        PROFILE["discord"]
    )

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# ABOUT
# ============================================================

st.header("About me")

st.write(PROFILE["bio"])

st.write("**Focus areas:** " + " · ".join(PROFILE["focus_areas"]))


# ============================================================
# SELECTED WORK
# ============================================================

st.header("Projects")

columns = st.columns(3)

for index, project in enumerate(st.session_state.projects):

    with columns[index % 3]:

        st.markdown(
            f'''
            <div class="card">
                <h3>{project["title"]}</h3>
                <p>{project["description"]}</p>
                <small>{project["stack"]}</small>
            </div>
            ''',
            unsafe_allow_html=True
        )

        st.link_button(
            "View project ↗",
            project["url"]
        )


# ============================================================
# BLOGS / WHAT I'M UP TO
# ============================================================

st.header("What I'm up to")

for blog in st.session_state.blogs:
    st.markdown(
        f"""
        <div class="card">
            <small>{blog['date']}</small>
            <h3>{blog['title']}</h3>
            <p>{blog['excerpt']}</p>
            <small>{' · '.join(blog['tags'])}</small>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")


# ============================================================
# CONTACT
# ============================================================

st.header("Let's work together")

st.write(
    "If you have a project in mind or just want to say hi, "
    "feel free to reach out!"
)


# Contact buttons
contact1, contact2, contact3, contact4 = st.columns(4)

with contact1:
    st.link_button(
        "Email me",
        f"mailto:{PROFILE['email']}"
    )

with contact2:
    st.link_button(
        "LinkedIn",
        PROFILE["linkedin"]
    )

with contact3:
    st.link_button(
        "Instagram",
        PROFILE["Instagram"]
    )
with contact4:
    st.link_button(
        "Discord",
        PROFILE["discord"]
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    f"© 2026 {PROFILE['name']} · Built with Python and Streamlit"
)