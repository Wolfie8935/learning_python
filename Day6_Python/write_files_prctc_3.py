record_last_session = ["John", "12/20/2022", "08:17:32 pm", "No loading errors"]

my_file = open("register.txt","a")

for l in record_last_session:
    my_file.writelines(l + "\t")
my_file.writelines("\n")
my_file.close()


my_new_file = open("register.txt","r")
content = my_new_file.read()
print(content)