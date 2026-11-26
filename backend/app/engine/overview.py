import pandas as pd
import io

def get_file_info(df: pd.DataFrame) -> str:
    """
    Provides an explanation of the file structure (data types, number of rows and columns).
    Uses df.info() captured in a string.
    """
    buffer = io.StringIO()
    # verbose=True to show all columns, buf=buffer to capture output
    df.info(buf=buffer)
    return buffer.getvalue()

def get_file_nd(df: pd.DataFrame) -> str:
    """
    Provides a numerical description of the file (like mean, median, etc.).
    Sets the first column (ID) as the index to exclude it from calculations.
    Renames mathematical terms to be more understandable for biologists.
    """
    if df.empty:
        return "The provided file is empty."

    # Copy the dataframe and set the first column as index (usually ID/Gene names)
    # as per the plan: "after making the ID (the first column) the index to avoid calculating it"
    df_temp = df.copy()
    first_col = df_temp.columns[0]
    df_temp = df_temp.set_index(first_col)
    
    # Get numerical description
    description = df_temp.describe()
    
    # Rename indices to biologist-friendly terms
    # "the code should handle it to show percent easy understandable values for biologists"
    # This refers to the percentiles and standard mathematical terms.
    rename_map = {
        "count": "Total Count",
        "mean": "Average",
        "std": "Variation (Std Dev)",
        "min": "Minimum",
        "25%": "25th Percentile (Lower)",
        "50%": "50th Percentile (Median)",
        "75%": "75th Percentile (Upper)",
        "max": "Maximum"
    }
    
    description = description.rename(index=rename_map)
    
    return description.to_string()
