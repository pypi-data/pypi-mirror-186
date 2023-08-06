class pymarshmallow:
    intro = None
    prompt = None
    commands = {}

    @staticmethod
    def properties(intro, prompt):
        pymarshmallow.intro = intro
        pymarshmallow.prompt = prompt

    @classmethod
    def command(cls, func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        cls.commands[func.__name__] = wrapper
        return wrapper

    @classmethod
    def run(cls):
        print(cls.intro)
        while True:
            user_input = input(cls.prompt)
            try:
                command, *args = user_input.split()
                if command in cls.commands:
                    cls.commands[command](*args)
                else:
                    print(f"{command} is not a valid command")
            except:
                print(f"{user_input} is not a valid input")