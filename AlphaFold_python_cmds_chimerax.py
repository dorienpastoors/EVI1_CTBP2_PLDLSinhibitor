import os

from chimerax.core.commands import run as rc

# change to folder with data files
os.chdir("directory")

# gather the names of .pdb files in the folder
# this is just a text file with on each line the path to the relaxed .pdb files

file_names = open("all_Relaxed_files.txt")

file_names = file_names.readlines()


# loop through the files, opening, processing, and closing each in turn
for fn in file_names:
    fn = fn.rstrip()
    
    open_cmd = "open " + fn
    
    rc(session, open_cmd)
    session.logger.status("Processing file")
    #interfaces
    rc(session, "interfaces select /A contacting /B")
    rc(session, "info selection level residue")
    rc(session, "interfaces select /B contacting /A")
    rc(session, "info selection level residue")
    rc(session, "log save "+fn+"_intResidues.txt executableLinks false")
    rc(session, "log clear")
    rc(session, "close all")
    
    
# uncommenting the line below will cause Chimera to exit when the script is done
#rc("stop now")

