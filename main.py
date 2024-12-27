import pandas as pd
from transformations.executor import apply_transformations
import json
from utils.argparser import arg_parse
from llm.llm_chat import LLMChat
from transformations.executor import apply_transformations

def main():
    # Parse the arguments
    args = arg_parse()

    # Load the Sample DataFrame
    df = pd.read_csv(args.data_path)

    # Initialize LLMChat
    cmd_schema_path = "schema/cmd_schema.json"
    llm_chat = LLMChat(model=args.model, schema_path=cmd_schema_path, args=args)

    # Stack to keep track of DataFrame states for rollback functionality
    df_history = []
    
    print("Original DataFrame:")
    print(df)

    while True:
        # Get user input
        user_input = input("\nEnter your commands (or type 'exit' to quit, 'rollback' to revert last change):\n")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if user_input.lower() == 'rollback':
            if df_history:
                # Pop the last state from history and revert to it
                df = df_history.pop()
                print("\nRolled back to previous DataFrame:")
                print(df)
            else:
                print("No previous state to roll back to.")
            continue

        try:
            # Store current DataFrame state before applying transformations
            df_history.append(df.copy())

            commands = llm_chat.generate_commands(user_input)

            if args.verbose:
                print("\nGenerated Commands:")
                print(json.dumps(commands, indent=4))

            # Apply transformations
            df = apply_transformations(df, commands)

            print("\nTransformed DataFrame:")
            print(df)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
