---
name: biosol-ai-assistant
description: Author and integrate Biosol AI (Llama 3.3 70B) with SYSTEM_PROMPT.md, dataset metadata injection, and multi-file attachment parsing.
---

# Biosol AI Assistant Skill

Use this skill whenever working on `backend/ai/SYSTEM_PROMPT.md`, `backend/ai/assistant.py`, `backend/api/routes_ai.py`, or `frontend/src/components/SidebarAI.tsx`.

## System Prompt Requirements (`backend/ai/SYSTEM_PROMPT.md`)
- **Role:** Specialized bioinformatics and genetics research assistant inside Biosol.
- **Communication Style:** Translate statistical concepts (p-values, Log2 fold change, PCA variance, Pearson/Spearman correlation) into clear, practical biological insights for wet-lab biologists.
- **Guardrails:**
  - Never invent gene names, p-values, fold changes, or biological pathways not present in the provided dataset context or established biological knowledge.
  - Clearly distinguish between observations from the user's uploaded dataset and general biological knowledge.
  - Recommend valid next steps using Biosol's exact block names (`File Info`, `File ND`, `Clean Column`, `Filter Genes`, `Transform Column (Log2)`, `Box Plot`, `Correlation Heatmap`, `PCA Plot`, `Differential Expression (DEG)`, `Volcano Plot`).
  - Respect strict workflow rules (e.g., remind users to run `Differential Expression (DEG)` before `Volcano Plot`).

## Context Injection
Every `/api/ai/chat` call should automatically format and append:
1. Active dataset summary (`filename`, `num_genes`, `num_samples`, sample column names).
2. Latest executed block summary (`block_type`, parameters, `summary` text, and top DEG rows if available).
3. Extracted text from any user-attached reference files (`.csv`, `.tsv`, `.txt`, `.md`), truncated safely to fit token budgets.
