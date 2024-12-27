import pandas as pd
from typing import Callable, List, Dict
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------------
# Set of pre-defined DataFrame transformations
# ----------------------------------------------------------------------------------

def filter_by_predicate(df: pd.DataFrame, column_name: str, predicate: Callable) -> pd.DataFrame:
    """Filter rows in the DataFrame based on a column and a predicate"""
    return df[df[column_name].apply(predicate)]

def select_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Select specific columns from the DataFrame"""
    return df[columns]

def sort_by_column(df: pd.DataFrame, column_name: str, ascending: bool = True) -> pd.DataFrame:
    """Sort the DataFrame by a column"""
    return df.sort_values(by=column_name, ascending=ascending)

def group_by_column(df: pd.DataFrame, group_column: str, aggregations: Dict[str, str]) -> pd.DataFrame:
    """
    Group by a column and apply aggregation.
    Aggregations should be a dictionary where keys are column names
    and values are aggregation functions like 'sum', 'mean', etc
    """
    return df.groupby(group_column).agg(aggregations).reset_index()

def drop_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with missing values"""
    return df.dropna()

def rename_columns(df: pd.DataFrame, column_mapping: Dict[str, str]) -> pd.DataFrame:
    """Rename columns using a mapping dictionary."""
    return df.rename(columns=column_mapping)

# ---------------------------------------------------------------------------------
# Set of pre-defined matplotlib visualizations
# ----------------------------------------------------------------------------------

def plot_histogram(df: pd.DataFrame, column_name: str, bins: int = 10) -> None:
    """Plot a histogram for a specified column."""
    plt.hist(df[column_name], bins=bins)
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()

def plot_bar_chart(df: pd.DataFrame, x_column: str, y_column: str) -> None:
    """Plot a bar chart for specified x and y columns."""
    df.plot.bar(x=x_column, y=y_column)
    plt.title(f'Bar Chart of {y_column} by {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

def plot_line_chart(df: pd.DataFrame, x_column: str, y_column: str) -> None:
    """Plot a line chart for specified x and y columns."""
    df.plot.line(x=x_column, y=y_column)
    plt.title(f'Line Chart of {y_column} over {x_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
