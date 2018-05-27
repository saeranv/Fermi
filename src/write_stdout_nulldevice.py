
# Overwrite standard output (stdout) with any file object.
# This should work cross platform and write to the null device.
sys.stdout = open(os.devnull, 'w')
sys.stdout = sys.__stdout__
