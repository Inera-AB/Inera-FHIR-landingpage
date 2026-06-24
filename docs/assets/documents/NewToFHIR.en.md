# New to FHIR?

This page provides a brief introduction to FHIR for those who are new to it or have limited experience with the standard.

## What is FHIR?

**FHIR** (Fast Healthcare Interoperability Resources) is an international standard developed by [HL7 International](https://www.hl7.org/fhir/) for the exchange of healthcare information. FHIR defines a set of **resources** — building blocks that represent common healthcare concepts such as a Patient, an Observation, a Medication or an Appointment.

FHIR is designed to be:

- **Web-friendly** — resources are exchanged using standard web technologies (HTTP, JSON, XML).
- **Modular** — you combine resources to represent complex healthcare scenarios.
- **Extensible** — base resources can be profiled and extended to fit local requirements.

## Key concepts

| Term | Description |
|------|-------------|
| **Resource** | A discrete unit of interoperable information, e.g. `Patient`, `Observation`, `MedicationRequest`. |
| **Profile** | A set of constraints applied to a base resource to fit a specific use case or national context. |
| **Implementation Guide (IG)** | A collection of profiles, extensions, value sets and narrative documentation for a specific standard or domain. |
| **Extension** | An additional data element added to a resource beyond what is in the base FHIR specification. |
| **ValueSet / CodeSystem** | Defines the coded values (terminology) that can be used in a given field. |
| **CapabilityStatement** | Describes what a FHIR server or client supports — which resources, interactions and search parameters. |

## How Inera authors Implementation Guides

Inera authors FHIR Implementation Guides using **FHIR Shorthand (FSH)** and the **FHIR IG Publisher**. This toolchain is the HL7-recommended way to produce IGs and is used by national programmes worldwide.

### FHIR Shorthand (FSH)

[FHIR Shorthand](https://build.fhir.org/ig/HL7/fhir-shorthand/) is a domain-specific language designed specifically for defining FHIR profiles, extensions, value sets and examples. It is compact and human-readable, making it much easier to author and review than raw JSON or XML StructureDefinitions.

A simple FSH profile looks like this:

```fsh
Profile: IneraPatient
Parent: Patient
Id: inera-patient
Title: "Inera Patient"
Description: "Patient profile adapted for Swedish national services."

* identifier 1..* MS
* identifier ^slicing.discriminator.type = #pattern
* identifier ^slicing.discriminator.path = "system"
* identifier ^slicing.rules = #open
```

**Learn FSH at [FSH School](https://fshschool.org)** — an interactive online course that walks you through the FSH language from basics to advanced profiling, with live exercises directly in the browser.

### IG Publisher and IG Builder

The **FHIR IG Publisher** is the official HL7 tool that takes FSH source files and produces a complete, publishable Implementation Guide website — including rendered profiles, examples, validation, and a navigable HTML site.

The **[IG Builder guidance](https://build.fhir.org/ig/FHIR/ig-guidance/)** on build.fhir.org covers everything you need to know about setting up and running an IG project:

- Project folder structure and `sushi-config.yaml`
- Running SUSHI (the FSH compiler) and the IG Publisher
- Configuring pages, menus and narrative content
- Publishing and CI/CD pipelines

The continuous integration server at [build.fhir.org](https://build.fhir.org) automatically builds every IG hosted on GitHub and makes a live preview available — Inera uses this for pre-release review of IGs before they are formally published.

## How to read an Implementation Guide

Inera's Implementation Guides are published at [fhir.inera.se](https://fhir.inera.se) following the URL pattern `https://fhir.inera.se/ig/<name>/` — for example [fhir.inera.se/ig/core/](https://fhir.inera.se/ig/core/). Each IG is structured as follows:

1. **Introduction** — describes the purpose and scope of the standard.
2. **Profiles** — lists the FHIR resource profiles defined in the IG, with constraints and cardinalities.
3. **Extensions** — lists any custom extensions introduced.
4. **Terminology** — lists the ValueSets and CodeSystems used.
5. **Examples** — shows concrete example FHIR resources conforming to the profiles.
6. **CapabilityStatements** — describes what implementers must support.

> Start with the **Introduction** and **Use cases** before diving into the profiles. Understanding the clinical and business context makes it much easier to interpret the technical constraints.

## Useful external resources

- [Inera FHIR standards](https://fhir.inera.se) — all Inera IGs
- [HL7 FHIR R4 specification](https://hl7.org/fhir/R4/)
- [FSH School](https://fshschool.org) — interactive course for learning FHIR Shorthand
- [IG Builder guidance](https://build.fhir.org/ig/FHIR/ig-guidance/) — official guide to authoring and publishing FHIR IGs
- [FHIR Shorthand specification](https://build.fhir.org/ig/HL7/fhir-shorthand/) — full FSH language reference
- [build.fhir.org](https://build.fhir.org) — continuous build server for FHIR IGs
- [FHIR for beginners (HL7)](https://www.hl7.org/fhir/overview.html)
- [HL7 Sweden](https://hl7.se) — Swedish FHIR community and base profiles

## Questions?

If you have questions about Inera's FHIR work, contact us at [fhir@inera.se](mailto:fhir@inera.se).
