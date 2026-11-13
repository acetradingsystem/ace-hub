import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(
    page_title="ACE scans",
    page_icon="♠",
    layout="wide",
)

st.markdown("""
<style>
  #MainMenu, footer, header { visibility: hidden; }
  [data-testid="stToolbar"] { display: none; }
  [data-testid="stHeader"] { display: none; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stAppViewContainer"] { background-color: #080c18 !important; }
  iframe { display: block; }
</style>
""", unsafe_allow_html=True)

# ── MARKET-HOURS STATUS ──────────────────────────────────────────────
et_tz = pytz.timezone("America/New_York")
now_et = datetime.now(et_tz)

hour = now_et.hour
minute = now_et.minute
is_trading_day = now_et.weekday() < 5

d1_active = is_trading_day and hour >= 16
h1_active = is_trading_day and (hour > 10 or (hour == 10 and minute >= 31))

READY = ("✦ READY TO RUN", "#00FF88", "#00FF8818", "#00FF8840")
d1_status = READY if d1_active else ("RUN AFTER 4:00 PM ET", "#F5A623", "#F5A62312", "#F5A62335")
h1_status = READY if h1_active else ("RUN AT 10:31 AM ET", "#F5A623", "#F5A62312", "#F5A62335")


# ── CARD BUILDER ─────────────────────────────────────────────────────
def scanner_card(code, num, title, kind, url, status):
    """kind = 'h1' (blue) or 'd1' (gold). status = (label, text, bg, border)."""
    label, color, bg, border = status
    return f"""
  <a href="{url}" target="_blank" rel="noopener" class="card card-{kind}">
    <div class="card-header">
      <span class="card-tag tag-{kind}">{code}</span>
      <span class="card-num">ACE {num}</span>
    </div>
    <div class="card-title">{title}</div>
    <div class="card-status" style="background:{bg};color:{color};border:1px solid {border}">
      <span class="dot" style="background:{color};box-shadow:0 0 5px {color}"></span>
      {label}
    </div>
    <div class="card-btn">▶ &nbsp;Go to Scanner</div>
  </a>"""


# Left → right order: H1-NS, D1-NS, H1-WS, D1-WS
cards_html = "\n".join([
    scanner_card("ACE-H1-NS", 3, "Narrow State Hourly Scan", "h1", "https://ace-h1-ns.streamlit.app", h1_status),
    scanner_card("ACE-D1-NS", 1, "Narrow State Daily Scan",  "d1", "https://ace-d1-ns.streamlit.app", d1_status),
    scanner_card("ACE-H1-WS", 4, "Wide State Hourly Scan",   "h1", "https://ace-h1-ws.streamlit.app", h1_status),
    scanner_card("ACE-D1-WS", 2, "Wide State Daily Scan",    "d1", "https://ace-d1-ws.streamlit.app", d1_status),
])

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}

body {{
  background: #080c18;
  color: #E8EAF0;
  font-family: 'Inter', sans-serif;
}}

/* ── HERO ── */
.hero {{
  text-align: center;
  padding: 1.8rem 1.5rem 1.4rem;
  background: radial-gradient(ellipse at 50% 0%, #0f1d3a 0%, #080c18 70%);
  border-bottom: 1px solid #111827;
}}

.hero-logo {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 2.8rem;
  font-weight: 800;
  letter-spacing: 0.22em;
  color: #F5A623;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  text-shadow: 0 0 40px #F5A62340;
}}

.hero-sub {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.32em;
  color: #7a8fa8;
  text-transform: uppercase;
  margin-top: 0.5rem;
}}

.hero-divider {{
  width: 60px;
  height: 1px;
  background: #F5A62340;
  margin: 0.3rem auto 0;
}}

/* ── SECTION LABEL ── */
.section-eyebrow {{
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.42em;
  text-transform: uppercase;
  color: #4DA6FF;
  text-shadow: 0 0 24px #4DA6FF40;
  margin: 2.6rem 0 0;
}}

.section-label {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.6rem;
  max-width: 1320px;
  margin: 0.7rem auto 2rem;
  padding: 0 1.5rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #E8EAF0;
  white-space: nowrap;
}}

.section-label::before,
.section-label::after {{
  content: '';
  flex: 1;
  height: 1px;
}}
.section-label::before {{ background: linear-gradient(90deg, transparent, #F5A62355); }}
.section-label::after  {{ background: linear-gradient(270deg, transparent, #F5A62355); }}

.section-label .tsx {{
  color: #F5A623;
  text-shadow: 0 0 28px #F5A62345;
}}

/* ── GRID: four cards in one centered row ── */
.grid {{
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.2rem;
  max-width: 1320px;
  margin: 0 auto;
  padding: 0 1.5rem;
  align-items: stretch;
}}

/* ── CARD ── */
.card {{
  background: linear-gradient(180deg, #0e1428 0%, #0b1020 100%);
  border-radius: 14px;
  border: 1px solid #141d30;
  padding: 1.7rem 1.4rem 1.4rem;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  transition: transform 0.18s, border-color 0.18s, box-shadow 0.18s;
}}

.card:hover {{ transform: translateY(-3px); text-decoration: none; }}
.card:focus-visible {{ outline: 2px solid #E8EAF0; outline-offset: 3px; }}

/* top accent line */
.card::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
}}

/* D1 card — gold */
.card-d1 {{ border-color: #1e2a40; }}
.card-d1::before {{ background: linear-gradient(90deg, transparent, #F5A623, transparent); }}
.card-d1:hover {{ border-color: #F5A62340; box-shadow: 0 8px 40px #F5A62318; }}

/* H1 card — blue */
.card-h1 {{ border-color: #1a2540; }}
.card-h1::before {{ background: linear-gradient(90deg, transparent, #4DA6FF, transparent); }}
.card-h1:hover {{ border-color: #4DA6FF40; box-shadow: 0 8px 40px #4DA6FF18; }}

/* header row: code badge + ACE number */
.card-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.3rem;
}}

.card-tag {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  padding: 0.22rem 0.6rem;
  border-radius: 5px;
  white-space: nowrap;
}}

.tag-d1 {{ background: #F5A62318; color: #F5A623; border: 1px solid #F5A62335; }}
.tag-h1 {{ background: #4DA6FF18; color: #4DA6FF; border: 1px solid #4DA6FF35; }}

.card-num {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  color: #34425f;
  font-weight: 700;
  letter-spacing: 0.1em;
  white-space: nowrap;
}}

/* title */
.card-title {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.05rem;
  font-weight: 700;
  color: #aab4c8;
  letter-spacing: 0.01em;
  line-height: 1.3;
  min-height: 2.7em;           /* keeps all four cards aligned if a title wraps */
}}

/* status pill */
.card-status {{
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.28rem 0.7rem;
  border-radius: 20px;
  margin: 1rem 0 1.6rem;
  width: fit-content;
  max-width: 100%;
  white-space: nowrap;
}}

.dot {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: inline-block;
  flex-shrink: 0;
}}

/* CTA — pinned to the bottom so buttons line up across the row */
.card-btn {{
  margin-top: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.8rem 1rem;
  border-radius: 8px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.74rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  transition: filter 0.15s;
}}

.card-d1 .card-btn {{
  background: linear-gradient(135deg, #c87d0e, #F5A623);
  color: #0a0c12;
  box-shadow: 0 4px 20px #F5A62330;
}}

.card-h1 .card-btn {{
  background: linear-gradient(135deg, #2a6bb5, #4DA6FF);
  color: #0a0c12;
  box-shadow: 0 4px 20px #4DA6FF30;
}}

.card:hover .card-btn {{ filter: brightness(1.12); }}

@media (prefers-reduced-motion: reduce) {{
  .card, .card-btn {{ transition: none; }}
  .card:hover {{ transform: none; }}
}}

/* ── FOOTER SPACER ── */
.footer {{ height: 2.5rem; }}

/* ── RESPONSIVE: 4 across → 2×2 → stacked ── */
@media (max-width: 1100px) {{
  .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
}}

@media (max-width: 600px) {{
  .hero {{ padding-top: 2.2rem; }}
  .hero-logo {{ font-size: 2rem; letter-spacing: 0.15em; }}
  .section-eyebrow {{ font-size: 0.62rem; letter-spacing: 0.26em; margin-top: 2rem; }}
  .section-label {{ font-size: 1.05rem; letter-spacing: 0.18em; gap: 0.9rem; margin: 0.5rem auto 1.4rem; }}
  .grid {{ grid-template-columns: 1fr; gap: 1rem; padding: 0 1rem; }}
  .card {{ padding: 1.4rem 1.2rem 1.3rem; }}
  .card-title {{ min-height: 0; }}
}}
</style>
</head>
<body>

<div class="hero">
  <div class="hero-logo">♠ACE</div>
  <div class="hero-sub">Accumulation Computation Engine</div>
  <div class="hero-divider"></div>
</div>

<div class="section-eyebrow">Narrow and Wide State</div>
<div class="section-label"><span><span class="tsx">TSX</span> MARKET SCANNERS</span></div>

<div class="grid">
{cards_html}
</div>

<div class="footer"></div>

<script>
  // Resize the embedding frame to fit the content, so on phones the whole
  // page scrolls normally instead of scrolling inside a fixed-height box.
  function fitFrame() {{
    try {{
      var h = Math.ceil(document.body.getBoundingClientRect().height);
      window.frameElement.style.height = h + 'px';
    }} catch (e) {{}}
  }}
  window.addEventListener('load', fitFrame);
  window.addEventListener('resize', fitFrame);
  if (window.ResizeObserver) {{ new ResizeObserver(fitFrame).observe(document.body); }}
  fitFrame();
</script>

</body>
</html>"""

components.html(html, height=770, scrolling=True)
