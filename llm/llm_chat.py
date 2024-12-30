import os
import getpass
import json
from langchain_openai import ChatOpenAI

# LLMChat class that uses LangChain's OpenAI API and structured_output to generate commands
class LLMChat:

    # Constructor method
    def __init__(self, model, schema_path, args):

        # Get the OpenAI API
        if not os.environ.get("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

        # Initialize the LLM
        self.llm = ChatOpenAI(model=model, 
                            temperature=args.temperature, 
                            top_p=args.top_p, 
                            frequency_penalty=args.frequency_penalty, 
                            presence_penalty=args.presence_penalty)

        # Load the JSON schema from file
        with open(schema_path, "r") as file:
            self.json_schema = json.load(file)

        # Ensure structured response
        self.llm = self.llm.with_structured_output(self.json_schema)

    # Method for generating commands
    def generate_commands(self, user_input: str) -> list:

        # Prompt with context
        prompt = f"""
        You are a data scientist assistant. Your task is to generate a sequence of transformations
        for a pandas dataframe or commands for matplotlib based on user input.

        Available commands:
        1. filter_by_predicate: Takes a column name and a Python lambda predicate as a parameter.
        2. select_columns: Takes a list of column names as a parameter.
        3. sort_by_column: Sorts the DataFrame by a column (ascending or descending).
        4. group_by_column: Groups the DataFrame by a column and aggregates with provided functions.
        5. drop_missing_values: Drops rows with missing values.
        6. rename_columns: Renames columns using a dictionary.
        7. plot_histogram: Plots a histogram for a specified column.
        8. plot_bar_chart: Plots a bar chart for specified x and y columns.
        9. plot_line_chart: Plots a line chart for specified x and y columns.

        User input: "{user_input}"
        Generate the sequence in JSON format.
        """

        # Get the response
        response = self.llm.invoke(prompt)

        return response["commands"]
