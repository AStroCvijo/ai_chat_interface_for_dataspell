import argparse

# Function for parsing arguments
def arg_parse():
    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Model arguments
    parser.add_argument('-m', '--model', type=str, default="gpt-3.5-turbo",
                        help="What model will be used (options: {})")

    # Finetuning arguments
    parser.add_argument('-t', '--temperature', type=float, default=0.0,
                        help="Controls the randomness of the model's output")
    parser.add_argument('-tp', '--top_p', type=float, default=0.8,
                        help="Controls diversity by narrowing the possible output tokens based on cumulative probability")
    parser.add_argument('-fp', '--frequency_penalty', type=float, default=0.0,
                        help="Penalizes tokens that have already been used frequently, encouraging the model to avoid repeating words")
    parser.add_argument('-pp', '--presence_penalty', type=float, default=0.0,
                        help="Penalizes the model for using words that have already appeared in the conversation, encouraging the model to introduce new concepts")

    # Other arguments
    parser.add_argument('-v', '--verbose', type=bool, default=False,
                        help="Whether to use verbose mode (useful for debugging)")
    parser.add_argument('-sp', '--data_path', type=str, default="data/data.csv",
                        help="Path to data")

    # Parse the arguments
    return parser.parse_args()