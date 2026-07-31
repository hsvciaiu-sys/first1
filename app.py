from datetime import date
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="宝宝，你完蛋了。",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent


def data_uri(relative_path: str, mime: str) -> str:
    payload = (ROOT / relative_path).read_text(encoding="ascii").strip()
    return f"data:{mime};base64,{payload}"


days_known = (date(2026, 8, 1) - date(2026, 7, 2)).days
assets = {
    "book": data_uri("assets/book.webp.b64", "image/webp"),
    "auditorium_close": data_uri("assets/auditorium-close.webp.b64", "image/webp"),
    "auditorium_wide": data_uri("assets/auditorium-wide.webp.b64", "image/webp"),
    "ktv_selfie": data_uri("assets/ktv-selfie.webp.b64", "image/webp"),
    "social_chat": data_uri("assets/social-chat.webp.b64", "image/webp"),
    "ktv_video": data_uri("assets/ktv-memory.mp4.b64", "video/mp4"),
}

st.markdown(
    """
    <style>
    #MainMenu, header, footer, [data-testid="stToolbar"],
    [data-testid="stDecoration"], [data-testid="stStatusWidget"] { display:none !important; }
    [data-testid="stAppViewContainer"], .stApp { background:#07090f; }
    [data-testid="stMain"] { overflow:hidden; }
    .block-container { max-width:none; padding:0 !important; }
    iframe { display:block; border:0; }
    </style>
    """,
    unsafe_allow_html=True,
)

html = (ROOT / "template.html").read_text(encoding="utf-8")
for placeholder, value in {
    "__CSS__": (ROOT / "style.css").read_text(encoding="utf-8"),
    "__JS__": (ROOT / "script.js").read_text(encoding="utf-8"),
    "__DAYS__": str(days_known),
    "__BOOK__": assets["book"],
    "__AUDITORIUM_CLOSE__": assets["auditorium_close"],
    "__AUDITORIUM_WIDE__": assets["auditorium_wide"],
    "__KTV_SELFIE__": assets["ktv_selfie"],
    "__SOCIAL_CHAT__": assets["social_chat"],
    "__KTV_VIDEO__": assets["ktv_video"],
}.items():
    html = html.replace(placeholder, value)

components.html(html, height=940, scrolling=False)
