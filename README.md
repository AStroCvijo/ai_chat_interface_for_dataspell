
# AI Chat Interface for DataSpell (Data Analysis IDE)

Project made for the purpose of applying to JetBrains internship.  

A Python framework that integrates predefined data transformation commands with an AI chat interface. Users can manipulate Pandas DataFrames through simple commands, while an AI model generates sequences of these transformations. The project also features Matplotlib visualizations for graphical representation of the data.

Date of creation: December, 2024

## Quickstart
1. Clone the repository:
    ```bash
    git clone https://github.com/AStroCvijo/ai_chat_interface_for_dataspell.git
    ```

2. Navigate to the project directory:
    ```bash
    cd ai_chat_interface_for_dataspell 
    ```

3. Set up the environment:
    ```bash
    source ./setup.sh
    ```

4. Run using the default settings:
    ```bash
    python main.py
    ```

## Arguments Guide

### Model Arguments
`-m or --model`  
Specify the model to use. Default: `gpt-3.5-turbo`.  
Options: any supported model name (e.g., GPT-based models).

### Finetuning Arguments
`-t or --temperature`  
Controls the randomness of the model's output. Default: `0.0`.  
Range: `0.0` (deterministic) to `1.0` (random).

`-tp or --top_p`  
Controls diversity by narrowing the possible output tokens based on cumulative probability. Default: `0.8`.  
Range: `0.0` (low diversity) to `1.0` (high diversity).

`-fp or --frequency_penalty`  
Penalizes tokens that have already been used frequently, encouraging the model to avoid repeating words. Default: `0.0`.  
Range: `0.0` (no penalty) to `2.0` (high penalty).

`-pp or --presence_penalty`  
Penalizes the model for using words that have already appeared in the conversation, encouraging the model to introduce new concepts. Default: `0.0`.  
Range: `0.0` (no penalty) to `2.0` (high penalty).

### Other Arguments
`-v or --verbose`  
Enable verbose mode for debugging. Default: `False`.  
Type: `True` or `False`.

`-sp or --data_path`  
Path to the data file. Default: `data/data.csv`.  
Type: `str` (path to your dataset).

 ### Example Usage: 
```
python main.py -m gpt-3.5-turbo -v true -t 0.0
```

## Available Commands
Here are the available commands that the AI chat interface supports so far for manipulating and visualizing Pandas DataFrames:

1. **filter_by_predicate**:  
   Takes a column name and a Python lambda predicate as parameters.  
   Example: `filter_by_predicate('column_name', lambda x: x > 10)`

2. **select_columns**:  
   Takes a list of column names as parameters to select specific columns from the DataFrame.  
   Example: `select_columns(['column1', 'column2'])`

3. **sort_by_column**:  
   Sorts the DataFrame by a column in either ascending or descending order.  
   Example: `sort_by_column('column_name', ascending=True)`

4. **drop_missing_values**:  
   Drops rows with missing values from the DataFrame.  
   Example: `drop_missing_values()`

5. **rename_columns**:  
   Renames columns using a dictionary to map old column names to new ones.  
   Example: `rename_columns({'old_name': 'new_name'})`

6. **plot_histogram**:  
   Plots a histogram for a specified column to visualize its distribution.  
   Example: `plot_histogram('column_name')`

7. **plot_bar_chart**:  
   Plots a bar chart for specified x and y columns.  
   Example: `plot_bar_chart('column1', 'column2')`

8. **plot_line_chart**:  
   Plots a line chart for specified x and y columns.  
   Example: `plot_line_chart('column1', 'column2')`
