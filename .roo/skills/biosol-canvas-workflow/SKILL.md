---
name: biosol-canvas-workflow
description: Build and maintain the React Flow drag-and-drop canvas, Scratch-style genetic analysis blocks, strict port type validation rules, and Plotly results drawer.
---

# Biosol Canvas & Block Validation Skill

Use this skill whenever implementing or modifying `frontend/src/lib/connectionRules.ts`, `frontend/src/components/CanvasArea.tsx`, `frontend/src/components/nodes/BioBlockNode.tsx`, `frontend/src/components/SidebarBlocks.tsx`, or `frontend/src/components/ResultsPanel.tsx`.

## Port Types & Block Colors
- `RAW_DATA` / `PROCESSED_DATA` (Blue port `#3B82F6`): Tabular gene expression DataFrame.
- `TEXT_REPORT` (Yellow port `#FACC15`): Terminal text/stats output (no output handle).
- `DEG_TABLE` (Purple port `#8B5CF6`): Differential expression gene table.
- `VISUAL_PLOT` (Green port `#10B981`): Terminal Plotly visualization (no output handle).

## Strict Connection Validation Matrix
Implement these exact checks inside `connectionRules.ts` and reject invalid edges with a clear user-facing error message:
1. **Terminal Blocks Have No Outputs:** `file_info`, `file_nd`, `box_plot`, `correlation_heatmap`, `pca_plot`, and `volcano_plot` cannot be source nodes.
2. **Overview Blocks (`Yellow`):** `file_info` and `file_nd` accept `RAW_DATA` from `upload_csv` (or `PROCESSED_DATA`).
3. **Sequential Cleaning Chain (`Lime`):**
   - `clean_column`: ONLY accepts `RAW_DATA` directly from `upload_csv`.
   - `filter_genes`: Accepts `RAW_DATA` (from `upload_csv`) OR `PROCESSED_DATA` (from `clean_column`). Cannot come after `log2_transform`.
   - `log2_transform`: Accepts `PROCESSED_DATA` (from `clean_column` or `filter_genes`). Cannot connect directly to `upload_csv` before cleaning/filtering.
4. **Visualization Blocks (`Orange-Green`):** `box_plot`, `correlation_heatmap`, `pca_plot` accept `RAW_DATA` or `PROCESSED_DATA`.
5. **DEG Block (`Blue`):** `deg` accepts `PROCESSED_DATA` (or `RAW_DATA` with a gentle warning) and outputs `DEG_TABLE`.
6. **Volcano Plot (`Blue/Purple`):** `volcano_plot` **ONLY** accepts `DEG_TABLE` from `deg`. If a user attempts to connect `RAW_DATA` or `PROCESSED_DATA` to `volcano_plot`, block the connection and display: `"Volcano Plot requires Differential Expression data."`

## Topological Upstream Resolution
When the user clicks **Run** on any node, traverse incoming edges backwards to build `upstream_chain` in execution order (`root -> ... -> parent`) so the backend can compute and cache any uncached intermediate nodes automatically.
