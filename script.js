const scenes=[...document.querySelectorAll('.scene')];
const steps=[...document.querySelectorAll('.chapter-nav i')];
let current=0,soundOn=true,audioCtx=null,typed=false;

function initAudio(){
  if(!audioCtx) audioCtx=new (window.AudioContext||window.webkitAudioContext)();
  if(audioCtx.state==='suspended') audioCtx.resume();
}
function note(freq=660,duration=.08,delay=0,volume=.035){
  if(!soundOn)return; initAudio();
  const o=audioCtx.createOscillator(),g=audioCtx.createGain();
  o.type='sine';o.frequency.value=freq;g.gain.setValueAtTime(0,audioCtx.currentTime+delay);
  g.gain.linearRampToValueAtTime(volume,audioCtx.currentTime+delay+.01);
  g.gain.exponentialRampToValueAtTime(.0001,audioCtx.currentTime+delay+duration);
  o.connect(g);g.connect(audioCtx.destination);o.start(audioCtx.currentTime+delay);o.stop(audioCtx.currentTime+delay+duration+.02);
}
function messageSound(){note(740,.1,0,.035);note(990,.12,.08,.025)}
function softChime(){note(523,.35,0,.02);note(659,.4,.13,.018);note(784,.5,.26,.015)}
function toggleSound(){soundOn=!soundOn;document.getElementById('soundBtn').textContent=soundOn?'♪':'×';showToast(soundOn?'声音已开启':'声音已关闭');if(soundOn)messageSound()}
function beginStory(){initAudio();messageSound();go(1)}
function go(index){
  if(index<0||index>=scenes.length)return;
  const video=scenes[current].querySelector('video');if(video&&!video.paused)video.pause();
  scenes[current].classList.remove('active');current=index;scenes[current].classList.add('active');
  window.scrollTo({top:0,left:0,behavior:'auto'});document.documentElement.scrollTop=0;document.body.scrollTop=0;
  steps.forEach((s,i)=>s.classList.toggle('on',i===Math.min(index,steps.length-1)));
  document.getElementById('chapterName').textContent=scenes[current].dataset.name;
  if(index===2)startTyping();if(index===5)updateCountdown();
}
function answerQuiz(answer){
  const chat=document.getElementById('nightChat'),b=document.createElement('div');b.className='bubble me';b.textContent=answer;chat.appendChild(b);
  document.querySelectorAll('.choice').forEach(x=>x.disabled=true);document.getElementById('verdict').classList.add('show');document.getElementById('quizNext').classList.add('show');messageSound();
}
function startTyping(){
  if(typed)return;typed=true;const el=document.getElementById('confessionText'),text=el.dataset.text;let i=0;
  const timer=setInterval(()=>{el.textContent=text.slice(0,++i);if(i>=text.length){clearInterval(timer);el.classList.remove('cursor')}},22);
}
function sendReply(){document.getElementById('replyMessage').classList.add('show');document.getElementById('replyBtn').style.display='none';document.getElementById('confessionNext').classList.add('show');messageSound()}
const routeCopies=[
  '八年前，你还是重庆课桌下偷偷看书的初中生。那时你大概没想过，有一天真的会坐上火车，去故事发生的地方。',
  '从四平到鞍山，高铁只有一个小时。出站时空气和四平差不多，可你知道这里不一样——因为你等了八年，才站在这里。',
  '你站在礼堂外，想告诉那时的自己：你后来走了很远的路，也没有变成你害怕的那种大人。那些书页，终于变成了脚下走过的路。'
];
function routeStory(i,el){document.querySelectorAll('.stop').forEach(x=>x.classList.remove('on'));el.classList.add('on');const box=document.getElementById('routeStory');box.style.opacity=0;setTimeout(()=>{box.textContent=routeCopies[i];box.style.opacity=1},180);note(520+i*100,.18,0,.02)}
function revealPromise(el){el.classList.toggle('open');note(620+Math.random()*200,.14,0,.018)}
function openLetter(){softChime();document.getElementById('letterIntro').style.display='none';document.getElementById('letterPane').classList.add('show');window.scrollTo({top:0,left:0,behavior:'smooth'})}
function receiveLetter(){confetti();softChime();setTimeout(()=>go(8),450)}
function updateCountdown(){
  const target=new Date('2026-08-14T00:00:00+08:00').getTime();let diff=Math.max(0,target-Date.now());
  const d=Math.floor(diff/86400000);diff%=86400000;const h=Math.floor(diff/3600000);diff%=3600000;const m=Math.floor(diff/60000),s=Math.floor((diff%60000)/1000);
  const vals=[d,h,m,s];document.querySelectorAll('#countdown strong').forEach((el,i)=>el.textContent=String(vals[i]).padStart(2,'0'));
}
setInterval(()=>{if(current===5)updateCountdown()},1000);
function showToast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');clearTimeout(window.toastTimer);window.toastTimer=setTimeout(()=>t.classList.remove('show'),1800)}
function confetti(){const colors=['#ef9b67','#8f7bf4','#78cbd5','#f6f0e7'];for(let i=0;i<48;i++){const p=document.createElement('i');p.className='confetti';p.style.left=Math.random()*100+'vw';p.style.top='-20px';p.style.background=colors[i%colors.length];p.style.setProperty('--x',(Math.random()*180-90)+'px');p.style.animationDelay=Math.random()*.45+'s';document.body.appendChild(p);setTimeout(()=>p.remove(),3200)}}
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&current>0)go(current-1);if((e.key==='Enter'||e.key===' ')&&document.activeElement.classList.contains('promise')){e.preventDefault();revealPromise(document.activeElement)}});
