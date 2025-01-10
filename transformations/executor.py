import pandas as pd

# Import all commands
from .commands import *

# Function that parses and executes all commands
def apply_transformations(df: pd.DataFrame, transformations: list) -> pd.DataFrame:
    try:
        for transformation in transformations:
            command = transformation["command"]
            parameters = transformation["parameters"]

            # Data commands
            if command == 'filter_by_predicate':
                column_name = parameters["column_name"]
                predicate_str = parameters["predicate"]
                predicate = eval(predicate_str)
                df = filter_by_predicate(df, column_name, predicate)
            elif command == 'select_columns':
                columns = parameters["columns"]
                df = select_columns(df, columns)
            elif command == 'sort_by_column':
                column_name = parameters["column_name"]
                ascending = parameters.get("ascending", True)
                df = sort_by_column(df, column_name, ascending)
            elif command == 'drop_missing_values':
                df = drop_missing_values(df)
            elif command == 'rename_columns':
                old_name = parameters["column_name"]
                new_name = parameters["new_column_name"]
                column_mapping = {old_name: new_name}
                df = rename_columns(df, column_mapping)

            # Visualization commands
            elif command == 'plot_histogram':
                column_name = parameters["column_name"]
                bins = parameters.get("bins", 10)
                plot_histogram(df, column_name, bins)
            elif command == 'plot_bar_chart':
                x_column = parameters["x_column"]
                y_column = parameters["y_column"]
                plot_bar_chart(df, x_column, y_column)
            elif command == 'plot_line_chart':
                x_column = parameters["x_column"]
                y_column = parameters["y_column"]
                plot_line_chart(df, x_column, y_column)

            else:
                raise ValueError(f"Unknown command: {command}")

    except KeyError as e:
        print(f"Missing key in parameters: {e}")
    except ValueError as e:
        print(f"Value error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return df

