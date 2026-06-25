# Styrning av Ineras FHIR-specifikationer

Den här sidan beskriver den generella styrningen för Ineras FHIR-specifikationer — hur de utvecklas, förvaltas, versionshanteras och avvecklas.

## Styrningsprinciper

Ineras FHIR-specifikationer styrs enligt följande principer:

- **Transparens** — alla specifikationer och deras ändringshistorik är offentligt tillgängliga på GitHub och Simplifier.net.
- **Samverkan** — krav samlas in i samarbete med regioner, kommuner, systemleverantörer och kliniska intressenter.
- **Stabilitet** — brytande ändringar minimeras och kommuniceras i god tid.
- **Interoperabilitet** — Ineras profiler bygger på nationella basprofiler från [HL7 Sweden](https://hl7.se) och internationella standarder från HL7 International.

## Livscykel för en FHIR-specifikation

```
Krav → Design → Granskning → Publicering (förhandsversion) → Pilot → Publicering (release) → Förvaltning → Avveckling
```

| Fas | Beskrivning |
|-----|-------------|
| **Krav** | Verksamhetskrav samlas in från intressenter och analyseras. |
| **Design** | FHIR-profiler, tillägg och terminologi utformas i samarbete med kliniska och tekniska experter. |
| **Granskning** | Utkast till IG granskas av intressenter och systemleverantörer. Återkoppling bearbetas. |
| **Förhandsversion** | IG:en publiceras som förhandsversion (t.ex. `1.0.0-beta.1`) för pilotimplementeringar. Ej för produktionsanvändning. |
| **Pilot** | Utvalda organisationer implementerar och testar standarden i en kontrollerad miljö. |
| **Release** | IG:en publiceras som stabil release och godkänns för produktionsanvändning. |
| **Förvaltning** | Löpande buggfixar (patch-versioner) och mindre förbättringar (minor-versioner). |
| **Avveckling** | Standarden fasas ut och avvecklas så småningom, med en migrationsväg till en efterföljande standard. |

## Versionshantering

Ineras FHIR-specifikationer använder [semantisk versionshantering (SemVer 2.0)](https://semver.org/):

- `MAJOR.MINOR.PATCH` — t.ex. `2.1.4`
- Förhandsversioner använder ett suffix — t.ex. `2.0.0-beta.1`

| Versionsdel | När den ändras |
|-------------|----------------|
| **MAJOR** | Inkompatibla ändringar — befintliga implementeringar behöver uppdateras. |
| **MINOR** | Nya funktioner tillagda på ett bakåtkompatibelt sätt. |
| **PATCH** | Bakåtkompatibla buggfixar. |

Beslut om major- och minorversioner fattas i samråd med relevanta styrningsgrupper och dokumenteras i versionsnyheter.

## Roller och ansvar

| Roll | Ansvar |
|------|--------|
| **Ineras FHIR-team** | Utformar och förvaltar FHIR-profiler och IG:er. |
| **Tjänsteförvaltare** | Äger verksamhetskraven för en specifik tjänst. |
| **Intressentgrupp** | Regioner, kommuner och kliniska experter som deltar i kravinhämtning och granskning. |
| **Systemleverantörer** | Implementerar specifikationerna och ger återkoppling från ett tekniskt implementeringsperspektiv. |

## Ändringshanteringsprocess

1. Ett ändringsönskemål skickas in som ett GitHub-ärende eller via e-post till [fhir@inera.se](mailto:fhir@inera.se).
2. Inera bedömer ärendets konsekvenser och angelägenhetsgrad.
3. Ärendet prioriteras och schemaläggs för en kommande version.
4. Ändringen implementeras, granskas och publiceras som en del av en ny version.
5. Den som lämnat in ärendet meddelas och ändringen dokumenteras i versionsnyheter.

## Frågor?

Kontakta Ineras FHIR-team på [fhir@inera.se](mailto:fhir@inera.se).
