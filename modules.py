import subprocess
import re

def cat(loc):
  st=subprocess.Popen(['cat',loc],stdout=subprocess.PIPE)
  output=st.communicate()[0]
  with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n******output*******\n\n")
      f.close()
  with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()
  

def strings(loc):   #calling strings command for PNG and JPG files
   st=subprocess.Popen(['head',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*****output head of strings*****\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close() 
   st=subprocess.Popen(['tail',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*****output tail of strings*****\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def exiftool(loc):  #calling exiftool for PNG and JPG files
    st=subprocess.Popen([f'exiftool {loc} | grep -v -E "Permissions|MIME|Subject|Title|Image Size|File Type|File Type Extension|File Name|Exiftool Version Number|Directory"'],stdout=subprocess.PIPE,shell=True)
    output=st.communicate()[0]
    
    with open("/home/arijit/Downloads/Report.md","a")as f:
       f.write("\n\n*****output******\n\n")
       f.close()
    with open("/home/arijit/Downloads/Report.md","a+b")as f:
       f.write(output)
       f.close()


def zsteg(loc):     #calling zsteg for PNG files
   st=subprocess.Popen(['zsteg',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n******output*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def binwalk(loc):   #reveals metadata stored in the image
   st=subprocess.Popen(['binwalk',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*******output*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()


def stegseek(loc):
   st=subprocess.Popen(['stegseek',loc,'/home/arijit/Downloads/rockyou.txt'],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*******output******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()


def imagemagick(loc):
   st=subprocess.Popen(['identify','-verbose',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n********output*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def xxd(loc):
   st=subprocess.Popen(['xxd','-a',loc],stdout=subprocess.PIPE)
   output=st.communicate()[0]
  
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*********output*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()

def outguess(loc):
   st=subprocess.Popen(['outguess','-r',loc,'output.txt'],stdout=subprocess.PIPE)
   output=st.communicate()[0]

   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*******output*******\n\n")
      f.close
   try:
      with open("/home/arijit/Downloads/output.txt","r")as l:
         text=l.read()
         l.close()
      with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write(text)
         f.close()
   except:
      with open("/home/arijit/Downloads/Report.md","a")as f:
         f.write("No Output")
         f.close()

def foremost(loc):
   st=subprocess.Popen(['foremost','-T',loc,'-v'],stdout=subprocess.PIPE)
   output=st.communicate()[0]
   with open("/home/arijit/Downloads/Report.md","a")as f:
      f.write("\n\n*********output*******\n\n")
      f.close()
   with open("/home/arijit/Downloads/Report.md","a+b")as f:
      f.write(output)
      f.close()
