from WebBrowser import Web_Browser

#runs main funcionality of program, reads through file and determines when commands run
class executive:

#initializes web browser
    def __init__(self):
        self.browser = Web_Browser()

#reads through values and stores commands into list, reads through list and executes necessary commands
    def run(self, file_name):
        str(file_name)
        input_file = open(file_name)
        list_commands = []
        for count, line in enumerate(input_file.readlines()):
            each_word = []
            for index, word in enumerate(line.split(" ")):
                each_word.append(word.rstrip("\n"))
            list_commands.append(each_word)

        for eachLine in list_commands:
            if eachLine[0] == 'NAVIGATE':
                self.browser.navigate_to(eachLine[1])
            elif eachLine[0] == 'HISTORY':
                self.browser.history()
            elif eachLine[0] == 'BACK':
                self.browser.back()
            elif eachLine[0] == 'FORWARD':
                self.browser.forward()
            else:
                print("Command not found")