import clr
import sys

# assembly_path = r"C:\Users\pethzero\source\repos\Showmessage\Showmessage\bin\Debug"
# sys.path.append(assembly_path)

clr.AddReference("Showmessage")
from Showmessage import MSGShow

msg = MSGShow()

# call Happy Function
print(msg.Happy("python"))

# call Sad Function
print(msg.Sad("Golang"))