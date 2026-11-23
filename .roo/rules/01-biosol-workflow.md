# Biosol Workspace Execution Rules

1. **Single Source of Truth:** Always consult `PLAN.md` for architecture, directory paths, API contracts, formulas, colors, and port connection rules before writing code.
2. **Strict Phase Isolation:** Implement ONLY the specific Phase requested in the user's prompt from `TASKS.md`. Never implement future phases or modify unrelated directories prematurely.
3. **Checklist Maintenance:** Update `TASKS.md` by changing `[ ]` to `[x]` as each subtask is completed and verified.
4. **No Placeholder Stubs:** Every function, endpoint, and component written for the active phase must be complete, typed, and functional—never leave `TODO` pass-through stubs.
5. **Token Efficiency:** Read only the files relevant to the current phase. Keep explanations concise and focused on verification steps.
