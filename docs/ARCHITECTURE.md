# Biosol Architecture Design

## Project Structure Overview

```text
biosol-mvp/
├── backend/                # Data Analysis Engine (Python/FastAPI or Flask)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # API entry point
│   │   ├── engine/         # Analysis logic
│   │   │   ├── __init__.py
│   │   │   ├── overview.py  # File info, File ND
│   │   │   ├── cleaning.py  # Clean, Transform, Filter
│   │   │   ├── viz.py       # Box plot, Heatmap, PCA
│   │   │   └── analysis.py  # DEG, Volcano plot
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── helpers.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── schema.py    # Request/Response models
│   └── tests/              # Pytest suite
│       ├── __init__.py
│       ├── test_engine.py
│       └── test_api.py
├── frontend/               # React-based UI
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/      # Red buttons, layout
│   │   │   ├── landing/     # First page components
│   │   │   ├── workspace/   # Second page components
│   │   │   │   ├── Canvas.js
│   │   │   │   ├── SidebarRight.js
│   │   │   │   └── SidebarLeft.js
│   │   │   └── nodes/       # React Flow custom nodes (Yellow, Lime, Orange, Blue)
│   │   ├── hooks/
│   │   ├── services/       # API integration
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   └── package.json
├── data/                   # Sample CSVs for testing
├── docs/                   # Documentation
├── requirements.txt        # Python dependencies
└── README.md
```

## Module Descriptions

### Backend (Data Analysis Engine)
- **`engine/overview.py`**: Implements `df.info()` and `df.describe()` with biologist-friendly formatting.
- **`engine/cleaning.py`**: Handles NaN replacement, `np.log2` transformations, and gene filtering logic.
- **`engine/viz.py`**: Generates Plotly JSON/HTML for interactive charts (Box, Heatmap, PCA).
- **`engine/analysis.py`**: Performs T-tests using `scipy` and prepares data for Volcano plots.

### Frontend
- **React Flow**: Used for the drag-and-drop canvas and connection logic.
- **Tailwind CSS**: For styling (White and Red theme).
- **Plotly.js**: For rendering interactive visualizations in the results sidebar.

## Data Flow & Connection Rules
- **Input/Output Ports**: Implemented via custom node types in React Flow.
- **Validation**: Frontend logic to enforce `Upload -> Clean -> Filter -> Transform` and strict 🟪 DEG Table input for Volcano plots.
