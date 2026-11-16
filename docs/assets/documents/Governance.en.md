# Governance of Inera's FHIR Specifications

This page describes the general governance for Inera's FHIR specifications — how they are developed, maintained, versioned and retired.

## Governance principles

Inera's FHIR specifications are governed according to the following principles:

- **Transparency** — all specifications and their change history are publicly available on GitHub and Simplifier.net.
- **Collaboration** — requirements are gathered in collaboration with regions, municipalities, system vendors and clinical stakeholders.
- **Stability** — breaking changes are minimised and communicated well in advance.
- **Interoperability** — Inera's profiles build on national base profiles from [HL7 Sweden](https://hl7.se) and international standards from HL7 International.

## Lifecycle of a FHIR specification

```
Requirement → Design → Review → Publish (pre-release) → Pilot → Publish (release) → Maintenance → Retirement
```

| Phase | Description |
|-------|-------------|
| **Requirement** | Business requirements are gathered from stakeholders and analysed. |
| **Design** | FHIR profiles, extensions and terminology are designed in collaboration with clinical and technical experts. |
| **Review** | Draft IG is reviewed by stakeholders and system vendors. Feedback is incorporated. |
| **Pre-release** | The IG is published as a pre-release (e.g. `1.0.0-beta.1`) for pilot implementations. Not for production use. |
| **Pilot** | Selected organisations implement and test the standard in a controlled environment. |
| **Release** | The IG is published as a stable release and approved for production use. |
| **Maintenance** | Ongoing bug fixes (patch versions) and minor improvements (minor versions). |
| **Retirement** | The standard is deprecated and eventually retired, with a migration path to a successor standard. |

## Versioning

Inera's FHIR specifications use [semantic versioning (SemVer 2.0)](https://semver.org/):

- `MAJOR.MINOR.PATCH` — e.g. `2.1.4`
- Pre-releases use a suffix — e.g. `2.0.0-beta.1`

| Version part | When it changes |
|---|---|
| **MAJOR** | Incompatible changes — existing implementations need to be updated. |
| **MINOR** | New features added in a backward-compatible way. |
| **PATCH** | Backward-compatible bug fixes. |

Major and minor version decisions are made in consultation with the relevant governance groups and documented in release notes.

## Roles and responsibilities

| Role | Responsibility |
|------|---------------|
| **Inera FHIR team** | Designs and maintains FHIR profiles and IGs. |
| **Service manager** | Owns the business requirements for a specific service. |
| **Stakeholder group** | Regions, municipalities and clinical experts who participate in requirements gathering and review. |
| **System vendors** | Implement the specifications and provide feedback from a technical implementation perspective. |

## Change request process

1. A change request is submitted as a GitHub issue or by email to [fhir@inera.se](mailto:fhir@inera.se).
2. Inera assesses the impact and urgency of the request.
3. The request is prioritised and scheduled for a future version.
4. The change is implemented, reviewed and published as part of a new version.
5. The requester is notified and the change is documented in the release notes.

## Questions?

Contact the Inera FHIR team at [fhir@inera.se](mailto:fhir@inera.se).
