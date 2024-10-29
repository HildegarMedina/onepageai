from dotenv import load_dotenv, set_key, get_key
import sys

class Configuration:
    def __init__(self):
        load_dotenv()

    def verify_api_key_openai(self):
        if not get_key('.env', 'OPENAI_API_KEY'):
            print('Please set the OPENAI_API_KEY environment variable\n')
            api_key = ""
            while not api_key:
                api_key = input('Enter your OpenAI API key: ')
            set_key('.env', 'OPENAI_API_KEY', api_key)
            print('\nAPI key set successfully')
            sys.exit(1)
