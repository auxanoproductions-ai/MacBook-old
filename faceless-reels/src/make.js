const {chromium}=require('playwright');const fs=require('fs');const {execSync,spawn}=require('child_process');
const S=__dirname,OUT='/home/user/MacBook-old/faceless-reels/videos';fs.mkdirSync(OUT,{recursive:true});
const reels=JSON.parse(fs.readFileSync(S+'/reels.json'));const only=process.argv.slice(2).map(Number);
const FPS=30,GAP=0.35,sh=c=>execSync(c,{stdio:['pipe','pipe','pipe']}).toString().trim();
(async()=>{const b=await chromium.launch();
for(const r of reels){if(only.length&&!only.includes(r.id))continue;const W=`${S}/w${r.id}`;fs.mkdirSync(W,{recursive:true});
 let t=0;const tl=[];const parts=[];
 r.scenes.forEach((sc,i)=>{const f=`${W}/s${i}.wav`;sh(`echo ${JSON.stringify(sc.vo)} | piper -m ${S}/voice/en-us-lessac-medium.onnx --length_scale 0.92 -f ${f}`);
  const d=parseFloat(sh(`ffprobe -v error -show_entries format=duration -of csv=p=0 ${f}`));const dur=d+GAP+(sc.k=='cta'?1.2:0)+(sc.k=='chat'?0.8:0);
  tl.push({start:t,end:t+dur});t+=dur;sh(`ffmpeg -y -v error -i ${f} -af apad=whole_dur=${dur.toFixed(3)} -ar 44100 -ac 1 ${W}/p${i}.wav`);parts.push(`file '${W}/p${i}.wav'`)});
 fs.writeFileSync(W+'/list.txt',parts.join('\n'));sh(`ffmpeg -y -v error -f concat -safe 0 -i ${W}/list.txt -c copy ${W}/vo.wav`);
 const D=t.toFixed(3);
 sh(`ffmpeg -y -v error -f lavfi -i "aevalsrc='0.035*(sin(2*PI*220*t)+sin(2*PI*261.6*t)+sin(2*PI*329.6*t))*(0.6+0.4*sin(2*PI*0.25*t))+0.25*sin(2*PI*55*t)*exp(-mod(t,0.6)*14)':s=44100:d=${D}" -af "lowpass=f=1800,afade=t=in:d=1,afade=t=out:st=${(t-1.5).toFixed(2)}:d=1.5" ${W}/music.wav`);
 sh(`ffmpeg -y -v error -i ${W}/vo.wav -i ${W}/music.wav -filter_complex "[0]volume=1.6[v];[1]volume=0.35[m];[v][m]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95" ${W}/audio.m4a`);
 const p=await b.newPage({viewport:{width:540,height:960},deviceScaleFactor:2});await p.goto('file://'+S+'/tpl.html');await p.evaluate(([r,tl])=>init(r,tl),[r,tl]);
 const ff=spawn('ffmpeg',['-y','-v','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-i',W+'/audio.m4a','-c:v','libx264','-pix_fmt','yuv420p','-preset','veryfast','-crf','20','-c:a','aac','-b:a','160k','-shortest','-movflags','+faststart',`${OUT}/reel-${String(r.id).padStart(2,'0')}-${r.kw.toLowerCase()}.mp4`]);
 await p.evaluate(x=>render(x),1.6);await p.screenshot({path:`${OUT}/../thumb-${r.id}.jpg`,type:'jpeg',quality:80});
 const N=Math.ceil(t*FPS);for(let f=0;f<N;f++){await p.evaluate(x=>render(x),f/FPS);const img=await p.screenshot({type:'jpeg',quality:90});if(!ff.stdin.write(img))await new Promise(z=>ff.stdin.once('drain',z))}
 ff.stdin.end();await new Promise(z=>ff.on('close',z));await p.close();
 r.duration=+t.toFixed(1);console.log('done',r.id,r.duration+'s');}
await b.close();})();
