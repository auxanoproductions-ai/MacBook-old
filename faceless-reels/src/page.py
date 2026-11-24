import json,html,subprocess
E=html.escape;S='/tmp/claude-0/-home-user-MacBook-old/b74287e2-0b94-538c-97c5-3439bf78bfa4/scratchpad'
R=json.load(open(S+'/reels.json'))
RES={
"COPY":("Steps + link","1. Install Google app (has Lens) on your phone.\n2. Sign into the same Google account in Chrome on your laptop.\n3. Open Lens, point at the page, tap Text.\n4. Select text, tap 'Copy to computer', pick your laptop.\n5. Press Ctrl+V on the laptop.","https://lens.google/"),
"TRANSLATE":("Prompt + link","Here's a photo of a menu. Translate every dish to English. For each one, explain in one line what it is, say if it's vegetarian, and mark anything spicy. Recommend 3 dishes for a first-timer.","https://translate.google.com/"),
"NO":("Prompt","Help me politely say no to this request. Keep it kind, firm, and under 60 words. Don't over-apologize or give long excuses. Offer one small alternative only if it's easy for me. Give 3 versions: warm, neutral, short. Request: [paste]",""),
"COVER":("Prompt","Write a 150-word cover letter for this job. Open with why this company specifically. Use 2 achievements from my resume with numbers. Match the job's keywords. End with a confident, simple close. No clichés like 'I am writing to apply'. Resume: [paste]. Job post: [paste].",""),
"EXCEL":("Prompt","You're an Excel expert. Give me the exact formula for this, assuming data starts in row 2: [describe in plain English]. Then explain it in one line and tell me how to drag it down. If Google Sheets differs, give that version too.",""),
"SUMMARY":("Prompt + link","Summarize this YouTube video in 5 key points with timestamps. Then give me the 1 most useful takeaway and tell me which part is worth watching in full. Link: [paste]","https://gemini.google.com/"),
"WISH":("Prompt","Write a heartfelt birthday message for my [relation], [name]. Use these real memories: 1) [memory] 2) [memory] 3) [memory]. Make it warm, a little funny, and under 100 words. End with a line that makes them feel truly seen. Give a short WhatsApp version too.",""),
"DEAL":("Prompt","Write a polite, confident message to negotiate a lower price. What I'm buying: [item/service]. Their price: [x]. My target: [y]. My reasons: [competitor price, loyalty, paying upfront, etc.]. Keep it friendly, under 80 words, and end with a clear question. Also give me a reply if they say no.",""),
"POWER":("Prompt","Here are my home appliances with wattage (if known) and daily hours of use: [list]. My electricity rate is [rate per unit]. Estimate the monthly cost of each, rank them highest to lowest, and give me 5 specific changes to cut my bill, with estimated savings for each.",""),
"QUIZ":("Prompt","Quiz me on these notes. Ask 10 questions, one at a time, mixing multiple choice and short answer. Wait for my answer before the next one. After each answer, tell me if I'm right and explain briefly. At the end, list the topics I should revise. Notes: [paste]",""),
}
dur=lambda k:subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'/home/user/MacBook-old/faceless-reels/videos/{k}']).decode().strip()
cards=[]
for r in R:
    v=f"reel-{r['id']:02d}-{r['kw'].lower()}.mp4";d=float(dur(v));kind,res,link=RES[r['kw']]
    hk="".join(f'<li><span class="sc">{s}</span><span class="ht">{E(h)}</span><button class="cp" data-c="{E(h)}">Copy</button></li>' for h,s in r['hooks'])
    vo=" ".join(s['vo'] for s in r['scenes'])
    dm=f"Hey! 👋 Here's what you asked for:\n\n{res}" + (f"\n\nLink: {link}" if link else "") + "\n\nFollow for one AI trick a day. 🚀"
    cap=f"{r['hooks'][0][0]} 🤯\n\nComment {r['kw']} and I'll DM you the free {kind.split(' ')[0].lower()}.\n\nSave this for later. Share it with someone who needs it.\n\n#ai #chatgpt #aitools #productivity #lifehacks"
    cards.append(f'''<article class="card"><div class="vid"><video controls preload="metadata" poster="thumb-{r['id']}.jpg" src="videos/{v}"></video><a class="dl" href="videos/{v}" download>Download MP4 · {d:.0f}s</a></div>
<div class="info"><header><span class="n">#{r['id']}</span><h2>{E(r['title'])}</h2></header>
<div class="lbl">3 hooks <small>(the video uses hook 1; swap in 2 or 3 for reposts)</small></div><ol class="hooks">{hk}</ol>
<details><summary>Voiceover script</summary><p>{E(vo)}</p></details>
<details><summary>Caption to post</summary><pre>{E(cap)}</pre><button class="cp" data-c="{E(cap)}">Copy caption</button></details>
<div class="lbl">Comment keyword</div><span class="kw">{r['kw']}</span>
<div class="lbl">Auto-DM message ({E(kind)})</div><pre class="pr">{E(dm)}</pre><button class="cp" data-c="{E(dm)}">Copy DM</button></div></article>''')
guide='''<section class="card guide"><h2>Comment-to-DM system</h2>
<h3>1. Set up the tool (one time, about 20 min)</h3><ol>
<li>Switch your Instagram to a <b>Professional</b> account (Creator or Business).</li>
<li>Sign up at <b>manychat.com</b> and connect Instagram. The free plan covers keyword auto-DMs for small accounts.</li>
<li>In Instagram settings, go to Messages and turn on <b>Allow access to messages</b> in connected tools.</li></ol>
<h3>2. Build one automation per reel</h3><ol>
<li>ManyChat → Automation → <b>New</b> → trigger: "User comments on your post or reel".</li>
<li>Pick the reel. Keyword = the word above (for example COPY). Add lowercase too.</li>
<li>Turn on <b>auto public reply</b>: "Sent! Check your DMs 📩". Public replies boost reach.</li>
<li>DM step 1: "Want the resource? Tap below 👇" with a button. A button tap opens the chat window, so delivery works.</li>
<li>DM step 2: paste the auto-DM message from the card.</li>
<li>Optional step 3: "Follow me to get one new trick daily" + ask for an email for your free AI guide. This builds your list.</li></ol>
<h3>3. Get more comments</h3><ul>
<li>Put the keyword <b>on screen</b>, in the <b>voiceover</b>, and in the <b>caption</b>. All 10 reels do this already.</li>
<li>Use one short keyword in capitals. People copy what they see.</li>
<li>Pin your own comment: "Comment KEYWORD 👇".</li>
<li>Reply to the first 30 to 50 comments by hand in the first hour. Early replies push the reel further.</li>
<li>Promise something specific: "the exact prompt", not "more info".</li>
<li>Post when your audience is online. Check Insights, then Audience, then Most active times.</li>
<li>Share the reel to your Story with a "Comment KEYWORD" sticker.</li></ul>
<h3>4. Rules to stay safe</h3><ul>
<li>Never DM people who didn't comment or message first.</li>
<li>Keep DMs helpful. No hard sales pitch in the first message.</li>
<li>Test every keyword from a second account before posting.</li></ul></section>'''
doc=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Faceless AI Reels</title><style>
:root{{--bg:#f6f6f3;--card:#fff;--ink:#1a1a1a;--mute:#666;--line:#e3e3de;--acc:#5b4bdb;--good:#1a7f4b}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111114;--card:#1b1b20;--ink:#eee;--mute:#9a9aa3;--line:#2c2c33;--acc:#9d92ff;--good:#4fd18b}}}}
:root[data-theme="dark"]{{--bg:#111114;--card:#1b1b20;--ink:#eee;--mute:#9a9aa3;--line:#2c2c33;--acc:#9d92ff;--good:#4fd18b}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,sans-serif}}.wrap{{max-width:1000px;margin:auto;padding:24px 16px}}
h1{{margin:0}}.sub{{color:var(--mute)}}.card{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;margin:16px 0}}
article.card{{display:grid;grid-template-columns:260px 1fr;gap:20px}}@media(max-width:700px){{article.card{{grid-template-columns:1fr}}}}
video{{width:100%;border-radius:12px;background:#000;aspect-ratio:9/16}}.dl{{display:block;text-align:center;margin-top:8px;color:var(--acc);font-weight:600;text-decoration:none}}
header{{display:flex;gap:10px;align-items:center}}h2{{margin:0;font-size:19px}}.n{{color:var(--acc);font-weight:800}}
.lbl{{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--mute);margin:14px 0 6px}}.lbl small{{text-transform:none;letter-spacing:0}}
.hooks{{list-style:none;padding:0;margin:0}}.hooks li{{display:flex;gap:10px;align-items:center;padding:6px 0;border-bottom:1px solid var(--line)}}.sc{{color:var(--good);font-weight:800;min-width:26px}}.ht{{flex:1;font-weight:600}}
.cp{{border:1px solid var(--line);background:transparent;color:var(--mute);font-size:12px;padding:3px 8px;border-radius:6px;cursor:pointer}}
.kw{{background:var(--acc);color:#fff;font-weight:800;padding:3px 12px;border-radius:6px}}pre{{white-space:pre-wrap;font:13px/1.45 ui-monospace,monospace;background:var(--bg);border:1px dashed var(--line);border-radius:8px;padding:10px;margin:0 0 6px}}
details{{margin-top:10px}}summary{{cursor:pointer;font-weight:600}}.guide h3{{margin:18px 0 6px;font-size:16px}}.guide li{{margin:4px 0}}
</style></head><body><div class="wrap"><h1>10 Faceless AI Reels</h1><p class="sub">Every reel is ready to post: 1080×1920 video with voiceover, music, motion graphics, captions and CTA. Each one comes with 3 hooks, a caption, an auto-DM message and the resource to send. Hook scores are estimates.</p>
{guide}{"".join(cards)}</div><script>document.querySelectorAll('.cp').forEach(b=>b.onclick=()=>{{try{{navigator.clipboard.writeText(b.dataset.c);const o=b.textContent;b.textContent='Copied';setTimeout(()=>b.textContent=o,1200)}}catch(e){{}}}})</script></body></html>'''
open('/home/user/MacBook-old/faceless-reels/index.html','w').write(doc)
