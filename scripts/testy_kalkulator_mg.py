# -*- coding: utf-8 -*-
"""T-044 — zestaw testow kalkulatora wapnowania z modulem Mg (produkcja)."""
import json, re, sys, urllib.parse, urllib.request
from decimal import Decimal, ROUND_HALF_UP

BASE='https://agria.pl'
AJAX=BASE+'/wp-admin/admin-ajax.php'

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'agria-test/1.0'}),timeout=60).read().decode('utf-8','replace')

NONCE=re.search(r'nonce:\s*"([a-f0-9]+)"',get(BASE+'/kalkulator-wapnowania/?cb=test044')).group(1)

def call(**kw):
    kw.update(action='agria_calc_liming',nonce=NONCE)
    body=urllib.parse.urlencode(kw).encode()
    raw=urllib.request.urlopen(urllib.request.Request(AJAX,data=body,headers={'User-Agent':'agria-test/1.0'}),timeout=60).read().decode('utf-8','replace')
    try: return json.loads(raw)
    except Exception: return {'_raw':raw}

OK=[]; FAIL=[]
def check(name,cond,detail=''):
    (OK if cond else FAIL).append(name+((' :: '+detail) if detail and not cond else ''))

# ---- zrodlo prawdy: tablice IUNG z class-iung-data.php ----
ARABLE={
 'bardzo_lekka':{'5.0':[0.2,0.2,0],'4.9':[0.5,0.5,0],'4.8':[0.8,0.8,0],'4.7':[1.0,1.0,0],'4.6':[1.3,1.3,0],'4.5':[1.6,1.6,0],'4.4':[1.8,1.8,0],'4.3':[2.0,2.0,0],'4.2':[2.2,2.2,0],'4.1':[2.4,2.4,0],'4.0':[2.8,2.8,0],'3.9':[3.1,3.1,0],'3.8':[3.4,3.4,0]},
 'lekka':{'5.5':[0.2,0.2,0],'5.4':[0.5,0.5,0],'5.3':[0.9,0.9,0],'5.2':[1.2,1.2,0],'5.1':[1.5,1.5,0],'5.0':[1.8,1.8,0],'4.9':[2.1,2.1,0],'4.8':[2.3,2.3,0],'4.7':[2.6,2.6,0],'4.6':[2.9,2.9,0],'4.5':[3.1,3.1,0],'4.4':[3.4,3.4,0],'4.3':[4.5,3.5,1.0],'4.2':[4.7,3.5,1.2],'4.1':[5.5,3.5,2.0],'4.0':[5.9,3.5,2.4],'3.9':[6.3,3.5,2.8],'3.8':[6.5,3.5,3.0]},
 'srednia':{'6.0':[0.4,0.4,0],'5.9':[0.8,0.8,0],'5.8':[1.2,1.2,0],'5.7':[1.6,1.6,0],'5.6':[2.0,2.0,0],'5.5':[2.4,2.4,0],'5.4':[2.8,2.8,0],'5.3':[3.2,3.2,0],'5.2':[3.6,3.6,0],'5.1':[3.9,3.9,0],'5.0':[4.2,4.2,0],'4.9':[4.4,4.4,0],'4.8':[4.8,4.8,0],'4.7':[5.0,5.0,0],'4.6':[5.4,5.0,0.4],'4.5':[5.8,5.0,0.8],'4.4':[6.2,5.0,1.2],'4.3':[6.4,5.0,1.4],'4.2':[6.6,5.0,1.6],'4.1':[7.0,5.0,2.0],'4.0':[7.4,5.0,2.4],'3.9':[7.8,5.0,2.8]},
 'ciezka':{'6.3':[0.2,0.2,0],'6.2':[0.2,0.2,0],'6.1':[0.5,0.5,0],'6.0':[0.8,0.8,0],'5.9':[1.0,1.0,0],'5.8':[1.5,1.5,0],'5.7':[2.0,2.0,0],'5.6':[2.5,2.5,0],'5.5':[3.0,3.0,0],'5.4':[3.5,3.5,0],'5.3':[3.8,3.8,0],'5.2':[4.1,4.1,0],'5.1':[4.5,4.5,0],'5.0':[4.8,4.8,0],'4.9':[5.1,5.1,0],'4.8':[5.4,5.4,0],'4.7':[5.7,5.7,0],'4.6':[5.8,5.8,0],'4.5':[6.0,6.0,0],'4.4':[7.0,6.0,1.0],'4.3':[7.5,6.0,1.5],'4.2':[8.0,6.0,2.0],'4.1':[9.0,6.0,3.0],'4.0':[9.8,6.0,3.8],'3.9':[10.8,6.0,4.8]}}
GRASS={'3.8':[1.5,2.0,3.0,3.0],'3.9':[1.5,2.0,3.0,3.0],'4.0':[1.5,2.0,3.0,3.0],'4.1':[1.5,2.0,3.0,3.0],'4.2':[1.5,2.0,3.0,2.9],'4.3':[1.5,2.0,3.0,2.8],'4.4':[1.5,2.0,3.0,2.7],'4.5':[1.5,2.0,3.0,2.4],'4.6':[1.5,1.9,2.9,2.1],'4.7':[1.3,1.8,2.8,1.7],'4.8':[1.2,1.7,2.7,1.3],'4.9':[1.1,1.6,2.6,0.9],'5.0':[1.0,1.5,2.5,0.5],'5.1':[0.9,0.9,0.0,0.0],'5.2':[0.8,0.8,0.0,0.0],'5.3':[0.7,0.7,0.0,0.0],'5.4':[0.6,0.6,0.0,0.0],'5.5':[0.5,0.5,0.0,0.0],'5.6':[0.0,0.5,0.0,0.0],'5.7':[0.0,0.4,0.0,0.0],'5.8':[0.0,0.3,0.0,0.0],'5.9':[0.0,0.2,0.0,0.0]}
CARBON=['c_below_2_5','c_2_6_to_5','c_5_1_to_10','c_above_10']

# ===== 1. Grunty orne: kazde pH kazdej kategorii =====
n=0
for cat,rows in ARABLE.items():
    for ph,(tot,p1,p2) in rows.items():
        r=call(usage_type='grunty_orne',soil_category=cat,ph=ph)
        d=r.get('data') if r.get('success') else None
        ok = d and abs(d['cao_dose']-tot)<1e-9 and abs(d['part_1']-p1)<1e-9 and abs(d['part_2']-p2)<1e-9
        check('IUNG orne %s pH %s'%(cat,ph), ok, str(d)[:90]); n+=1
print('1. Grunty orne — %d kombinacji pH x kategoria'%n)

# ===== 2. Uzytki zielone: kazde pH x kazda klasa C =====
n=0
for ph,row in GRASS.items():
    for i,c in enumerate(CARBON):
        r=call(usage_type='uzytki_zielone',carbon_content=c,ph=ph)
        d=r.get('data') if r.get('success') else None
        exp=row[i]
        ok = d and abs(d['cao_dose']-exp)<1e-9
        check('IUNG zielone %s pH %s'%(c,ph), ok, str(d)[:90]); n+=1
print('2. Uzytki zielone — %d kombinacji pH x klasa C'%n)

# ===== 3. Granice klas zasobnosci Mg ("do X" nalezy do klasy nizszej) =====
TH={'bardzo_lekka':[1.0,2.0,4.0,6.0],'lekka':[2.0,3.0,5.0,7.0],'srednia':[3.0,5.0,7.0,9.0],'ciezka':[4.0,6.0,10.0,14.0]}
NAZWY=['Bardzo niska','Niska','Średnia','Wysoka']
n=0
for grp,t in TH.items():
    for i,prog in enumerate(t):
        # dokladnie na progu -> klasa nizsza
        r=call(usage_type='grunty_orne',soil_category=grp,ph='4.5',mg_value=str(prog))
        mg=r['data']['mg']
        check('Mg granica %s = %s -> %s'%(grp,prog,NAZWY[i]), mg['class']==NAZWY[i], mg['class']); n+=1
        # tuz powyzej progu -> klasa wyzsza (o ile nie ostatni prog)
        if i<3:
            r=call(usage_type='grunty_orne',soil_category=grp,ph='4.5',mg_value=str(round(prog+0.1,1)))
            mg=r['data']['mg']
            check('Mg %s = %s -> %s'%(grp,round(prog+0.1,1),NAZWY[i+1]), mg['class']==NAZWY[i+1], mg['class']); n+=1
print('3. Granice klas Mg — %d punktow granicznych'%n)

# ===== 4. Przycinanie wartosci i celu =====
for grp,t in TH.items():
    mx=t[3]; mn=round(t[1]+0.1,1)
    r=call(usage_type='grunty_orne',soil_category=grp,ph='4.5',mg_value='99')
    mg=r['data']['mg']
    check('Przyciecie zbadanego Mg do max %s (%s)'%(mx,grp), mg['mg']==mx, str(mg['mg']))
    r=call(usage_type='grunty_orne',soil_category=grp,ph='4.5',mg_value='0.5',mg_target='0.1')
    mg=r['data']['mg']
    check('Cel ponizej minimum -> %s (%s)'%(mn,grp), abs(mg['target']-mn)<1e-9, str(mg['target']))
    r=call(usage_type='grunty_orne',soil_category=grp,ph='4.5',mg_value='0.5',mg_target='999')
    mg=r['data']['mg']
    check('Cel powyzej maksimum -> %s (%s)'%(mx,grp), abs(mg['target']-mx)<1e-9, str(mg['target']))
    r=call(usage_type='grunty_orne',soil_category=grp,ph='4.5',mg_value='0.5')
    mg=r['data']['mg']
    check('Cel domyslny = gorna granica wysokiej (%s)'%grp, abs(mg['target']-mx)<1e-9, str(mg['target']))
print('4. Przycinanie i cel domyslny — 16 sprawdzen')

# ===== 5. Matematyka dawki Mg i doboru dwuetapowego =====
MGO=40.304/24.305
for grp in TH:
    for val in ['0.5','1.5','2.5']:
        r=call(usage_type='grunty_orne',soil_category=grp,ph='4.5',mg_value=val)
        d=r['data']; mg=d['mg']
        exp_def=round(mg['target']-mg['mg'],1)
        exp_mg=round(exp_def*30,1); exp_mgo=round(exp_mg*MGO,1)
        check('Deficyt %s %s'%(grp,val), abs(mg['deficit']-exp_def)<1e-9, str(mg['deficit']))
        check('kg Mg/ha %s %s'%(grp,val), abs(mg['dose_mg']-exp_mg)<1e-9, str(mg['dose_mg']))
        check('kg MgO/ha %s %s'%(grp,val), abs(mg['dose_mgo']-exp_mgo)<0.15, '%s vs %s'%(mg['dose_mgo'],exp_mgo))
        if d['mg_products']:
            cao=d['cao_dose']; topup=d['cao_topup']
            check('Sort po MgO malejaco %s %s'%(grp,val),
                  [p['mgo_pct'] for p in d['mg_products']]==sorted([p['mgo_pct'] for p in d['mg_products']],reverse=True))
            for p in d['mg_products']:
                # lancuch jak w prototypie: pelna precyzja, zaokraglenie tylko przy wyswietleniu
                e_dose=(mg['dose_mgo']/(p['mgo_pct']/100))/1000
                e_giv=e_dose*(p['cao_pct']/100)
                e_left=max(0.0,float(Decimal(repr(cao-e_giv)).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)))
                e_top=e_left/(topup['cao_pct']/100) if e_left>0 else 0
                check('Dobor %s: dawka wg Mg'%p['id'], abs(p['dose_by_mg']-e_dose)<1e-9, str(p['dose_by_mg']))
                check('Dobor %s: CaO pokryte'%p['id'], abs(p['cao_given']-e_giv)<1e-9, str(p['cao_given']))
                check('Dobor %s: CaO do dopokrycia'%p['id'], abs(p['cao_left']-e_left)<1e-9, str(p['cao_left']))
                check('Dobor %s: dopokrycie wapnem'%p['id'], abs(p['topup']-e_top)<1e-9, str(p['topup']))
            check('Dolomit liczony z CaO netto 30%', any(p['id']==302 and p['cao_pct']==30 for p in d['mg_products']))
            check('#313 liczone z CaO 70%', any(p['id']==313 and p['cao_pct']==70 for p in d['mg_products']))
            check('Produkt dopokrycia = Agrobielik 70', topup['id']==310 and topup['cao_pct']==70, str(topup))
print('5. Matematyka Mg i doboru dwuetapowego')

# ===== 6. Filtr listy CaO wg deklaracji Mg =====
MG_IDS={302,313,317,318,319}
r=call(usage_type='grunty_orne',soil_category='lekka',ph='4.5')
ids={p['id'] for p in r['data']['products']}
check('Bez deklaracji Mg: 10 pozycji, zero magnezowych', len(ids)==10 and not (ids&MG_IDS), str(sorted(ids)))
r=call(usage_type='grunty_orne',soil_category='bardzo_lekka',ph='4.5',mg_value='6')  # wysoka, brak deficytu
ids={p['id'] for p in r['data']['products']}
check('Mg zadeklarowany bez deficytu: 15 pozycji z magnezowymi', len(ids)==15 and MG_IDS<=ids, str(len(ids)))
check('Kreda malarska #304 poza doborem', 304 not in ids)
check('Kreda pastewna #307 poza doborem', 307 not in ids)
r=call(usage_type='grunty_orne',soil_category='lekka',ph='4.5',mg_value='1.5')
check('Tabela Mg zastepuje klasyczna liste', r['data']['products']==[] and len(r['data']['mg_products'])==5)
print('6. Filtr listy CaO')

# ===== 7. Stan "wapnowanie zbedne + magnez do uzupelnienia" =====
r=call(usage_type='uzytki_zielone',carbon_content='c_below_2_5',ph='5.6',mg_value='1',mg_soil_group='lekka')
d=r['data']
check('CaO = 0 przy zadeklarowanym Mg', d['cao_dose']==0)
check('Blok Mg mimo zerowej dawki CaO', d['mg'] and d['mg']['needs'])
check('Tabela Mg mimo zerowej dawki CaO', len(d['mg_products'])==5)
check('Zero dopokrycia gdy wapnowanie zbedne', all(p['cao_left']==0 and p['topup']==0 for p in d['mg_products']))
# uzytki zielone bez grupy
r=call(usage_type='uzytki_zielone',carbon_content='c_2_6_to_5',ph='4.8',mg_value='2')
check('Uzytki zielone bez grupy -> brak oceny', r['data']['mg']=={'no_group':True}, str(r['data']['mg']))
r=call(usage_type='uzytki_zielone',carbon_content='c_2_6_to_5',ph='4.8',mg_value='2',mg_soil_group='srednia')
check('Uzytki zielone z grupa -> ocena', r['data']['mg'].get('group')=='srednia')
print('7. Stany brzegowe wynikow')

# ===== 8. Walidacja i sciezki bledu =====
bad=[('pH poza formatem',dict(usage_type='grunty_orne',soil_category='lekka',ph='45')),
     ('pH spoza tablicy',dict(usage_type='grunty_orne',soil_category='lekka',ph='9.9')),
     ('kategoria gleby zmyslona',dict(usage_type='grunty_orne',soil_category='ksiezycowa',ph='4.5')),
     ('typ uzytku zmyslony',dict(usage_type='sad',ph='4.5')),
     ('brak pH',dict(usage_type='grunty_orne',soil_category='lekka')),
     ('klasa C zmyslona',dict(usage_type='uzytki_zielone',carbon_content='c_dowolna',ph='4.8'))]
for name,kw in bad:
    r=call(**kw)
    check('Odrzucone: '+name, r.get('success') is False, str(r)[:60])
# grupa Mg zmyslona -> ocena pominieta, nie blad
r=call(usage_type='uzytki_zielone',carbon_content='c_2_6_to_5',ph='4.8',mg_value='2',mg_soil_group='ksiezycowa')
check('Zmyslona grupa Mg -> brak oceny, nie blad', r.get('success') and r['data']['mg']=={'no_group':True})
# Mg niebedace liczba -> ignorowane
r=call(usage_type='grunty_orne',soil_category='lekka',ph='4.5',mg_value='abc')
check('Mg nieliczbowe -> ignorowane, 10 pozycji', r['data']['mg'] is None and len(r['data']['products'])==10)
# ujemne Mg
r=call(usage_type='grunty_orne',soil_category='lekka',ph='4.5',mg_value='-5')
check('Mg ujemne -> ignorowane', r['data']['mg'] is None)
# zly nonce
body=urllib.parse.urlencode(dict(action='agria_calc_liming',nonce='0000000000',usage_type='grunty_orne',soil_category='lekka',ph='4.5')).encode()
try:
    raw=urllib.request.urlopen(urllib.request.Request(AJAX,data=body),timeout=60).read().decode()
    check('Zly nonce odrzucony', raw.strip() in ('-1','0'), raw[:40])
except urllib.error.HTTPError as e:
    check('Zly nonce odrzucony (HTTP %d)'%e.code, e.code in (400,403), str(e.code))
print('8. Walidacja i sciezki bledu')

print('\n'+'='*60)
print('ZALICZONE: %d   NIEZALICZONE: %d'%(len(OK),len(FAIL)))
if FAIL:
    print('\nNIEZALICZONE:')
    for f in FAIL[:40]: print('  -',f)
    sys.exit(1)
