import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import pytz

st.set_page_config(
    page_title="ACE Trading System",
    page_icon="⚡",
    layout="wide",
)

# Hide Streamlit chrome
st.markdown("""
<style>
  #MainMenu, footer, header { visibility: hidden; }
  [data-testid="stToolbar"] { display: none; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  [data-testid="stAppViewContainer"] { background-color: #0D0F14 !important; }
</style>
""", unsafe_allow_html=True)

# ── Time logic ──
et_tz = pytz.timezone("America/New_York")
now_et = datetime.now(et_tz)
time_str = now_et.strftime("%H:%M:%S")
date_str = now_et.strftime("%a %b %d, %Y")

hour = now_et.hour
minute = now_et.minute
is_trading_day = now_et.weekday() < 5

d1_active = is_trading_day and hour >= 16
h1_active = is_trading_day and (hour > 10 or (hour == 10 and minute >= 31))

d1_dot_class  = "dot-green" if d1_active  else "dot-dim"
h1_dot_class  = "dot-blue"  if h1_active  else "dot-dim"
d1_text = "D1 — Ready to run" if d1_active else "D1 — Run after 4:00 PM ET"
h1_text = "H1 — Ready to run" if h1_active else "H1 — Run after 10:31 AM ET"

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    background: #0D0F14;
    color: #E8EAF0;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    display: flex;
    justify-content: center;
  }}

  .ace-wrapper {{
    width: 100%;
    max-width: 960px;
    padding: 2.5rem 2rem 2rem 2rem;
  }}

  .ace-header {{
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    margin-bottom: 2.8rem;
    border-bottom: 1px solid #1E2130;
    padding-bottom: 1.2rem;
  }}

  .ace-logo {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.9rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: #FFFFFF;
  }}

  .ace-logo span {{ color: #00FF88; }}

  .ace-tagline {{
    font-size: 0.78rem;
    color: #5A6178;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-top: 0.2rem;
    font-family: 'JetBrains Mono', monospace;
  }}

  .ace-clock-block {{ text-align: right; }}

  .ace-clock {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.5rem;
    font-weight: 600;
    color: #FFFFFF;
    letter-spacing: 0.06em;
  }}

  .ace-clock-label {{
    font-size: 0.72rem;
    color: #5A6178;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-top: 0.15rem;
    font-family: 'JetBrains Mono', monospace;
  }}

  .ace-status-bar {{
    display: flex;
    gap: 1.5rem;
    margin-bottom: 2.2rem;
    flex-wrap: wrap;
  }}

  .ace-status-pill {{
    display: flex;
    align-items: center;
    gap: 0.45rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    letter-spacing: 0.08em;
    color: #8892A4;
    text-transform: uppercase;
  }}

  .ace-dot {{
    width: 7px;
    height: 7px;
    border-radius: 50%;
    flex-shrink: 0;
  }}

  .dot-green {{ background: #00FF88; box-shadow: 0 0 6px #00FF88; }}
  .dot-blue  {{ background: #4DA6FF; box-shadow: 0 0 6px #4DA6FF; }}
  .dot-dim   {{ background: #2A2E3D; }}

  .ace-section {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #3A4055;
    margin-bottom: 1rem;
  }}

  .ace-grid {{
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.2rem;
  }}

  .ace-card {{
    background: #131620;
    border: 1px solid #1E2130;
    border-radius: 10px;
    padding: 1.6rem 1.8rem;
    text-decoration: none;
    display: block;
    transition: border-color 0.18s, background 0.18s, transform 0.15s;
    position: relative;
    overflow: hidden;
  }}

  .ace-card::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    border-radius: 10px 10px 0 0;
    opacity: 0;
    transition: opacity 0.18s;
  }}

  .ace-card:hover {{
    background: #161926;
    transform: translateY(-2px);
    text-decoration: none;
  }}

  .ace-card:hover::before {{ opacity: 1; }}

  .card-d1::before {{ background: #00FF88; }}
  .card-h1::before {{ background: #4DA6FF; }}
  .card-d1:hover {{ border-color: #00FF8833; }}
  .card-h1:hover {{ border-color: #4DA6FF33; }}

  .card-top {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1rem;
  }}

  .card-badge {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 0.2rem 0.55rem;
    border-radius: 4px;
  }}

  .badge-d1 {{ background: #00FF8815; color: #00FF88; border: 1px solid #00FF8830; }}
  .badge-h1 {{ background: #4DA6FF15; color: #4DA6FF; border: 1px solid #4DA6FF30; }}

  .card-num {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: #2A2E3D;
    font-weight: 600;
  }}

  .card-title {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.05rem;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: 0.03em;
    margin-bottom: 0.35rem;
  }}

  .card-desc {{
    font-size: 0.8rem;
    color: #5A6178;
    line-height: 1.5;
  }}

  .card-footer {{
    margin-top: 1.1rem;
    padding-top: 0.9rem;
    border-top: 1px solid #1A1D2A;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}

  .card-timing {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: #3A4055;
    letter-spacing: 0.06em;
  }}

  .card-arrow {{
    font-size: 0.9rem;
    color: #2A2E3D;
    transition: color 0.18s, transform 0.18s;
  }}

  .card-d1:hover .card-arrow {{ color: #00FF88; }}
  .card-h1:hover .card-arrow {{ color: #4DA6FF; }}
  .ace-card:hover .card-arrow {{ transform: translateX(3px); }}

  .ace-footer {{
    margin-top: 3rem;
    padding-top: 1.2rem;
    border-top: 1px solid #1A1D2A;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: #2A2E3D;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 0.5rem;
  }}
</style>
</head>
<body>
<div class="ace-wrapper">

  <div class="ace-header">
    <div>
      <div class="ace-logo">ACE<span>.</span>TRADING</div>
      <div class="ace-tagline">Scanner Suite — TSX</div>
    </div>
    <div class="ace-clock-block">
      <div class="ace-clock">{time_str}</div>
      <div class="ace-clock-label">ET &nbsp;·&nbsp; {date_str}</div>
    </div>
  </div>

  <div class="ace-status-bar">
    <div class="ace-status-pill"><span class="ace-dot {d1_dot_class}"></span> {d1_text}</div>
    <div class="ace-status-pill"><span class="ace-dot {h1_dot_class}"></span> {h1_text}</div>
    <div class="ace-status-pill"><span class="ace-dot dot-dim"></span> Excludes: Mining · Energy · Gold · Materials · Utilities · Real Estate</div>
  </div>

  <div class="ace-section">// Scanners</div>

  <div class="ace-grid">

    <a href="https://ace-d1-ns.streamlit.app" target="_blank" class="ace-card card-d1">
      <div class="card-top">
        <span class="card-badge badge-d1">D1 · Daily</span>
        <span class="card-num">ACE 1</span>
      </div>
      <div class="card-title">Narrow State</div>
      <div class="card-desc">MA20 ≈ MA200 within 3% — rarest, highest conviction breakout setups. Holy Grail score 9+.</div>
      <div class="card-footer">
        <span class="card-timing">⏱ Run after 4:00 PM ET</span>
        <span class="card-arrow">→</span>
      </div>
    </a>

    <a href="https://ace-d1-ws.streamlit.app" target="_blank" class="ace-card card-d1">
      <div class="card-top">
        <span class="card-badge badge-d1">D1 · Daily</span>
        <span class="card-num">ACE 2</span>
      </div>
      <div class="card-title">Wide Down RCB</div>
      <div class="card-desc">MA20 well below MA200 — Random Consolidation Breakout setups in declining MA state.</div>
      <div class="card-footer">
        <span class="card-timing">⏱ Run after 4:00 PM ET</span>
        <span class="card-arrow">→</span>
      </div>
    </a>

    <a href="https://ace-h1-ns.streamlit.app" target="_blank" class="ace-card card-h1">
      <div class="card-top">
        <span class="card-badge badge-h1">H1 · Hourly</span>
        <span class="card-num">ACE 3</span>
      </div>
      <div class="card-title">Narrow State H1</div>
      <div class="card-desc">Hourly Narrow State breakouts — intraday MA convergence signals for same-day entries.</div>
      <div class="card-footer">
        <span class="card-timing">⏱ Run at 10:31 AM ET</span>
        <span class="card-arrow">→</span>
      </div>
    </a>

    <a href="https://ace-h1-ws.streamlit.app" target="_blank" class="ace-card card-h1">
      <div class="card-top">
        <span class="card-badge badge-h1">H1 · Hourly</span>
        <span class="card-num">ACE 4</span>
      </div>
      <div class="card-title">Wide Down RCB H1</div>
      <div class="card-desc">Hourly Wide Down RCB setups — declining MA state breakouts on the first hourly bar.</div>
      <div class="card-footer">
        <span class="card-timing">⏱ Run at 10:31 AM ET</span>
        <span class="card-arrow">→</span>
      </div>
    </a>

  </div>

  <div class="ace-footer">
    <span>acetradingsystem.com</span>
    <span>TSX · Min $5 CAD · Oliver Velez / iFundTraders methodology</span>
  </div>

</div>
</body>
</html>
"""

components.html(html, height=700, scrolling=False)
