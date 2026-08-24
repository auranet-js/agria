// Panel WordPressa AGRII oczami Claude'a — bez pozyczania przegladarki Janka.
//
// Docelowe miejsce: ~/opt/pptr/narzedzia/agria-panel.mjs (zeby dzialalo `pptr agria-panel`).
// Instalacja:  cp scripts/agria-panel.mjs ~/opt/pptr/narzedzia/
//
// Wczytuje ciasteczka sesji z ~/secrets/agria/wp-sesja.json (generuje je
// scripts/wp_sesja.sh), wchodzi pod podany adres wp-admin i zwraca wynik.
//
// Uzycie:
//   pptr agria-panel <URL> [plik.png] [rankmath|tekst|zrzut]
//
// Przyklad:
//   pptr agria-panel "https://agria.pl/wp-admin/post.php?post=2796&action=edit" /tmp/x.png rankmath

import puppeteer from 'puppeteer-core';
import { readFileSync } from 'fs';
import { homedir } from 'os';

const [URL_, PLIK, TRYB = 'rankmath'] = process.argv.slice(2);
if (!URL_) { console.error('Uzycie: pptr agria-panel <URL> [plik.png] [rankmath|tekst|zrzut]'); process.exit(1); }

const sesja = JSON.parse(readFileSync(`${homedir()}/secrets/agria/wp-sesja.json`, 'utf8'));
const ciasteczka = Object.entries(sesja.cookies).map(([name, value]) => ({
  name, value, domain: sesja.domena, path: '/', httpOnly: true, secure: true, sameSite: 'Lax',
}));

const b = await puppeteer.launch({executablePath: process.env.CHROME_BIN, headless: true,
  args: ['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--no-zygote','--single-process']});
const p = await b.newPage();
await p.setViewport({width: 1600, height: 1000});
await b.setCookie(...ciasteczka);
await p.goto(URL_, {waitUntil: 'networkidle2', timeout: 120000});
await new Promise(r => setTimeout(r, 3000));

const zalogowany = await p.evaluate(() => !document.body.classList.contains('login') && !location.href.includes('wp-login.php'));
if (!zalogowany) {
  console.log(JSON.stringify({blad: 'sesja nieaktywna — odnow: bash scripts/wp_sesja.sh', url: p.url()}, null, 1));
  await b.close(); process.exit(2);
}

if (TRYB === 'rankmath') {
  await p.evaluate(() => {
    document.querySelectorAll('.rank-math-result-title, .rank-math-analyzer-title, [class*="accordion"] button')
      .forEach(e => { try { e.click(); } catch (_) {} });
  });
  await new Promise(r => setTimeout(r, 1200));
  const r = await p.evaluate(() => {
    const tekst = e => e ? (e.innerText || '').replace(/\s+/g, ' ').trim() : '';
    const wynik = [...document.querySelectorAll('[class*="seo-score"], .rank-math-total-score, button')]
      .map(tekst).find(t => /^\d{1,3}\s*\/\s*100$/.test(t)) || null;
    const zle = [...document.querySelectorAll('.rank-math-test-result.bad, li.bad, .test-result.bad')].map(tekst);
    const dobre = [...document.querySelectorAll('.rank-math-test-result.good, li.good, .test-result.good')].map(tekst);
    return {
      wynik,
      fraza: (document.querySelector('.rank-math-focus-keyword input, #rank_math_focus_keyword') || {}).value || null,
      doPoprawy: zle.filter(Boolean),
      zaliczone: dobre.filter(Boolean).length,
    };
  });
  console.log(JSON.stringify(r, null, 1));
} else if (TRYB === 'tekst') {
  console.log((await p.evaluate(() => document.body.innerText)).slice(0, 12000));
}

if (PLIK) await p.screenshot({path: PLIK, fullPage: false});
await b.close();
