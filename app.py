import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(
    page_title="ACE SCANS",
    page_icon="♠",
    layout="wide",
)

st.markdown("""
<style>
  #MainMenu, footer, header { visibility: hidden; }
  [data-testid="stToolbar"] { display: none; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stAppViewContainer"] { background-color: #080c18 !important; }
  iframe { display: block; }
</style>
""", unsafe_allow_html=True)

et_tz = pytz.timezone("America/New_York")
now_et = datetime.now(et_tz)

hour = now_et.hour
minute = now_et.minute
is_trading_day = now_et.weekday() < 5

d1_active = is_trading_day and hour >= 16
h1_active = is_trading_day and (hour > 10 or (hour == 10 and minute >= 31))

d1_status = ("✦ READY TO RUN", "#00FF88", "#00FF8818", "#00FF8840") if d1_active else ("RUN AFTER 4:00 PM ET", "#F5A623", "#F5A62312", "#F5A62335")
h1_status = ("✦ READY TO RUN", "#00FF88", "#00FF8818", "#00FF8840") if h1_active else ("RUN AT 10:31 AM ET", "#F5A623", "#F5A62312", "#F5A62335")

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
  min-height: 100vh;
}}

/* ── HERO ── */
.hero {{
  text-align: center;
  padding: 2.8rem 1.5rem 2rem;
  background: radial-gradient(ellipse at 50% 0%, #0f1d3a 0%, #080c18 70%);
  border-bottom: 1px solid #111827;
  position: relative;
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
  color: #3a4a60;
  text-transform: uppercase;
  margin-top: 0.5rem;
}}

/* ── EXCLUDE BAR ── */
.section-label {{
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #2a3650;
  margin: 2.2rem 0 1.4rem;
}}

/* ── GRID ── */
.grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.4rem;
  max-width: 860px;
  margin: 0 auto;
  padding: 0 1.5rem;
}}

/* ── CARD ── */
.card {{
  background: #0c1122;
  border-radius: 14px;
  border: 1px solid #141d30;
  padding: 1.8rem 1.6rem 1.6rem;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  gap: 0;
  position: relative;
  overflow: hidden;
  transition: transform 0.18s, border-color 0.18s, box-shadow 0.18s;
}}

.card::after {{
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 14px;
  opacity: 0;
  transition: opacity 0.2s;
  pointer-events: none;
}}

.card:hover {{
  transform: translateY(-3px);
  text-decoration: none;
}}

/* D1 card — gold glow */
.card-d1 {{ border-color: #1e2a40; }}
.card-d1:hover {{ border-color: #F5A62340; box-shadow: 0 8px 40px #F5A62318; }}
.card-d1::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, transparent, #F5A623, transparent);
  border-radius: 14px 14px 0 0;
}}

/* H1 card — blue glow */
.card-h1 {{ border-color: #1a2540; }}
.card-h1:hover {{ border-color: #4DA6FF40; box-shadow: 0 8px 40px #4DA6FF18; }}
.card-h1::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; height: 3px;
  background: linear-gradient(90deg, transparent, #4DA6FF, transparent);
  border-radius: 14px 14px 0 0;
}}

/* Card header row */
.card-header {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.2rem;
}}

.card-tag {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  padding: 0.22rem 0.6rem;
  border-radius: 5px;
}}

.tag-d1 {{ background: #F5A62318; color: #F5A623; border: 1px solid #F5A62335; }}
.tag-h1 {{ background: #4DA6FF18; color: #4DA6FF; border: 1px solid #4DA6FF35; }}

.card-num {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.65rem;
  color: #1e2840;
  font-weight: 700;
  letter-spacing: 0.1em;
}}

/* Card title */
.card-title {{
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.15rem;
  font-weight: 700;
  color: #FFFFFF;
  letter-spacing: 0.02em;
  margin-bottom: 0.5rem;
  line-height: 1.2;
}}

.card-desc {{
  font-size: 0.78rem;
  color: #4a5878;
  line-height: 1.55;
  flex: 1;
}}

/* Status badge */
.card-status {{
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 0.25rem 0.7rem;
  border-radius: 20px;
  margin: 1rem 0 1.3rem;
  width: fit-content;
}}

/* CTA Button */
.card-btn {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  width: 100%;
  padding: 0.85rem 1rem;
  border-radius: 8px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  transition: filter 0.15s, transform 0.12s;
}}

.card-d1 .card-btn {{
  background: linear-gradient(135deg, #c87d0e, #F5A623);
  color: #0a0c12;
  box-shadow: 0 4px 20px #F5A62330;
}}

.card-h1 .card-btn {{
  background: linear-gradient(135deg, #2a6bb5, #4DA6FF);
  color: #ffffff;
  box-shadow: 0 4px 20px #4DA6FF30;
}}

.card:hover .card-btn {{
  filter: brightness(1.12);
}}

/* ── EXCLUDE BAR ── */
.exclude-bar {{
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  letter-spacing: 0.12em;
  color: #1e2840;
  text-transform: uppercase;
  padding: 2rem 1.5rem 0.5rem;
  max-width: 860px;
  margin: 0 auto;
}}

/* ── FOOTER ── */
.footer {{
  text-align: center;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.62rem;
  color: #1a2235;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 1.5rem 1.5rem 2rem;
}}

/* ── MOBILE ── */
@media (max-width: 600px) {{
  .hero-logo {{ font-size: 2rem; letter-spacing: 0.15em; }}
  .grid {{ grid-template-columns: 1fr; gap: 1rem; padding: 0 1rem; }}
  .card {{ padding: 1.4rem 1.2rem 1.3rem; }}
  .card-title {{ font-size: 1rem; }}
}}
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-logo">♠&nbsp;ACE&nbsp;SCANS</div>
  <div class="hero-sub">Accumulation Computation Engine</div>
  <div class="hero-divider"></div>
</div>

<!-- SECTION -->
<div class="section-label">// TSX Market State Scanners</div>

<!-- CARDS -->
<div class="grid">

  <!-- ACE 1 -->
  <a href="https://ace-d1-ns.streamlit.app" target="_blank" class="card card-d1">
    <div class="card-header">
      <span class="card-tag tag-d1">ACE-D1-NS</span>
      <span class="card-num">ACE 1</span>
    </div>
    <div class="card-title">Narrow State Daily Scan</div>
    <div class="card-status" style="background:{d1_status[2]};color:{d1_status[1]};border:1px solid {d1_status[3]}">
      <span style="width:6px;height:6px;border-radius:50%;background:{d1_status[1]};box-shadow:0 0 5px {d1_status[1]};display:inline-block;flex-shrink:0"></span>
      {d1_status[0]}
    </div>
    <div class="card-btn">▶ &nbsp;Go to Scanner</div>
  </a>

  <!-- ACE 2 -->
  <a href="https://ace-d1-ws.streamlit.app" target="_blank" class="card card-d1">
    <div class="card-header">
      <span class="card-tag tag-d1">ACE-D1-WS</span>
      <span class="card-num">ACE 2</span>
    </div>
    <div class="card-title">Wide State Daily Scan</div>
    <div class="card-status" style="background:{d1_status[2]};color:{d1_status[1]};border:1px solid {d1_status[3]}">
      <span style="width:6px;height:6px;border-radius:50%;background:{d1_status[1]};box-shadow:0 0 5px {d1_status[1]};display:inline-block;flex-shrink:0"></span>
      {d1_status[0]}
    </div>
    <div class="card-btn">▶ &nbsp;Go to Scanner</div>
  </a>

  <!-- ACE 3 -->
  <a href="https://ace-h1-ns.streamlit.app" target="_blank" class="card card-h1">
    <div class="card-header">
      <span class="card-tag tag-h1">ACE-H1-NS</span>
      <span class="card-num">ACE 3</span>
    </div>
    <div class="card-title">Narrow State Scan</div>
    <div class="card-status" style="background:{h1_status[2]};color:{h1_status[1]};border:1px solid {h1_status[3]}">
      <span style="width:6px;height:6px;border-radius:50%;background:{h1_status[1]};box-shadow:0 0 5px {h1_status[1]};display:inline-block;flex-shrink:0"></span>
      {h1_status[0]}
    </div>
    <div class="card-btn">▶ &nbsp;Go to Scanner</div>
  </a>

  <!-- ACE 4 -->
  <a href="https://ace-h1-ws.streamlit.app" target="_blank" class="card card-h1">
    <div class="card-header">
      <span class="card-tag tag-h1">ACE-H1-WS</span>
      <span class="card-num">ACE 4</span>
    </div>
    <div class="card-title">Wide State Scan</div>
    <div class="card-status" style="background:{h1_status[2]};color:{h1_status[1]};border:1px solid {h1_status[3]}">
      <span style="width:6px;height:6px;border-radius:50%;background:{h1_status[1]};box-shadow:0 0 5px {h1_status[1]};display:inline-block;flex-shrink:0"></span>
      {h1_status[0]}
    </div>
    <div class="card-btn">▶ &nbsp;Go to Scanner</div>
  </a>

</div>

<div class="exclude-bar">
  Excludes: Mining · Energy · Gold · Materials · Utilities · Real Estate &nbsp;·&nbsp; Min $5 CAD
</div>

<div class="footer">acetradingsystem.com</div>

</body>
</html>"""

components.html(html, height=1050, scrolling=True)
