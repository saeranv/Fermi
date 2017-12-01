import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""

    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        return True


if run:
    print 'type greet to get greeting'
    print 'type EOF to quit (cmd)'
    h = HelloWorld()
    h.cmdloop()
