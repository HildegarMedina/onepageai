import argparse

def parser_arguments():
    parser = argparse.ArgumentParser(description='Create a Simple One Page')
    parser.add_argument('-n', '--name', type=str, help='Company name.', required=True)
    parser.add_argument('-pc', '--primary_color', type=str, help='Primary color used in the project. \nDefault: "#1abc9c"', default='#1abc9c')
    parser.add_argument('-sc', '--secondary_color', type=str, help='Secondary color used in the project. \nDefault: "#ecf0f1"', default='#ecf0f1')
    parser.add_argument('-bc', '--background_color', type=str, help='Background color used in the project. \nDefault: "#2ecc71"', default='#2ecc71')
    parser.add_argument('-l', '--location', type=str, help='Company location.')
    parser.add_argument('-d', '--description', type=str, help='Company description. \nExample: Real estate sales and rentals.')
    parser.add_argument('-s', '--sections', type=str, default='Banner,Services,About', help='Sections to include in the one page. \nExample: "About,Services,Contact"')
    parser.add_argument('-lg', '--language', default='English', type=str, help='Language of the prompt. \nDefault: "English"')
    parser.add_argument('-m', '--model', default='gpt-4o-mini', type=str, help='Model to use. \nDefault: "gpt-4o-mini"')
    parser.add_argument('-p', '--path', default='onepage.html', type=str, help='Path to save the one page. \nDefault: "onepage.html"')
    return parser.parse_args()
