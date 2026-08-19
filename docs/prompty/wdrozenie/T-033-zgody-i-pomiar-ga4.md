# T-033 — zgody i pomiar GA4: rediagnoza od zera

| | |
|---|---|
| **Linia / zakres** | Analityka · **R** |
| **Status** | 🔵 do rozstrzygnięcia — zakres miękki |
| **Szacunek** | 3–4 h diagnozy |

---

## 1. Czego to dotyka

Complianz Privacy Suite premium **7.5.7.2** (aktywny), GTM `GTM-TDC85TQN`, GA4 `538301430` /
`G-KVFMR3NZDH`, Consent Mode v2. Pośrednio: **ocena skuteczności kampanii Ads** (T-039),
raportowanie do klienta, oraz **geoblok** — baza GeoLite2 należy do Complianz
(`uploads/complianz/maxmind/GeoLite2-Country.mmdb`), więc przekonfigurowanie Complianz może
rozbroić `T-048`.

## 2. Strefy kruche

1. **Memory i backlog twierdzą, że CMP nie ma. To nieprawda.** Complianz premium 7.5.7.2 jest
   aktywny i leci na froncie (95 wystąpień `cmplz`). Diagnoza, która startuje od „trzeba wdrożyć
   banner", jest z góry błędna. **Zacznij od zera, nie od notatek.**
2. **Nie ruszaj Complianz bez sprawdzenia, gdzie leży baza GeoLite2.** Deaktywacja wtyczki
   zabiera geoblokowi bazę → fail-open → wraca ruch botowy z Singapuru, który zafałszował
   GA4 w pierwszej połowie sierpnia. Jeden problem naprawiony kosztem drugiego.
3. **Consent Mode działa poprawnie technicznie** — sprawdzone 19.08: `gtag('consent','default')`
   z `analytics_storage: denied`, potem `consent update` po zdarzeniu `cmplz_fire_categories`.
   Czyli implementacja jest, a mimo to pokrycie jest częściowe. **Szukaj przyczyny w zachowaniu
   użytkowników i w konfiguracji GTM, nie w braku kodu.**
4. **RODO nie jest polem do optymalizacji.** Nie „naprawiaj" pomiaru przez odpalanie tagów przed
   zgodą ani przez zmianę `consenttype` z `optin` na coś innego. Region jest ustawiony na `eu`
   i tak ma zostać.
5. **Zmiany w GTM wymagają publikacji kontenera** — nowa wersja jest natychmiast żywa dla
   wszystkich. Testuj w trybie podglądu.
6. **Lokalny Chrome ma bloker maskujący GTM** — testuj przez GA4 Realtime API albo przez
   podgląd GTM, nie przez „widzę tag w konsoli".

## 3. Stan zmierzony 19.08.2026

```
Complianz:  7.5.7.2 premium, aktywny; consenttype „optin", region „eu", geoip 1
Front:      gtag('consent','default') → analytics_storage denied, ad_storage denied,
            ad_user_data denied, ad_personalization denied, functionality/security granted
            → gtag('consent','update') w handlerze cmplz_fire_categories
GTM:        GTM-TDC85TQN obecny; 7× dataLayer, 5× gtag(
GA4 (1–19.08, Data API):
   Direct        107 sesji / 772 zdarzenia
   Paid Search    49 sesji / 397           ← wobec 100 kliknięć w Ads API za ten sam okres
   Organic        21 sesji / 203
   Unassigned     14 · Cross-network 5 · AI Assistant 1 · Organic Social 1
```
**To jest inny obraz niż w memory** (`5 sesji organicznych w lipcu przy 221 kliknięciach GSC).
Pomiar działa, ale niekompletnie: Paid Search łapie ~49 % kliknięć.

## 4. Warunki wejścia

- [ ] Zgoda Janka na wejście w konfigurację GTM (publikacja kontenera to zmiana produkcyjna).

## 5. Co robisz — hipotezy od najtańszej

1. **Ile osób w ogóle klika zgodę.** Complianz zbiera statystyki bannera — sprawdź współczynnik
   akceptacji. Jeśli 50 % odmawia, ~49 % pokrycia Paid Search jest **poprawnym** wynikiem
   i zadanie kończy się wnioskiem, nie naprawą.
2. **Czy tag GA4 w GTM ma ustawienia zgody** (`Additional consent checks`) i czy nie jest
   blokowany twardo zamiast działać w trybie cookieless. Consent Mode „advanced" wysyła pingi
   bez cookies i pozwala Google modelować konwersje — „basic" nie.
3. **Czy Google Ads ma połączenie z GA4** i czy modelowanie konwersji jest włączone.
4. **Porównanie referencyjne**: GSC (kliknięcia organiczne) vs GA4 (sesje organiczne)
   za ten sam okres, dzień po dniu. Różnica stała w procentach = zgody. Różnica skokowa =
   błąd techniczny w konkretnym dniu.
5. Dopiero po ustaleniu przyczyny — propozycja dla Janka. Możliwe wnioski: „działa poprawnie,
   ~50 % to koszt zgód", „brakuje Consent Mode advanced", „tag odpala się za późno".

## 6. Jak sprawdzasz w trakcie

Każda hipoteza kończy się liczbą. Zapis w `tmp/T-033-diagnoza.md`: hipoteza → sposób pomiaru →
wynik → wniosek.

## 7. Jak testujesz

GA4 Realtime API podczas własnej wizyty z zaakceptowaną zgodą i z odrzuconą — dwa przebiegi,
dwa wyniki. To jedyny test, który rozstrzyga, czy tag odpala się zgodnie z założeniem.

## 8. Dowód do rejestru

Tabela GSC vs GA4 vs Ads za ten sam okres, współczynnik akceptacji zgód, wniosek o przyczynie.
**Ten task może zamknąć się wnioskiem „pomiar jest poprawny, pokrycie ograniczają zgody"** —
i to jest pełnoprawne domknięcie, pod warunkiem że liczby są w rejestrze.

## 9. Rollback

GTM ma wersjonowanie kontenera — powrót do poprzedniej wersji jednym kliknięciem.
Complianz: **nie ruszaj bez osobnej decyzji** (patrz strefa kruche 2).

## 10. Rozliczenie

Zakres **R**, 3–4 h. Wynik wchodzi do raportu M3 jako wyjaśnienie, dlaczego liczby GA4
i Ads się nie zgadzają — klient to zauważy wcześniej czy później.

## 11. Recheck

| Kiedy | Co |
|---|---|
| **+7 dni** | GA4 vs Ads za tydzień po zmianie — czy pokrycie wzrosło |
| **+30 dni** | GSC vs GA4 dla organicznych |
| **przy każdej aktualizacji Complianz** | czy `GeoLite2-Country.mmdb` nadal na miejscu (T-048) i czy consent nadal się wysyła |
