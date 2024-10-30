from args import parser_arguments
from services.onepagebuilder import OnePageBuilder
from services.configuration import Configuration
from rich.console import Console
from rich.panel import Panel
from config.config import PANEL_DESCRIPTION, PANEL_TITLE, PANEL_SUBTITLE
import sys
from modules.chatgpt import ChatGPT

def main():
    console = Console()
    if len(sys.argv) == 1:
        console.print(Panel(PANEL_DESCRIPTION, title=PANEL_TITLE, subtitle=PANEL_SUBTITLE))
        sys.exit(1)

    args = parser_arguments()

    configuration = Configuration(console)
    configuration.verify_api_key_openai()

    chatgpt = ChatGPT(console, model=args.model)
    onepagebuilder = OnePageBuilder(console, chatgpt)

    onepagebuilder.build(args)

if __name__ == "__main__":
    main()
