import streamlit as st
import streamlit.components.v1 as components
from pipeline import run_research_pipeline
import html


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="ResearchPilot",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SESSION STATE
# ============================================================

st.session_state.setdefault("topic", "")
st.session_state.setdefault("result", None)
st.session_state.setdefault("researching", False)
st.session_state.setdefault("scroll_to_progress", False)


# ============================================================
# GLOBAL CSS
# ============================================================

st.html("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap'
);


/* ============================================================
   GLOBAL
   ============================================================ */

html,
body {
    margin: 0;
    padding: 0;
    background: #050812;
}

.stApp {
    min-height: 100vh;
    background:
        radial-gradient(
            circle at 80% 5%,
            rgba(112,72,235,.14),
            transparent 27%
        ),
        radial-gradient(
            circle at 10% 35%,
            rgba(39,105,190,.05),
            transparent 25%
        ),
        linear-gradient(
            180deg,
            #050812 0%,
            #060a14 100%
        );
    color: #eef1f7;
}

.block-container {
    width: 100%;
    max-width: 1180px;
    padding: 2px 28px 50px;
}

#MainMenu,
header,
footer {
    visibility: hidden;
}

* {
    box-sizing: border-box;
}

button,
input {
    font-family: "DM Sans", sans-serif !important;
}


/* ============================================================
   BRAND
   ============================================================ */

.brand {
    display: flex;
    align-items: center;
    gap: 10px;
    height: 38px;
    margin-bottom: 0px;
    margin-top: 10px;
}

.brand-mark {
    color: #a66aff;
    font-size: 21px;
    text-shadow: 0 0 16px rgba(166,106,255,.65);
}

.brand-name {
    color: #cbd1dc;
    font-family: "Space Grotesk", sans-serif;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: .16em;
    text-transform: uppercase;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    position: relative;
    min-height: 340px;
    overflow: hidden;
    border: 1px solid #1b2538;
    border-radius: 14px;
    margin-top: 14px;
    background:
        radial-gradient(
            circle at 77% 50%,
            rgba(108,65,225,.09),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #0c1220,
            #070c17
        );
}

.hero-copy {
    position: relative;
    z-index: 5;
    width: 56%;
    padding: 28px 42px;
}

.hero-project-name {
    margin: 0 0 14px;
    font-family: "Space Grotesk", sans-serif;
    font-size: clamp(46px, 6vw, 68px);
    font-weight: 700;
    line-height: .98;
    letter-spacing: -.055em;
    white-space: nowrap;
}

.hero-project-name .research {
    color: #a66aff;
}

.hero-project-name .pilot {
    background: linear-gradient(90deg, #d45dc9, #ff806e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-kicker {
    margin-bottom: 16px;
    color: #b078ff;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: .18em;
}

.hero-title {
    margin: 0;
    color: #f3f5f8;
    font-family: "Space Grotesk", sans-serif;
    font-size: clamp(46px, 6vw, 68px);
    font-weight: 700;
    line-height: .98;
    letter-spacing: -.055em;
}

.hero-title .gradient {
    background:
        linear-gradient(
            90deg,
            #9561ff,
            #d45dc9,
            #ff806e
        );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    max-width: 440px;
    margin-top: 21px;
    color: #8994a7;
    font-size: 16px;
    line-height: 1.75;
}


/* ============================================================
   ORBIT
   ============================================================ */

.orbit-area {
    position: absolute;
    top: 0;
    right: 0;
    width: 46%;
    height: 100%;
}

.orbit {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 285px;
    height: 285px;
    border: 1px solid rgba(133,90,255,.18);
    border-radius: 50%;
    transform: translate(-50%,-50%);
}

.orbit-2 {
    width: 218px;
    height: 218px;
    border-color: rgba(134,89,255,.22);
}

.orbit-3 {
    width: 158px;
    height: 158px;
    border-color: rgba(175,92,255,.25);
}

.orbit-4 {
    width: 96px;
    height: 96px;
    border-color: rgba(202,104,255,.30);
}

.orbit-diagonal {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 300px;
    height: 118px;
    border: 1px solid rgba(210,93,200,.28);
    border-radius: 50%;
    transform: translate(-50%,-50%) rotate(-22deg);
}

.core {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 53px;
    height: 53px;
    border-radius: 12px;
    background:
        linear-gradient(
            135deg,
            #9e64ff,
            #6241d1
        );
    box-shadow:
        0 0 36px rgba(122,73,238,.58),
        inset 0 0 16px rgba(255,255,255,.12);
    transform: translate(-50%,-50%) rotate(45deg);
    animation: corePulse 3s ease-in-out infinite;
}

.core::after {
    content: "✦";
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 24px;
    transform: rotate(-45deg);
}

@keyframes corePulse {

    0%,100% {
        transform:
            translate(-50%,-50%)
            rotate(45deg)
            scale(.94);
    }

    50% {
        transform:
            translate(-50%,-50%)
            rotate(45deg)
            scale(1.06);
    }
}

.planet {
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    box-shadow: 0 0 15px currentColor;
}

.planet-1 {
    top: 25%;
    right: 20%;
    color: #ff7187;
    background: #ff7187;
}

.planet-2 {
    right: 22%;
    bottom: 23%;
    color: #ff6685;
    background: #ff6685;
}

.planet-3 {
    top: 30%;
    left: 20%;
    color: #8d6cff;
    background: #8d6cff;
}

.planet-4 {
    bottom: 28%;
    left: 24%;
    color: #b079ff;
    background: #b079ff;
}


/* ============================================================
   RESEARCH WORKSPACE
   ============================================================ */
/*

   IMPORTANT:
   The workspace is now a real Streamlit container:
       st.container(key="workspace")

   This means the title, input and button are actually
   contained inside the same visual card.
*/

.st-key-workspace {
    position: relative;
    z-index: 10;

    margin: -2px 32px 34px 0px !important;
    padding: 22px 24px 24px !important;

    border: 1px solid #49328d;
    border-radius: 11px;

    background:
        linear-gradient(
            145deg,
            #111827,
            #0a111e
        );

    box-shadow:
        0 16px 45px rgba(0,0,0,.30);
}


/* Workspace heading */

.workspace-title {
    display: flex;
    align-items: center;
    gap: 9px;

    margin-bottom: 15px;

    color: #eef1f6;
    font-family: "Space Grotesk", sans-serif;
    font-size: 17px;
    font-weight: 600;
}

.workspace-icon {
    color: #ae70ff;
    font-size: 20px;
}


/* Input */

.stTextInput > label {
    display: none !important;
}

.stTextInput input {
    width: 100% !important;

    height: 50px !important;
    min-height: 50px !important;

    padding: 0 16px !important;

    background: #141c2c !important;

    border: 1px solid #27344a !important;
    border-radius: 8px !important;

    color: #eef1f6 !important;

    font-size: 13px !important;
}

.stTextInput input::placeholder {
    color: #69768b !important;
}

.stTextInput input:focus {
    border-color: #8058e1 !important;

    box-shadow:
        0 0 0 1px rgba(128,88,225,.20),
        0 0 18px rgba(111,69,215,.08) !important;
}


/* Investigate */

.start-button {
    width: 100%;
}

@media(min-width:701px) {
    .st-key-investigate_button {
        width: 100% !important;
        margin-top: 2px !important;
        transform: translateY(-18px);
    }
}

.start-button button {
    width: 100% !important;

    height: 50px !important;
    min-height: 50px !important;

    margin: 0 !important;

    border: none !important;
    border-radius: 8px !important;

    background:
        linear-gradient(
            110deg,
            #6841db,
            #b34bc3,
            #fb786d
        ) !important;

    color: white !important;

    font-size: 12px !important;
    font-weight: 700 !important;

    box-shadow:
        0 8px 24px rgba(109,63,211,.20);

    transition:
        transform .2s ease,
        filter .2s ease;
}

.start-button button:hover {
    filter: brightness(1.09);
    transform: translateY(-1px);
}


/* ============================================================
   PIPELINE
   ============================================================ */

.pipeline-section {
    margin-top: 4px;
}

.pipeline-heading {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
}

.pipeline-heading-left {
    display: flex;
    align-items: center;
    gap: 9px;
}

.pipeline-spark {
    color: #aa6cff;
    font-size: 20px;
}

.pipeline-title {
    color: #eef1f5;
    font-family: "Space Grotesk", sans-serif;
    font-size: 18px;
    font-weight: 600;
}

.pipeline-count {
    padding: 6px 10px;

    border: 1px solid #263249;
    border-radius: 999px;

    background: #0d1524;

    color: #8793a6;

    font-size: 9px;
    font-weight: 600;
}

.pipeline-subtitle {
    margin-bottom: 14px;

    color: #718096;
    font-size: 10px;
}

.pipeline-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
}

.pipeline-card {
    position: relative;

    min-height: 142px;
    padding: 16px;

    overflow: hidden;

    border: 1px solid #242f43;
    border-radius: 10px;

    background:
        linear-gradient(
            145deg,
            #101827,
            #0b1220
        );
}

.pipeline-card::after {
    content: "";

    position: absolute;
    right: -30px;
    bottom: -30px;

    width: 90px;
    height: 90px;

    border-radius: 50%;

    background: rgba(116,67,220,.06);

    filter: blur(18px);
}

.pipeline-icon {
    width: 38px;
    height: 38px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-bottom: 12px;

    border-radius: 50%;

    background: rgba(119,70,221,.12);

    color: #b274ff;

    font-size: 16px;
}

.pipeline-card:nth-child(2) .pipeline-icon {
    background: rgba(65,121,219,.11);
    color: #64a4ff;
}

.pipeline-card:nth-child(3) .pipeline-icon {
    background: rgba(57,177,112,.10);
    color: #55d995;
}

.pipeline-card:nth-child(4) .pipeline-icon {
    background: rgba(224,73,119,.10);
    color: #ff7199;
}

.pipeline-number {
    position: absolute;
    top: 16px;
    right: 16px;

    color: #66738a;
    font-size: 9px;
}

.pipeline-name {
    color: #edf0f5;
    font-size: 12px;
    font-weight: 700;
}

.pipeline-description {
    max-width: 190px;
    margin-top: 7px;

    color: #78859a;

    font-size: 9px;
    line-height: 1.55;
}


/* ============================================================
   RESEARCH PROGRESS
   ============================================================ */

.progress-anchor {
    scroll-margin-top: 20px;
}

.loading-card {
    margin: 28px 32px 32px;

    padding: 29px;

    border: 1px solid #503695;
    border-radius: 11px;

    background:
        radial-gradient(
            circle at 20% 50%,
            rgba(109,62,220,.11),
            transparent 31%
        ),
        #0b1220;

    box-shadow:
        0 15px 45px rgba(0,0,0,.24);
}

.loading-layout {
    display: grid;
    grid-template-columns: 36% 64%;
    align-items: center;
}

.loading-visual {
    position: relative;

    width: 200px;
    height: 125px;

    margin: auto;
}

.loading-ring {
    position: absolute;

    top: 50%;
    left: 50%;

    width: 190px;
    height: 55px;

    border: 1px solid rgba(147,100,255,.35);
    border-radius: 50%;

    transform:
        translate(-50%,-50%)
        rotate(-8deg);
}

.loading-ring.two {
    width: 150px;
    height: 43px;

    border-color: rgba(198,94,230,.32);
}

.loading-ring.three {
    width: 110px;
    height: 32px;

    border-color: rgba(105,106,246,.36);
}

.loading-core {
    position: absolute;

    top: 50%;
    left: 50%;

    width: 29px;
    height: 29px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle at 35% 30%,
            #e7c9ff,
            #a35eff 45%,
            #5732be
        );

    box-shadow:
        0 0 28px rgba(156,88,255,.65);

    transform:
        translate(-50%,-50%);

    animation:
        loadingCore 1.5s ease-in-out infinite;
}

@keyframes loadingCore {

    0%,100% {
        transform:
            translate(-50%,-50%)
            scale(.85);
    }

    50% {
        transform:
            translate(-50%,-50%)
            scale(1.1);
    }
}

.loading-dot {
    position: absolute;

    width: 6px;
    height: 6px;

    border-radius: 50%;

    background: #9870ff;

    box-shadow:
        0 0 10px #9870ff;

    animation:
        loadingDot 2s ease-in-out infinite;
}

.loading-dot.one {
    top: 18px;
    left: 28px;
}

.loading-dot.two {
    right: 19px;
    bottom: 25px;

    background: #ff718f;

    box-shadow:
        0 0 10px #ff718f;

    animation-delay: .5s;
}

.loading-dot.three {
    top: 50px;
    right: 7px;

    animation-delay: 1s;
}

@keyframes loadingDot {

    50% {
        transform: translateY(-8px);
        opacity: .45;
    }
}

.loading-title {
    display: flex;
    align-items: center;
    gap: 8px;

    color: #f0f2f6;

    font-size: 17px;
    font-weight: 700;
}

.loading-title-icon {
    color: #b36aff;
}

.loading-topic {
    margin-top: 6px;

    color: #78859a;
    font-size: 10px;
}

.loading-steps {
    margin-top: 18px;
}

.loading-step {
    display: flex;
    align-items: center;
    gap: 9px;

    margin-bottom: 9px;

    color: #818da0;

    font-size: 10px;
}

.loading-step-dot {
    width: 17px;
    height: 17px;

    display: flex;
    align-items: center;
    justify-content: center;

    border: 1px solid #4c3a7c;
    border-radius: 50%;

    color: #aa77ff;

    font-size: 8px;
}

.loading-step.active {
    color: #c6ccd6;
}

.loading-step.active .loading-step-dot {
    background: #6948c1;

    box-shadow:
        0 0 10px rgba(124,78,223,.4);
}

.progress {
    height: 5px;

    margin-top: 15px;

    overflow: hidden;

    border-radius: 99px;

    background: #1b2537;
}

.progress-bar {
    width: 50%;
    height: 100%;

    background:
        linear-gradient(
            90deg,
            #7445dc,
            #b75ac7,
            #ff7b82
        );

    animation:
        progressMove 1.7s ease-in-out infinite;
}

@keyframes progressMove {

    0% {
        transform: translateX(-110%);
    }

    50% {
        transform: translateX(70%);
    }

    100% {
        transform: translateX(210%);
    }
}


/* ============================================================
   RESULTS
   ============================================================ */

.results {
    margin: 42px 32px 0;
    scroll-margin-top: 20px;
}

.results-header {
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 15px;
}

.results-left {
    display: flex;
    align-items: center;
    gap: 10px;
}

.results-icon {
    color: #ae6cff;
    font-size: 22px;
}

.results-title {
    color: #eef0f5;

    font-family: "Space Grotesk", sans-serif;

    font-size: 19px;
    font-weight: 700;
}

.results-subtitle {
    margin-top: 4px;

    color: #707d92;

    font-size: 10px;
}

.completed {
    display: flex;
    align-items: center;
    gap: 6px;

    padding: 7px 10px;

    border: 1px solid rgba(63,181,126,.18);
    border-radius: 999px;

    background: rgba(48,160,107,.07);

    color: #4ed497;

    font-size: 8px;
}

.completed-dot {
    width: 6px;
    height: 6px;

    border-radius: 50%;

    background: #42d28d;
}


/* ============================================================
   TABS
   ============================================================ */

.stTabs [data-baseweb="tab-list"] {
    gap: 0;

    border-bottom: 1px solid #202a3d;
}

.stTabs [data-baseweb="tab"] {
    min-height: 40px !important;

    padding: 0 18px !important;

    color: #7c889c !important;

    font-size: 10px !important;
    font-weight: 600 !important;
}

.stTabs [aria-selected="true"] {
    color: #bd7cff !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    height: 2px !important;

    background: #9c5dff !important;
}


/* ============================================================
   REPORT
   ============================================================ */

.report-card {
    margin-top: 15px;

    padding: 23px;

    border: 1px solid #202b3e;
    border-radius: 10px;

    background:
        linear-gradient(
            145deg,
            #101827,
            #0b1220
        );
}

.report-grid {
    display: grid;

    grid-template-columns: 1fr 185px;

    gap: 27px;
}

.report-heading {
    display: flex;
    align-items: center;
    gap: 10px;

    padding-bottom: 14px;

    border-bottom: 1px solid #202a3b;
}

.report-icon {
    width: 36px;
    height: 36px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 8px;

    background: rgba(134,71,220,.16);

    color: #b46cff;

    font-size: 15px;
}

.report-name {
    color: #eef1f5;

    font-size: 14px;
    font-weight: 700;
}

.report-topic {
    margin-top: 3px;

    color: #707c90;

    font-size: 9px;
}

.report-body {
    margin-top: 18px;
}

.report-body p {
    color: #b2bccb !important;

    font-size: 12px !important;

    line-height: 1.8 !important;
}

.report-body h1,
.report-body h2,
.report-body h3 {
    color: #eef1f5 !important;

    font-family: "Space Grotesk", sans-serif !important;
}

.report-body h1 {
    font-size: 25px !important;
}

.report-body h2 {
    margin-top: 27px !important;

    font-size: 19px !important;
}

.report-body h3 {
    font-size: 16px !important;
}

.report-body strong {
    color: #eef1f5 !important;
}

.report-body li {
    color: #b2bccb !important;

    font-size: 11px !important;

    line-height: 1.75 !important;
}

.report-body a {
    color: #b579ff !important;
}


/* ============================================================
   AT A GLANCE
   ============================================================ */

.glance {
    padding-left: 20px;

    border-left: 1px solid #202a3b;
}

.glance-title {
    margin-bottom: 20px;

    color: #e7eaf0;

    font-size: 11px;
    font-weight: 700;
}

.metric {
    display: flex;
    align-items: center;
    gap: 8px;

    margin-bottom: 17px;
}

.metric-icon {
    width: 28px;
    height: 28px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: rgba(127,67,219,.13);

    color: #b36dff;

    font-size: 10px;
}

.metric-value {
    color: #edf0f4;

    font-size: 11px;
    font-weight: 700;
}

.metric-label {
    margin-top: 2px;

    color: #68758a;

    font-size: 8px;
}


/* ============================================================
   CRITIC
   ============================================================ */

.critic-card {
    display: grid;

    grid-template-columns: 1fr 110px;

    gap: 20px;

    align-items: center;

    margin-top: 15px;

    padding: 19px;

    border: 1px solid #202b3e;
    border-radius: 10px;

    background: #0d1524;
}

.critic-main {
    display: flex;
    align-items: flex-start;
    gap: 11px;
}

.critic-icon {
    width: 36px;
    height: 36px;

    flex-shrink: 0;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 8px;

    background: rgba(220,64,113,.11);

    color: #ff6e98;
}

.critic-title {
    color: #edf0f5;

    font-size: 12px;
    font-weight: 700;
}

.critic-description {
    margin-top: 7px;

    color: #aab4c2;

    font-size: 10px;
    line-height: 1.7;
}

.review-score {
    padding-left: 18px;

    border-left: 1px solid #222d40;
}

.review-label {
    color: #707d91;

    font-size: 8px;
}

.review-value {
    margin-top: 5px;

    color: #ff74a2;

    font-size: 22px;
    font-weight: 700;
}


/* ============================================================
   DOWNLOAD
   ============================================================ */

.download-area {
    margin-top: 14px;
}

[data-testid="stDownloadButton"] button {
    min-height: 38px !important;

    border: 1px solid #29364b !important;
    border-radius: 7px !important;

    background: #101a2a !important;

    color: #bdc6d3 !important;

    font-size: 9px !important;
}


/* ============================================================
   NEW RESEARCH
   ============================================================ */

.new-research {
    margin-top: 30px;
}

.new-research button {
    min-height: 39px !important;

    border: 1px solid #28344a !important;
    border-radius: 7px !important;

    background: #0d1524 !important;

    color: #a6b0c0 !important;

    font-size: 10px !important;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    display: flex;
    justify-content: space-between;

    margin: 40px 32px 0;

    padding-top: 18px;

    border-top: 1px solid #151e2d;

    color: #566277;

    font-size: 8px;
}


/* ============================================================
   TABLET
   ============================================================ */

@media(max-width:900px) {

    .hero-copy {
        width: 60%;
    }

    .hero-title {
        font-size: 50px;
    }

    .orbit-area {
        width: 45%;
    }

    .pipeline-grid {
        grid-template-columns: 1fr 1fr;
    }

    .report-grid {
        grid-template-columns: 1fr;
    }

    .glance {
        display: grid;

        grid-template-columns:
            repeat(4,1fr);

        gap: 9px;

        padding: 18px 0 0;

        border-top: 1px solid #202a3b;
        border-left: 0;
    }

    .glance-title {
        grid-column: 1 / -1;

        margin-bottom: 3px;
    }

    .metric {
        margin-bottom: 0;
    }
}


/* ============================================================
   MOBILE
   ============================================================ */

@media(max-width:700px) {

    .block-container {
        padding: 12px 12px 35px !important;
    }

    .brand {
        margin-bottom: 12px;
    }

    .brand-name {
        font-size: 10px;
    }

    .hero {
        min-height: 505px;
    }

    .hero-copy {
        width: 100%;
        padding: 28px 20px;
    }

    .hero-project-name {
        font-size: 43px;
        margin-bottom: 12px;
        white-space: normal;
    }

    .hero-kicker {
        font-size: 9px;
    }

    .hero-title {
        font-size: 43px;
    }

    .hero-description {
        max-width: 330px;
        font-size: 10px;
    }

    .orbit-area {
        top: 205px;
        right: 0;
        width: 100%;
        height: 280px;
    }

    .orbit {
        width: 245px;
        height: 245px;
    }

    .orbit-2 {
        width: 190px;
        height: 190px;
    }

    .orbit-3 {
        width: 140px;
        height: 140px;
    }

    .orbit-4 {
        width: 90px;
        height: 90px;
    }

    .orbit-diagonal {
        width: 270px;
    }


    /* ========================================================
       MOBILE WORKSPACE
       Kept consistent with previous mobile layout.
       ======================================================== */

    .st-key-workspace {
        margin: 0 0 27px !important;
        padding: 15px !important;
    }

    .workspace-title {
        font-size: 15px;
    }

    .stTextInput input {
        min-height: 49px !important;
        font-size: 12px !important;
    }

    .start-button button {
        min-height: 49px !important;

        margin-top: 8px !important;

        font-size: 11px !important;
    }


    .pipeline-title {
        font-size: 16px;
    }

    .pipeline-subtitle {
        font-size: 9px;
    }

    .pipeline-grid {
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }

    .pipeline-card {
        min-height: 125px;
        padding: 13px;
    }

    .pipeline-name {
        font-size: 10px;
    }

    .pipeline-description {
        font-size: 8px;
    }


    .loading-card {
        margin: 24px 0 27px;
        padding: 22px 15px;
    }

    .loading-layout {
        grid-template-columns: 1fr;
    }

    .loading-visual {
        transform: scale(.82);

        margin-top: -10px;
        margin-bottom: -9px;
    }

    .loading-title {
        justify-content: center;
        font-size: 15px;
    }

    .loading-topic {
        text-align: center;
        font-size: 9px;
    }

    .loading-step {
        font-size: 9px;
    }


    .results {
        margin: 31px 0 0;
    }

    .results-title {
        font-size: 16px;
    }

    .results-subtitle {
        font-size: 9px;
    }


    .report-card {
        padding: 16px;
    }

    .report-grid {
        grid-template-columns: 1fr;
    }

    .report-body p {
        font-size: 11px !important;
    }

    .report-body li {
        font-size: 10px !important;
    }


    .glance {
        grid-template-columns: 1fr 1fr;
    }


    .critic-card {
        grid-template-columns: 1fr;
    }

    .review-score {
        padding: 12px 0 0;

        border-top: 1px solid #222d40;
        border-left: 0;
    }


    .footer {
        margin-left: 0;
        margin-right: 0;

        flex-direction: column;

        gap: 7px;
    }
}


/* ============================================================
   SMALL PHONES
   ============================================================ */

@media(max-width:480px) {

    .block-container {
        padding-left: 9px !important;
        padding-right: 9px !important;
    }

    .hero {
        min-height: 485px;
    }

    .hero-copy {
        padding: 25px 16px;
    }

    .hero-project-name {
        font-size: 39px;
        margin-bottom: 10px;
    }

    .hero-title {
        font-size: 39px;
    }

    .hero-description {
        font-size: 9px;
    }

    .orbit-area {
        top: 200px;

        transform: scale(.86);

        transform-origin: center top;
    }


    .pipeline-grid {
        grid-template-columns: 1fr;
    }

    .pipeline-card {
        min-height: 100px;
    }

    .pipeline-description {
        max-width: 280px;

        font-size: 9px;
    }


    .loading-visual {
        transform: scale(.72);
    }


    .stTabs [data-baseweb="tab"] {
        padding: 0 8px !important;
        font-size: 8px !important;
    }

    .completed {
        font-size: 7px;
    }
}

</style>
""")


# ============================================================
# HERO
# ============================================================

st.html("""
<div class="hero">

    <div class="hero-copy">

        <div class="hero-project-name">
            <span class="research">Research</span><span class="pilot">Pilot</span>
        </div>

        <div class="hero-kicker">
            AI-POWERED RESEARCH
        </div>

        <div class="hero-title">
            Explore.<br>
            Understand.<br>
            <span class="gradient">Go Deeper.</span>
        </div>

        <div class="hero-description">
            A multi-agent research system that searches,
            reads, synthesizes and critically reviews
            information to produce a structured report.
        </div>

    </div>


    <div class="orbit-area">

        <div class="orbit"></div>

        <div class="orbit orbit-2"></div>

        <div class="orbit orbit-3"></div>

        <div class="orbit orbit-4"></div>

        <div class="orbit-diagonal"></div>

        <div class="core"></div>

        <div class="planet planet-1"></div>

        <div class="planet planet-2"></div>

        <div class="planet planet-3"></div>

        <div class="planet planet-4"></div>

    </div>

</div>
""")


# ============================================================
# RESEARCH WORKSPACE
# ============================================================

with st.container(key="workspace"):

    st.html("""
    <div class="workspace-title">
        <span class="workspace-icon">✣</span>
        What do you want to research?
    </div>
    """)

    input_col, button_col = st.columns(
        [5, 1.05],
        gap="medium"
    )


    # --------------------------------------------------------
    # TOPIC INPUT
    # --------------------------------------------------------

    with input_col:

        topic = st.text_input(
            "Research Topic",
            value=st.session_state.topic,
            placeholder=(
                "e.g. How will AI agents transform "
                "software development?"
            ),
            label_visibility="collapsed",
            disabled=st.session_state.researching
        )

        st.session_state.topic = topic


    # --------------------------------------------------------
    # INVESTIGATE BUTTON
    # --------------------------------------------------------

    with button_col:

        st.html('<div class="start-button">')

        start = st.button(
            "Investigate →",
            use_container_width=True,
            disabled=st.session_state.researching,
            key="investigate_button"
        )

        st.html("</div>")


# ============================================================
# PIPELINE
# ============================================================

st.html("""
<div class="pipeline-section">

    <div class="pipeline-heading">

        <div class="pipeline-heading-left">

            <div class="pipeline-spark">
                ✣
            </div>

            <div class="pipeline-title">
                Research Pipeline
            </div>

        </div>

        <div class="pipeline-count">
            4 STAGES
        </div>

    </div>


    <div class="pipeline-subtitle">
        Four specialized agents working together
    </div>


    <div class="pipeline-grid">


        <div class="pipeline-card">

            <div class="pipeline-icon">
                ⌕
            </div>

            <div class="pipeline-number">
                01
            </div>

            <div class="pipeline-name">
                Search Agent
            </div>

            <div class="pipeline-description">
                Finds recent and reliable sources from the web.
            </div>

        </div>


        <div class="pipeline-card">

            <div class="pipeline-icon">
                ▣
            </div>

            <div class="pipeline-number">
                02
            </div>

            <div class="pipeline-name">
                Reader Agent
            </div>

            <div class="pipeline-description">
                Selects the most relevant resource and
                extracts deeper content.
            </div>

        </div>


        <div class="pipeline-card">

            <div class="pipeline-icon">
                ✎
            </div>

            <div class="pipeline-number">
                03
            </div>

            <div class="pipeline-name">
                Writer Chain
            </div>

            <div class="pipeline-description">
                Synthesizes the research into a structured report.
            </div>

        </div>


        <div class="pipeline-card">

            <div class="pipeline-icon">
                ♢
            </div>

            <div class="pipeline-number">
                04
            </div>

            <div class="pipeline-name">
                Critic Chain
            </div>

            <div class="pipeline-description">
                Reviews the report and provides critical feedback.
            </div>

        </div>


    </div>

</div>
""")


# ============================================================
# START RESEARCH
# ============================================================

if start:

    current_topic = st.session_state.topic.strip()

    if not current_topic:

        st.warning(
            "Enter a research topic to begin."
        )

    else:

        st.session_state.result = None

        st.session_state.researching = True

        st.session_state.scroll_to_progress = True

        st.rerun()


# ============================================================
# RESEARCH IN PROGRESS
# ============================================================

if st.session_state.researching:

    safe_topic = html.escape(
        st.session_state.topic.strip()
    )


    # --------------------------------------------------------
    # LOADING UI
    # --------------------------------------------------------

    st.html(
        f"""
<div
    id="research-progress"
    class="progress-anchor loading-card"
>

    <div class="loading-layout">


        <div class="loading-visual">

            <div class="loading-ring"></div>

            <div class="loading-ring two"></div>

            <div class="loading-ring three"></div>

            <div class="loading-core"></div>

            <div class="loading-dot one"></div>

            <div class="loading-dot two"></div>

            <div class="loading-dot three"></div>

        </div>


        <div>

            <div class="loading-title">

                <span class="loading-title-icon">
                    ✦
                </span>

                Research in Progress

            </div>


            <div class="loading-topic">
                Investigating: {safe_topic}
            </div>


            <div class="loading-steps">


                <div class="loading-step active">

                    <div class="loading-step-dot">
                        ✓
                    </div>

                    Searching recent and reliable sources

                </div>


                <div class="loading-step active">

                    <div class="loading-step-dot">
                        ✓
                    </div>

                    Reading and extracting useful information

                </div>


                <div class="loading-step active">

                    <div class="loading-step-dot">
                        ◌
                    </div>

                    Synthesizing the research report

                </div>


                <div class="loading-step active">

                    <div class="loading-step-dot">
                        ◌
                    </div>

                    Critically reviewing the final report

                </div>


            </div>


            <div class="progress">

                <div class="progress-bar"></div>

            </div>


        </div>

    </div>

</div>
"""
    )


    # ========================================================
    # SMOOTH SCROLL TO RESEARCH PROGRESS
    # ========================================================

    if st.session_state.scroll_to_progress:

        components.html(
            """
<script>

(function () {

    let attempts = 0;

    const timer = setInterval(function () {

        attempts++;

        try {

            const doc =
                window.parent.document;

            const target =
                doc.getElementById(
                    "research-progress"
                );

            if (target) {

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

                clearInterval(timer);
            }

        } catch (error) {
            console.log(error);
        }

        if (attempts >= 25) {
            clearInterval(timer);
        }

    }, 120);

})();

</script>
""",
            height=0
        )

        st.session_state.scroll_to_progress = False


    # ========================================================
    # RUN EXISTING PIPELINE
    # ========================================================

    try:

        result = run_research_pipeline(
            st.session_state.topic.strip()
        )

        st.session_state.result = result

        st.session_state.researching = False

        st.rerun()


    except Exception as error:

        st.session_state.researching = False

        st.error(
            "The research pipeline encountered an error."
        )

        with st.expander("Technical details"):

            st.exception(error)


# ============================================================
# RESULTS
# ============================================================

if st.session_state.result:

    result = st.session_state.result

    current_topic = st.session_state.topic.strip()

    safe_topic = html.escape(
        current_topic
    )


    # ========================================================
    # RESULTS HEADER
    # ========================================================

    st.html(
        f"""
<div
    id="research-results"
    class="results"
>

    <div class="results-header">

        <div class="results-left">

            <div class="results-icon">
                ▤
            </div>

            <div>

                <div class="results-title">
                    Research Results
                </div>

                <div class="results-subtitle">
                    Your comprehensive research report
                </div>

            </div>

        </div>


        <div class="completed">

            <div class="completed-dot"></div>

            Completed

        </div>

    </div>

</div>
"""
    )


    # ========================================================
    # AUTO SCROLL TO RESULTS
    # ========================================================

    components.html(
        """
<script>

(function () {

    let attempts = 0;

    const timer = setInterval(function () {

        attempts++;

        try {

            const doc =
                window.parent.document;

            const target =
                doc.getElementById(
                    "research-results"
                );

            if (target) {

                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });

                clearInterval(timer);
            }

        } catch (error) {
            console.log(error);
        }

        if (attempts >= 25) {
            clearInterval(timer);
        }

    }, 120);

})();

</script>
""",
        height=0
    )


    # ========================================================
    # RESULT TABS
    # ========================================================

    report_tab, sources_tab, read_tab, critic_tab = st.tabs(
        [
            "Report",
            "Sources",
            "Deep Read",
            "Critic Review"
        ]
    )


    # ========================================================
    # REPORT
    # ========================================================

    with report_tab:

        report = result.get(
            "report",
            "No report was generated."
        )

        if hasattr(report, "content"):
            report = report.content

        report = str(report)


        st.html(
            f"""
<div class="report-card">

    <div class="report-grid">

        <div>

            <div class="report-heading">

                <div class="report-icon">
                    ▤
                </div>

                <div>

                    <div class="report-name">
                        Research Report
                    </div>

                    <div class="report-topic">
                        {safe_topic}
                    </div>

                </div>

            </div>


            <div class="report-body">
"""
        )

        st.markdown(report)

        st.html("""
            </div>

        </div>


        <div class="glance">

            <div class="glance-title">
                At a Glance
            </div>


            <div class="metric">

                <div class="metric-icon">
                    ◈
                </div>

                <div>

                    <div class="metric-value">
                        Multi-Agent
                    </div>

                    <div class="metric-label">
                        Research system
                    </div>

                </div>

            </div>


            <div class="metric">

                <div class="metric-icon">
                    ⌕
                </div>

                <div>

                    <div class="metric-value">
                        Web Search
                    </div>

                    <div class="metric-label">
                        Source discovery
                    </div>

                </div>

            </div>


            <div class="metric">

                <div class="metric-icon">
                    ✎
                </div>

                <div>

                    <div class="metric-value">
                        Synthesis
                    </div>

                    <div class="metric-label">
                        Report generation
                    </div>

                </div>

            </div>


            <div class="metric">

                <div class="metric-icon">
                    ✓
                </div>

                <div>

                    <div class="metric-value">
                        Reviewed
                    </div>

                    <div class="metric-label">
                        Critic stage
                    </div>

                </div>

            </div>

        </div>

    </div>

</div>
""")


        st.html('<div class="download-area">')

        st.download_button(
            "↓  Download Report",
            data=report,
            file_name="research_report.md",
            mime="text/markdown"
        )

        st.html("</div>")


    # ========================================================
    # SOURCES
    # ========================================================

    with sources_tab:

        sources = result.get(
            "search_results",
            "No search results were returned."
        )

        if hasattr(sources, "content"):
            sources = sources.content

        st.html("""
<div class="report-card">

    <div class="report-heading">

        <div class="report-icon">
            ⌕
        </div>

        <div>

            <div class="report-name">
                Research Sources
            </div>

            <div class="report-topic">
                Sources discovered by Search Agent
            </div>

        </div>

    </div>


    <div class="report-body">

""")

        st.markdown(
            str(sources)
        )

        st.html("""
    </div>

</div>
""")


    # ========================================================
    # DEEP READ
    # ========================================================

    with read_tab:

        scraped = result.get(
            "scraped_content",
            "No scraped content was returned."
        )

        if hasattr(scraped, "content"):
            scraped = scraped.content

        st.html("""
<div class="report-card">

    <div class="report-heading">

        <div class="report-icon">
            ▣
        </div>

        <div>

            <div class="report-name">
                Deep Reading
            </div>

            <div class="report-topic">
                Content extracted by Reader Agent
            </div>

        </div>

    </div>


    <div class="report-body">

""")

        st.markdown(
            str(scraped)
        )

        st.html("""
    </div>

</div>
""")


    # ========================================================
    # CRITIC REVIEW
    # ========================================================

    with critic_tab:

        feedback = result.get(
            "feedback",
            "No critic feedback was returned."
        )

        if hasattr(feedback, "content"):
            feedback = feedback.content

        st.html("""
<div class="critic-card">

    <div class="critic-main">

        <div class="critic-icon">
            ♢
        </div>

        <div>

            <div class="critic-title">
                Critic Review
            </div>

            <div class="critic-description">

""")

        st.markdown(
            str(feedback)
        )

        st.html("""
            </div>

        </div>

    </div>


    <div class="review-score">

        <div class="review-label">
            REVIEW STATUS
        </div>

        <div class="review-value">
            ✓
        </div>

    </div>

</div>
""")


    # ========================================================
    # NEW RESEARCH
    # ========================================================

    st.html('<div class="new-research">')

    if st.button(
        "＋  Start New Research",
        use_container_width=True
    ):

        st.session_state.topic = ""
        st.session_state.result = None
        st.session_state.researching = False

        st.rerun()

    st.html("</div>")


# ============================================================
# FOOTER
# ============================================================

st.html("""
<div class="footer">

    <div>

        <span style="color:#8994a7;">
            ✦ ResearchPilot
        </span>

        &nbsp; · &nbsp;

        Multi-Agent Research

    </div>


    <div>
        Search · Read · Write · Critique
    </div>

</div>
""")
