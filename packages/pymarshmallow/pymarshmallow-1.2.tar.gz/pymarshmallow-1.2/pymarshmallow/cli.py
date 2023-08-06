import argparse

class cli:
    intro = None
    prompt = None
    commands = {}
    command_options = {}

    @staticmethod
    def properties(intro, prompt):
        cli.intro = intro
        cli.prompt = prompt

    @classmethod
    def command(cls, func):
        def wrapper(*args, **kwargs):
            parser = argparse.ArgumentParser()
            for args, kwargs in cls.command_options.get(func.__name__, []):
                parser.add_argument(*args, **kwargs)
            return func(parser.parse_args(*args, **kwargs))
        cls.commands[func.__name__] = wrapper
        return wrapper

    @classmethod
    def option(cls, *args, **kwargs):
        def decorator(func):
            if func.__name__ not in cls.command_options:
                cls.command_options[func.__name__] = []
            cls.command_options[func.__name__].append((args, kwargs))
            return func
        return decorator

    @classmethod
    def run(cls):
        print(cls.intro)
        while True:
            user_input = input(cls.prompt)
            try:
                command, *args = user_input.split()
                if command == 'quit':
                    print("Exiting the program")
                    break
                elif command in cls.commands:
                    cls.commands[command](*args)
                else:
                    print(f"{command} is not a valid command")
            except ValueError:
                print("Please enter a command")
            except Exception as e:
                print(f"An error occurred: {e}")
