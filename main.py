import os
import sys
import pandas as pd
import json
import readline
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.spinner import Spinner
from transformations.executor import apply_transformations
from utils.argparser import arg_parse
from llm.llm_chat import LLMChat

# Instantiate console for rich text display
console = Console()

def print_banner():
    """Displays a nice banner for the assistant."""
    console.print(
        Panel(
            "[bold cyan]Welcome to the AI-Powered Data Transformer![/bold cyan]", 
            border_style="cyan"
        )
    )

def clear_screen():
    """Clears the screen in a cross-platform way."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()

def main():
    # Parse the arguments
    args = arg_parse()
    
    # Load the Sample DataFrame
    df = pd.read_csv(args.data_path)
    df_history = []  # Stack for rollback functionality

    # Initialize LLMChat
    cmd_schema_path = "schema/cmd_schema.json"
    llm_chat = LLMChat(model=args.model, schema_path=cmd_schema_path, args=args)

    clear_screen()
    console.print("[bold green]Original DataFrame:[/bold green]")
    console.print(df)

    while True:
        try:
            user_input = Prompt.ask("[bold blue]Enter command[/bold blue]")
            
            if user_input.lower() in {"exit", "quit"}:
                console.print("\n[bold red]Goodbye![/bold red] 👋")
                break
            elif user_input.lower() == "clear":
                clear_screen()
                continue
            elif user_input.lower() == "help":
                console.print("\n[bold cyan]Available Commands:[/bold cyan]")
                console.print("  [bold yellow]exit[/bold yellow]  - Quit the assistant")
                console.print("  [bold yellow]clear[/bold yellow] - Clear the terminal screen")
                console.print("  [bold yellow]rollback[/bold yellow] - Revert to the last DataFrame state")
                console.print("  [bold yellow]help[/bold yellow]  - Show available commands\n")
                continue
            elif user_input.lower() == "rollback":
                if df_history:
                    df = df_history.pop()
                    console.print("\n[bold yellow]Rolled back to previous DataFrame:[/bold yellow]")
                    console.print(df)
                else:
                    console.print("[bold red]No previous state to roll back to.[/bold red]")
                continue

            # Store current DataFrame state before applying transformations
            df_history.append(df.copy())

            # Generate transformation commands
            with console.status("[bold green]Generating commands...[/bold green]", spinner="dots"):
                commands = llm_chat.generate_commands(user_input, df.columns.tolist())

            if args.verbose:
                console.print("\n[bold cyan]Generated Commands:[/bold cyan]")
                console.print(json.dumps(commands, indent=4))

            if commands[0]["command"] == "unknown":
                console.print("\n[bold cyan]⚠ Generated Commands:[/bold cyan] (Unknown Command Detected)")
                continue

            # Apply transformations
            with console.status("[bold green]Applying transformations...[/bold green]", spinner="dots"):
                df = apply_transformations(df, commands)

            console.print("\n[bold green]Transformed DataFrame:[/bold green]")
            console.print(df)

        except KeyboardInterrupt:
            console.print("\n\n[bold red]Exiting...[/bold red]")
            sys.exit(0)
        except EOFError:
            console.print("\n\n[bold red]Goodbye![/bold red] 👋")
            sys.exit(0)
        except Exception as e:
            console.print(f"[bold red]An error occurred:[/bold red] {e}")

if __name__ == "__main__":
    main()
