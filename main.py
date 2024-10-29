from args import parser_arguments
from services.onepagebuilder import OnePageBuilder
from services.configuration import Configuration

def main():
    args = parser_arguments()
    configuration = Configuration()
    onepagebuilder = OnePageBuilder('openai')
    
    configuration.verify_api_key_openai()
    onepagebuilder.build(args)

if __name__ == "__main__":
    main()
