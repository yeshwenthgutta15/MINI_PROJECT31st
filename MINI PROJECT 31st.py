import re
from prettytable import PrettyTable

class Search:
    def __init__(self):
        # file = self.read_text_from_file()
        # print(file)
        self.pattern = input('Enter the text to search: ')
        print('1. Start\n2. End\n3. Any Position')
        self.pos = int(input('Where do you want to search the pattern: '))

        if self.pos == 1:
            self.run_search_on_start()
        elif self.pos == 2:
            self.run_search_on_end()
        elif self.pos == 3:
            print('1. First occurrence\n2. All occurrences')
            self.no = int(input('How many occurrences do you want to search: '))
            self.run_search_on_any_pos()
        else:
            print('Invalid input')

    def read_text_from_file(self):
        with open('search.txt', 'r') as file:
            return file.read()

    def run_search_on_any_pos(self):
        text = self.read_text_from_file()
        regex = self.pattern

        if self.no == 1:
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            match = re.finditer(regex, text)
            if match:
                for i in match:
                    start = i.start()
                    end = i.end()
                    table.add_row([start, end, text[start:end]])
                print(table)
            else:
                print('No match found')

        elif self.no == 2:
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            match = re.finditer(regex, text)
            if match:
                for i in match:
                    start = i.start()
                    end = i.end()
                    table.add_row([start, end, text[start:end]])
                print(table)
            else:
                print('No match found')

    def run_search_on_start(self):
        text = self.read_text_from_file()
        pattern = r'\A' + self.pattern
        regex = re.compile(pattern)
        match = re.search(regex, text)
        if match:
            start = match.span()[0]
            end = match.span()[1]
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            table.add_row([start, end, text[start:end]])
            print(table)
        else:
            print('No match found')

    def run_search_on_end(self):
        text = self.read_text_from_file()
        pattern = self.pattern + r'$'
        regex = re.compile(pattern)
        match = re.search(regex, text)
        if match:
            start = match.span()[0]
            end = match.span()[1]
            table = PrettyTable()
            table.field_names = ['Start Index', 'End Index', 'Match String']
            table.add_row([start, end, text[start:end]])
            print(table)
        else:
            print('No match found')

search_obj = Search()


            