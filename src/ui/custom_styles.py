import streamlit as st


def load_custom_css() -> None:
    """Inject the Vedic Gita Scriptures inspired Streamlit visual system."""
    st.markdown(
        """
<style>
:root {
  --bg-black: #05030a;
  --deep-purple: #16001f;
  --royal-purple: #2a0a3d;
  --violet: #7c3aed;
  --lavender: #c4b5fd;
  --gold: #f5c542;
  --soft-gold: #f8dfa0;
  --white: #f8fafc;
  --muted: #a1a1aa;
  --glass: rgba(255, 255, 255, 0.07);
  --glass-strong: rgba(255, 255, 255, 0.12);
  --border: rgba(245, 197, 66, 0.28);
  --violet-border: rgba(196, 181, 253, 0.24);
  --ease: cubic-bezier(.2,.8,.2,1);
  --shadow-violet: 0 28px 95px rgba(124, 58, 237, 0.34);
  --shadow-gold: 0 0 34px rgba(245, 197, 66, 0.15);
}

#MainMenu, footer, header { visibility: hidden; }

html, body, [class*="css"] {
  font-family: "Inter", "Geist Sans", "SF Pro Display", "Helvetica Neue", Arial, sans-serif;
  font-size-adjust: 0.52;
}

.stApp {
  color: var(--white);
  background:
    radial-gradient(circle at 12% 12%, rgba(124, 58, 237, 0.32), transparent 30%),
    radial-gradient(circle at 86% 8%, rgba(245, 197, 66, 0.13), transparent 24%),
    radial-gradient(circle at 55% 92%, rgba(42, 10, 61, 0.88), transparent 40%),
    linear-gradient(130deg, var(--bg-black) 0%, var(--deep-purple) 48%, #07020d 100%);
  background-size: 150% 150%;
  animation: shimmer 18s var(--ease) infinite alternate;
}

.stApp:before {
  content: "";
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-image:
    radial-gradient(circle, rgba(248, 250, 252, 0.28) 0 1px, transparent 1.5px),
    radial-gradient(circle, rgba(245, 197, 66, 0.22) 0 1px, transparent 1.4px);
  background-size: 76px 76px, 128px 128px;
  opacity: 0.32;
  animation: float 22s ease-in-out infinite alternate;
}

.block-container {
  position: relative;
  z-index: 1;
  max-width: 1220px;
  padding-top: 2rem;
  padding-bottom: 3.5rem;
}

h1, h2, h3 {
  color: var(--white);
  font-weight: 800 !important;
  letter-spacing: 0;
  line-height: 1.08;
}

p, li, div, label, span {
  line-height: 1.5;
}

label {
  color: rgba(248, 250, 252, 0.86) !important;
  font-weight: 700 !important;
}

[data-testid="stSidebar"] {
  background: rgba(5, 3, 10, 0.9);
  border-right: 1px solid rgba(245, 197, 66, 0.18);
  backdrop-filter: blur(18px);
}

[data-testid="stSidebar"] * { color: var(--white); }

.stButton > button,
.stFormSubmitButton > button {
  min-height: 3.15rem;
  border: 1px solid rgba(245, 197, 66, 0.54);
  border-radius: 999px;
  color: var(--white);
  background: linear-gradient(135deg, #4c1d95 0%, var(--violet) 44%, #b982ff 70%, var(--gold) 100%);
  background-size: 190% 190%;
  box-shadow: 0 16px 42px rgba(124, 58, 237, 0.38), inset 0 1px 0 rgba(255,255,255,0.18);
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  transition: all 0.35s var(--ease);
  white-space: nowrap;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
  transform: translateY(-2px) scale(1.01);
  background-position: 100% 50%;
  border-color: rgba(248, 223, 160, 0.96);
  box-shadow: 0 22px 62px rgba(124, 58, 237, 0.58), 0 0 22px rgba(245, 197, 66, 0.22);
}

.stTextArea textarea,
.stTextInput input,
.stNumberInput input,
.stSelectbox [data-baseweb="select"] {
  border-radius: 22px !important;
  border: 1px solid rgba(245, 197, 66, 0.26) !important;
  background: rgba(255, 255, 255, 0.075) !important;
  color: var(--white) !important;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,0.035), 0 14px 38px rgba(0,0,0,0.22);
  transition: all 0.35s var(--ease);
}

.stTextArea textarea:focus,
.stTextInput input:focus,
.stNumberInput input:focus {
  border-color: rgba(248, 223, 160, 0.7) !important;
  box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.25), 0 18px 48px rgba(0,0,0,0.26) !important;
}

[data-testid="stDataFrame"] {
  border: 1px solid rgba(245, 197, 66, 0.2);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 18px 50px rgba(0,0,0,0.24);
}

.scripture-hero,
.scripture-panel,
.chat-shell,
.form-scroll {
  position: relative;
  overflow: hidden;
  border: 1px solid var(--border);
  border-radius: 28px;
  background:
    linear-gradient(145deg, rgba(255,255,255,0.105), rgba(255,255,255,0.032)),
    radial-gradient(circle at 78% 18%, rgba(124,58,237,0.24), transparent 38%),
    linear-gradient(90deg, rgba(245,197,66,0.035) 0 1px, transparent 1px),
    linear-gradient(0deg, rgba(245,197,66,0.025) 0 1px, transparent 1px);
  background-size: auto, auto, 36px 36px, 36px 36px;
  box-shadow: var(--shadow-violet), var(--shadow-gold);
  backdrop-filter: blur(18px);
}

.scripture-hero {
  min-height: 78vh;
  padding: clamp(2.2rem, 6vw, 6.6rem);
}

.scripture-panel,
.chat-shell,
.form-scroll {
  padding: clamp(1.35rem, 4vw, 2.7rem);
}

.scripture-hero:before,
.scripture-hero:after,
.mandala-ripple {
  content: "";
  position: absolute;
  pointer-events: none;
  border-radius: 50%;
  background:
    repeating-radial-gradient(circle at center, transparent 0 18px, rgba(245,197,66,0.17) 19px 20px, transparent 21px 42px),
    conic-gradient(from 90deg, transparent, rgba(196,181,253,0.2), transparent 34%, rgba(245,197,66,0.14), transparent);
  mask-image: radial-gradient(circle at center, black 0 38%, transparent 66%);
  animation: slowRotate 56s linear infinite;
}

.scripture-hero:before {
  width: 760px;
  height: 760px;
  right: -220px;
  top: -230px;
  opacity: 0.8;
}

.scripture-hero:after {
  width: 520px;
  height: 520px;
  left: -170px;
  bottom: -210px;
  opacity: 0.42;
  animation-direction: reverse;
  animation-duration: 38s;
}

.particle-field {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image:
    radial-gradient(circle, rgba(248,250,252,0.34) 0 1px, transparent 1.5px),
    radial-gradient(circle, rgba(245,197,66,0.26) 0 1px, transparent 1.3px);
  background-size: 72px 72px, 118px 118px;
  opacity: 0.34;
  animation: float 18s ease-in-out infinite alternate;
}

.aura {
  position: absolute;
  width: 320px;
  height: 320px;
  right: 7%;
  bottom: 8%;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(196,181,253,0.38), rgba(124,58,237,0.13) 42%, transparent 70%);
  filter: blur(4px);
  animation: pulseGlow 5.8s ease-in-out infinite;
}

.scripture-frame {
  position: absolute;
  inset: 22px;
  border: 1px solid rgba(245, 197, 66, 0.32);
  border-radius: 20px;
  pointer-events: none;
}

.scripture-frame:before,
.scripture-frame:after {
  content: "";
  position: absolute;
  width: 112px;
  height: 1px;
  top: 18px;
  background: linear-gradient(90deg, transparent, rgba(248,223,160,0.95), transparent);
}

.scripture-frame:before { left: 28px; }
.scripture-frame:after { right: 28px; }

.copy-block,
.section-copy,
.transition-copy {
  position: relative;
  z-index: 2;
  max-width: 880px;
  animation: fadeUp 0.78s var(--ease) both;
}

.eyebrow,
.status-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.48rem;
  color: var(--gold);
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.16em;
  text-transform: uppercase;
}

.title-xl {
  margin: 0.8rem 0 1rem;
  font-size: clamp(2.55rem, 7vw, 6rem);
  color: var(--white);
  text-wrap: balance;
}

.subtitle {
  max-width: 850px;
  margin: 0 0 0.8rem;
  color: var(--lavender);
  font-size: clamp(1.05rem, 2vw, 1.38rem);
  font-weight: 600;
}

.sutra-line {
  color: var(--soft-gold);
  font-weight: 700;
  letter-spacing: 0.03em;
}

.body-copy {
  max-width: 790px;
  color: rgba(248,250,252,0.76);
  font-size: 1.02rem;
  font-weight: 400;
}

.disclaimer-inline,
.footer-note {
  margin-top: 1.2rem;
  padding: 1rem 1.15rem;
  border: 1px solid rgba(245,197,66,0.24);
  border-radius: 20px;
  background: rgba(245,197,66,0.06);
  color: rgba(248,250,252,0.7);
  font-size: 0.92rem;
}

.journey-grid,
.recommend-grid {
  display: grid;
  gap: 1rem;
}

.journey-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
  margin-top: 2rem;
}

.recommend-grid {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.scripture-card,
.result-card,
.profile-card,
.recommend-card,
.graph-card {
  position: relative;
  min-height: 150px;
  padding: 1.22rem;
  border: 1px solid rgba(245,197,66,0.24);
  border-radius: 24px;
  background:
    linear-gradient(145deg, rgba(255,255,255,0.105), rgba(255,255,255,0.04)),
    repeating-linear-gradient(0deg, rgba(245,197,66,0.035) 0 1px, transparent 1px 14px);
  box-shadow: 0 18px 54px rgba(0,0,0,0.25);
  backdrop-filter: blur(14px);
  transition: all 0.35s var(--ease);
  animation: fadeUp 0.72s var(--ease) both;
}

.scripture-card:nth-child(2) { animation-delay: 0.08s; }
.scripture-card:nth-child(3) { animation-delay: 0.16s; }
.scripture-card:nth-child(4) { animation-delay: 0.24s; }

.scripture-card:before,
.result-card:before,
.recommend-card:before,
.chat-bubble:before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(120deg, transparent, rgba(245,197,66,0.72), rgba(196,181,253,0.58), transparent);
  mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.35s var(--ease);
  animation: borderBeam 4s linear infinite;
}

.scripture-card:hover,
.result-card:hover,
.recommend-card:hover,
.chat-bubble:hover:before { opacity: 1; }

.card-symbol {
  width: 46px;
  height: 46px;
  margin-bottom: 0.95rem;
  border-radius: 50%;
  border: 1px solid rgba(245,197,66,0.62);
  background:
    radial-gradient(circle, rgba(245,197,66,0.62), transparent 28%),
    conic-gradient(from 45deg, rgba(124,58,237,0.14), rgba(196,181,253,0.84), rgba(124,58,237,0.14));
  box-shadow: 0 0 28px rgba(196,181,253,0.3);
  animation: pulseGlow 4.8s ease-in-out infinite;
}

.scripture-card h3,
.result-card h3,
.recommend-card h3,
.profile-card h3 { margin: 0 0 0.55rem; }

.scripture-card p,
.result-card p,
.recommend-card p,
.profile-card p { color: rgba(248,250,252,0.74); margin: 0.28rem 0; }

.chat-header {
  position: relative;
  z-index: 1;
  display: grid;
  grid-template-columns: minmax(0, 1.55fr) minmax(280px, 0.8fr);
  gap: 1rem;
  align-items: stretch;
}

.profile-card { min-height: auto; }

.chip-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin: 1rem 0;
}

.status-chip {
  padding: 0.62rem 0.78rem;
  border: 1px solid rgba(245,197,66,0.22);
  border-radius: 999px;
  background: rgba(255,255,255,0.065);
  box-shadow: inset 0 0 18px rgba(124,58,237,0.1);
  color: rgba(248,250,252,0.86);
  animation: pulseGlow 3.1s ease-in-out infinite;
}

.chat-panel {
  position: relative;
  z-index: 1;
  margin-top: 1.2rem;
  padding: clamp(1rem, 2.4vw, 1.5rem);
  border: 1px solid rgba(245,197,66,0.2);
  border-radius: 26px;
  background: rgba(5,3,10,0.42);
}

.chat-bubble {
  position: relative;
  width: fit-content;
  max-width: min(850px, 100%);
  margin: 0.9rem 0;
  padding: 1rem 1.15rem;
  border: 1px solid rgba(245,197,66,0.22);
  border-radius: 22px;
  background: rgba(255,255,255,0.075);
  box-shadow: 0 16px 44px rgba(0,0,0,0.2);
  animation: fadeUp 0.58s var(--ease) both;
}

.chat-bubble.user {
  margin-left: auto;
  background: linear-gradient(135deg, rgba(124,58,237,0.52), rgba(168,85,247,0.2));
  border-color: rgba(245,197,66,0.34);
}

.chat-bubble.ai { background: rgba(255,255,255,0.072); }
.chat-bubble.delay-1 { animation-delay: 0.08s; }
.chat-bubble.delay-2 { animation-delay: 0.16s; }
.chat-bubble.delay-3 { animation-delay: 0.24s; }
.chat-bubble.delay-4 { animation-delay: 0.32s; }

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(18px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes slowRotate { to { transform: rotate(360deg); } }

@keyframes ripple {
  0%, 100% { transform: scale(0.92); opacity: 0.48; }
  50% { transform: scale(1.07); opacity: 0.88; }
}

@keyframes float {
  0% { transform: translate3d(0, 0, 0); }
  100% { transform: translate3d(24px, -18px, 0); }
}

@keyframes pulseGlow {
  0%, 100% { opacity: 0.72; box-shadow: 0 0 18px rgba(124,58,237,0.14); }
  50% { opacity: 1; box-shadow: 0 0 34px rgba(245,197,66,0.18), 0 0 44px rgba(124,58,237,0.28); }
}

@keyframes borderBeam {
  0% { filter: hue-rotate(0deg); }
  100% { filter: hue-rotate(360deg); }
}

@keyframes shimmer {
  0% { background-position: 0% 50%; }
  100% { background-position: 100% 50%; }
}

@media (max-width: 980px) {
  .journey-grid,
  .chat-header,
  .recommend-grid { grid-template-columns: 1fr 1fr; }
  .scripture-hero { min-height: 68vh; }
}

@media (max-width: 620px) {
  .journey-grid,
  .chat-header,
  .recommend-grid { grid-template-columns: 1fr; }
  .title-xl { font-size: 2.5rem; }
  .scripture-hero { padding: 2rem 1.2rem; }
  .scripture-frame { inset: 14px; }
}
</style>
        """,
        unsafe_allow_html=True,
    )
