# Frequently Asked Questions

## General

**What is Inera's role in FHIR standardisation?**

Inera manages the national digital infrastructure for Swedish healthcare and is responsible for defining how FHIR should be used within the national services it operates. Inera's FHIR Implementation Guides define profiles adapted to Swedish requirements — such as the use of the personal identity number (personnummer) and HSA-id — and are built on top of the base profiles from [HL7 Sweden](https://hl7.se).

**Where are Inera's Implementation Guides published?**

All Inera FHIR Implementation Guides are published at [fhir.inera.se](https://fhir.inera.se) following the URL pattern `https://fhir.inera.se/ig/<name>/`. For example:

- [fhir.inera.se/ig/core/](https://fhir.inera.se/ig/core/)
- [fhir.inera.se/ig/careteam/](https://fhir.inera.se/ig/careteam/)
- [fhir.inera.se/ig/forms/](https://fhir.inera.se/ig/forms/)

Source code and issue tracking are available on [GitHub](https://github.com/Inera-AB).

---

## Implementation

**What version of FHIR do Inera's specifications use?**

Inera's current specifications target **FHIR R4** (version 4.0.1).

**Do I need to implement all profiles in an IG?**

No. Each IG's CapabilityStatement specifies which profiles and interactions are required (SHALL) versus recommended (SHOULD) or optional (MAY) for a given actor (client or server). Start by reading the CapabilityStatement for your role.

**Where can I find example FHIR resources?**

Example resources are included in each Implementation Guide at [fhir.inera.se](https://fhir.inera.se). They can be downloaded as JSON or XML and used as a starting point for your implementation.

**Can I validate my FHIR resources against Inera's profiles?**

Yes. You can validate resources using the official [HL7 FHIR Validator](https://confluence.hl7.org/display/FHIR/Using+the+FHIR+Validator) with the relevant Inera IG loaded from [fhir.inera.se](https://fhir.inera.se).

---

## Testing

**How do I get access to Inera's test environments?**

Contact Inera Customer Service at [kundservice@inera.se](mailto:kundservice@inera.se) or the responsible service manager for the specific service. Access to test environments typically requires a signed agreement.

**Is there a sandbox or open test environment?**

Inera currently provides test environments for connected system vendors. Please refer to the documentation for the specific service you are implementing to find out what test infrastructure is available.

---

## Change management

**How are changes to Inera's FHIR specifications communicated?**

Changes are communicated through:

- Release notes in the Implementation Guide.
- GitHub releases and issues in the relevant repository.
- Inera's website and newsletters.

**How do I report a bug or suggest an improvement?**

- For technical issues with an IG: create an issue in the relevant [Inera GitHub repository](https://github.com/Inera-AB).
- For other questions: write to [fhir@inera.se](mailto:fhir@inera.se).

---

## Contact

| Topic | Contact |
|-------|---------|
| Technical FHIR questions | [fhir@inera.se](mailto:fhir@inera.se) |
| Customer service | [kundservice@inera.se](mailto:kundservice@inera.se) |
| General information | [inera.se](https://www.inera.se) |
