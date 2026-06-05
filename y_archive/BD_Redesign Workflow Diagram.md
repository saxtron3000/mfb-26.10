# BD_Redesign Workflow Diagram

# Diploma Redesign Workflow

```mermaid
flowchart TD
 NN["🔒 Non-Negotiables<br/>Bitcoin-only education<br/>Core Outcomes fixed<br/>Modular & adaptable"] --> A["1. Define the End"]
 
 A --> B["2. Define Outcomes"]
 B --> C["3. Define Evidence"]
 C --> D["4. Design Structure"]
 D --> E["5. Decide Delivery Constraints"]
 E --> F["6. Rewrite Diploma and Guide"]
 F --> G["7. Pilot Test with Teachers"]
 G --> H{"Achieves Phase 1<br/>goals & success criteria?"}
 H -->|Issues found| I["Return to Phase<br/>for revision"]
 I --> G
 H -->|Success| J["✓ Launch & Monitor"]

 subgraph P1["Phase 1: Define the End"]
 A1["Purpose of the diploma"]
 A2["Primary audience"]
 A3["Learner end state"]
 A4["Meaning of certificate"]
 A5["Definition of success"]
 end

 subgraph P2["Phase 2: Define Outcomes"]
 B1["Whole-program outcomes"]
 B2["Module outcomes"]
 B3["Essential vs optional outcomes"]
 B4["Knowledge, reasoning, practical skills"]
 B5["Outcomes aligned with Evidence model"]
 end

 subgraph P3["Phase 3: Define Evidence"]
 C1["Assessment model"]
 C2["Passing criteria"]
 C3["Continuous, final, or mixed"]
 C4["Practical and theoretical evidence"]
 C5["What the diploma certifies"]
 end

 subgraph P4["Phase 4: Design Structure"]
 D1["Linear, modular, or semi-modular"]
 D2["Module order & prerequisites"]
 D3["Lesson duration"]
 D4["Pacing model"]
 D5["Coherence & spiral review"]
 end

 subgraph P5["Phase 5: Decide Delivery Constraints"]
 E1["In-person first or online first"]
 E2["Fixed vs. flexible elements"]
 E3["Teacher role & support needs"]
 E4["Tech requirements"]
 E5["Resource assumptions"]
 end

 subgraph P6["Phase 6: Rewrite Diploma and Guide"]
 F1["Content audit: keep, cut, move, rewrite"]
 F2["Student material decisions"]
 F3["Teacher guide decisions"]
 F4["Ensure alignment with Phase 1 purpose"]
 end

 A -.-> P1
 B -.-> P2
 C -.-> P3
 D -.-> P4
 E -.-> P5
 F -.-> P6

 classDef phase1 fill:#e1f5ff,stroke:#01579b,stroke-width:2px
 classDef phase2 fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
 classDef phase3 fill:#fff3e0,stroke:#e65100,stroke-width:2px
 classDef validation fill:#fce4ec,stroke:#880e4f,stroke-width:2px
 classDef success fill:#e0f2f1,stroke:#004d40,stroke-width:2px

 class P1 phase1
 class P2 phase2
 class P3 phase3
 class P5,P6 phase3
 class G,H validation
 class J success
```

## Legend

* **🔒 Non-Negotiables** — Constraints that apply to every phase
* **Phase 1–2** — Leadership and curriculum team define the vision
* **Phase 3–5** — Curriculum, pedagogy, and logistics take shape
* **Phase 6** — Full team writes/revises materials
* **Phase 7 (Validation)** — Pilot test against Phase 1 goals; loop back if needed

## Key Improvements

✅ **Non-Negotiables gate** — Sits above Phase 1, constrains all decisions\n✅ **Validation loop** — Phase 7 tests against Phase 1 success criteria; feeds back if needed\n✅ **Phase 5 clarification** — "Fixed vs. flexible elements" made explicit\n✅ **Phase 2 addition** — "Outcomes aligned with Evidence model" ensures Phase 2–3 alignment\n✅ **Phase 4 addition** — "Coherence & spiral review" added\n✅ **Phase 6 clarification** — Added "Ensure alignment with Phase 1 purpose"\n✅ **Color-coding** — Visual distinction between decision layers (optional; can be removed if not needed)\n✅ **Return loop** — If pilot testing fails, you return to the relevant phase—not back to square one

## Usage


1. Start at Non-Negotiables
2. Move linearly through Phases 1–6
3. Use Phase 7 to validate against Phase 1 goals
4. If issues found, return to the relevant phase for revision (not necessarily the beginning)
5. Once pilot succeeds, move to "Launch & Monitor"