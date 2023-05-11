import os

os.subprocess.run(["ls", "-l", "/dev/null"], capture_output=True)