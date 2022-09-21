from Executive import executive

#takes in input file, passes it to executive
def main():
    file_name = input("Enter file name: ")
    input_file = open(f"{file_name}")
    my_executive = executive()
    my_executive.run(file_name)

main()