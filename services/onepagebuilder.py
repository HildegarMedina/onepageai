import sys
import re
from config.prompts import CREATE_ONE_PAGE
from config.config import COLOR_SUCCESS, COLOR_WARNING

class OnePageBuilder:
    def __init__(self, console, module_ai):
        self.console = console
        self.module_ai = module_ai

    def prepare_prompt(self, args):
        description = args.description if args.description else ''
        location = args.location if args.location else ''
        name = args.name if args.name else ''
        lang = args.language if args.language else 'English'

        prompt = CREATE_ONE_PAGE
        prompt = prompt.replace('{description}', description)
        if location:
            prompt = prompt.replace('{location}', f"ubicada en {location}.")
        prompt = prompt.replace('{location}', '')

        if args.primary_color:
            prompt = prompt.replace('{primary_color}', args.primary_color)
        if args.secondary_color:
            prompt = prompt.replace('{secondary_color}', args.secondary_color)
        if args.background_color:
            prompt = prompt.replace('{background_color}', args.background_color)

        prompt = prompt.replace('{company_name}', f"Mi empresa que se llama {name}")
        prompt = prompt.replace('{lang}', lang)
        prompt = prompt.replace('{sections}', args.sections.replace(',', ', '))

        return prompt

    def save_one_page(self, content, path='onepage.html'):
        with open(path, 'w') as file:
            file.write(content)
        self.console.print(f"\n[{COLOR_SUCCESS}]One page saved in {path}[/{COLOR_SUCCESS}]")

    def build(self, args):
        prompt = self.prepare_prompt(args)

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        html = self.module_ai.completion(messages, prompt)
        clean_html = re.sub(r'```html(.*?)```', r'\1', html, flags=re.DOTALL)
        self.save_one_page(clean_html, args.path)

        response = ''
        while response not in ['y', 'yes', 'n', 'no']:
            response = input('\nWould you like to change something? (y/n): ').lower()
            if response in ['y', 'yes']:
                prompt_change = input('\nWhat would you like to change?: ')
                messages_change = messages + [
                    {
                        "role": "assistant",
                        "content": html
                    },
                    {
                        "role": "system",
                        "content": "Debes cambiar el contenido html para ajustar las demandas, no respondas ni expliques, solo haz los cambios y retorna el html."
                    },
                    {
                        "role": "user",
                        "content": prompt_change
                    }
                ]
                html = self.module_ai.completion(messages_change, prompt_change)
                clean_html = re.sub(r'```html(.*?)```', r'\1', html, flags=re.DOTALL)
                self.save_one_page(clean_html, args.path)
                response = ''
            elif response in ['n', 'no']:
                sys.exit(1)

