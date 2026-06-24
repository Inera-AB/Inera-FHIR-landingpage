# Välkommen till Ineras FHIR®-standarder

**Innehållsförteckning**

* [1 Ineras FHIR-standarder](#1-ineras-fhir-standarder)
* [2 Implementera en Inera FHIR-standard](#2-implementera-en-inera-fhir-standard)
    * [2.1 Standarddokumentation](#21-standarddokumentation)
    * [2.2 Generell styrning för Inera FHIR-standarder](#22-generell-styrning-for-inera-fhir-standarder)
* [3 Test och verifiering](#3-test-och-verifiering)
* [4 Ändringshantering och versionshantering](#4-andringshantering-och-versionshantering)
    * [4.1 Versionshantering av Inera FHIR-standarder](#41-versionshantering-av-inera-fhir-standarder)
    * [4.2 Ändringsönskemål och förbättringar](#42-andringsonskemal-och-forbattringar)
* [5 Vill du hålla dig uppdaterad?](#5-vill-du-halla-dig-uppdaterad)
* [6 Ny på FHIR?](#6-ny-pa-fhir)
* [7 Vanliga frågor](#7-vanliga-fragor)

---

Inera förvaltar och utvecklar nationell digital infrastruktur för svensk hälso- och sjukvård. Som en del av detta arbete publicerar Inera FHIR-baserade Implementation Guides (IG:er) som möjliggör standardiserat och interoperabelt informationsutbyte mellan vårdsystem och aktörer i Sverige.

Syftet med denna webbplats är att vägleda dig till rätt dokumentation och tekniska specifikationer för Ineras FHIR-standarder.

> **Notera:** Teknisk dokumentation publiceras på engelska. Kliniska riktlinjer och styrdokument publiceras på svenska.

---

## 1 Ineras FHIR-standarder

Ineras FHIR-standarder täcker ett brett spektrum av nationella e-hälsotjänster. Varje standard beskrivs i en Implementation Guide (IG) som innehåller profiler, tillägg, terminologi och regler för hur information ska struktureras och utbytas.

Alla Inera FHIR Implementation Guides publiceras på **[fhir.inera.se](https://fhir.inera.se)**. Varje IG följer ett förutsägbart URL-mönster baserat på sitt namn:

```
https://fhir.inera.se/ig/<namn>/
```

Till exempel: [`fhir.inera.se/ig/core/`](https://fhir.inera.se/ig/core/), [`fhir.inera.se/ig/careteam/`](https://fhir.inera.se/ig/careteam/).

Vissa profiler delas mellan flera standarder. Dessa samlas i Ineras kärnprofiler och återanvänds i tjänstespecifika IG:er. Terminologi — kodsystem, värdemängder och begreppskartor — tillhandahålls av Ineras nationella terminologiserver.

Tabellen nedan ger en översikt över Ineras FHIR-standarder, indelade i tre delar:

1. **Ineras FHIR-tjänster** — tjänstespecifika standarder och deras verksamhetskrav.
2. **Terminologi** — Ineras nationella terminologiserver.
3. **Generiska profiler** — profiler som återanvänds i flera standarder.

<br>

<div style="overflow-x:auto;">
<table class="tg" id="Tab1">
<caption style="color:#7E2A4C;font-weight:bold;text-align:left;padding-bottom:6px;">Tabell 1: Översikt över Ineras FHIR-standarder</caption>
<colgroup>
<col style="width:20%">
<col style="width:20%">
<col style="width:50%">
<col style="width:10%">
</colgroup>
<thead>
  <tr>
    <th class="tg-header" scope="col">Tjänst</th>
    <th class="tg-header" scope="col">Svenskt namn</th>
    <th class="tg-header" scope="col">Kort beskrivning</th>
    <th class="tg-header" scope="col">Version</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-category" colspan="4"><em>Ineras nationella tjänster</em></td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://fhir.inera.se/ig/careteam/" target="_blank">Inera CareTeam</a></td>
    <td class="tg-cell">Fast vårdkontakt via 1177</td>
    <td class="tg-cell">Profiler för att representera en patients utsedda vårdkontakt (fast vårdkontakt) och vårdteam. Används som den första FHIR-profilen i 1177-journaltjänsten.</td>
    <td class="tg-cell">Se IG</td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://fhir.inera.se/ig/forms/" target="_blank">Inera FHIR Forms</a></td>
    <td class="tg-cell">Formulärtjänsten</td>
    <td class="tg-cell">Profiler för <code>Questionnaire</code> och <code>QuestionnaireResponse</code> som stöder Ineras nationella formulärtjänst. Möjliggör strukturerad insamling och utbyte av formulärbaserad hälsoinformation.</td>
    <td class="tg-cell">Se IG</td>
  </tr>
  <tr>
    <td class="tg-category" colspan="4"><em>Terminologi</em></td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://test.api.terminologitjansten.inera.se" target="_blank">Inera Terminologitjänst</a></td>
    <td class="tg-cell">Terminologitjänsten</td>
    <td class="tg-cell">Ineras nationella terminologiserver som tillhandahåller kodsystem, värdemängder och begreppsslagningar för svensk hälso- och sjukvård. Exponerar ett FHIR Terminology API.</td>
    <td class="tg-cell"></td>
  </tr>
  <tr>
    <td class="tg-category" colspan="4"><em>Generiska profiler</em></td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://fhir.inera.se/ig/core/" target="_blank">Inera Core</a></td>
    <td class="tg-cell">Kärnprofiler</td>
    <td class="tg-cell">Grundläggande profiler som återanvänds i Ineras FHIR-standarder, t.ex. Patient-, Organisations- och Utövarprofiler anpassade till svenska krav (personnummer, HSA-id, etc.).</td>
    <td class="tg-cell">Se IG</td>
  </tr>
</tbody>
</table>
</div>

<br><br>

## 2 Implementera en Inera FHIR-standard

Vid implementering av en Inera FHIR-standard är det viktigt att förstå både verksamhetssammanhanget och de tekniska specifikationerna. Avsnitten nedan beskriver standarddokumentationens huvudkomponenter och den styrning som reglerar hur informationsutbyte ska genomföras.

<br>

### 2.1 Standarddokumentation

Varje Inera FHIR-standard levereras med dokumentation som beskriver hur standarden ska användas och vilka krav som gäller. Dokumentationen kan bestå av:

- **Implementation Guide (IG):** De tekniska specifikationerna för standarden, publicerade på [fhir.inera.se/ig/\<namn\>/](https://fhir.inera.se).
- **Kliniska riktlinjer:** Bakgrund och klinisk motivering bakom standarden.
- **Användningsfall:** Beskrivningar av de avsedda scenarierna för standarden.
- **Testprotokoll:** Används vid test och verifiering för att dokumentera att implementeringen uppfyller standarden.
- **Konformansresurser:** FHIR CapabilityStatements och OperationDefinitions som beskriver vad en server eller klient måste stödja.

<br>

### 2.2 Generell styrning för Inera FHIR-standarder

Styrningen beskriver hur Inera hanterar livscykeln för sina FHIR-standarder — från kravinhämtning och publicering till ändringshantering och avveckling. Det är viktigt att förstå styrningsprocessen innan en implementering påbörjas.

[Klicka här för mer information om styrning av Ineras FHIR-standarder.](assets/documents/Governance.md)

<br>

## 3 Test och verifiering

Innan en implementering sätts i produktion och börjar utbyta patientinformation måste den verifieras mot Ineras testmiljöer. Inera tillhandahåller:

- **Testmiljöer (QA/Staging):** Separata miljöer för integrations- och systemtestning.
- **Validerare:** Möjlighet att validera FHIR-resurser mot publicerade profiler med [HL7 FHIR Validator](https://confluence.hl7.org/display/FHIR/Using+the+FHIR+Validator) med relevant Inera IG inläst från [fhir.inera.se](https://fhir.inera.se).
- **Konformanstest:** Inera kan erbjuda stöd för konformanstest mot publicerade CapabilityStatements.

Kontakta Ineras kundtjänst eller ansvarig tjänsteförvaltare för att påbörja testprocessen för en specifik tjänst.

> Kontakt: [kundservice@inera.se](mailto:kundservice@inera.se)

<br>

## 4 Ändringshantering och versionshantering

### 4.1 Versionshantering av Inera FHIR-standarder

Ineras FHIR-standarder följer [semantisk versionshantering (SemVer 2.0)](https://semver.org/), anpassad till Ineras styrningsprocess. En versionsidentifierare består av tre siffror separerade med punkter, t.ex. **2.1.4**, som representerar *major.minor.patch*:

- **MAJOR** — ändras vid inkompatibla ändringar av API:et eller profileringen.
- **MINOR** — ändras vid tillägg av ny funktionalitet på ett bakåtkompatibelt sätt.
- **PATCH** — ändras vid bakåtkompatibla buggfixar.

En version med ett suffix som `2.1.0-beta.1` är en förhandsversion och är inte avsedd för produktionsanvändning.

Beslut om stora versionsändringar (major och minor) fattas i samråd med relevanta styrningsgrupper och kommuniceras via Ineras webbplats och GitHub.

<br>

### 4.2 Ändringsönskemål och förbättringar

Systemleverantörer och vårdorganisationer är välkomna att skicka in ändringsönskemål:

- **Tekniska frågor om en IG:** Skapa ett ärende i relevant [Inera GitHub-arkiv](https://github.com/Inera-AB).
- **Verksamhetsfrågor eller annan dokumentation:** Kontakta ansvarig tjänsteförvaltare eller skriv till [fhir@inera.se](mailto:fhir@inera.se).

Inera genomför en konsekvensanalys av inkomna ärenden och beslutar om och när ändringar ska implementeras samt vilken versionsnivå som berörs.

<br>

## 5 Vill du hålla dig uppdaterad?

Du kan prenumerera på uppdateringar från Ineras FHIR-arkiv på GitHub:

1. Gå till [Inera AB på GitHub](https://github.com/Inera-AB).
2. Välj det arkiv du vill följa.
3. Klicka på knappen **Watch** i det övre högra hörnet och välj önskat aviseringsalternativ.

> Du behöver ett GitHub-konto för att bevaka ett arkiv. Skapa ett kostnadsfritt konto på [github.com/signup](https://github.com/signup).

Du kan även följa [inera.se](https://www.inera.se) för nyheter om tjänsteutveckling och FHIR-standarder.

<br>

## 6 Ny på FHIR?

Det här avsnittet ger en kort introduktion till FHIR för dig som är ny inom området eller har begränsad erfarenhet av standarden. Här finns en översikt av de vanligaste termerna, en steg-för-steg-guide till hur en Implementation Guide är strukturerad samt länkar till externa resurser för vidare lärande.

[Klicka här för en introduktion till FHIR och hur man läser en Implementation Guide.](assets/documents/NewToFHIR.md)

<br>

## 7 Vanliga frågor

Här hittar du svar på de vanligaste frågorna om Ineras FHIR-arbete och hur du kommer igång.

[Klicka här för att läsa vanliga frågor.](assets/documents/FAQ.md)
