#!/usr/bin/env python3
"""Pozycja ogłoszeń AGRII w LOKALNYM wyszukiwaniu OLX — najmocniejszy zmierzony predyktor kontaktu.

Dla każdego miasta z rejestru pyta publiczne API o „wapno nawozowe" w kat. 4368 z filtrem
`city_id` + `distance=50` i szuka, na której pozycji stoi AGRIA. Zwraca też `visible_total_count`,
czyli gęstość konkurencji w promieniu.

Pomiar 28.08.2026 (53 miasta, 200 ogłoszeń, 8 dni emisji):
    pozycja 1–20   → 0,227 odsłony numeru na ogłoszenie
    pozycja 21–50  → 0,114
    pozycja >50    → 0,062     (112 z 200 ogłoszeń stoi właśnie tutaj)

Wynik: data/olx/pozycje-YYYY-MM-DD.json
"""
import sys, json, time
sys.path.insert(0,'/home/host476470/projekty/agria/scripts/olx')
import olx_market as m
D='/home/host476470/projekty/agria/data/olx/'
posted=json.load(open(D+'posted.json'))
plan={(r['siatka'],r['city']):r for r in json.load(open(D+'plan-ogloszen.json'))}
h=json.load(open(D+'statystyki.json')); now=h[-1]['per_ogloszenie']
cid={}; wynik={}
for k,v in posted.items():
    # city_id bierzemy z JAWNEGO pola rejestru (od 28.08, T-106), nie z nazwy klucza: po
    # przełożeniu ogłoszenia external_id niesie city_id sprzed przekładki, a plan nie zna
    # nowych par (siatka, miasto). Parsowanie klucza zostaje tylko jako fallback dla wpisów
    # sprzed migracji rejestru.
    s=v.get('wariant') or k[len('agria-'):].rsplit('-',1)[0]
    c=v.get('city_id') or (plan.get((s,v['city'])) or {}).get('city_id')
    if c: cid[v['city']]=c
    od,tel=now.get(str(v['advert_id']),[0,0])
    a=wynik.setdefault(v['city'],[0,0,0]); a[0]+=1; a[1]+=od; a[2]+=tel
out=[]
for miasto,c in cid.items():
    poz=[]; vis=None
    for off in (0,50):
        try:
            r=m.fetch({"query":"wapno nawozowe","limit":50,"offset":off,"category_id":4368,
                       "city_id":c,"distance":50})
        except Exception as e:
            time.sleep(2); continue
        if off==0: vis=r.get("metadata",{}).get("visible_total_count")
        for i,o in enumerate(r.get("data",[])):
            u=o.get("user") or {}
            if 'AGRIA' in (u.get("company_name") or u.get("name") or "").upper(): poz.append(off+i+1)
        time.sleep(0.3)
    n,od,tel=wynik[miasto]
    out.append(dict(miasto=miasto,gestosc=vis,najlepsza=min(poz) if poz else None,
                    w_top20=sum(1 for p in poz if p<=20),ogl=n,odslony=od,tel=tel))
sciezka=D+'pozycje-'+time.strftime('%Y-%m-%d')+'.json'
json.dump(out,open(sciezka,'w'),ensure_ascii=False,indent=1)
print("gotowe:",len(out),"→",sciezka)
