import os
sourceFilesList=""
IncludeFilesList=""
IncludeDuplictFilter=""
ManualAddDirectories = 0
ProceedAddDirectory = 1
ManualDirectoryDuplictFilter=""

print("Do you want to Directories Manually ? (Y/N)")
Confirmation = input()
if (Confirmation == "Y" or Confirmation == "y"):
     ManualAddDirectories = 1

def AskForProceeding (root):
     if(ManualAddDirectories == 1):
          print(root + ", Do you want to add ? (Y/N)")
          Confirmation = input()
          if (Confirmation == "Y" or Confirmation == "y"):
               ProcdAddDirectory = 1
          else:
               ProcdAddDirectory = 0
              
     else:
          ProcdAddDirectory = 1

     return ProcdAddDirectory

for root, dirs,files  in os.walk(".", topdown=True):

          for name in files:
               fileName = ""
               includePath = ""
               fileDetected = 0
               if (name.endswith(".c")):
                    fileNameWithPath = os.path.join(root, name)
                    fileName = fileNameWithPath[2:]
                    fileDetected = 1

               if (name.endswith(".h")):
                    if(IncludeDuplictFilter!= root):
                         IncludeDuplictFilter = root
                         includePath = IncludeDuplictFilter[2:]
                         fileDetected = 1

               if (fileDetected == 1 and ManualDirectoryDuplictFilter != root):
                    ProceedAddDirectory = AskForProceeding(root)
                    ManualDirectoryDuplictFilter = root

               if(ProceedAddDirectory == 1):
                    if(fileName != ""):
                         sourceFilesList = sourceFilesList + "\n" + '"' + fileName + '"'
                    if(includePath != ""):
                         IncludeFilesList = IncludeFilesList + "\n"+'"'+includePath+'"'


print(sourceFilesList)
print("\n")
print(IncludeFilesList)

if(sourceFilesList != ""):
     sourceFilesList = "\nSRCS "+ sourceFilesList

if(IncludeFilesList != ""):
     IncludeFilesList = "\n\nINCLUDE_DIRS " + IncludeFilesList

if(sourceFilesList == "" and IncludeFilesList == ""):
     print("Not Including any directories,Press any key and Enter to exit")
     Confirmation = input()
     exit()
else:
     CMakeListText="idf_component_register("+sourceFilesList+IncludeFilesList+")"
     CMakeListText = CMakeListText.replace('\\','/')
     f = open("CMakeLists.txt", "w")
     f.write(CMakeListText)
     f.close()