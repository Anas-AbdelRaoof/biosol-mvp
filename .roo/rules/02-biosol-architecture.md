# Biosol Coding & Architecture Standards

1. **Backend (Python / FastAPI):**
   - Use Python 3.11+ type hints and Pydantic v2 models for all request/response schemas.
   - Keep `backend/analysis/` functions pure (accepting a Pandas DataFrame + parameters, returning structured dicts or Plotly JSON strings via `fig.to_json()`), decoupled from FastAPI HTTP objects.
   - Always treat the first column of uploaded genetic CSVs as the `Gene_ID` index so gene identifiers are never included in numerical calculations.
   - Never send full gene matrices back to the frontend over JSON; store them in `backend/core/session_store.py` keyed by `session_id` and `node_id`.

2. **Frontend (React / TypeScript / Tailwind):**
   - Enforce strict TypeScript types (`frontend/src/types/workflow.ts`) with zero `any` types.
   - Follow the exact UI theme: clinical white (`#FFFFFF`) background with simple red (`#DC2626`) primary accents, and exact block group colors (`Yellow #FACC15`, `Lime #84CC16`, `Orange-Green #F97316/#10B981`, `Blue #3B82F6`).
   - All visualizations must use `react-plotly.js` rendering backend-generated Plotly JSON.
