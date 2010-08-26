"""
Remote Control icecream entities
"""
import telnetlib
import re

from icecc.util import parse_command

RE_COMMAND = re.compile(".*?200.*?\n", re.MULTILINE | re.DOTALL)

class SchedulerControl(object):
    """
    Control a specific icecream scheduler(host:port)

    This implementation uses telnet management channel
    to push commands and retrieve their output. It's not
    brilliantly fast, but it gets the job done.
    """

    def __init__(self, host='localhost', port=8766):
        self.port = port
        self.host = host

        self.version = '-'
        self.hosts = 0
        self.jobs = 0



    def __parse_greet(self, line):
        """
	Parse a greeting line, updating the version, hosts and jobs vars


	"""
        params = line.split()
        try:
            self.version = params[1].split(':')[0]
            self.hosts = params[4]
            self.jobs = params[6]
        except IndexError:
            pass





    def __push_all(self, queue, raw=False):
        """
        Pass the scheduler the given queue of commands
        """
        tn_con = telnetlib.Telnet(self.host, self.port)
        cmds = []

        while len(queue) != 0:
            cmd = queue.pop()
            tn_con.write(str(cmd + "\n"))
            cmds.append( cmd )

        tn_con.write("quit\n")

        output = tn_con.read_all() 
        answers = RE_COMMAND.findall( output )

        self.__parse_greet(answers[0])

        result = []
        for i in range(len(cmds)):
            result.append (parse_command( cmds[i], answers[i+2], raw ) )

        result.reverse()
        return result

    def runall(self, queue, raw=False):
        """
	Run a queue of commands in order

	Returns a list with the outcome of each command

	>> ctrl = SchedulerControl()
	>> ctrl.runall(["help", "listcs", "internals"])
	"""
        return self.__push_all( queue, raw )
    def run(self, cmd, raw=False):
        """
        Run the given command and yield the output
        """
        return self.__push_all( [cmd], raw )[0]


    def help(self):
        """
	Returns a list of available commands
	"""
        return self.run("help")
    def internals(self):
        """
        Return a host-indexed dictionary with the internal state of the secheduler
        """
        return self.run("internals")
    def listcs(self):
        """
	Returns a list of cs host associated with the scheduler.

	Each element is tuple in the form 
		(name, address, arch, speed, jobs, load)
	"""
        return self.run("listcs")
    def blockcs(self, host):
        """
	Remove a cs host by name, the name is the as supplied by listcs.

	Returns True on success
	"""
        return self.run("blockcs %s" % host)
    def listjobs(self):
        """
	Returns a list of jobs associated with the scheduler.

	Each element is tuple in the form 
		(id, state, source, cs, file)
	"""
        return self.run("listjobs")
    def listblocks(self):
        """
	Returns a list of blocked CS hosts.

	Each element is an address
	"""
        return self.run("listblocks")




