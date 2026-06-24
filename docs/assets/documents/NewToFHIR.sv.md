# Ny på FHIR?

Den här sidan ger en kort introduktion till FHIR för dig som är ny inom området eller har begränsad erfarenhet av standarden.

## Vad är FHIR?

**FHIR** (Fast Healthcare Interoperability Resources) är en internationell standard framtagen av [HL7 International](https://www.hl7.org/fhir/) för utbyte av hälso- och sjukvårdsinformation. FHIR definierar en uppsättning **resurser** — byggstenar som representerar vanliga vårdinformationsbegrepp som Patient, Observation, Läkemedel eller Möte.

FHIR är utformat för att vara:

- **Webbaserat** — resurser utbyts med standardiserade webbtekniker (HTTP, JSON, XML).
- **Modulärt** — du kombinerar resurser för att representera komplexa vårdscenarier.
- **Utbyggbart** — basresurser kan profileras och utökas för att passa lokala krav.

## Nyckelbegrepp

| Term | Beskrivning |
|------|-------------|
| **Resurs** | En diskret enhet interoperabel information, t.ex. `Patient`, `Observation`, `MedicationRequest`. |
| **Profil** | En uppsättning begränsningar tillämpade på en basresurs för att passa ett specifikt användningsfall eller nationellt sammanhang. |
| **Implementation Guide (IG)** | En samling profiler, tillägg, värdemängder och narrativ dokumentation för en specifik standard eller domän. |
| **Tillägg (Extension)** | Ett ytterligare dataelement lagt till en resurs utöver vad som finns i bas-FHIR-specifikationen. |
| **ValueSet / CodeSystem** | Definierar de kodade värden (terminologi) som kan användas i ett givet fält. |
| **CapabilityStatement** | Beskriver vad en FHIR-server eller klient stöder — vilka resurser, interaktioner och sökparametrar. |

## Hur Inera tar fram Implementation Guides

Inera tar fram FHIR Implementation Guides med hjälp av **FHIR Shorthand (FSH)** och **FHIR IG Publisher**. Denna verktygskedja är HL7:s rekommenderade sätt att producera IG:er och används av nationella program världen över.

### FHIR Shorthand (FSH)

[FHIR Shorthand](https://build.fhir.org/ig/HL7/fhir-shorthand/) är ett domänspecifikt språk framtaget specifikt för att definiera FHIR-profiler, tillägg, värdemängder och exempel. Det är kompakt och lättläst, vilket gör det mycket enklare att skapa och granska än råa JSON- eller XML-StructureDefinitions.

En enkel FSH-profil ser ut så här:

```fsh
Profile: IneraPatient
Parent: Patient
Id: inera-patient
Title: "Inera Patient"
Description: "Patientprofil anpassad för svenska nationella tjänster."

* identifier 1..* MS
* identifier ^slicing.discriminator.type = #pattern
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
```

**Lär dig FSH på [FSH School](https://fshschool.org)** — en interaktiv onlinekurs som guidar dig genom FSH-språket från grunderna till avancerad profilering, med direkta övningar i webbläsaren.

### IG Publisher och IG Builder

**FHIR IG Publisher** är det officiella HL7-verktyget som tar FSH-källfiler och producerar en komplett, publicerbar Implementation Guide-webbplats — inklusive renderade profiler, exempel, validering och en navigerbar HTML-sajt.

**[IG Builder-vägledningen](https://build.fhir.org/ig/FHIR/ig-guidance/)** på build.fhir.org täcker allt du behöver veta om att sätta upp och köra ett IG-projekt:

- Projektmappsstruktur och `sushi-config.yaml`
- Köra SUSHI (FSH-kompilatorn) och IG Publisher
- Konfigurera sidor, menyer och narrativt innehåll
- Publicering och CI/CD-pipelines

Den kontinuerliga integrationsservern på [build.fhir.org](https://build.fhir.org) bygger automatiskt varje IG som finns på GitHub och gör en direktförhandsvisning tillgänglig — Inera använder detta för förhandsgranskning av IG:er innan de publiceras formellt.

## Hur man läser en Implementation Guide

Ineras Implementation Guides publiceras på [fhir.inera.se](https://fhir.inera.se) enligt URL-mönstret `https://fhir.inera.se/ig/<namn>/` — till exempel [fhir.inera.se/ig/core/](https://fhir.inera.se/ig/core/). Varje IG är strukturerad på följande sätt:

1. **Introduktion** — beskriver standardens syfte och omfattning.
2. **Profiler** — listar de FHIR-resursprofiler som definieras i IG:en, med begränsningar och kardinaliteter.
3. **Tillägg** — listar eventuella anpassade tillägg som introduceras.
4. **Terminologi** — listar de ValueSets och CodeSystems som används.
5. **Exempel** — visar konkreta exempel på FHIR-resurser som följer profilerna.
6. **CapabilityStatements** — beskriver vad implementatörer måste stödja.

> Börja med **Introduktionen** och **Användningsfallen** innan du dyker in i profilerna. Att förstå det kliniska och verksamhetsmässiga sammanhanget gör det mycket lättare att tolka de tekniska begränsningarna.

## Användbara externa resurser

- [Ineras FHIR-standarder](https://fhir.inera.se) — alla Inera IG:er
- [HL7 FHIR R4-specifikationen](https://hl7.org/fhir/R4/)
- [FSH School](https://fshschool.org) — interaktiv kurs för att lära sig FHIR Shorthand
- [IG Builder-vägledning](https://build.fhir.org/ig/FHIR/ig-guidance/) — officiell guide för att ta fram och publicera FHIR IG:er
- [FHIR Shorthand-specifikationen](https://build.fhir.org/ig/HL7/fhir-shorthand/) — fullständig FSH-språkreferens
- [build.fhir.org](https://build.fhir.org) — kontinuerlig byggserver för FHIR IG:er
- [FHIR för nybörjare (HL7)](https://www.hl7.org/fhir/overview.html)
- [HL7 Sweden](https://hl7.se) — svensk FHIR-community och basprofiler

## Frågor?

Har du frågor om Ineras FHIR-arbete, kontakta oss på [fhir@inera.se](mailto:fhir@inera.se).
