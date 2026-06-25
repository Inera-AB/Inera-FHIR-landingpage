# Välkommen till Ineras FHIR®-specifikationer

**Innehållsförteckning**

* [1 Ineras FHIR-specifikationer](#1-ineras-fhir-standarder)
* [2 Implementera en Inera FHIR-specifikation](#2-implementera-en-inera-fhir-standard)
    * [2.1 Specifikationsdokumentation](#21-specifikationsdokumentation)
    * [2.2 Generell styrning för Inera FHIR-specifikationer](#22-generell-styrning-for-inera-fhir-standarder)
* [3 Test och verifiering](#3-test-och-verifiering)
* [4 Ändringshantering och versionshantering](#4-andringshantering-och-versionshantering)
    * [4.1 Versionshantering av Inera FHIR-specifikationer](#41-versionshantering-av-inera-fhir-standarder)
    * [4.2 Ändringsönskemål och förbättringar](#42-andringsonskemal-och-forbattringar)
* [5 Vill du hålla dig uppdaterad?](#5-vill-du-halla-dig-uppdaterad)
* [6 Ny på FHIR?](#6-ny-pa-fhir)
* [7 Vanliga frågor](#7-vanliga-fragor)

---

Inera förvaltar och utvecklar nationell digital infrastruktur för svensk hälso- och sjukvård. Som en del av detta arbete publicerar Inera FHIR-baserade Implementation Guides (IG:er) som möjliggör standardiserat och interoperabelt informationsutbyte mellan vårdsystem och aktörer i Sverige.

Syftet med denna webbplats är att vägleda dig till rätt dokumentation och tekniska specifikationer för Ineras FHIR-specifikationer.

> **Notera:** Teknisk dokumentation publiceras på engelska. Kliniska riktlinjer och styrdokument publiceras på svenska.

---

## 1 Ineras FHIR-specifikationer

Ineras FHIR-specifikationer täcker ett brett spektrum av nationella e-hälsotjänster. Varje specifikation beskrivs i en Implementation Guide (IG) som innehåller profiler, tillägg, terminologi och regler för hur information ska struktureras och utbytas.

Alla Inera FHIR Implementation Guides publiceras på **[fhir.inera.se](https://fhir.inera.se)**. Varje IG följer ett förutsägbart URL-mönster baserat på sitt namn:

```
https://fhir.inera.se/ig/<namn>/
```

Till exempel: [`fhir.inera.se/ig/core/`](https://fhir.inera.se/ig/core/), [`fhir.inera.se/ig/careteam/`](https://fhir.inera.se/ig/careteam/).

### Publicerade Implementation Guides

En komplett och uppdaterad lista över alla publicerade Inera FHIR Implementation Guides finns på **[fhir.inera.se/ig/](https://fhir.inera.se/ig/index.html)**. Publicerade IG:ar inkluderar för närvarande:

- **[Inera EHDS Tjänstekontrakt](https://fhir.inera.se/ig/EHDS-TK)** - FHIR IG som beskriver hur Ineras RIVTA-tjänstekontrakt mappas till FHIR för att informationsförsörja NPÖ och 1177 Journal.

Kommande IG:ar är:
- **[Inera CareTeam](https://fhir.inera.se/ig/careteam/)** — Profiler för att representera en patients utsedda vårdkontakt (*fast vårdkontakt*) och vårdteam. Används som den första FHIR-profilen i 1177-journaltjänsten.
- **[Inera FHIR Forms](https://fhir.inera.se/ig/forms/)** — Profiler för `Questionnaire` och `QuestionnaireResponse` som stöder Ineras nationella formulärtjänst. Möjliggör strukturerad insamling och utbyte av formulärbaserad hälsoinformation.

### Terminologitjänsten

**[Inera Terminologitjänst](https://test.api.terminologitjansten.inera.se)** är Ineras nationella terminologiserver som tillhandahåller kodsystem, värdemängder och begreppsslagningar för svensk hälso- och sjukvård. Den exponerar ett FHIR Terminology API.

### Verktyg och stöd

- **Inera Core** *(kommer snart)* — Grundläggande profiler som återanvänds i Ineras FHIR-specifikationer, t.ex. Patient-, Organisations- och Utövarprofiler anpassade till svenska krav (personnummer, HSA-id, etc.).
- **[IneraFHIRTemplate](https://github.com/Inera-AB/IneraFHIRTemplate)** — Ett GitHub-mallarkiv för att skapa nya Inera FHIR Implementation Guides, med förkonfigurerad verktygskedja, CI/CD och Ineras varumärkesstil.

<br><br>

## 2 Implementera en Inera FHIR-specifikation

Vid implementering av en Inera FHIR-specifikation är det viktigt att förstå både verksamhetssammanhanget och de tekniska specifikationerna. Avsnitten nedan beskriver specifikationsdokumentationens huvudkomponenter och den styrning som reglerar hur informationsutbyte ska genomföras.

<br>

### 2.1 Specifikationsdokumentation

Varje Inera FHIR-specifikation levereras med dokumentation som beskriver hur specifikationen ska användas och vilka krav som gäller. Dokumentationen kan bestå av:

- **Implementation Guide (IG):** De tekniska specifikationerna för standarden, publicerade på [fhir.inera.se/ig/\<namn\>/](https://fhir.inera.se).
- **Kliniska riktlinjer:** Bakgrund och klinisk motivering bakom standarden.
- **Användningsfall:** Beskrivningar av de avsedda scenarierna för standarden.
- **Testprotokoll:** Används vid test och verifiering för att dokumentera att implementeringen uppfyller standarden.
- **Konformansresurser:** FHIR CapabilityStatements och OperationDefinitions som beskriver vad en server eller klient måste stödja.

<br>

### 2.2 Generell styrning för Inera FHIR-specifikationer

Styrningen beskriver hur Inera hanterar livscykeln för sina FHIR-specifikationer — från kravinhämtning och publicering till ändringshantering och avveckling. Det är viktigt att förstå styrningsprocessen innan en implementering påbörjas.

[Klicka här för mer information om styrning av Ineras FHIR-specifikationer.](assets/documents/Governance.md)

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

### 4.1 Versionshantering av Inera FHIR-specifikationer

Ineras FHIR-specifikationer följer [semantisk versionshantering (SemVer 2.0)](https://semver.org/), anpassad till Ineras styrningsprocess. En versionsidentifierare består av tre siffror separerade med punkter, t.ex. **2.1.4**, som representerar *major.minor.patch*:

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

Du kan även följa [inera.se](https://www.inera.se) för nyheter om tjänsteutveckling och FHIR-specifikationer.

<br>

## 6 Ny på FHIR?

Det här avsnittet ger en kort introduktion till FHIR för dig som är ny inom området eller har begränsad erfarenhet av standarden. Här finns en översikt av de vanligaste termerna, en steg-för-steg-guide till hur en Implementation Guide är strukturerad samt länkar till externa resurser för vidare lärande.

[Klicka här för en introduktion till FHIR och hur man läser en Implementation Guide.](assets/documents/NewToFHIR.md)

<br>

## 7 Vanliga frågor

Här hittar du svar på de vanligaste frågorna om Ineras FHIR-arbete och hur du kommer igång.

[Klicka här för att läsa vanliga frågor.](assets/documents/FAQ.md)
