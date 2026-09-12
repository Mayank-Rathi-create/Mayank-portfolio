"""Streamlit portfolio application.

Run with ``streamlit run portfolio.py``.
Keep the requirements minimal: add ``streamlit`` to requirements.txt.
The app is suitable for GitHub and Python hosting.

To update the site after deployment, edit PROFILE or PROJECTS, commit the
change, and redeploy.
"""

import streamlit as st


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
    background: #0b1020;
    color: #eef2ff;
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
    color: #a5b4fc;
    font-size: 1.1rem;
}

.card {
    background: #151d35;
    border: 1px solid #29365c;
    border-radius: 16px;
    padding: 1.3rem;
    min-height: 180px;
    margin-bottom: .8rem;
}

a {
    color: #93c5fd !important;
}

/* Profile buttons */
div[data-testid="stLinkButton"] a {
    border-radius: 12px;
    font-weight: 600;
    padding: 0.6rem 1rem;
    width: 100%;
    text-align: center;
}

div[data-testid="stLinkButton"] a:hover {
    transform: translateY(-2px);
    transition: 0.2s ease;
}
</style>
""",
unsafe_allow_html=True
)


# Edit this single data section to update the deployed portfolio
PROFILE = {
    "name": "Mayank Rathi",
    "role": "Python developer and product-minded problem solver",
    "bio": "I build useful and playful digital products with Python, data, and thoughtful design.",
    "email": "mayankrathinp@gmail.com",
    "github": "https://github.com/Mayank-Rathi-create",
    "linkedin": "https://www.linkedin.com/in/mayank-rathi-555007427/",
    "Instagram": "https://www.instagram.com/mayankrathi_/",
    "discord": "mayankrathi0719",
}

PROJECTS = [
    {
        "title": "Number guessing game",
        "description": "A fun and interactive game to test your number prediction skills.",
        "stack": "Python",
        "url": "https://github.com/Mayank-Rathi-create/number_guess.git"
    },
    {
        "title": "Working on more projects",
        "description": "Exploring new ideas and technologies.",
        "stack": "Python, java, C",
        "url": "https://github.com/Mayank-Rathi-create/"
    }
]


if "projects" not in st.session_state:
    st.session_state.projects = [project.copy() for project in PROJECTS]


# ============================================================
# HERO SECTION
# ============================================================

st.markdown('<div class="hero">', unsafe_allow_html=True)

st.caption("PORTFOLIO / 2026")

st.markdown(f"# Hi, I’m {PROFILE['name']}.")

st.markdown(f"### {PROFILE['role']}")

st.write(PROFILE["bio"])

st.write("Get in touch or explore my work below.")


# Profile buttons
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.link_button(
        "📧 Email",
        f"mailto:{PROFILE['email']}"
    )

with col2:
    st.link_button(
        "GitHub",
        PROFILE["github"]
    )

with col3:
    st.link_button(
        "🔗 LinkedIn",
        PROFILE["linkedin"]
    )

with col4:
    st.link_button(
        "Instagram",
        PROFILE["Instagram"]
    )


st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# ABOUT
# ============================================================

st.header("About me")

st.write(PROFILE["bio"])

st.write(
    "**Focus areas:** Python · Streamlit · APIs · Data visualization · "
    "UX · Clean architecture · vibe coding · problem solving · teamwork"
)


# ============================================================
# SELECTED WORK
# ============================================================

st.header("Projects : ")

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
# CONTACT
# ============================================================

st.header("Let's work together")

st.write(
    "If you have a project in mind or just want to say hi, "
    "feel free to reach out!"
)


# Contact buttons
contact1, contact2, contact3 = st.columns(3)

with contact1:
    st.link_button(
        "📧 Email me",
        f"mailto:{PROFILE['email']}"
    )

with contact2:
    st.link_button(
        "🔗 LinkedIn",
        PROFILE["linkedin"]
    )

with contact3:
    st.link_button(
        "Instagram",
        PROFILE["Instagram"]
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    f"© 2026 {PROFILE['name']} · Built with Python and Streamlit"
)