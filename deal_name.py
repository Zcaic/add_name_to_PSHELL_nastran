import re 
from pathlib import Path 
from termcolor import cprint

def deal_name(nasfile,outfile):
    def sub_func(match):
        old_str:list=match.group().split("\n")
        pshell_name=match.group("name")
        pshell_id=match.group("id")
        insert_str=f"$ANSA_NAME_COMMENT;{pshell_id};PSHELL;{pshell_name};"
        old_str.insert(1,insert_str)
        new_str="\n".join(old_str)
        return new_str
    
    pattern=r"\$\*\s+Property:\s(?P<name>.*)\nPSHELL\s+(?P<id>\d+)\s+.*\n"
    pattern=re.compile(pattern)

    content=Path(nasfile).read_text()
    new_content=re.sub(pattern,sub_func,content)
    outfile=Path(outfile)
    outfile.write_text(new_content)
    cprint(f"new nastran file `{outfile.name}` is generated","green",attrs=["bold"])


if __name__=="__main__":
    nasfile="./bulk.dat"
    deal_name(nasfile,"new_bulk.dat")