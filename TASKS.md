# Development Workflow
## 1. Architecture (files and folders names, no code) and requirements.txt
**Create the architecture of the app, the folders names (and files if needed), `requirements.txt` containing the Python deps of every needed library and frameworks. Don't write any code in this step, only the architecture design.**
## 2. Data Analysis Engine
**The part for data analysis parts and blocks.**
### 2.1. File overview - get the [info](PLAN.md#file-overview) about File overview group
* #### 2.1.1. File info - get the [info](PLAN.md#file-info-an-explanation-of-the-file-structure-like-data-types-and-number-of-rows-and-columns-it-uses-dfinfo) about `File info` block
* #### 2.1.2 File ND - get [info](PLAN.md#file-nd-for-file-numerical-description-like-mean-it-uses-dfdescribe-after-making-the-id-the-first-column-the-index-to-avoid-calculating-it-it-should-not-show-numerical-mathematical-values-for-biologists-the-code-should-handle-it-to-show-percent-easy-understandable-values-for-biologists) about `File ND` block
### 2.2. Cleaning and preparation - get [info](PLAN.md#cleaning-and-preparation) about this group
* #### 2.2.1. Clean column [X] by replacing NaN with [Y] - get [info](PLAN.md#clean-column-x-by-replacing-nan-with-y-which-x-is-list-of-columns-all-and-numerical-columns-only-which-the-biologist-can-choose-from-it-what-to-clean-and-y-is-the-type-of-cleaning-replacing-with-0-mean-or-other-cleaning-types) about `Cleaning column [X] by replacing NaN with [Y]` block
* #### 2.2.2. Transform column [X] - get [info](PLAN.md#transform-cloumn-x-getting-log2-for-making-the-numbers-better-for-analyses-it-uses-nplog2df--1-x-is-also-the-columns-list) about `Transform column [X]` block
* #### 2.2.3. Filter genes by [X] and [Y] - get [info](PLAN.md#filter-genes-by-x-and-y-which-x-is-the-minimum-expression-value-counts-a-gene-needs-to-have-and-y-is-the-minimum-number-of-samples-that-must-have-this-value-it-uses-df--dfdf--xsumaxis1--y-to-remove-genes-that-are-basically-noise-or-not-expressed-at-all-making-the-data-smaller-and-faster-to-analyze) about `Filter genes by [X] and [Y]` block
### 2.3. Data visualization and comparing - get [info](PLAN.md#data-visualization-and-comparing) about this group
* #### 2.3.1. Box plot - get [info](PLAN.md#box-plot-creating-a-boxplot-for-each-column-to-compareshow-each-other) about `Box plot` block
* #### 2.3.2. Correlation heatmap using [X] - get [info](PLAN.md#correlation-heatmap-using-x-which-x-is-the-correlation-method-pearson-spearman-etc-which-the-biologist-can-choose-from-it-uses-dfcorrmethodx-to-calculate-how-similar-the-samples-are-to-each-other-and-generates-a-colored-interactive-heatmap-using-plotly-every-visualization-block-will-use-plotly-image-it-helps-the-biologist-see-if-their-replicates-like-control_1-control_2-control_3-group-together-correctly-and-if-any-sample-is-an-outlier-that-ruins-the-experiment) about `Correlation heatmap using [x]` block
* #### 2.3.3. PCA plot grouped by [X] - get [info](PLAN.md#pca-plot-grouped-by-x-which-x-is-the-list-of-sample-groups-or-conditions-like-control-vs-treatment-that-the-biologist-can-assign-to-color-the-dots-it-uses-sklearndecompositionpca-to-compress-the-thousands-of-genes-into-two-dimensions-and-plots-the-samples-as-dots-it-helps-the-biologist-see-if-their-samples-cluster-together-correctly-based-on-their-biological-condition-making-it-easy-to-spot-if-the-experiment-worked-or-if-there-are-any-weird-outlier-samples) about `PCA plotg rouped by [X]` block
### 2.4. Data analysis - get [info](PLAN.md#data-analysis) about `Data analysis` group
* #### 2.4.1. Differential expression (DEG) between [X] and [Y] - get [info](PLAN.md#differential-expression-deg-between-x-and-y-which-x-is-the-list-of-columns-for-the-control-group-and-y-is-the-list-of-columns-for-the-treatment-group-the-code-uses-scipystatsttest_ind-and-fold-change-calculations-to-compare-the-two-groups-and-it-should-show-a-simple-table-for-biologists-containing-the-top-significantly-upregulated-and-downregulated-genes-including-gene-id-fold-change-and-p-value) about `Differential expression (DEG) between [X] and [Y]` block
* #### 2.4.2. Volcano plot using [X] and [Y] - get [info](PLAN.md#volcano-plot-using-x-and-y-which-x-is-the-p-value-threshold-eg-005-and-y-is-the-fold-change-threshold-eg-10-which-the-biologist-can-adjust-using-sliders-it-also-uses-plotly-to-generate-an-interactive-scatter-plot-where-the-x-axis-is-the-log2-fold-change-and-the-y-axis-is-the--log10-p-value-it-helps-the-biologist-instantly-visualize-which-genes-are-significantly-upregulated-red-dots-or-downregulated-blue-dots-making-it-easy-to-spot-the-most-biologically-important-changes) about `Volcano plot using [X] and [Y]` block
**At the end create tests on these functions, you can use `pytest` or other libraries.**
## 3. AI Assistant Backend and `SYSTEM_PROMPT.md` 
**Use my Groq API key from `.env` with `openai/gpt-oss-20b` as a chatbot, here are the details:**
* **Source: [Biosol AI](PLAN.md#-left-sidebar-biosol-ai-using-openaigpt-oss-20b-your-assistant-helping-you-understand-the-data-specialized-on-genetics-and-biology-using-system_promptmd-a-clear-and-very-specific-system-prompt-for-its-function-and-limits)**
### 3.1. Use my API key from `.env` with `Groq` and `dotenv` to make a chatbot (make it endless, I can give it questions and get answers like ChatGPT), also install these two libraries if not.
### 3.2. Inject `SYSTEM_PROMPT.md` to the model to answer based on its rules.
**At the end create tests on the bot, you can use `pytest` or other libraries.**
## 4. Frontend: First Page - Uploading File
**The first page for uploading CSV file.**
* **Source: [First Page](PLAN.md#first-page-welcome-and-uploading-the-file)**
### 4.1. The title **Biosol** above in the page.
### 4.2. A greenish red button called **Upload file** in the middle when clicking on it a list of file types appear, it's only CSV in this level, which the user can click/choose it, then the "My Computer" or the computer of the user appears to choose the file, upload only CSV and reject any other file type.
### 4.3. The file appears beneath the file with its type and size.
### 4.4. Another button appears called **Continue to workspace** which you can go the next page
**When the user uploads a file with this the file goes to the first part (Data Analysis Engine) to be ready for analyzing (like via `pd.read_csv()`...).**
## 5. Frontend: Second Page - Workspace
**The actual workspace for analysis.**
* **Source: [Second Page](PLAN.md#second-page-workspace)**
### 5.1. Right Sidebar - get [info](PLAN.md#-right-sidebar-about-10---15-blocks-for-analyzing-the-genetic-data-distributed-over-groups-like-motion-and-looks-in-scratch-here-but-for-genetic-analyses) about `Right Sidebar` part
**Containing the groups (File overview, Cleaning and preparation, Data visualization and comparing, and Data analysis) like Scratch, each group when containing its blocks (like File info and File ND for File overview), when clicking it the blocks appear beneath it like Scratch.**
### 5.2. Canvas - get [info](PLAN.md#-canvas-in-the-middle-a-white-space-which-you-can-drag-and-drop-blocks-into-it-and-connect-them) about `Canvas` part
**In the middle (but above) there is a white space which the user can drag-and-drop blocks into it (you can use `React Flow` and choose the suitable tool for drag-and-drop and connecting blocks/nodes).**
### 5.3. Left Sidebar - get [info](PLAN.md#-left-sidebar-biosol-ai-using-openaigpt-oss-20b-your-assistant-helping-you-understand-the-data-specialized-on-genetics-and-biology-using-system_promptmd-a-clear-and-very-specific-system-prompt-for-its-function-and-limits) about `Left Sidebar` part
**The Biosol AI chat window, which the user can chat it like ChatGPT (it's the GPT OSS past part).**
### 5.4. Result Window - get [info](PLAN.md#-down-the-result-appears-here)
**Down but in the middle the result appears, like the graphs or numerical result.**
**Notice: we can not connect blocks randomly, the path must be `Upload -> Clean -> Filter -> Transform`, here is the [specific path](PLAN.md#block-connection-rules-the-path-logic)**
* _**Notice: read the source/info of each part that refers to its specific details in `PLAN.md`, don't create data or things not here or in `PLAN.md`.**_