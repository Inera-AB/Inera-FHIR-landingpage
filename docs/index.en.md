# Welcome to Inera's FHIR® Specifications

**Table of contents**

* [1 Inera's FHIR specifications](#1-ineras-fhir-standards)
* [2 Implementing an Inera FHIR specification](#2-implementing-an-inera-fhir-standard)
    * [2.1 Specification documentation](#21-specification-documentation)
    * [2.2 General governance for Inera FHIR specifications](#22-general-governance-for-inera-fhir-standards)
* [3 Test and verification](#3-test-and-verification)
* [4 Change management and versioning](#4-change-management-and-versioning)
    * [4.1 Versioning of Inera FHIR specifications](#41-versioning-of-inera-fhir-standards)
    * [4.2 Change requests and improvements](#42-change-requests-and-improvements)
* [5 Want to stay updated?](#5-want-to-stay-updated)
* [6 New to FHIR?](#6-new-to-fhir)
* [7 Frequently asked questions](#7-frequently-asked-questions)

---

Inera manages and develops national digital infrastructure for Swedish healthcare. As part of this work, Inera publishes FHIR-based Implementation Guides (IGs) that enable standardised and interoperable information exchange between healthcare systems and actors across Sweden.

The purpose of this site is to guide you to the right documentation and technical specifications for Inera's FHIR specifications.

> **Note:** Technical documentation is published in English. Clinical guidelines and governance documents are published in Swedish.

---

## 1 Inera's FHIR specifications

Inera's FHIR specifications cover a wide range of national e-health services. Each specification is described in an Implementation Guide (IG) containing profiles, extensions, terminology and rules for how information shall be structured and exchanged.

All Inera FHIR Implementation Guides are published at **[fhir.inera.se](https://fhir.inera.se)**. Each IG follows a predictable URL pattern based on its name:

```
https://fhir.inera.se/ig/<name>/
```

For example: [`fhir.inera.se/ig/core/`](https://fhir.inera.se/ig/core/), [`fhir.inera.se/ig/careteam/`](https://fhir.inera.se/ig/careteam/).

### Published Implementation Guides

A complete and up-to-date listing of all published Inera FHIR Implementation Guides is available at **[fhir.inera.se/ig/](https://fhir.inera.se/ig/index.html)**. Currently published IGs include:

- **[Inera CareTeam](https://fhir.inera.se/ig/careteam/)** — Profiles for representing a patient's designated care contact (*fast vårdkontakt*) and care team. Used as the first FHIR profile in the 1177 Journal service.
- **[Inera FHIR Forms](https://fhir.inera.se/ig/forms/)** — Profiles for `Questionnaire` and `QuestionnaireResponse` supporting Inera's national forms service. Enables structured collection and exchange of form-based health information.

### Terminology Service

**[Inera Terminologitjänst](https://test.api.terminologitjansten.inera.se)** (*Terminologitjänsten*) is Inera's national terminology server providing CodeSystems, ValueSets and concept lookups used across Swedish healthcare. It exposes a FHIR Terminology API.

### Tools and Support

- **Inera Core** *(coming soon)* — Foundational profiles reused across Inera's FHIR specifications, e.g. Patient, Organisation and Practitioner profiles adapted to Swedish requirements (personal identity number, HSA-id, etc.).
- **[IneraFHIRTemplate](https://github.com/Inera-AB/IneraFHIRTemplate)** — A GitHub template repository for creating new Inera FHIR Implementation Guides, with pre-configured toolchain, CI/CD and Inera branding.

<br><br>

## 2 Implementing an Inera FHIR specification

When implementing an Inera FHIR specification it is important to understand both the business context and the technical specifications. The sections below describe the key components of the specification documentation and the governance that governs how information exchange shall be carried out.

<br>

### 2.1 Specification documentation

Each Inera FHIR specification is delivered with documentation that describes how the specification should be used and what requirements apply. The documentation may consist of:

- **Implementation Guide (IG):** The technical specifications for the standard, published at [fhir.inera.se/ig/\<name\>/](https://fhir.inera.se).
- **Clinical guidelines:** Background and clinical rationale behind the standard.
- **Use cases:** Descriptions of the intended scenarios for the standard.
- **Test protocol:** Used during test and verification to document that the implementation fulfils the standard.
- **Conformance resources:** FHIR CapabilityStatements and OperationDefinitions describing what a server or client must support.

<br>

### 2.2 General governance for Inera FHIR specifications

The governance describes how Inera manages the lifecycle of its FHIR specifications — from requirements gathering and publication to change management and decommissioning. It is important to understand the governance process before starting an implementation.

[Click here for more information about governance of Inera's FHIR specifications.](assets/documents/Governance.md)

<br>

## 3 Test and verification

Before an implementation is put into production and starts exchanging patient information, it must be verified against Inera's test environments. Inera provides:

- **Test environments (QA/Staging):** Separate environments for integration and system testing.
- **Validators:** Ability to validate FHIR resources against published profiles using the [HL7 FHIR Validator](https://confluence.hl7.org/display/FHIR/Using+the+FHIR+Validator) with the relevant Inera IG loaded from [fhir.inera.se](https://fhir.inera.se).
- **Conformance testing:** Inera can offer support for conformance testing against published CapabilityStatements.

Contact Inera Customer Service or the responsible service manager to start the testing process for a specific service.

> Contact: [kundservice@inera.se](mailto:kundservice@inera.se)

<br>

## 4 Change management and versioning

### 4.1 Versioning of Inera FHIR specifications

Inera's FHIR specifications follow [semantic versioning (SemVer 2.0)](https://semver.org/), adapted to Inera's governance process. A version identifier consists of three numbers separated by dots, e.g. **2.1.4**, representing *major.minor.patch*:

- **MAJOR** — changed when making incompatible changes to the API or profiling.
- **MINOR** — changed when adding new functionality in a backward-compatible manner.
- **PATCH** — changed when making backward-compatible bug fixes.

A version with a suffix such as `2.1.0-beta.1` is a pre-release and is not intended for production use.

Major version changes (major and minor) are decided in consultation with relevant governance groups and communicated via Inera's website and GitHub.

<br>

### 4.2 Change requests and improvements

System vendors and healthcare organisations are welcome to submit requests for changes or improvements:

- **Technical questions about an IG:** Create an issue in the relevant [Inera GitHub repository](https://github.com/Inera-AB).
- **Business questions or other documentation:** Contact the responsible service manager or write to [fhir@inera.se](mailto:fhir@inera.se).

Inera performs an impact assessment of incoming requests and decides whether and when changes should be implemented and which version level is affected.

<br>

## 5 Want to stay updated?

You can subscribe to updates from Inera's FHIR repositories on GitHub:

1. Go to [Inera AB on GitHub](https://github.com/Inera-AB).
2. Choose the repository you want to follow.
3. Click the **Watch** button in the upper right corner and select your preferred notification option.

> You need a GitHub account to watch a repository. Create a free account at [github.com/signup](https://github.com/signup).

You can also follow [inera.se](https://www.inera.se) for news about service development and FHIR specifications.

<br>

## 6 New to FHIR?

This section provides a brief introduction to FHIR for those who are new to it or have limited experience with the standard. You will find an overview of the most commonly used terms, a step-by-step guide to how an Implementation Guide is structured, and links to external resources for further learning.

[Click here for an introduction to FHIR and how to read an Implementation Guide.](assets/documents/NewToFHIR.md)

<br>

## 7 Frequently asked questions

Here you will find answers to the most common questions about Inera's FHIR work and how to get started.

[Click here to read frequently asked questions.](assets/documents/FAQ.md)
