import subprocess
import os
import json

def apply_external(cmd_ary, out):
    # http://reganmian.net/blog/2014/09/22/easy-interoperability-between-ruby-and-python-scripts-with-json/
    proc = subprocess.Popen(
        cmd_ary,stdout=subprocess.PIPE,
        stdin=subprocess.PIPE)
    proc.stdin.write(bytes(out, "UTF-8"))
    proc.stdin.close()
    result = proc.stdout.read()
    result = result.decode("UTF-8")
    return(result)

ruby_script = os.path.join(os.getcwd(), "stdout.rb")
ret = apply_external(['ruby', ruby_script], "hello sv")
data = json.loads(ret)

print(data['zone_8'][0])