from dotenv import load_dotenv, set_key, get_key
import sys
from config.colors import WARNING, SUCCESS

class Configuration:
    def __init__(self, console):
        self.console = console
        load_dotenv()

    def verify_api_key_openai(self):
        if not get_key('.env', 'OPENAI_API_KEY'):
            self.console.print(f"\n[italic {WARNING}]Please set the OPENAI_API_KEY environment variable[/italic {WARNING}]\n")
            api_key = ""
            while not api_key:
                api_key = input('Enter your OpenAI API key: ')
            set_key('.env', 'OPENAI_API_KEY', api_key)
            self.console.print(f'\n[{SUCCESS}]API key set successfully[/{SUCCESS}]\n')
            sys.exit(1)
