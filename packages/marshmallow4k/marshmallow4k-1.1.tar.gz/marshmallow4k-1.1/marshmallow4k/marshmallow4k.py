class marshmallow4k:
    intro = None
    prompt = None
    commands = {}

    @staticmethod
    def properties(intro, prompt):
        marshmallow4k.intro = intro
        marshmallow4k.prompt = prompt

    @classmethod
    def command(cls, func):
        cls.commands[func.__name__] = func
        return func

    @classmethod
    def run(cls):
        print(cls.intro)
        while True:
            user_input = input(cls.prompt)
            try:
                command, *args = user_input.split()
                if command in cls.commands:
                    args = [int(x) for x in args]
                    cls.commands[command](*args)
                else:
                    print(f"{command} is not a valid command")
            except:
                print(f"{user_input} is not a valid input")