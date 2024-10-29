from config.prompts import CREATE_ONE_PAGE

class OnePageBuilder:
    def __init__(self, agent_ai):
        self.agent_ai = agent_ai

    def prepare_prompt(self, args):
        description = args.description if args.description else ''
        location = args.location if args.location else ''
        colors = args.colors if args.colors else ''
        name = args.name if args.name else ''
        lang = args.language if args.language else 'English'

        prompt = CREATE_ONE_PAGE
        prompt = prompt.replace('{technologies}', args.technologies.replace(',', ', '))
        prompt = prompt.replace('{description}', description)
        if location:
            prompt = prompt.replace('{location}', f"ubicada en {location}.")
        prompt = prompt.replace('{location}', '')
        if colors:
            colors = colors.replace(',', ', ')
            prompt = prompt.replace('{colors}', f"Usa los colores {colors} en el diseño.")
        prompt = prompt.replace('{company_name}', f"Mi empresa se llama {name}")
        prompt = prompt.replace('{lang}', f" en {lang}")
        prompt = prompt.replace('{sections}', args.sections.replace(',', ', '))

        return prompt

    def build(self, args):
        prompt = self.prepare_prompt(args)
        print(prompt)
        # Call the AI agent to generate the content
        # response = self.agent_ai(prompt)
        # print(response)
