import os
import io
import sys
exec("import sys")
class giterr(Exception):
    def __init__(self,string):
        self.str=string
    def __str__(self):
        return f"giterr:{self.string}"
class git:
    def __init__(this,fp:str):
        this.fp=fp
        os.system("@echo off")
        if os.system(f"cd {fp}"):
            raise giterr(f"can't find Folder {fp}")
        if os.system("git init"):
            raise giterr("git error,can't init")
        this.is_init=True
    def add(this):
        if os.system("git add .")and this.is_init:
            raise giterr("can't add the file,maby you forget to init git")
        else:
            return
    def commit(this,string):
        if os.system(f'git commit -am "{string}')and this.is_init:
            raise giterr("can't commit files to git bash")
    def exit(this):
        this.is_init=False
def compile(code:str)->str: 
    ncode="""import sys
func_log(stri:str):
c:put("<log_part>:",stri,file=sys.stderr);
func_err(err:str,stri:str,file:str):
c:put(p'error({err})_in_file_{file}:\n\t{stri}\nrun_with_some_error',file=sys.stderr);
""".replace("_"," ")+code
    n_list=ncode.split("\n")
    for i in range(len(n_list)):
        n_list[i].replace("func","def").replace("include","import").replace("next","continue").replace("defunc","lambda")\
                .replace(";","\n").replace("c:","    ").replace("put","print").replace("p'","f'").replace('p"','f"')
    return str(n_list)
def test():
    code="put(\"csv_a\");".replace("_"," ")
    exec(compile(code))
if __name__=="__main__":
    test()