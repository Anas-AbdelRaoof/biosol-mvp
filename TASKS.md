# Biosol — Step-by-Step AI Development Tasks

> **Instructions for Coding Agent (ZooCode):**
> 1. Always read `PLAN.md` first for exact architecture, formulas, colors, API contracts, and connection rules.
> 2. Execute **ONLY** the specific Phase requested in the user prompt. Do not start future phases early.
> 3. Write clean, modular, type-safe, production-ready code with proper error handling.
> 4. Mark completed items with `[x]` in this file when finished.

---

## Phase 1: Project Scaffolding & Architecture
- [ ] **1.1 Backend Skeleton:** Create `backend/` directory structure (`core/`, `analysis/`, `ai/`, `api/`), `backend/requirements.txt` (`fastapi`, `uvicorn[standard]`, `pandas`, `numpy`, `scipy`, `scikit-learn`, `plotly`, `python-multipart`, `openai`, `pydantic-settings`), and `backend/.env.example`.
- [ ] **1.2 FastAPI Core & Health Check:** Implement `backend/core/config.py` using `pydantic-settings` (`LLM_API_KEY`, `LLM_BASE_URL`, `LLM_MODEL`, `CORS_ORIGINS`, `MAX_UPLOAD_MB=50`) and `backend/main.py` with CORS middleware, global exception handlers, and `GET /health` returning `{"status": "ok", "version": "0.1.0-mvp"}`.
- [ ] **1.3 Frontend Skeleton:** Initialize Vite + React + TypeScript + Tailwind CSS in `frontend/`, installing `@xyflow/react`, `plotly.js-dist-min`, `react-plotly.js`, `@types/react-plotly.js`, and `lucide-react`, plus `frontend/.env.example` (`VITE_API_BASE_URL=http://localhost:8000`).
- [ ] **1.4 Shared TypeScript Contracts:** Create `frontend/src/types/workflow.ts` defining `PortType`, `BlockType`, `BlockDefinition`, `BioNodeData`, `ExecutionResult`, `UploadMetadata`, and `ChatMessage` matching `PLAN.md` Section 4.
- [ ] **Verify Phase 1:** Confirm `uvicorn main:app` starts cleanly and `npm run build` succeeds in `frontend/` with zero TypeScript errors.

---

## Phase 2: Backend Core & Data Analysis Engine
- [ ] **2.1 Session Store:** Implement `backend/core/session_store.py` managing uploaded raw DataFrames (`session_id`) and cached intermediate node outputs (`session_id:node_id`) with automatic cleanup/TTL and safe handling of the first column as `Gene_ID` index.
- [ ] **2.2 File Overview Module:** Implement `backend/analysis/overview.py`:
  - `run_file_info(df)`: extracts column names, dtypes, non-null counts, total genes, and total samples.
  - `run_file_nd(df)`: computes `df.describe()` on numeric columns and converts metrics into biologist-friendly percentages and plain-English distribution summaries (zero-count %, high-expression %, missing data %).
- [ ] **2.3 Preprocessing Module:** Implement `backend/analysis/preprocessing.py`:
  - `run_clean_column(df, columns, method)`: supports `0`, `mean`, `median`, `drop_rows` across all or selected numeric columns.
  - `run_filter_genes(df, min_counts, min_samples)`: implements `df[(df >= min_counts).sum(axis=1) >= min_samples]`.
  - `run_log2_transform(df, columns)`: implements `np.log2(df[cols].clip(lower=0) + 1)`.
- [ ] **2.4 Visualization Module:** Implement `backend/analysis/visualization.py` returning `fig.to_json()` with clean white clinical styling:
  - `run_box_plot(df)`: interactive Plotly box plot across all sample columns.
  - `run_correlation_heatmap(df, method)`: computes `df.corr(method=method)` (`pearson`, `spearman`, `kendall`) and builds an annotated Plotly heatmap.
  - `run_pca_plot(df, sample_groups)`: transposes sample matrix, applies `StandardScaler` + `PCA(n_components=2)`, and returns a grouped Plotly scatter plot with % variance explained in axis labels.
- [ ] **2.5 Statistics Module:** Implement `backend/analysis/statistics.py`:
  - `run_deg(df, control_cols, treatment_cols)`: computes Log2 Fold Change and Welch's t-test (`scipy.stats.ttest_ind(..., equal_var=False)`), returning both a DataFrame (for downstream Volcano Plot) and formatted JSON rows (`Gene ID`, `Log2 Fold Change`, `P-value`, `Direction`).
  - `run_volcano_plot(deg_df, p_threshold, fc_threshold)`: validates DEG input columns and generates an interactive Plotly scatter plot (`Log2 Fold Change` vs `-Log10 P-value`) with red upregulated, blue downregulated, and grey non-significant dots.
- [ ] **2.6 File & Pipeline API Routes:** Implement `POST /api/upload` in `backend/api/routes_files.py` and `POST /api/execute-node` in `backend/api/routes_pipeline.py` (automatically executing any uncached nodes in `upstream_chain` before running the target node) and register routers in `backend/main.py`.
- [ ] **Verify Phase 2:** Run an automated test script verifying `Upload -> File Info -> File ND -> Clean -> Filter -> Log2 -> Box/Heatmap/PCA -> DEG -> Volcano` on a synthetic gene count CSV.

---

## Phase 3: AI Assistant Backend & `SYSTEM_PROMPT.md`
- [ ] **3.1 System Prompt:** Author `backend/ai/SYSTEM_PROMPT.md` establishing Biosol AI's identity as a specialized genetics and bioinformatics assistant that explains statistical metrics in plain biological terms, never fabricates gene functions or p-values, respects missing context, and recommends valid next Biosol blocks.
- [ ] **3.2 Llama 3.3 70B Service:** Implement `backend/ai/assistant.py` using `AsyncOpenAI` pointed at `LLM_BASE_URL` with `LLM_MODEL` (`llama-3.3-70b-versatile` default), injecting `SYSTEM_PROMPT.md`, active dataset metadata (gene count, sample names), latest executed node summary, and parsed content from any user-attached files.
- [ ] **3.3 AI Chat Route:** Implement `POST /api/ai/chat` in `backend/api/routes_ai.py` handling `multipart/form-data` (message, conversation history, `session_id`, active node context, and optional supplementary file uploads) and register in `backend/main.py`.
- [ ] **Verify Phase 3:** Test `POST /api/ai/chat` with dataset context and an attached gene list file to confirm accurate, grounded biological responses.

---

## Phase 4: Frontend Page 1 (Upload) & Page 2 (Workspace Shell)
- [ ] **4.1 Theme & App State:** Configure white (`#FFFFFF`) and simple red (`#DC2626`) palette in Tailwind, set up global workflow state in `App.tsx` (`sessionId`, `uploadMetadata`, `activeResult`), and handle transition between `UploadPage` and `WorkspacePage`.
- [ ] **4.2 Page 1 (`UploadPage.tsx`):** Build clean white landing & upload screen featuring:
  - Biosol logo/title, concise description, supported file formats, and size/format limits.
  - File type selector cards (`CSV` active and selected by default; `FASTQ` and others visible as disabled *"Coming Soon"* options).
  - Prominent red upload button (`#DC2626`) with drag-and-drop file dropzone support.
  - File details panel appearing beneath the upload button (filename, size, gene count, sample count, sample column pills, 5-row preview table) + red **"Enter Workspace"** button.
  - Subtle **MVP / Beta Version** badge.
- [ ] **4.3 Page 2 Workspace Shell (`WorkspacePage.tsx`):**
  - Top bar with Biosol branding, active dataset badge, "Upload New File" button, and MVP badge.
  - **Left Sidebar (`SidebarAI.tsx`):** Biosol AI chat stream, input box, send button, and file attachment button with selected-file chip.
  - **Center (`CanvasArea.tsx`):** Workspace container ready for React Flow.
  - **Right Sidebar (`SidebarBlocks.tsx`):** Collapsible, color-coded block palette grouped into Yellow (*File Overview*), Lime (*Cleaning & Preparation*), Orange-Green (*Data Visualization*), and Blue (*Data Analyses & Volcano Plot*).
  - **Bottom Drawer (`ResultsPanel.tsx`):** Collapsible/resizable drawer with tabs/views for Interactive Plots, Data Tables, and Biologist Summaries.
- [ ] **Verify Phase 4:** Confirm clean visual rendering, responsive pane sizing, and smooth navigation from Page 1 to Page 2.

---

## Phase 5: Interactive Drag-and-Drop Canvas & Port Validation
- [ ] **5.1 Connection Rules Engine:** Implement `frontend/src/lib/connectionRules.ts` encoding all port types (`RAW_DATA`, `PROCESSED_DATA`, `TEXT_REPORT`, `DEG_TABLE`, `VISUAL_PLOT`), terminal node rules, strict sequential rules (`Clean -> Filter -> Transform`, `Clean` only from `Upload`), and strict `DEG_TABLE -> Volcano Plot` enforcement returning exact error messages (e.g., `"Volcano Plot requires Differential Expression data."`).
- [ ] **5.2 Custom Block Node (`BioBlockNode.tsx`):** Build Scratch-inspired custom React Flow nodes styled with each category's exact color, typed input/output handles, status indicator (idle, running, success, error), inline `[X]`/`[Y]` parameter controls (column multi-select, NaN method dropdown, numeric thresholds, Volcano sliders, sample group assignment modal/popover for PCA & DEG), and an individual **"Run"** button.
- [ ] **5.3 Interactive Canvas (`CanvasArea.tsx`):** Initialize React Flow with the locked `Uploaded CSV` root node (`RAW_DATA` output), implement drag-and-drop block instantiation from `SidebarBlocks.tsx`, validate connections on `onConnect` / `isValidConnection`, display clear red toast notifications on invalid connection attempts, and compute `upstream_chain` automatically for any node.
- [ ] **Verify Phase 5:** Test dragging all 10 blocks, assigning sample groups for PCA/DEG, wiring valid pipelines, and verifying that invalid connections (such as connecting `Processed Data` to `Volcano Plot` or `Log2` before `Clean`) are blocked with clear error feedback.

---

## Phase 6: Full-Stack Wiring & Deployment Configs
- [ ] **6.1 Typed API Client (`frontend/src/lib/api.ts`):** Implement `uploadCsvFile`, `executePipelineNode`, and `sendAiChatMessage` using `VITE_API_BASE_URL` with clean error parsing.
- [ ] **6.2 End-to-End Upload & Node Execution:** Wire `UploadPage.tsx` to `POST /api/upload` and `BioBlockNode.tsx` "Run" buttons to `POST /api/execute-node`. Render Plotly JSON figures in `ResultsPanel.tsx` via `react-plotly.js` (`useResizeHandler`, responsive layout), sortable/searchable DEG tables with CSV export button, and formatted biologist summary cards for `File Info` and `File ND`.
- [ ] **6.3 End-to-End AI Sidebar:** Wire `SidebarAI.tsx` to `POST /api/ai/chat`, automatically passing `session_id`, the currently selected/executed node's result summary, and any attached files.
- [ ] **6.4 Production Deployment Configs:** Create `render.yaml` (configuring Python FastAPI web service with `uvicorn backend.main:app --host 0.0.0.0 --port $PORT` and env var placeholders) and `frontend/vercel.json` (SPA fallback rewrites), and verify CORS settings support Vercel domains.
- [ ] **Verify Phase 6:** Run full end-to-end verification in browser: upload a CSV, run File ND, execute `Clean -> Filter -> Log2 -> PCA` and `DEG -> Volcano Plot`, inspect interactive charts, and ask Biosol AI to interpret the results.
