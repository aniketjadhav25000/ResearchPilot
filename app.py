import streamlit as st
import streamlit.components.v1 as components
from pipeline import run_research_pipeline


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchPilot",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# SESSION STATE
# ============================================================

if "result" not in st.session_state:
    st.session_state.result = None

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "researching" not in st.session_state:
    st.session_state.researching = False

if "history" not in st.session_state:
    st.session_state.history = []


# ============================================================
# GLOBAL CSS
# OCEAN BLUE + EMERALD THEME
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       COLOR THEME
       Ocean Blue + Emerald
       ======================================================== */

    :root {
        --bg: #050B14;
        --bg-2: #07111D;

        --card: #0B1422;
        --card-2: #101B2C;

        --border: #1D3045;
        --border-hover: #2C4963;

        --text: #F1F5F9;
        --text-2: #94A3B8;
        --text-3: #64748B;

        --blue: #0EA5E9;
        --blue-light: #38BDF8;
        --blue-dark: #0284C7;

        --emerald: #10B981;
        --emerald-light: #34D399;
        --emerald-dark: #059669;

        --cyan: #67E8F9;
    }


    /* ========================================================
       GLOBAL
       ======================================================== */

    html,
    body {
        margin: 0;
        padding: 0;
        background: var(--bg);
    }

    .stApp {
        min-height: 100vh;

        background:
            radial-gradient(
                circle at 8% -10%,
                rgba(14, 165, 233, 0.11),
                transparent 30%
            ),

            radial-gradient(
                circle at 94% 10%,
                rgba(16, 185, 129, 0.08),
                transparent 28%
            ),

            radial-gradient(
                circle at 50% 110%,
                rgba(14, 165, 233, 0.045),
                transparent 32%
            ),

            var(--bg);
    }

    .block-container {
        max-width: 1180px;
        padding: 0.45rem 2.5rem 2.5rem;
    }

    #MainMenu,
    header,
    footer {
        visibility: hidden;
    }

    html,
    body,
    [class*="css"] {
        font-family:
            "Manrope",
            sans-serif;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        padding: 1.15rem 0 1.05rem;
    }

    .hero-top {
        display: flex;
        align-items: center;
        gap: 9px;
        margin-bottom: 11px;
    }

    .hero-dot {
        width: 7px;
        height: 7px;
        flex-shrink: 0;

        border-radius: 50%;

        background: var(--blue);

        box-shadow:
            0 0 15px
            rgba(14, 165, 233, 0.9);
    }

    .hero-label {
        font-family:
            "Space Mono",
            monospace;

        font-size: 10px;
        font-weight: 700;

        letter-spacing: 0.16em;
        text-transform: uppercase;

        color: #71839A;
    }

    .hero h1 {
        margin: 0;

        font-size:
            clamp(3.2rem, 6vw, 5rem);

        line-height: 0.95;
        letter-spacing: -0.055em;

        font-weight: 800;

        color: var(--text);
    }

    .hero-accent {
        background:
            linear-gradient(
                135deg,
                var(--blue),
                var(--emerald)
            );

        -webkit-background-clip: text;
        background-clip: text;

        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        max-width: 680px;

        margin-top: 13px;

        color: var(--text-2);

        font-size: 14px;
        font-weight: 500;

        line-height: 1.65;
    }


    /* ========================================================
       DIVIDER
       ======================================================== */

    .top-line {
        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(14, 165, 233, 0.30),
                rgba(16, 185, 129, 0.20),
                transparent
            );

        margin-bottom: 23px;
    }


    /* ========================================================
       SECTION LABEL
       ======================================================== */

    .workspace-title {
        font-family:
            "Space Mono",
            monospace;

        font-size: 10px;
        font-weight: 700;

        letter-spacing: 0.16em;
        text-transform: uppercase;

        color: #687B91;

        margin-bottom: 8px;
    }


    /* ========================================================
       INPUT AREA
       ======================================================== */

    .input-shell {
        background:
            linear-gradient(
                145deg,
                rgba(11, 20, 34, 0.98),
                rgba(6, 14, 24, 0.98)
            );

        border:
            1px solid var(--border);

        border-radius: 14px;

        padding: 18px;

        box-shadow:
            0 15px 40px
            rgba(0, 0, 0, 0.22);
    }

    .input-shell:hover {
        border-color:
            var(--border-hover);
    }


    /* ========================================================
       TEXT INPUT
       ======================================================== */

    .stTextInput > label {
        font-family:
            "Space Mono",
            monospace !important;

        font-size: 10px !important;
        font-weight: 700 !important;

        letter-spacing: 0.14em !important;
        text-transform: uppercase !important;

        color:
            var(--blue-light) !important;
    }

    .stTextInput input {
        background:
            #060D17 !important;

        border:
            1px solid
            #20354B !important;

        border-radius:
            9px !important;

        color:
            var(--text) !important;

        font-family:
            "Manrope",
            sans-serif !important;

        font-size:
            14px !important;

        font-weight:
            500 !important;

        min-height:
            42px !important;

        transition:
            all 0.2s ease !important;
    }

    .stTextInput input::placeholder {
        color:
            #586B80 !important;
    }

    .stTextInput input:focus {
        border-color:
            var(--blue) !important;

        box-shadow:
            0 0 0 2px
            rgba(14, 165, 233, 0.12) !important;
    }


    /* ========================================================
       BUTTON BASE
       ======================================================== */

    div[data-testid="stButton"] button {
        min-height:
            42px !important;

        border-radius:
            9px !important;

        font-family:
            "Manrope",
            sans-serif !important;

        font-size:
            13px !important;

        font-weight:
            700 !important;

        transition:
            all 0.2s ease !important;
    }


    /* ========================================================
       START RESEARCH BUTTON
       ======================================================== */

    .research-button button {
        width:
            100% !important;

        background:
            linear-gradient(
                135deg,
                #0EA5E9,
                #10B981
            ) !important;

        border:
            none !important;

        color:
            #FFFFFF !important;

        box-shadow:
            0 8px 25px
            rgba(14, 165, 233, 0.22) !important;
    }

    .research-button button:hover {
        background:
            linear-gradient(
                135deg,
                #38BDF8,
                #34D399
            ) !important;

        transform:
            translateY(-1px);

        box-shadow:
            0 11px 30px
            rgba(14, 165, 233, 0.32) !important;
    }


    /* ========================================================
       RESEARCHING BUTTON
       ======================================================== */

    .researching-button button {
        width:
            100% !important;

        background:
            linear-gradient(
                135deg,
                #087DB5,
                #07855F
            ) !important;

        border:
            1px solid
            rgba(103, 232, 249, 0.15) !important;

        color:
            #E6F9FF !important;

        cursor:
            wait !important;

        opacity:
            0.96 !important;

        box-shadow:
            0 8px 25px
            rgba(14, 165, 233, 0.18) !important;
    }

    .researching-button button:hover {
        transform:
            none !important;
    }


    /* ========================================================
       SUGGESTED TOPICS
       ======================================================== */

    .examples-label {
        font-family:
            "Space Mono",
            monospace;

        font-size: 9px;
        font-weight: 700;

        color: #596B80;

        letter-spacing: 0.11em;

        margin-top: 11px;
        margin-bottom: 7px;
    }

    .example-btn button {
        min-height:
            32px !important;

        font-size:
            10px !important;

        font-weight:
            500 !important;

        background:
            #09121E !important;

        border:
            1px solid
            #1D3045 !important;

        color:
            #74869A !important;

        box-shadow:
            none !important;
    }

    .example-btn button:hover {
        color:
            var(--blue-light) !important;

        border-color:
            #31516C !important;

        background:
            #0D1927 !important;

        transform:
            none !important;
    }


    /* ========================================================
       PIPELINE
       ======================================================== */

    .pipeline {
        padding-left: 3px;
    }

    .pipeline-heading {
        display:
            flex;

        align-items:
            center;

        justify-content:
            space-between;

        margin-bottom:
            10px;
    }

    .pipeline-title {
        color:
            #E6EDF4;

        font-size:
            19px;

        font-weight:
            800;
    }

    .pipeline-count {
        font-family:
            "Space Mono",
            monospace;

        font-size:
            9px;

        font-weight:
            700;

        color:
            #5E7187;

        letter-spacing:
            0.08em;
    }


    /* ========================================================
       AGENT CARD
       ======================================================== */

    .agent {
        position:
            relative;

        padding:
            13px 16px 13px 20px;

        background:
            linear-gradient(
                145deg,
                #0B1523,
                #080F19
            );

        border:
            1px solid
            #1D3045;

        border-radius:
            11px;

        margin-bottom:
            7px;

        transition:
            all 0.2s ease;
    }

    .agent:hover {
        border-color:
            #31506A;

        background:
            #0D1827;
    }

    .agent::before {
        content:
            "";

        position:
            absolute;

        left:
            0;

        top:
            9px;

        bottom:
            9px;

        width:
            2px;

        background:
            linear-gradient(
                180deg,
                var(--blue),
                var(--emerald)
            );

        border-radius:
            2px;
    }

    .agent-header {
        display:
            flex;

        align-items:
            center;

        gap:
            9px;
    }

    .agent-number {
        font-family:
            "Space Mono",
            monospace;

        font-size:
            10px;

        font-weight:
            700;

        color:
            var(--blue-light);
    }

    .agent-name {
        color:
            #DCE6EE;

        font-size:
            13px;

        font-weight:
            750;
    }

    .agent-status {
        margin-left:
            auto;

        font-family:
            "Space Mono",
            monospace;

        font-size:
            8px;

        font-weight:
            700;

        letter-spacing:
            0.08em;

        color:
            #53677D;
    }

    .agent-description {
        margin-top:
            5px;

        color:
            #708399;

        font-size:
            10px;

        font-weight:
            500;

        line-height:
            1.45;
    }


    /* ========================================================
       RESULTS HEADER
       ======================================================== */

    .results-header {
        display:
            flex;

        align-items:
            flex-end;

        justify-content:
            space-between;

        margin-top:
            38px;

        margin-bottom:
            18px;

        padding-top:
            10px;

        scroll-margin-top:
            20px;
    }

    .results-title {
        font-size:
            32px;

        font-weight:
            850;

        letter-spacing:
            -0.035em;

        color:
            #F1F7FB;
    }

    .results-subtitle {
        color:
            #73869B;

        font-size:
            12px;

        font-weight:
            500;

        margin-top:
            6px;
    }

    .results-tag {
        font-family:
            "Space Mono",
            monospace;

        font-size:
            9px;

        font-weight:
            700;

        color:
            var(--emerald-light);

        border:
            1px solid
            rgba(16, 185, 129, 0.25);

        background:
            rgba(16, 185, 129, 0.06);

        border-radius:
            999px;

        padding:
            6px 10px;
    }


    /* ========================================================
       TABS
       ======================================================== */

    button[data-baseweb="tab"] {
        color:
            #687B90 !important;

        font-size:
            13px !important;

        font-weight:
            750 !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color:
            var(--blue-light) !important;
    }


    /* ========================================================
       REPORT CARD
       ======================================================== */

    .report-box {
        margin-top:
            18px;

        padding:
            27px 30px;

        background:
            linear-gradient(
                145deg,
                #0B1523,
                #080F19
            );

        border:
            1px solid
            #20354A;

        border-radius:
            15px;

        box-shadow:
            0 18px 50px
            rgba(0, 0, 0, 0.18);
    }

    .report-label {
        font-family:
            "Space Mono",
            monospace;

        font-size:
            13px;

        font-weight:
            700;

        letter-spacing:
            0.13em;

        color:
            var(--blue-light);

        text-transform:
            uppercase;

        padding-bottom:
            14px;

        margin-bottom:
            22px;

        border-bottom:
            1px solid
            #1E3347;
    }


    /* ========================================================
       GENERATED MARKDOWN
       ======================================================== */

    .stMarkdown {
        color:
            #D1DCE5;
    }

    .stMarkdown p {
        font-size:
            16px;

        font-weight:
            500;

        line-height:
            1.82;

        color:
            #D0DBE4;
    }

    .stMarkdown strong {
        font-weight:
            800;

        color:
            #F0F6FA;
    }

    .stMarkdown h1 {
        font-size:
            36px;

        font-weight:
            850;

        line-height:
            1.18;

        letter-spacing:
            -0.035em;

        color:
            #F2F8FC;

        margin-top:
            30px;

        margin-bottom:
            14px;

        padding-bottom:
            10px;

        border-bottom:
            1px solid
            #21374A;
    }

    .stMarkdown h2 {
        font-size:
            29px;

        font-weight:
            850;

        line-height:
            1.25;

        letter-spacing:
            -0.025em;

        color:
            #EAF4FA;

        margin-top:
            30px;

        margin-bottom:
            12px;
    }

    .stMarkdown h3 {
        font-size:
            23px;

        font-weight:
            800;

        line-height:
            1.3;

        color:
            var(--blue-light);

        margin-top:
            25px;

        margin-bottom:
            10px;
    }

    .stMarkdown h4 {
        font-size:
            19px;

        font-weight:
            800;

        color:
            var(--emerald-light);

        margin-top:
            20px;

        margin-bottom:
            8px;
    }

    .stMarkdown li {
        font-size:
            15px;

        font-weight:
            500;

        line-height:
            1.75;

        color:
            #C5D1DB;

        margin-bottom:
            6px;
    }

    .stMarkdown blockquote {
        border-left:
            3px solid
            var(--blue);

        padding:
            10px 18px;

        background:
            rgba(14, 165, 233, 0.045);

        color:
            #B8C7D3;
    }

    .stMarkdown code {
        color:
            var(--cyan);

        background:
            #111D2B;

        border-radius:
            5px;

        padding:
            2px 6px;
    }

    .stMarkdown hr {
        border:
            none;

        border-top:
            1px solid
            #213445;

        margin:
            28px 0;
    }


    /* ========================================================
       REVIEW
       ======================================================== */

    .review-box {
        margin-top:
            18px;

        padding:
            25px;

        background:
            #0B1523;

        border:
            1px solid
            rgba(16, 185, 129, 0.18);

        border-radius:
            15px;
    }

    .review-label {
        font-family:
            "Space Mono",
            monospace;

        font-size:
            13px;

        font-weight:
            700;

        letter-spacing:
            0.13em;

        color:
            var(--emerald-light);

        text-transform:
            uppercase;

        padding-bottom:
            14px;

        margin-bottom:
            20px;

        border-bottom:
            1px solid
            rgba(16, 185, 129, 0.13);
    }


    /* ========================================================
       DOWNLOAD BUTTON
       ======================================================== */

    [data-testid="stDownloadButton"] button {
        width:
            auto !important;

        min-width:
            150px;

        background:
            #0D1927 !important;

        border:
            1px solid
            #294158 !important;

        color:
            #BFCED9 !important;

        font-size:
            12px !important;

        box-shadow:
            none !important;
    }

    [data-testid="stDownloadButton"] button:hover {
        background:
            #122336 !important;

        border-color:
            var(--blue) !important;

        color:
            #DFF5FF !important;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        margin-top:
            45px;

        padding-top:
            16px;

        border-top:
            1px solid
            #142334;

        text-align:
            center;

        font-family:
            "Space Mono",
            monospace;

        font-size:
            9px;

        font-weight:
            700;

        color:
            #465B70;

        letter-spacing:
            0.08em;
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .block-container {
            max-width:
                100%;

            padding:
                0.7rem 1rem 2rem;
        }

        .hero {
            padding:
                1rem 0 1.15rem;
        }

        .hero-label {
            font-size:
                9px;
        }

        .hero h1 {
            font-size:
                3rem;

            line-height:
                0.98;
        }

        .hero-description {
            font-size:
                13px;

            line-height:
                1.65;
        }

        .input-shell {
            padding:
                16px;

            border-radius:
                13px;
        }

        .stTextInput input {
            min-height:
                46px !important;

            font-size:
                16px !important;
        }

        div[data-testid="stButton"] button {
            min-height:
                46px !important;
        }

        .pipeline {
            padding-left:
                0;

            margin-top:
                24px;
        }

        .pipeline-title {
            font-size:
                18px;
        }

        .agent {
            padding:
                14px 15px 14px 19px;
        }

        .results-header {
            margin-top:
                28px;

            align-items:
                flex-start;

            flex-direction:
                column;

            gap:
                10px;
        }

        .results-title {
            font-size:
                27px;
        }

        .report-box {
            padding:
                21px 17px;
        }

        .report-label {
            font-size:
                11px;
        }

        .stMarkdown p {
            font-size:
                14px;

            line-height:
                1.8;
        }

        .stMarkdown h1 {
            font-size:
                29px;
        }

        .stMarkdown h2 {
            font-size:
                24px;
        }

        .stMarkdown h3 {
            font-size:
                20px;
        }

        .stMarkdown h4 {
            font-size:
                17px;
        }

        .stMarkdown li {
            font-size:
                13px;
        }

        button[data-baseweb="tab"] {
            font-size:
                11px !important;

            padding-left:
                7px !important;

            padding-right:
                7px !important;
        }

        [data-testid="stDownloadButton"] button {
            width:
                100% !important;

            min-width:
                0;

            min-height:
                44px !important;
        }
    }


    /* ========================================================
       SMALL MOBILE
       ======================================================== */

    @media (max-width: 480px) {

        .block-container {
            padding:
                0.5rem 0.8rem 1.5rem;
        }

        .hero h1 {
            font-size:
                2.65rem;
        }

        .hero-description {
            font-size:
                12px;
        }

        .input-shell {
            padding:
                14px;
        }

        .results-title {
            font-size:
                24px;
        }

        .stMarkdown h1 {
            font-size:
                26px;
        }

        .stMarkdown h2 {
            font-size:
                22px;
        }

        .stMarkdown h3 {
            font-size:
                19px;
        }
    }

    </style>
    """
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-top">

            <div class="hero-dot"></div>

            <div class="hero-label">
                Multi-Agent Intelligence
            </div>

        </div>

        <h1>
            Research<span class="hero-accent">Pilot</span>
        </h1>

        <div class="hero-description">
            Research complex topics through a coordinated
            pipeline of specialized AI agents — from web
            discovery to final quality review.
        </div>

    </div>

    <div class="top-line"></div>
    """
)


# ============================================================
# MAIN LAYOUT
# ============================================================

input_col, pipeline_col = st.columns(
    [1.05, 0.95],
    gap="large",
)


# ============================================================
# RESEARCH WORKSPACE
# ============================================================

with input_col:

    st.html(
        """
        <div class="workspace-title">
            Research Workspace
        </div>

        <div class="input-shell">
        """
    )


    # --------------------------------------------------------
    # TOPIC INPUT
    # --------------------------------------------------------

    topic = st.text_input(
        "Research Topic",
        value=st.session_state.topic,
        placeholder="Enter a topic you want to investigate...",
        label_visibility="visible",
        disabled=st.session_state.researching,
    )

    st.session_state.topic = topic


    # --------------------------------------------------------
    # RESEARCH BUTTON
    # --------------------------------------------------------

    if st.session_state.researching:

        st.html(
            '<div class="researching-button">'
        )

        st.button(
            "Researching...",
            use_container_width=True,
            disabled=True,
            key="researching_button",
        )

        st.html(
            "</div>"
        )

        run = False

    else:

        st.html(
            '<div class="research-button">'
        )

        run = st.button(
            "Start Research  →",
            type="primary",
            use_container_width=True,
            key="start_research",
        )

        st.html(
            "</div>"
        )


    st.html(
        """
        </div>

        <div class="examples-label">
            SUGGESTED TOPICS
        </div>
        """
    )


    # --------------------------------------------------------
    # SUGGESTED TOPICS
    # --------------------------------------------------------

    ex1, ex2, ex3 = st.columns(3)

    examples = [
        "AI agents in 2026",
        "Quantum computing",
        "Fusion energy",
    ]


    for col, example, index in zip(
        [ex1, ex2, ex3],
        examples,
        range(3),
    ):

        with col:

            st.html(
                '<div class="example-btn">'
            )

            clicked = st.button(
                example,
                key=f"example_{index}",
                use_container_width=True,
                disabled=st.session_state.researching,
            )

            st.html(
                "</div>"
            )


            if clicked:

                st.session_state.topic = example

                st.rerun()


# ============================================================
# AGENT PIPELINE
# ============================================================

with pipeline_col:

    st.html(
        """
        <div class="pipeline">

            <div class="pipeline-heading">

                <div class="pipeline-title">
                    Agent Pipeline
                </div>

                <div class="pipeline-count">
                    04 AGENTS
                </div>

            </div>


            <div class="agent">

                <div class="agent-header">

                    <div class="agent-number">
                        01
                    </div>

                    <div class="agent-name">
                        Search Agent
                    </div>

                    <div class="agent-status">
                        READY
                    </div>

                </div>

                <div class="agent-description">
                    Discovers recent and reliable web sources.
                </div>

            </div>


            <div class="agent">

                <div class="agent-header">

                    <div class="agent-number">
                        02
                    </div>

                    <div class="agent-name">
                        Reader Agent
                    </div>

                    <div class="agent-status">
                        READY
                    </div>

                </div>

                <div class="agent-description">
                    Selects and extracts deeper source content.
                </div>

            </div>


            <div class="agent">

                <div class="agent-header">

                    <div class="agent-number">
                        03
                    </div>

                    <div class="agent-name">
                        Writer Chain
                    </div>

                    <div class="agent-status">
                        READY
                    </div>

                </div>

                <div class="agent-description">
                    Converts research into a structured report.
                </div>

            </div>


            <div class="agent">

                <div class="agent-header">

                    <div class="agent-number">
                        04
                    </div>

                    <div class="agent-name">
                        Critic Chain
                    </div>

                    <div class="agent-status">
                        READY
                    </div>

                </div>

                <div class="agent-description">
                    Reviews the report for quality and accuracy.
                </div>

            </div>

        </div>
        """
    )


# ============================================================
# START RESEARCH
# ============================================================

if run:

    current_topic = st.session_state.topic.strip()

    if not current_topic:

        st.warning(
            "Please enter a research topic before starting."
        )

    else:

        st.session_state.result = None

        st.session_state.researching = True

        st.rerun()


# ============================================================
# RUN PIPELINE
# ============================================================

if st.session_state.researching:

    current_topic = st.session_state.topic.strip()

    try:

        result = run_research_pipeline(
            current_topic
        )

        st.session_state.result = result

        if current_topic not in st.session_state.history:

            st.session_state.history.append(
                current_topic
            )

        st.session_state.researching = False

        st.rerun()

    except Exception as error:

        st.session_state.researching = False

        st.error(
            "The research pipeline failed."
        )

        with st.expander(
            "Technical details"
        ):

            st.exception(error)


# ============================================================
# GENERATED RESULTS
# ============================================================

if st.session_state.result:

    result = st.session_state.result


    # --------------------------------------------------------
    # RESULT HEADER
    # --------------------------------------------------------

    st.html(
        f"""
        <div
            id="research-results-anchor"
            class="results-header">

            <div>

                <div class="results-title">
                    Research Results
                </div>

                <div class="results-subtitle">
                    {st.session_state.topic}
                </div>

            </div>

            <div class="results-tag">
                COMPLETED
            </div>

        </div>
        """
    )


    # --------------------------------------------------------
    # AUTO SCROLL
    # --------------------------------------------------------

    components.html(
        """
        <script>

        function scrollToResults() {

            try {

                const parentDocument =
                    window.parent.document;

                const target =
                    parentDocument.getElementById(
                        "research-results-anchor"
                    );

                if (target) {

                    target.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });

                    return true;
                }

            } catch (error) {

                console.log(
                    "Scroll error:",
                    error
                );

            }

            return false;
        }


        let attempts = 0;

        const interval =
            setInterval(function () {

                attempts++;

                const success =
                    scrollToResults();

                if (
                    success ||
                    attempts >= 10
                ) {

                    clearInterval(interval);

                }

            }, 200);

        </script>
        """,
        height=0,
    )


    # ========================================================
    # RESULT TABS
    # ========================================================

    report_tab, sources_tab, analysis_tab, review_tab = st.tabs(
        [
            "Report",
            "Sources",
            "Analysis",
            "Review",
        ]
    )


    # ========================================================
    # REPORT
    # ========================================================

    with report_tab:

        report = result.get(
            "report",
            "No report was generated.",
        )

        if hasattr(report, "content"):

            report = report.content

        report = str(report)


        st.html(
            """
            <div class="report-box">

                <div class="report-label">
                    Final Research Report
                </div>

            </div>
            """
        )


        st.markdown(report)


        st.write("")


        st.download_button(
            label="Download Report",
            data=report,
            file_name="researchpilot_report.md",
            mime="text/markdown",
        )


    # ========================================================
    # SOURCES
    # ========================================================

    with sources_tab:

        sources = result.get(
            "search_results",
            "No search results available.",
        )

        if hasattr(sources, "content"):

            sources = sources.content


        st.html(
            """
            <div class="report-box">

                <div class="report-label">
                    Research Sources
                </div>

            </div>
            """
        )


        st.markdown(
            str(sources)
        )


    # ========================================================
    # ANALYSIS
    # ========================================================

    with analysis_tab:

        scraped = result.get(
            "scraped_content",
            "No scraped content available.",
        )

        if hasattr(scraped, "content"):

            scraped = scraped.content


        st.html(
            """
            <div class="report-box">

                <div class="report-label">
                    Deep Source Analysis
                </div>

            </div>
            """
        )


        st.markdown(
            str(scraped)
        )


    # ========================================================
    # REVIEW
    # ========================================================

    with review_tab:

        feedback = result.get(
            "feedback",
            "No critic feedback available.",
        )

        if hasattr(feedback, "content"):

            feedback = feedback.content


        st.html(
            """
            <div class="review-box">

                <div class="review-label">
                    Critic Review
                </div>

            </div>
            """
        )


        st.markdown(
            str(feedback)
        )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">
        RESEARCHPILOT · MULTI-AGENT RESEARCH SYSTEM · STREAMLIT
    </div>
    """
)