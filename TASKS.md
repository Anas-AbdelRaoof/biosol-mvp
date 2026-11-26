# Development Workflow
## 1. Architecture (files and folders names, no code) and requirements.txt
**Create the architecture of the app, the folders names (and files if needed), requirements.txt containing the latest version of every needed library and frameworks. Don't write any code in this step, only the architecture design.**
## 2. Data Analysis Engine
**The part for data analysis parts and blocks.**
### 2.1. File overview
* #### 2.1.1. File info
* #### 2.1.2 File ND
### 2.2. Cleaning and preparation
* #### 2.2.1. Clean  column [X] by replacing NaN with [Y]
* #### 2.2.2. Transform column [X]
* #### 2.2.3. Filter genes by [X] and [Y]
### 2.3. Data visualization and comparing
* #### 2.3.1. Box plot
* #### 2.3.2. Correlation heatmap using [X]
* #### 2.3.3. PCA plot grouped by [X]
### 2.4. Data analysis
* #### 2.4.1. Differential expression (DEG) between [X] and [Y]
* #### 2.4.2. Volcano plot using [X] and [Y]
**At the end create tests on these functions, you can use `pytest` or other libraries.**
## 3. AI Assistant Backend and `SYSTEM_PROMPT.md`
**Use my Groq API key from `.env` with `openai/gpt-oss-20b` as a chatbot, here are the details:**
### 3.1. Use my API key from `.env` with `Groq` and `dotenv` to make a chatbot (make it endless, I can give it questions and get answers like ChatGPT), also install these two libraries if not.
### 3.2. Inject `SYSTEM_PROMPT.md` to the model to answer based on its rules.
**At the end create tests on the bot, you can use `pytest` or other libraries.**
## 4. Frontend: First Page - Uploading File
**The first page for uploading CSV file.**
### 4.1. The title **Biosol** above in the page.
### 4.2. A greenish red button called **Upload file** in the middle when clicking on it a list of file types appear, it's only CSV in this level, which the user can click/choose it, then the "My Computer" or the computer of the user appears to choose the file, upload only CSV and reject any other file type.
### 4.3. The file appears beneath the file with its type and size.
### 4.4. Another button appears called **Continue to workspace** which you can go the next page
**When the user uploads a file with this the file goes to the first part (Data Analysis Engine) to be ready for analyzing (like via `pd.read_csv()`...).**
## 5. Frontend: Secong Page - Workspace
### 5.1. Right Sidebar
**Containing the four groups (File overview, Cleaning and preparation, Data visualization and comparing, and Data analysis) like Scratch, each group when containing its blocks (like File info and File ND for File overview), when clicking it the blocks appear beneath it like Scratch.**
### 5.2. Canvas
**In the middle (but above) there is a white space which the user can drag-and-drop blocks into it (you can use `React Flow` and choose the suitable tool for drag-and-drop and connecting blocks/nodes).**
### 5.3. Left Sidebar
**The Biosol AI chat window, which the user can chat it like ChatGPT (it's the GPT OSS past part).**
### 5.4. Result Window
**Down but in the middle the result appears, like the graphs or numerical result.**
**Notice: we can not connect blocks randomly, the path must be `Upload -> Clean -> Filter -> Transform`, here is the [specific path](PLAN.md#block-connection-rules-the-path-logic)**