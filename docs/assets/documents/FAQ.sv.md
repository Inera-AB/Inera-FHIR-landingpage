# Vanliga frågor

## Allmänt

**Vilken roll har Inera i FHIR-standardiseringsarbetet?**

Inera förvaltar den nationella digitala infrastrukturen för svensk hälso- och sjukvård och ansvarar för att definiera hur FHIR ska användas inom de nationella tjänster som Inera driver. Ineras FHIR Implementation Guides definierar profiler anpassade till svenska krav — exempelvis användningen av personnummer och HSA-id — och bygger på basprofiler från [HL7 Sweden](https://hl7.se).

**Var publiceras Ineras Implementation Guides?**

Alla Inera FHIR Implementation Guides publiceras på [fhir.inera.se](https://fhir.inera.se) enligt URL-mönstret `https://fhir.inera.se/ig/<namn>/`. Till exempel:

- [fhir.inera.se/ig/core/](https://fhir.inera.se/ig/core/)
- [fhir.inera.se/ig/careteam/](https://fhir.inera.se/ig/careteam/)
- [fhir.inera.se/ig/forms/](https://fhir.inera.se/ig/forms/)

Källkod och ärendehantering finns på [GitHub](https://github.com/Inera-AB).

---

## Implementering

**Vilken version av FHIR använder Ineras standarder?**

Ineras nuvarande standarder riktar sig mot **FHIR R4** (version 4.0.1).

**Måste jag implementera alla profiler i en IG?**

Nej. Varje IG:s CapabilityStatement specificerar vilka profiler och interaktioner som är obligatoriska (SHALL) respektive rekommenderade (SHOULD) eller frivilliga (MAY) för en given aktör (klient eller server). Börja med att läsa CapabilityStatement för din roll.

**Var hittar jag exempelresurser för FHIR?**

Exempelresurser finns i varje Implementation Guide på [fhir.inera.se](https://fhir.inera.se). De kan laddas ner som JSON eller XML och användas som utgångspunkt för din implementering.

**Kan jag validera mina FHIR-resurser mot Ineras profiler?**

Ja. Du kan validera resurser med den officiella [HL7 FHIR Validator](https://confluence.hl7.org/display/FHIR/Using+the+FHIR+Validator) med relevant Inera IG inläst från [fhir.inera.se](https://fhir.inera.se).

---

## Testning

**Hur får jag tillgång till Ineras testmiljöer?**

Kontakta Ineras kundtjänst på [kundservice@inera.se](mailto:kundservice@inera.se) eller ansvarig tjänsteförvaltare för den aktuella tjänsten. Tillgång till testmiljöer kräver vanligtvis ett tecknat avtal.

**Finns det en sandbox eller öppen testmiljö?**

Inera tillhandahåller för närvarande testmiljöer för anslutna systemleverantörer. Se dokumentationen för den specifika tjänst du implementerar för att ta reda på vilken testinfrastruktur som finns tillgänglig.

---

## Ändringshantering

**Hur kommuniceras ändringar i Ineras FHIR-standarder?**

Ändringar kommuniceras via:

- Versionsnyheter i Implementation Guide:en.
- GitHub-releaser och ärenden i relevant arkiv.
- Ineras webbplats och nyhetsbrev.

**Hur rapporterar jag en bugg eller föreslår en förbättring?**

- För tekniska problem med en IG: skapa ett ärende i relevant [Inera GitHub-arkiv](https://github.com/Inera-AB).
- För övriga frågor: skriv till [fhir@inera.se](mailto:fhir@inera.se).

---

## Kontakt

| Ämne | Kontakt |
|------|---------|
| Tekniska FHIR-frågor | [fhir@inera.se](mailto:fhir@inera.se) |
| Kundtjänst | [kundservice@inera.se](mailto:kundservice@inera.se) |
| Allmän information | [inera.se](https://www.inera.se) |
