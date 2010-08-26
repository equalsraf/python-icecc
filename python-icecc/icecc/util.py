"""
Utility functions to parse output from the icecc scheduler
"""

def map_listcs(item):
    """
    Turn a single output line from listcs into a tuple

    Intended to be uses as map function, for ex.
    >> map(map_listcs, lines)
    """
    fields = item.split()

    fields = [x.split("=", 1)[-1] for x in fields]

    return tuple( fields )


def map_listjobs(item):
    """
    Turn a single output line from listjobs into a tuple

    Intended to be uses as map function, for ex.
    >> map(map_listjobs, lines)
    """
    fields = item.split()

    fields =  [x.split(":", 1)[-1] for x in fields]

    return tuple( fields )


def parse_internals(lines):
    """
    Takes a list of output lines from the "internals" command
    and turns it into a host indexed dictionary
    """
    internals = {}
    key = None
    for line in lines:
        if line.startswith("Node"):
            key = line.split()[2]
            internals[key] = []
            continue
        elif not key:
            continue

        args = line.split(":", 1)
        if len(args) != 2:
            args = line.split("=", 1)
        if len(args) != 2:
            continue

        internals[key].append( (args[0].strip(), args[1].strip()) )
      
    return internals

def parse_command( cmd, outcome, raw=False):
    """
    Given a command and its output, return the proper data type for its outcome

    - If the command in unsupported ( or raw is True) 
      you'll get the raw text as provided by the scheduler
    
    Currently the following commands are supported:
    - help 		- Returns a list of commands
    - internals 	- Returns a host-indexed dictionary
    - listcs	- Returns a list of tuples
    - blockcs	- Returns True on success

    """

    lines = outcome.splitlines()
    if len(lines) == 1:
        return ''

    result = None

    if raw:
        pass
    elif cmd.startswith("help"):
        result = lines[:-1]
    elif cmd.startswith("internals"):
        result = parse_internals(lines[:-1])
    elif cmd.startswith("listcs"):
        valid = [ x for x in lines[:-1] if not x.startswith("  ")]
        result = [map_listcs(x) for x in valid]
    elif cmd.startswith("blockcs "):
        if len(lines) == 1:
            return False

        if lines[0].startswith("removing host "):
            return True
            
        return False
    elif cmd.startswith("listjobs"):
        result =  [ map_listjobs(x) for x in  lines[:-1] ]
    elif cmd.startswith("listblocks"):
        result = [x.strip() for x in lines[:-1]]

    if result:
        return result

    # Unknown commands
    return '\n'.join(lines[:-1])

