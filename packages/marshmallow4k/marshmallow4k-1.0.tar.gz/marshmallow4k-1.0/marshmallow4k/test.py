import marshmallow4k

marshmallow4k = marshmallow4k.marshmallow4k()
marshmallow4k.properties("Welcome to Marshmallow!", ">>> ")

@marshmallow4k.command
def add(x:int, y:int):
    print(x + y)

@marshmallow4k.command
def subtract(x:int, y:int):
    print(x - y)

@marshmallow4k.command
def multiply(x:int, y:int):
    print(x * y)

@marshmallow4k.command
def divide(x:int, y:int):
    print(x / y)

marshmallow4k.run()
