---
name: biosol-bioinformatics-engine
description: Build and verify the Python genetic expression analysis blocks (File Info, File ND, Clean, Filter, Log2, Box Plot, Correlation Heatmap, PCA, DEG, Volcano Plot) with exact biological formulas and Plotly JSON outputs.
---

# Biosol Bioinformatics Engine Skill

Use this skill whenever implementing, testing, or debugging files inside `backend/analysis/` or `backend/api/routes_pipeline.py`.

## Core Data Assumptions
- Input DataFrames have `Gene_ID` as the index and sample names (e.g., `Control_1`, `Treat_1`) as columns.
- Always validate that required numeric columns exist and return clean HTTP 400 errors with biologist-friendly messages if inputs are invalid (e.g., empty after filtering, fewer than 2 samples per group in DEG).

## Exact Formulas & Output Contracts
1. **File Info (`overview.py`):** Capture `df.info()` buffer plus structured counts (`num_genes`, `num_samples`, column dtypes, missing value counts). Output type: `TEXT_REPORT`.
2. **File ND (`overview.py`):** Run `df.describe()` and translate into plain-English biologist percentages:
   - Percentage of zero-expression entries across the matrix.
   - Percentage of missing (`NaN`) values.
   - Percentage of genes with high expression (above 75th percentile) and plain-language summary of sample consistency.
   - Avoid raw statistical jargon where possible. Output type: `TEXT_REPORT`.
3. **Clean Column (`preprocessing.py`):** Replace `NaN` in target columns (`all` or selected list) using `0`, column `mean`, column `median`, or `drop_rows`. Output type: `PROCESSED_DATA`.
4. **Filter Genes (`preprocessing.py`):** Keep rows where expression `>= min_counts` in at least `min_samples` columns:
   `df = df[(df >= min_counts).sum(axis=1) >= min_samples]`
   Output type: `PROCESSED_DATA`.
5. **Log2 Transform (`preprocessing.py`):** Apply `np.log2(df[cols].clip(lower=0) + 1)`. Output type: `PROCESSED_DATA`.
6. **Box Plot (`visualization.py`):** Plotly `go.Box` per sample column on white clinical background (`template="plotly_white"`). Return `fig.to_json()`. Output type: `VISUAL_PLOT`.
7. **Correlation Heatmap (`visualization.py`):** Compute `df.corr(method=method)` (`pearson`, `spearman`, or `kendall`) and render annotated Plotly heatmap (`colorscale="RdBu_r"`, `zmin=-1`, `zmax=1`). Return `fig.to_json()`. Output type: `VISUAL_PLOT`.
8. **PCA Plot (`visualization.py`):** Transpose (`df.T` so rows = samples, cols = genes), run `StandardScaler().fit_transform(...)` then `PCA(n_components=2)`, and plot PC1 vs PC2 colored by user-assigned `sample_groups` with explained variance % in axis titles. Return `fig.to_json()`. Output type: `VISUAL_PLOT`.
9. **Differential Expression / DEG (`statistics.py`):**
   - Compare `control_cols` (`X`) vs `treatment_cols` (`Y`).
   - Detect if data is already log2-scaled (e.g., max value < 30); if log2-scaled, `log2_fc = mean(Y) - mean(X)`, else `log2_fc = np.log2((mean(Y) + 1e-9) / (mean(X) + 1e-9))`.
   - Run Welch's t-test: `scipy.stats.ttest_ind(df[treatment_cols], df[control_cols], axis=1, equal_var=False, nan_policy="omit")`.
   - Cache full DEG DataFrame in `session_store` (needed by Volcano Plot) and return sorted top genes (`Gene_ID`, `log2_fc`, `p_value`, `direction`). Output type: `DEG_TABLE`.
10. **Volcano Plot (`statistics.py`):**
    - Requires upstream `DEG_TABLE` DataFrame (`log2_fc`, `p_value`).
    - Compute `neg_log10_p = -np.log10(np.clip(p_value, 1e-300, 1.0))`.
    - Classify dots: Upregulated (`log2_fc >= fc_threshold` and `p_value <= p_threshold`) in `#DC2626` (red); Downregulated (`log2_fc <= -fc_threshold` and `p_value <= p_threshold`) in `#2563EB` (blue); Non-significant in `#94A3B8` (grey).
    - Include dashed threshold lines and Gene ID hover tooltips. Return `fig.to_json()`. Output type: `VISUAL_PLOT`.
