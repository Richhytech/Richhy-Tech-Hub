from nova.brain import handle_command

def respond(user_input):
    response = handle_command(user_input)
    return response