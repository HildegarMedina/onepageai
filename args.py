import argparse

def parser_arguments():
    parser = argparse.ArgumentParser(description='Create a Simple One Page')
    parser.add_argument('-n', '--name', type=str, help='Company name.', required=True)
    parser.add_argument('-t', '--technologies', default='HTML5,CSS3,Javascript,Bootstrap 5', type=str,
                        help='Technologies used in the project. \nDefault: "HTML5,CSS3,Javascript,Bootstrap 5"')
    parser.add_argument('-c', '--colors', type=str, help='Colors used in the project. \nExample: "#1abc9c,#ecf0f1,#2ecc71"')
    parser.add_argument('-l', '--location', type=str, help='Company location.')
    parser.add_argument('-d', '--description', type=str, help='Company description. \nExample: Real estate sales and rentals.')
    parser.add_argument('-s', '--sections', type=str, default='Banner,Services,About', help='Sections to include in the one page. \nExample: "About,Services,Contact"')
    parser.add_argument('-lg', '--language', default='English', type=str, help='Language of the prompt. \nDefault: "English"')
    parser.add_argument('-m', '--model', default='gpt-3.5-turbo', type=str, help='Model to use. \nDefault: "gpt-3.5-turbo"')
    parser.add_argument('-p', '--path', default='onepage.html', type=str, help='Path to save the one page. \nDefault: "onepage.html"')
    return parser.parse_args()
