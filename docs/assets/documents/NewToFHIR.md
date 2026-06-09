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

## How to read an Implementation Guide

An Inera Implementation Guide is published on [Simplifier.net](https://simplifier.net) and is structured as follows:

1. **Introduction** — describes the purpose and scope of the standard.
2. **Profiles** — lists the FHIR resource profiles defined in the IG, with constraints and cardinalities.
3. **Extensions** — lists any custom extensions introduced.
4. **Terminology** — lists the ValueSets and CodeSystems used.
5. **Examples** — shows concrete example FHIR resources conforming to the profiles.
6. **CapabilityStatements** — describes what implementers must support.

> Start with the **Introduction** and **Use cases** before diving into the profiles. Understanding the clinical and business context makes it much easier to interpret the technical constraints.

## Useful external resources

- [HL7 FHIR R4 specification](https://hl7.org/fhir/R4/)
- [Simplifier.net](https://simplifier.net) — profile registry where Inera publishes its IGs
- [FHIR for beginners (HL7)](https://www.hl7.org/fhir/overview.html)
- [HL7 Sweden](https://hl7.se) — Swedish FHIR community and base profiles

## Questions?

If you have questions about Inera's FHIR work, contact us at [fhir@inera.se](mailto:fhir@inera.se).
