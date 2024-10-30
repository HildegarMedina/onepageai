from args import parser_arguments
from services.onepagebuilder import OnePageBuilder
from services.configuration import Configuration
from rich.console import Console

def main():
    console = Console()
    args = parser_arguments()
    configuration = Configuration(console)
    onepagebuilder = OnePageBuilder('openai')

    configuration.verify_api_key_openai()
    onepagebuilder.build(args)

if __name__ == "__main__":
    main()
