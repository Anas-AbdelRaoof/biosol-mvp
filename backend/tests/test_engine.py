import pandas as pd
import pytest
from app.engine.overview import get_file_info, get_file_nd

def test_get_file_info():
    data = {
        'GeneID': ['G1', 'G2', 'G3'],
        'Sample1': [10, 20, 30],
        'Sample2': [15, 25, 35]
    }
    df = pd.DataFrame(data)
    info = get_file_info(df)
    assert "GeneID" in info
    assert "Sample1" in info
    assert "3 entries" in info

def test_get_file_nd():
    data = {
        'GeneID': ['G1', 'G2', 'G3'],
        'Sample1': [10.0, 20.0, 30.0],
        'Sample2': [15.0, 25.0, 35.0]
    }
    df = pd.DataFrame(data)
    nd = get_file_nd(df)
    
    # Verify biologist-friendly names are present
    assert "Average" in nd
    assert "Median" in nd
    assert "Total Count" in nd
    assert "Maximum" in nd
    
    # Verify sample columns are present
    assert "Sample1" in nd
    assert "Sample2" in nd
    
    # GeneID should be the index, so it shouldn't be in the describe output columns
    # Note: in string representation, index name might appear, but as a column to describe? no.
    # Actually, describe() on a DF with string index and numerical columns will only describe numerical ones.

def test_get_file_nd_empty():
    df = pd.DataFrame()
    nd = get_file_nd(df)
    assert "empty" in nd.lower()
