# MVP Plan
_**Biosol is a drag-and-drop tool for biologists to analyze their genetic data in hours instead of weeks, instead of calling statisticians or learning programming themselves.**_
## UI/UX
**When you open the app you will find these**
### First page: welcome and uploading the file
* The name Biosol, small description, and file type and limits.
* Choices to choose the genetic data file type (CSV, FASTQ, etc. CSV in this level).
* A greenish red button appears to upload the file(s), and the file details will appear beneath it, when clicking the button a list of files types appear, but only CSV is available, which the user can choose it.
* A tiny text showing that the software is MVP/beta version.
* Colours are white and simple red.
### Second page: workspace
#### * **Right Sidebar**: containing the groups that contain the blocks for analyzing the genetic data
![alt text](image-2.png)
#### * **Canvas**: in the middle, a white space which you can drag-and-drop blocks into it, and connect them.
#### * **Left Sidebar**: Biosol AI (using `openai/gpt-oss-20b`), your assistant helping you understand the data, specialized on genetics and biology using `SYSTEM_PROMPT.md`, a clear and very specific system prompt for its function and limits.
#### * **Down**: the result appears here.
## Features
**The features of the software in MVP/beta version**
### CSV analyzing: blocks
**Blocks are distributed over groups as said, containing related blocks**
#### File overview
**The blocks in this group are coloured yellow.**
##### **File info**
* **An explanation of the file structure (like data types and number of rows and columns), it uses `df.info()`.**
##### **File ND**
* **For file numerical description (like mean), it uses `df.describe()` after making the ID (the first column) the index to avoid calculating it, it should not show numerical mathematical values for biologists, the code should handle it to show percent easy understandable values for biologists.**
#### Cleaning and preparation
**The blocks in this group are coloured lime**
##### **Clean column [X] by replacing NaN with [Y]**
* **Which X is list of columns (all, and numerical columns only) which the biologist can choose from it what to clean, and Y is the type of cleaning (replacing with 0, mean, or other cleaning types).**
##### **Transform cloumn [X]**
* **Getting log2 for making the numbers better for analyses, it uses `np.log2(df + 1)`, X is also the columns list.**
##### **Filter genes by [X] and [Y]** 
* **Which X is the minimum expression value (counts) a gene needs to have, and Y is the minimum number of samples that must have this value. It uses `df = df[(df >= X).sum(axis=1) >= Y]` to remove genes that are basically noise or not expressed at all, making the data smaller and faster to analyze.**
#### Data visualization and comparing
**The blocks in this group are coloured orange green**
##### **Box plot**
* **Creating a boxplot for each column to compare/show each other.**
##### **Correlation heatmap using [X]**
* **Which X is the correlation method (Pearson, Spearman, etc.) which the biologist can choose from. It uses `df.corr(method=X)` to calculate how similar the samples are to each other, and generates a colored interactive heatmap (using Plotly, every visualization block will use Plotly) image. It helps the biologist see if their replicates (like Control_1, Control_2, Control_3) group together correctly, and if any sample is an outlier that ruins the experiment.**
##### **PCA plot grouped by [X]**
* **Which X is the list of sample groups or conditions (like Control vs Treatment) that the biologist can assign to color the dots. It uses `sklearn.decomposition.PCA` to compress the thousands of genes into two dimensions and plots the samples as dots. It helps the biologist see if their samples cluster together correctly based on their biological condition, making it easy to spot if the experiment worked or if there are any weird outlier samples.**
#### Data analysis
**The blocks in this group are coloured blue**
##### **Differential expression (DEG) between [X] and [Y]**
* **Which X is the list of columns for the Control group and Y is the list of columns for the Treatment group. The code uses `scipy.stats.ttest_ind` and fold-change calculations to compare the two groups, and it should show a simple table for biologists containing the top significantly upregulated and downregulated genes (including Gene ID, Fold Change, and P-value).**
##### **Volcano plot using [X] and [Y]**
* **Which X is the p-value threshold (e.g., 0.05) and Y is the fold-change threshold (e.g., 1.0), which the biologist can adjust using sliders. It also uses Plotly to generate an interactive scatter plot where the x-axis is the Log2 Fold Change and the y-axis is the -Log10 P-value. It helps the biologist instantly visualize which genes are significantly upregulated (red dots) or downregulated (blue dots), making it easy to spot the most biologically important changes.**
### Block Connection Rules (The "Path" Logic)
To ensure biological accuracy and prevent errors, blocks are not randomly connectable. The canvas uses strict rules based on "Input Ports" and "Output Ports" and the **Data Type** flowing between them (similar to how Scratch uses shapes).

**1. The Starting Point (Upload Node)**
- Everything starts with the uploaded **CSV File** (the starting node). 
- You can connect the CSV File to multiple blocks at once (e.g., to see File Info AND to start Cleaning).

**2. Data Flow Types**
- 🟦 **Raw/Processed Data:** A data table (Pandas DataFrame).
- 🟨 **Text/Report:** Just text or a statistical table (no data for further analysis).
- 🟪 **DEG Table:** A specific table of significantly changed genes.
- 🟢 **Visual/Plot:** An interactive Plotly image (end of the line).

---

**Rules by Block Category:**

**Group 1: File Overview (The "Reporters")**
- **File info:** Takes 🟦 Raw Data -> Outputs 🟨 Text. 
  - *Rule:* It cannot be connected to any other block. It is a "dead end" (terminal) block.
- **File ND:** Takes 🟦 Raw Data -> Outputs 🟨 Text.
  - *Rule:* It cannot be connected to any other block. It is a terminal block.

**Group 2: Cleaning and Preparation (The "Processors")**
- **Clean column:** Takes 🟦 Raw Data -> Outputs 🟦 Processed Data.
- **Filter genes:** Takes 🟦 Raw Data OR 🟦 Processed Data -> Outputs 🟦 Processed Data.
- **Transform column (Log2):** Takes 🟦 Processed Data -> Outputs 🟦 Processed Data.
  - *Rule:* These three blocks are the only ones that can be chained together sequentially. 
  - *Logic Path:* `Upload -> Clean -> Filter -> Transform`. (You cannot connect Log2 *before* Clean, as you should clean raw data first. You cannot connect these to the Overview blocks).

**Group 3: Data Visualization (The "Viewers")**
- **Box plot:** Takes 🟦 Processed Data -> Outputs 🟢 Visual.
- **Correlation heatmap:** Takes 🟦 Processed Data -> Outputs 🟢 Visual.
- **PCA plot:** Takes 🟦 Processed Data + [User Group Assignment] -> Outputs 🟢 Visual.
  - *Rule:* These blocks are "dead ends". You cannot connect a Box Plot to a DEG block. They are for visual inspection only.

**Group 4: Data Analyses (The "Heavy Lifters")**
- **Differential expression (DEG):** Takes 🟦 Processed Data (highly recommended to be Log2 transformed) + [User Group Assignment] -> Outputs 🟪 DEG Table.
  - *Rule:* This block strictly requires processed, normalized data to work mathematically. 

**Group 5: Analysis Visualization**
- **Volcano plot:** Takes 🟪 DEG Table -> Outputs 🟢 Visual.
  - *Rule:* **Strict Connection:** The Volcano Plot *only* accepts the 🟪 DEG Table output. It cannot connect directly to the Uploaded CSV or the Processed Data. If the user tries to connect it to a cleaned CSV, the UI should reject the connection (or show a red error state: "Volcano Plot requires Differential Expression data").