from collections import deque

def simulate_undo_operation(commands):
    stack = deque()

    for command in commands:
        if command.lower() == 'undo':
            if stack:
                stack.pop()
            else:
                print("Cannot perform UNDO operation!!..")
                return
        else:
            stack.append(command[-1])
    return ''.join(stack)

commands = ['type A', 'type B', 'undo', 'type C', 'type D', 'type D', 'type D','undo', 'type C']
print(simulate_undo_operation(commands))