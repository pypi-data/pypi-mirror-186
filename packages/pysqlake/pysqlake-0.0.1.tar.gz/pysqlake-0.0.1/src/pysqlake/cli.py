import json
import subprocess

def run(cmd,token):
                        
    proc1 = subprocess.Popen(["upsolver","execute","-t", token,"-c", cmd],
    shell=False, text=True,universal_newlines=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
    proc2 = subprocess.Popen(["jq","-s"],
    shell=False, text=True,universal_newlines=True, stdin=proc1.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    proc3 = subprocess.Popen(["jq","-s"],
    shell=False, text=True,universal_newlines=True, stdin=proc1.stderr,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    output, err = proc2.communicate()[0],proc3.communicate()[1]
   
    if err == '':
        return True,json.loads(output)
    else:
        return False,err



