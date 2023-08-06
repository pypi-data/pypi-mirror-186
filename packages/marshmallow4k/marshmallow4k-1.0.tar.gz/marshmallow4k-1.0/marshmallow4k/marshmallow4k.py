class marshmallow4k:
    def __init__(self):
        self.intro = None
        self.prompt = None
        self.commands = {}

    def properties(self, intro, prompt):
        self.intro = intro
        self.prompt = prompt
        print(intro)

    def command(self, func):
        self.commands[func.__name__] = func
        return func

    def run(self):
        while True:
            user_input = input(self.prompt)
            try:
                command, *args = user_input.split()
                if command in self.commands:
                    args = [int(x) for x in args]
                    self.commands[command](*args)
                else:
                    print(f"{command} is not a valid command")
            except:
                print(f"{user_input} is not a valid input")
