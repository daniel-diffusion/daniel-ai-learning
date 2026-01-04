import os

folder ="files_to_rename"
files =os.listdir(folder)
#print(f"files are: {files}")

counter =1

for filename in files:
    old_path= os.path.join(folder, filename)
    new_name = f"daniel_file_{counter}.txt"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)
    counter +=1
print (f"renamed {filename} to {new_name}")
