#!/usr/bin/env python3
"""T-080: treść poradnika /ph-gleby/ w blokach Gutenberga (wzorzec: wpis 2837 /wapno-pod-ziemniaki/)."""
import html, sys

def p(t):  return f'<!-- wp:paragraph -->\n<p>{t}</p>\n<!-- /wp:paragraph -->\n\n'
def h2(t): return f'<!-- wp:heading -->\n<h2 class="wp-block-heading">{t}</h2>\n<!-- /wp:heading -->\n\n'
def h3(t): return f'<!-- wp:heading {{"level":3}} -->\n<h3 class="wp-block-heading">{t}</h3>\n<!-- /wp:heading -->\n\n'
def ul(items):
    li = ''.join(f'<!-- wp:list-item -->\n<li>{i}</li>\n<!-- /wp:list-item -->\n\n' for i in items).rstrip()
    return f'<!-- wp:list -->\n<ul class="wp-block-list">{li}</ul>\n<!-- /wp:list -->\n\n'
def table(head, rows):
    th = ''.join(f'<th>{c}</th>' for c in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<!-- wp:table -->\n<figure class="wp-block-table"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>\n<!-- /wp:table -->\n\n'
def zrodlo(t): return p(f'<em>Źródło: {t}</em>')

S21 = 'IUNG-PIB, „Poradnik wapnowania gleb gruntów ornych”, Puławy 2021'
S22 = 'IUNG-PIB, „Zasady ustalania dawek wapna w doradztwie nawozowym”, Puławy 2022'
K = 'https://agria.pl/wapno-nawozowe-rolnictwo/'

box = (
 '<!-- wp:group {"style":{"color":{"background":"#eef7ec"},"spacing":{"padding":{"top":"20px","right":"24px","bottom":"12px","left":"24px"}},"border":{"radius":"6px"}}} -->\n'
 '<div class="wp-block-group has-background" style="border-radius:6px;background-color:#eef7ec;padding-top:20px;padding-right:24px;padding-bottom:12px;padding-left:24px">'
 + h2('pH gleby — szybka odpowiedź')
 + p('<strong>pH gleby mówi, czy pole trzeba wapnować. W skrócie:</strong>')
 + ul([
   '<strong>Skala:</strong> poniżej 4,5 gleba jest bardzo kwaśna, 4,6–5,5 kwaśna, 5,6–6,5 lekko kwaśna, 6,6–7,2 obojętna, powyżej 7,2 zasadowa.',
   '<strong>Granica ostrzegawcza:</strong> przy <strong>pH 5,5</strong> w glebie zaczyna pojawiać się toksyczny glin, a poniżej 4,5 jego szkodliwość rośnie.',
   '<strong>Jakie pH jest dobre:</strong> pszenica, jęczmień, rzepak, kukurydza i buraki najlepiej rosną przy <strong>pH 6,0–7,5</strong>; żyto, owies i ziemniaki przy 5,0–6,5.',
   '<strong>Jak sprawdzić:</strong> tester daje wynik orientacyjny. Do ustalenia dawki wapna potrzebny jest pomiar laboratoryjny w roztworze KCl.',
   '<strong>Jak podnieść:</strong> wapnowaniem. Dawkę wyznacza pH i kategoria gleby — lekka gleba potrzebuje mniej wapna niż ciężka przy tym samym pH.',
 ])
 + p('Dawkę dla swojego pola wyliczysz w <a href="https://agria.pl/kalkulator-wapnowania/">kalkulatorze wapnowania</a>. Niżej tłumaczymy, skąd biorą się te liczby.')
 + '</div>\n<!-- /wp:group -->\n\n')

c = box
c += h2('Co oznacza pH gleby')
c += p('pH to miara kwasowości. Im niższa liczba, tym gleba bardziej kwaśna. W glebie rozróżnia się dwie kwasowości: <strong>czynną</strong> — wolne jony wodoru w roztworze glebowym — i <strong>potencjalną</strong>, ukrytą w kompleksie sorpcyjnym.')
c += p('Kwasowość czynna zmienia się w ciągu roku: jest największa latem, mniejsza wiosną i jesienią, a najmniejsza zimą, gdy gleba zamarza. Dlatego wskazuje orientacyjnie, <strong>czy</strong> glebę trzeba wapnować, ale nie odpowiada na pytanie, <strong>ile</strong> wapna potrzeba. Do tego służy kwasowość wymienna, którą mierzy się w roztworze chlorku potasu (KCl) — i to pH w KCl jest podstawą zaleceń wapnowania w Polsce.')
c += zrodlo(S21 + ', s. 12–13; ' + S22 + ', s. 3')

c += h2('Jakie pH gleby jest dobre — tabela odczynu')
c += table(['Ocena odczynu', 'pH w KCl'], [
  ['bardzo kwaśny', 'poniżej 4,5'], ['kwaśny', '4,6–5,5'], ['lekko kwaśny', '5,6–6,5'],
  ['obojętny', '6,6–7,2'], ['zasadowy', 'powyżej 7,2']])
c += p('To, czy dany odczyn wymaga wapnowania, zależy jeszcze od <strong>kategorii agronomicznej gleby</strong>. Gleba ciężka przy tym samym pH ma wyższą kwasowość wymienną niż lekka, więc wymaga wapnowania wcześniej:')
c += table(['Potrzeby wapnowania', 'bardzo lekka', 'lekka', 'średnia', 'ciężka'], [
  ['konieczne', 'do 4,0', 'do 4,5', 'do 5,0', 'do 5,5'],
  ['potrzebne', '4,1–4,5', '4,6–5,0', '5,1–5,5', '5,6–6,0'],
  ['wskazane', '4,6–5,0', '5,1–5,5', '5,6–6,0', '6,1–6,5'],
  ['ograniczone', '5,1–5,5', '5,6–6,0', '6,1–6,5', '6,6–7,0'],
  ['zbędne', 'od 5,6', 'od 6,1', 'od 6,6', 'od 7,1']])
c += p('Przykład: pH 5,8 na glebie lekkiej oznacza wapnowanie ograniczone, a na glebie ciężkiej — potrzebne. Kategorię gleby (od bardzo lekkiej do ciężkiej) podaje wynik badania w stacji chemiczno-rolniczej razem z pH.')
c += zrodlo(S22 + ', tab. 2 i 3, s. 4–5')

c += h2('Jakie pH lubią rośliny uprawne')
c += p('IUNG-PIB dzieli rośliny na trzy grupy według reakcji na zakwaszenie gleby:')
c += table(['Grupa', 'Optymalne pH', 'Rośliny (wybór)'], [
  ['silnie reagujące na zakwaszenie', '6,0–7,5', 'pszenica ozima i jara, jęczmień, kukurydza, rzepak, buraki cukrowe i pastewne, lucerna, koniczyna, bobik, soja'],
  ['mniej wrażliwe', '5,0–6,5', 'żyto, owies, ziemniaki, groch, fasola, marchew, len, ogórki, pomidory, jabłoń'],
  ['mało wrażliwe', 'poniżej 5,0', 'gryka, łubin żółty, seradela']])
c += p('Najmocniej na wapnowanie reagują kukurydza i buraki, potem jęczmień i pszenica, owies, żyto, a najsłabiej ziemniak. Dlatego pod ziemniaki wapnuje się z wyprzedzeniem — szczegóły w poradniku <a href="https://agria.pl/wapno-pod-ziemniaki/">wapno pod ziemniaki</a>.')
c += zrodlo(S21 + ', tab. 8, s. 33 (za: Szczepaniak W., 2017)')

c += h2('Jak sprawdzić pH gleby')
c += p('<strong>Tester lub kwasomierz</strong> mierzy kwasowość czynną. Pokaże, czy gleba jest kwaśna, ale wynik zależy od pory roku i nie nadaje się do wyliczenia dawki wapna.')
c += p('<strong>Do ustalenia dawki</strong> potrzebne jest badanie laboratoryjne: pomiar pH w roztworze KCl (norma PN-ISO 10390) i oznaczenie kategorii agronomicznej gleby. Wykonują je stacje chemiczno-rolnicze i laboratoria agrochemiczne. Wiarygodność wyniku zależy przede wszystkim od tego, czy próbka gleby jest reprezentatywna — pobiera się ją według normy PN-R-04031.')
c += p('Z wynikiem badania (pH w KCl i kategoria gleby) dawkę CaO na hektar wyliczysz w <a href="https://agria.pl/kalkulator-wapnowania/">kalkulatorze wapnowania</a>.')
c += zrodlo(S22 + ', s. 3; ' + S21 + ', s. 12')

c += h2('Co zakwasza glebę i czym to grozi')
c += p('Gleba zakwasza się sama — przez wymywanie związków zasadowych w głąb profilu, kwasy organiczne z rozkładu resztek roślinnych i dwutlenek węgla. Proces przyspieszają <strong>nawozy fizjologicznie kwaśne</strong>.')
c += p('Skutki są wymierne:')
c += ul([
  'od <strong>pH 5,5</strong> w glebie pojawia się toksyczny glin, który niszczy system korzeniowy — szczególnie szkodzi jęczmieniowi, pszenicy, burakom, gorczycy i koniczynie;',
  'z gleby wymywa się wapń, magnez i potas, a fosfor, molibden i bor stają się trudno dostępne;',
  'z trzech podstawowych składników (N, P, K) najsilniej na zakwaszenie reaguje <strong>fosfor</strong> — w glebach bardzo kwaśnych 52,5% próbek ma bardzo niską lub niską zawartość fosforu przyswajalnego, w obojętnych 12,4%;',
  'na glebach kwaśnych rosną straty azotu do atmosfery, a nawozy pracują gorzej.',
])
c += p('Innymi słowy: na kwaśnej glebie część zapłaconego nawozu nie trafia do rośliny.')
c += zrodlo(S21 + ', s. 10–14 i 21–25, tab. 6 (za: Ochal, 2011)')

c += h2('Zakwaszenie gleb w Małopolsce i na Podkarpaciu')
c += p('Południowo-wschodnia Polska ma najbardziej zakwaszone gleby w kraju. Gleby kwaśne i bardzo kwaśne stanowią <strong>74,2% próbek w Małopolsce</strong> i <strong>75,8% na Podkarpaciu</strong> — więcej niż w jakimkolwiek innym województwie.')
c += table(['Województwo', 'Wapnowanie konieczne i potrzebne', 'Zużycie wapna w 2019 r.'], [
  ['małopolskie', '77,5% próbek', '26,9 kg CaO/ha'],
  ['podkarpackie', '73,4% próbek', '15,1 kg CaO/ha'],
  ['świętokrzyskie', '42,8% próbek', '15,0 kg CaO/ha'],
  ['Polska', '49,7% próbek', '56,4 kg CaO/ha']])
c += p('Zużycie wapna w regionie jest kilkakrotnie niższe od średniej krajowej, która i tak — według IUNG-PIB — często nie pokrywa nawet naturalnego wymywania wapnia z gleby.')
c += zrodlo(S21 + ', s. 10–17, tab. 1 (za: Smreczak i Łysiak, 2017) i tab. 2 (GUS, 2020)')

c += h2('Jak podnieść pH gleby')
c += p('pH podnosi się <strong>wapnowaniem</strong>. Orientacyjne dawki czystego składnika według klasy potrzeb wapnowania:')
c += table(['Kategoria gleby', 'konieczne', 'potrzebne', 'wskazane', 'ograniczone'], [
  ['bardzo lekka', '3,0 t CaO/ha', '2,0', '1,0', '—'],
  ['lekka', '3,5', '2,5', '1,5', '—'],
  ['średnia', '4,5', '3,0', '1,7', '1,0'],
  ['ciężka', '6,0', '3,0', '2,0', '1,0']])
c += p('Od 2022 r. IUNG-PIB podaje dawki dokładniej — dla każdej dziesiątej części pH. Według tych tablic liczy nasz <a href="https://agria.pl/kalkulator-wapnowania/">kalkulator wapnowania</a>.')
c += p('Jak szybko rośnie pH? Kwasowość wyraźnie spada już w pierwszym roku po wapnowaniu, a przy małych dawkach minimum osiąga się w drugim lub trzecim roku. Jednorazowa dawka poniżej 0,5 t CaCO<sub>3</sub>/ha nie wywołuje większych zmian. Wapno działa szybciej, gdy jest dobrze wymieszane z glebą, gleba jest wilgotna, a nawóz drobno zmielony. Duże dawki dzieli się: <strong>3/4 jesienią przed orką, 1/4 w drugim roku</strong>. Kiedy wapnować, rozpisaliśmy w <a href="https://agria.pl/jak-stosowac-wapno-nawozowe/">terminarzu wapnowania</a>.')
c += zrodlo(S22 + ', tab. 4, s. 5; ' + S21 + ', s. 21 i 49')

c += h3('Wapno nawozowe AGRIA do podniesienia pH')
c += table(['Produkt', 'Zawartość', 'Forma', 'Dawka', 'Kiedy wybrać'], [
  [f'<a href="{K}agrobielik-70/">Agrobielik 70</a>', 'min. 70% CaO', 'sypkie 0–2 mm', '2–6 t/ha', 'wapno tlenkowe — szybka korekta pH (wg karty 2–4 tygodnie)'],
  [f'<a href="{K}kreda-nawozowa-sypka/">Kreda nawozowa sypka</a>', 'min. 50% CaO', 'sypkie', '3–6 t/ha', 'pełna dawka węglanowa, dostawa luzem 24 t'],
  [f'<a href="{K}kreda-nawozowa-granulowana/">Kreda nawozowa granulowana</a>', 'min. 50% CaO', 'granulat 3–6 mm', '0,5–1,5 t/ha', 'dawka podtrzymująca, rozsiewacz nawozowy, gleby lekkie'],
  [f'<a href="{K}weglanowe-granulowane/">Wapno węglanowe granulowane</a>', 'min. 50% CaO', 'granulat 3–6 mm', '1–6 t/ha', 'odkwaszanie rozłożone w czasie, wysiew własnym rozsiewaczem'],
  [f'<a href="{K}weglanowe-magnez-granulowane/">Wapno węglanowe z magnezem granulowane</a>', 'min. 31% CaO + 16% MgO', 'granulat 3–6 mm', '1–6 t/ha', 'gleba kwaśna z niedoborem magnezu'],
  [f'<a href="{K}dolomit/">Dolomit</a>', 'CaO + MgO min. 45%, w tym MgO min. 15%', 'sypkie 0–2 mm', '1,5–6 t/ha', 'gleby lekkie i piaszczyste z deficytem Mg']])
c += p(f'Parametry pochodzą z kart produktów — pełne zestawienia, formy dostawy i ceny za tonę znajdziesz w <a href="{K}">ofercie wapna nawozowego</a>.')

c += h2('Najczęściej zadawane pytania')
faq = [
 ('Po czym poznać, że gleba jest kwaśna?', 'Sygnałem bywa masowo występujący szczaw polny i płytki, słaby system korzeniowy zbóż. Pewność daje dopiero pomiar pH — tester pokaże kierunek, badanie w stacji chemiczno-rolniczej da wynik, na którym liczy się dawkę wapna.'),
 ('Jakie pH gleby jest najlepsze?', 'Dla gleb uprawnych optymalny jest odczyn od 5,6 do 7,2. Dokładny cel zależy od uprawy: pszenica, jęczmień, rzepak i buraki lubią 6,0–7,5, a żyto, owies i ziemniaki 5,0–6,5.'),
 ('Co oznacza pH 7 gleby?', 'Odczyn obojętny — mieści się w przedziale 6,6–7,2. Na takiej glebie wapnowanie jest zwykle zbędne lub ograniczone, zależnie od kategorii gleby.'),
 ('Jak najszybciej podnieść pH gleby?', f'Wapnem tlenkowym — karta produktu <a href="{K}agrobielik-70/">Agrobielika 70</a> podaje działanie w 2–4 tygodnie. Reakcja jest najszybsza, gdy wapno jest dobrze wymieszane z wilgotną glebą. Wapno węglanowe działa łagodniej i wolniej.'),
 ('Czy wapno obniża pH gleby?', 'Nie — wapno podnosi pH, czyli odkwasza glebę. Gleb zasadowych w Polsce jest niewiele: według IUNG-PIB to 7,7% badanych próbek.'),
 ('Jakie pH lubią pomidory i ogórki?', 'Oba należą do grupy roślin mniej wrażliwych na zakwaszenie, z optimum pH 5,0–6,5.'),
]
for q, a in faq:
    c += h3(q) + p(a)

c += h2('Wapno nawozowe z dostawą całosamochodową')
c += p('AGRIA dostarcza wapno nawozowe luzem, w big-bagach i w workach, z magazynów w Tarnowie, Niedomicach i Radgoszczy oraz bezpośrednio z zakładów producentów. Ceny podajemy za tonę, bez transportu — wycena dostawy zależy od kierunku i wielkości ładunku.')
c += p(f'Po dobór produktu i wycenę zadzwoń albo napisz — <a href="https://agria.pl/kontakt/">dane kontaktowe</a>. Pełna oferta: <a href="{K}">wapno nawozowe</a>.')

open(sys.argv[1], 'w').write(c.rstrip() + '\n')
print(len(c), 'B')
