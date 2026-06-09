# Welcome to Inera's FHIR® Standards

**Table of contents**

* [1 Inera's FHIR standards](#1-ineras-fhir-standards)
* [2 Implementing an Inera FHIR standard](#2-implementing-an-inera-fhir-standard)
    * [2.1 Standard documentation](#21-standard-documentation)
    * [2.2 General governance for Inera FHIR standards](#22-general-governance-for-inera-fhir-standards)
* [3 Test and verification](#3-test-and-verification)
* [4 Change management and versioning](#4-change-management-and-versioning)
    * [4.1 Versioning of Inera FHIR standards](#41-versioning-of-inera-fhir-standards)
    * [4.2 Change requests and improvements](#42-change-requests-and-improvements)
* [5 Want to stay updated?](#5-want-to-stay-updated)
* [6 New to FHIR?](#6-new-to-fhir)
* [7 Frequently asked questions](#7-frequently-asked-questions)

---

Inera manages and develops national digital infrastructure for Swedish healthcare. As part of this work, Inera publishes FHIR-based Implementation Guides (IGs) that enable standardised and interoperable information exchange between healthcare systems and actors across Sweden.

The purpose of this site is to guide you to the right documentation and technical specifications for Inera's FHIR standards.

> **Note:** Technical documentation is published in English. Clinical guidelines and governance documents are published in Swedish.

---

## 1 Inera's FHIR standards

Inera's FHIR standards cover a wide range of national e-health services. Each standard is described in an Implementation Guide (IG) containing profiles, extensions, terminology and rules for how information shall be structured and exchanged.

All Inera FHIR Implementation Guides are published at **[fhir.inera.se](https://fhir.inera.se)**. Each IG follows a predictable URL pattern based on its name:

```
https://fhir.inera.se/ig/<name>/
```

For example: [`fhir.inera.se/ig/core/`](https://fhir.inera.se/ig/core/), [`fhir.inera.se/ig/careteam/`](https://fhir.inera.se/ig/careteam/).

Some profiles are shared across multiple standards. These are gathered in Inera's core profiles and reused in the service-specific IGs. Terminology — code systems, value sets and concept maps — is provided by Inera's national terminology server.

The table below provides an overview of Inera's FHIR standards, divided into three parts:

1. **Inera's FHIR services** — service-specific standards and their business requirements.
2. **Terminology** — Inera's national terminology server.
3. **Generic profiles** — profiles reused across multiple standards.

<br>

<div style="overflow-x:auto;">
<table class="tg" id="Tab1">
<caption style="color:#7E2A4C;font-weight:bold;text-align:left;padding-bottom:6px;">Table 1: Overview of Inera's FHIR standards</caption>
<colgroup>
<col style="width:20%">
<col style="width:20%">
<col style="width:50%">
<col style="width:10%">
</colgroup>
<thead>
  <tr>
    <th class="tg-header">Service</th>
    <th class="tg-header">Swedish name</th>
    <th class="tg-header">Short description</th>
    <th class="tg-header">Version</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-category" colspan="4"><em>Inera's national services</em></td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://fhir.inera.se/ig/careteam/" target="_blank">Inera CareTeam</a></td>
    <td class="tg-cell">Fast vårdkontakt via 1177</td>
    <td class="tg-cell">Profiles for representing a patient's designated care contact (fast vårdkontakt) and care team. Used as the first FHIR profile in the 1177 Journal service.</td>
    <td class="tg-cell">See IG</td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://fhir.inera.se/ig/forms/" target="_blank">Inera FHIR Forms</a></td>
    <td class="tg-cell">Formulärtjänsten</td>
    <td class="tg-cell">Profiles for <code>Questionnaire</code> and <code>QuestionnaireResponse</code> supporting Inera's national forms service. Enables structured collection and exchange of form-based health information.</td>
    <td class="tg-cell">See IG</td>
  </tr>
  <tr>
    <td class="tg-category" colspan="4"><em>Terminology</em></td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://test.api.terminologitjansten.inera.se" target="_blank">Inera Terminologitjänst</a></td>
    <td class="tg-cell">Terminologitjänsten</td>
    <td class="tg-cell">Inera's national terminology server providing CodeSystems, ValueSets and concept lookups used across Swedish healthcare. Exposes a FHIR Terminology API.</td>
    <td class="tg-cell"></td>
  </tr>
  <tr>
    <td class="tg-category" colspan="4"><em>Generic profiles</em></td>
  </tr>
  <tr>
    <td class="tg-cell"><a href="https://fhir.inera.se/ig/core/" target="_blank">Inera Core</a></td>
    <td class="tg-cell">Kärnprofiler</td>
    <td class="tg-cell">Foundational profiles reused across Inera's FHIR standards, e.g. Patient, Organisation and Practitioner profiles adapted to Swedish requirements (personal identity number, HSA-id, etc.).</td>
    <td class="tg-cell">See IG</td>
  </tr>
</tbody>
</table>
</div>

<br><br>

## 2 Implementing an Inera FHIR standard

When implementing an Inera FHIR standard it is important to understand both the business context and the technical specifications. The sections below describe the key components of the standard documentation and the governance that governs how information exchange shall be carried out.

<br>

### 2.1 Standard documentation

Each Inera FHIR standard is delivered with documentation that describes how the standard should be used and what requirements apply. The documentation may consist of:

- **Implementation Guide (IG):** The technical specifications for the standard, published at [fhir.inera.se/ig/\<name\>/](https://fhir.inera.se).
- **Clinical guidelines:** Background and clinical rationale behind the standard.
- **Use cases:** Descriptions of the intended scenarios for the standard.
- **Test protocol:** Used during test and verification to document that the implementation fulfils the standard.
- **Conformance resources:** FHIR CapabilityStatements and OperationDefinitions describing what a server or client must support.

<br>

### 2.2 General governance for Inera FHIR standards

The governance describes how Inera manages the lifecycle of its FHIR standards — from requirements gathering and publication to change management and decommissioning. It is important to understand the governance process before starting an implementation.

[Click here for more information about governance of Inera's FHIR standards.](assets/documents/Governance.md)

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

### 4.1 Versioning of Inera FHIR standards

Inera's FHIR standards follow [semantic versioning (SemVer 2.0)](https://semver.org/), adapted to Inera's governance process. A version identifier consists of three numbers separated by dots, e.g. **2.1.4**, representing *major.minor.patch*:

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

You can also follow [inera.se](https://www.inera.se) for news about service development and FHIR standards.

<br>

## 6 New to FHIR?

This section provides a brief introduction to FHIR for those who are new to it or have limited experience with the standard. You will find an overview of the most commonly used terms, a step-by-step guide to how an Implementation Guide is structured, and links to external resources for further learning.

[Click here for an introduction to FHIR and how to read an Implementation Guide.](assets/documents/NewToFHIR.md)

<br>

## 7 Frequently asked questions

Here you will find answers to the most common questions about Inera's FHIR work and how to get started.

[Click here to read frequently asked questions.](assets/documents/FAQ.md)
