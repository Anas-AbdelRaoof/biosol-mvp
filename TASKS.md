# Development Workflow
* _**Notice: read the source/info of each part that refers to its specific details in `PLAN.md`, don't create data or things not here or in `PLAN.md`.**_
## 1. Architecture (files and folders names, no code) and requirements.txt
**Create the architecture of the app, the folders names (and files if needed), `requirements.txt` containing the Python deps of every needed library and frameworks. Don't write any code in this step, only the architecture design.**
## 2. Data Analysis Engine
**The part for data analysis parts and blocks.**
### 2.1. File overview - get the [info](PLAN.md#file-overview) about File overview group
* #### 2.1.1. File info - get the [info](PLAN.md#file-info) about `File info` block
* #### 2.1.2 File ND - get [info](PLAN.md#file-nd) about `File ND` block
### 2.2. Cleaning and preparation - get [info](PLAN.md#cleaning-and-preparation) about this group
* #### 2.2.1. Clean column [X] by replacing NaN with [Y] - get [info](PLAN.md#clean-column-x-by-replacing-nan-with-y) about `Cleaning column [X] by replacing NaN with [Y]` block
* #### 2.2.2. Transform column [X] - get [info](PLAN.md#transform-cloumn-x) about `Transform column [X]` block
* #### 2.2.3. Filter genes by [X] and [Y] - get [info](PLAN.md#filter-genes-by-x-and-y) about `Filter genes by [X] and [Y]` block
### 2.3. Data visualization and comparing - get [info](PLAN.md#data-visualization-and-comparing) about this group
* #### 2.3.1. Box plot - get [info](PLAN.md#box-plot) about `Box plot` block
* #### 2.3.2. Correlation heatmap using [X] - get [info](PLAN.md#correlation-heatmap-using-x) about `Correlation heatmap using [x]` block
* #### 2.3.3. PCA plot grouped by [X] - get [info](PLAN.md#pca-plot-grouped-by-x) about `PCA plotg rouped by [X]` block
### 2.4. Data analysis - get [info](PLAN.md#data-analysis) about `Data analysis` group
* #### 2.4.1. Differential expression (DEG) between [X] and [Y] - get [info](PLAN.md#differential-expression-deg-between-x-and-y) about `Differential expression (DEG) between [X] and [Y]` block
* #### 2.4.2. Volcano plot using [X] and [Y] - get [info](PLAN.md#volcano-plot-using-x-and-y) about `Volcano plot using [X] and [Y]` block
**At the end create tests on these functions, you can use `pytest` or other libraries.**
## 3. Frontend: First Page - Uploading File
**The first page for uploading CSV file.**
* **Source: [First Page](PLAN.md#first-page-welcome-and-uploading-the-file)**
### 3.1. The title **Biosol** above in the page.
### 3.2. A red button called **Upload file** in the middle when clicking on it a list of file types appear, it's only CSV in this level, which the user can click/choose it, then the "My Computer" or the computer of the user appears to choose the file, upload only CSV and reject any other file type.
### 3.3. The file appears beneath the file with its type and size.
### 3.4. Another button appears called **Continue to workspace** which you can go the next page
**When the user uploads a file with this the file goes to the first part (Data Analysis Engine) to be ready for analyzing (like via `pd.read_csv()`...).**
## 4. Frontend: Second Page - Workspace
**The actual workspace for analysis.**
* **Source: [Second Page](PLAN.md#second-page-workspace)**
### 4.1. Right Sidebar - get [info](PLAN.md#-right-sidebar-containing-the-groups-that-contain-the-blocks-for-analyzing-the-genetic-data) about `Right Sidebar` part
**Containing the groups (File overview, Cleaning and preparation, Data visualization and comparing, and Data analysis) like Scratch, each group when containing its blocks (like File info and File ND for File overview), when clicking it the blocks appear beneath it like Scratch.**
### 4.2. Canvas - get [info](PLAN.md#-canvas-in-the-middle-a-white-space-which-you-can-drag-and-drop-blocks-into-it-and-connect-them) about `Canvas` part
**In the middle (but above) there is a white space which the user can drag-and-drop blocks into it (you can use `React Flow` and choose the suitable tool for drag-and-drop and connecting blocks/nodes).**
* **Notice: we can not connect blocks randomly, the path must be `Upload -> Clean -> Filter -> Transform`, here is the [specific path](PLAN.md#block-connection-rules-the-path-logic)**
### 4.3. Left Sidebar: Result Window- get [info](PLAN.md#-down-the-result-appears-here) `Result Window` part
**The result appears, like the graphs or numerical result, with run button.**