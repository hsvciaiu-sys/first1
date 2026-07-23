import streamlit as st
import streamlit.components.v1 as components
from datetime import date

st.set_page_config(
    page_title="给周凡寓的小惊喜",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed",
)

meet_date = date(2026, 7, 2)
today = date.today()
days_known = max((today - meet_date).days, 0)

html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>给周凡寓的小惊喜</title>
<style>
* {{ box-sizing: border-box; }}
html, body {{
    margin: 0;
    padding: 0;
    min-height: 100%;
    font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
    background:
        radial-gradient(circle at 15% 15%, rgba(255,255,255,.9), transparent 28%),
        linear-gradient(145deg, #fff7fa 0%, #ffe4ed 48%, #ffd3e2 100%);
    color: #66434f;
    overflow-x: hidden;
}}
body {{ min-height: 100vh; }}
.page {{
    display: none;
    min-height: 100vh;
    padding: 34px 22px 45px;
    align-items: center;
    justify-content: center;
    text-align: center;
    animation: fade .7s ease;
}}
.page.active {{ display: flex; }}
.card {{
    width: min(92vw, 690px);
    padding: 38px 26px;
    border-radius: 28px;
    background: rgba(255,255,255,.78);
    border: 1px solid rgba(255,255,255,.95);
    box-shadow: 0 18px 55px rgba(177, 72, 111, .18);
    backdrop-filter: blur(10px);
}}
h1 {{
    margin: 0 0 22px;
    color: #cf527d;
    font-size: clamp(30px, 8vw, 52px);
}}
h2 {{
    margin: 0 0 22px;
    color: #cf527d;
    font-size: clamp(25px, 6vw, 38px);
}}
p {{
    font-size: clamp(17px, 4.3vw, 21px);
    line-height: 1.9;
    margin: 13px 0;
}}
.small {{ font-size: 14px; color: #a26e80; }}
.days {{
    font-size: clamp(72px, 22vw, 145px);
    line-height: 1;
    margin: 24px 0 10px;
    color: #f05f8f;
    font-weight: 800;
    text-shadow: 0 8px 25px rgba(240,95,143,.23);
}}
button {{
    margin-top: 25px;
    padding: 13px 28px;
    border: 0;
    border-radius: 999px;
    background: linear-gradient(135deg, #f66f9c, #d94e7c);
    color: white;
    font-size: 17px;
    font-weight: 700;
    cursor: pointer;
    box-shadow: 0 10px 24px rgba(217,78,124,.28);
    transition: transform .18s ease, box-shadow .18s ease;
}}
button:active {{ transform: scale(.96); }}
.heart {{
    position: relative;
    width: 115px;
    height: 102px;
    margin: 42px auto 35px;
    transform: rotate(-45deg);
    background: #f15386;
    animation: heartbeat 1.05s infinite;
    box-shadow: 0 15px 35px rgba(241,83,134,.35);
}}
.heart::before,
.heart::after {{
    content: "";
    position: absolute;
    width: 115px;
    height: 102px;
    border-radius: 50%;
    background: #f15386;
}}
.heart::before {{ top: -57px; left: 0; }}
.heart::after {{ left: 57px; top: 0; }}
.memory {{
    min-height: 165px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    border-radius: 22px;
    background: #fff7fa;
    border: 1px dashed #eaa4bc;
    font-size: clamp(18px, 4.6vw, 22px);
    line-height: 1.9;
}}
.letter {{
    text-align: left;
    line-height: 2;
    background: #fffdfd;
    padding: 28px 24px;
    border-radius: 18px;
    border-left: 5px solid #ed88aa;
}}
.signature {{
    text-align: right;
    color: #cf527d;
    font-weight: 700;
    margin-top: 24px;
}}
.float-heart {{
    position: fixed;
    bottom: -50px;
    opacity: .58;
    animation: floatUp linear forwards;
    pointer-events: none;
}}
#hugText {{
    display: none;
    margin-top: 24px;
    padding: 18px;
    border-radius: 18px;
    background: #fff0f5;
    color: #d34877;
    font-weight: 700;
    font-size: 19px;
}}
@keyframes fade {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}
@keyframes heartbeat {{
    0%, 100% {{ transform: rotate(-45deg) scale(1); }}
    15% {{ transform: rotate(-45deg) scale(1.13); }}
    30% {{ transform: rotate(-45deg) scale(1); }}
    45% {{ transform: rotate(-45deg) scale(1.09); }}
}}
@keyframes floatUp {{
    to {{
        transform: translateY(-115vh) rotate(360deg);
        opacity: 0;
    }}
}}
</style>
</head>
<body>

<section class="page active" id="p1">
  <div class="card">
    <div class="small">一份来自王尔波的小心意</div>
    <h1>周凡寓，你好呀</h1>
    <p>我偷偷做了一个小东西送给你。</p>
    <p>它不贵重，也不复杂，<br>只是装着一些我想认真告诉你的话。</p>
    <button onclick="go(2)">点击开启惊喜</button>
  </div>
</section>

<section class="page" id="p2">
  <div class="card">
    <h2>我们的故事，从这一天开始</h2>
    <p>2026 年 7 月 2 日</p>
    <p>从我们相识到今天，已经过去了</p>
    <div class="days">{days_known}</div>
    <p>天</p>
    <p class="small">每一天，都让这段相遇变得更特别。</p>
    <button onclick="go(3)">继续</button>
  </div>
</section>

<section class="page" id="p3">
  <div class="card">
    <h2>有几句话想告诉你</h2>
    <div class="memory" id="memory">
      第一次认识你的时候，我没有想到，<br>你后来会变成一个让我如此在意的人。
    </div>
    <button id="memoryBtn" onclick="nextMemory()">再点一下</button>
  </div>
</section>

<section class="page" id="p4">
  <div class="card">
    <h2>有些相遇，会让人心里发光</h2>
    <div class="heart"></div>
    <p>你就是那个，<br>让我开始期待每一天的人。</p>
    <p>我希望以后还有很多普通又特别的日子，<br>可以和你一起慢慢经历。</p>
    <button onclick="go(5)">打开最后一封信</button>
  </div>
</section>

<section class="page" id="p5">
  <div class="card">
    <h2>写给周凡寓</h2>
    <div class="letter">
      <p>周凡寓：</p>
      <p>
        很开心在 2026 年 7 月 2 日认识了你。
        从那一天开始，生活里好像多了一份期待：
        期待你的消息，期待和你分享小事，也期待慢慢了解更多关于你的故事。
      </p>
      <p>
        和你相处的时间也许还不算很长，
        但你已经让很多普通的时刻变得不一样。
        有时候只是看到你的名字，心情也会悄悄变好。
      </p>
      <p>
        我不急着给我们的故事定义什么，
        我只是很珍惜现在，也认真期待以后。
        希望接下来的日子里，我可以继续陪你聊天、陪你开心，
        和你一起把平凡的日子变成值得记住的日子。
      </p>
      <p>
        谢谢你出现在我的生活里。
      </p>
      <div class="signature">—— 王尔波</div>
    </div>
    <button onclick="receiveHug()">领取王尔波的抱抱</button>
    <div id="hugText">
      抱抱已成功送达 💗<br>
      有效期：永远<br>
      使用次数：不限
    </div>
  </div>
</section>

<script>
let memoryIndex = 0;
const memories = [
  "第一次认识你的时候，我没有想到，<br>你后来会变成一个让我如此在意的人。",
  "和你聊天的时候，哪怕只是很普通的小事，<br>也会让我觉得这一天变得更有意思。",
  "你可能不知道，有时候看到你的消息，<br>我会在屏幕前偷偷开心很久。",
  "我不急着给我们的故事写下结局。<br>我只希望，可以陪你把下一页慢慢写完。"
];

function go(n) {{
  document.querySelectorAll(".page").forEach(p => p.classList.remove("active"));
  document.getElementById("p" + n).classList.add("active");
  window.scrollTo({{top: 0, behavior: "smooth"}});
}}

function nextMemory() {{
  memoryIndex++;
  if (memoryIndex < memories.length) {{
    document.getElementById("memory").innerHTML = memories[memoryIndex];
  }}
  if (memoryIndex === memories.length - 1) {{
    const btn = document.getElementById("memoryBtn");
    btn.innerText = "还有最后一个惊喜";
    btn.onclick = () => go(4);
  }}
}}

function receiveHug() {{
  document.getElementById("hugText").style.display = "block";
  for (let i = 0; i < 28; i++) {{
    setTimeout(createFloatingHeart, i * 80);
  }}
}}

function createFloatingHeart() {{
  const heart = document.createElement("div");
  heart.className = "float-heart";
  heart.innerHTML = Math.random() > .5 ? "💗" : "💕";
  heart.style.left = Math.random() * 100 + "vw";
  heart.style.fontSize = (18 + Math.random() * 25) + "px";
  heart.style.animationDuration = (3 + Math.random() * 3) + "s";
  document.body.appendChild(heart);
  setTimeout(() => heart.remove(), 6500);
}}

setInterval(() => {{
  if (Math.random() > .55) createFloatingHeart();
}}, 1300);
</script>
</body>
</html>
"""

components.html(html, height=900, scrolling=True)
