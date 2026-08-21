// Zrzut OLX oczami klienta na telefonie (390x844, DPR 2) + pomiar kadru miniatury.
//
// Uruchamianie: skrypt musi leżeć w ~/opt/pptr/narzedzia/ (runner `pptr` nie widzi
// ścieżek spoza tego katalogu — brak puppeteer-core w NODE_PATH):
//   cp scripts/olx/zrzut_mobile.mjs ~/opt/pptr/narzedzia/agria-olx-mobile.mjs
//   pptr agria-olx-mobile <URL> <plik.png> ["fraza do przewinięcia"]
//
// Reklamy są blokowane: skrypty baxter/googlesyndication rozpychają layout do 887 px
// i psują pomiar (karta robi się szersza niż ekran, tytuł łamie się po literze).
import puppeteer from 'puppeteer-core';
const [URL, PLIK, FRAZA] = process.argv.slice(2);
const BLOK = /googlesyndication|doubleclick|baxter|btloader|adnxs|criteo|googletagservices|amazon-adsystem|onetrust|hotjar/;
const b = await puppeteer.launch({executablePath: process.env.CHROME_BIN, headless:true,
  args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--no-zygote','--single-process']});
const p = await b.newPage();
// UA MUSI być mobilny: przy desktopowym OLX podmienia meta viewport na width=887
// i mierzy się wtedy layout, którego klient na telefonie nigdy nie zobaczy.
await p.setUserAgent('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1');
await p.setRequestInterception(true);
p.on('request', r => BLOK.test(r.url()) ? r.abort() : r.continue());
await p.setViewport({width:390,height:844,isMobile:true,hasTouch:true,deviceScaleFactor:2});
await p.goto(URL, {waitUntil:'networkidle2', timeout:120000});
await p.evaluate(()=>{const x=Array.from(document.querySelectorAll('button')).find(e=>/Akceptuj niezb/i.test(e.textContent));x&&x.click();});
await new Promise(r=>setTimeout(r,3000));
if (FRAZA) {
  const y = await p.evaluate(f=>{
    const el = Array.from(document.querySelectorAll('h4,h6,a,p')).find(e=>e.textContent.includes(f));
    if(!el) return null;
    return (el.closest('[data-cy="l-card"]')||el).getBoundingClientRect().top + scrollY - 70;
  }, FRAZA);
  if (y!==null) { await p.evaluate(v=>scrollTo(0,v), y); await new Promise(r=>setTimeout(r,2500)); }
}
const pomiar = await p.evaluate(()=>({
  viewport: innerWidth,
  kadry: Array.from(document.querySelectorAll('[data-cy="l-card"] img')).map(i=>{
    const r=i.getBoundingClientRect();
    return {w:Math.round(r.width), h:Math.round(r.height), ratio:+(r.width/r.height).toFixed(2),
            fit:getComputedStyle(i).objectFit, nat:i.naturalWidth+'x'+i.naturalHeight};
  }).filter(k=>k.h>40).slice(0,5)
}));
await p.screenshot({path:PLIK});
console.log(JSON.stringify(pomiar,null,1));
await b.close();
