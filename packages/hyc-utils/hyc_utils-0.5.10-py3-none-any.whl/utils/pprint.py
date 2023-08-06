def pformat(d, indent=0, spaces=4, verbose=False):
    output = ''
    for key, value in d.items():
        output += f"{' ' * spaces * indent}'{str(key)}':\n"
        if isinstance(value, dict):
            output += f"{pformat(value, indent+1)}\n"
        else:
            if not verbose:
                value = type(value)
            output += '\n'.join([f"{' ' * spaces * (indent+1)}{line}" for line in str(value).split('\n')]) + '\n'
    return output.rstrip('\n')

def pprint(d, **kwargs):
    print(pformat(d, **kwargs))