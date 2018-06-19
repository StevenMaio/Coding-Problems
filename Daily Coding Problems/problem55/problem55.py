from random import randint

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def random_short():
    short = ''

    for i in range(6):
        index = randint(0, len(chars) - 1)
        short += chars[index]

    return short

class URLShortener:
    def __init__(self):
        self.short_to_url = {}
        self.url_to_short = {}

    def shorten(self, url):
        short = None

        # Determine if the url has already been shortened
        try:
            # Return the short if it's there
            short = self.url_to_short[url]
            return short

        except:
            # Create a short and return it
            short = random_short()
            uniq_short = False

            # Handle the case of the short being already in use
            while not uniq_short:
                if short in self.short_to_url.keys():
                    short = random_short()
                else:
                    uniq_short = True

            # Add an entry to short_to_url and url_to_short
            self.url_to_short[url] = short
            self.short_to_url[short] = url
            return short

    def restore(self, short):
        # Return the value associated with short, if it exists
        try:
            return self.short_to_url[short]

        # Otherwise, return null
        except:
            return None

def main():
    url_s = URLShortener()

    while True:
        # Parse input
        line = input('> ')

        line = line.split(' ')
        command = line[0]

        if command == 'help':
            if len(line) != 1:
                print('Error : print requires no arguments')
                continue
            
            print('Commands')
            print('help\t\t- print a list of available commands')
            print('exit\t\t- exit the program')
            print('shorten url\t- converts url into a 6 character string')
            print('restore short\t- restores the short to a url')
            print('print\t\t- prints all of the url/short pairs')

        elif command == 'exit':
            print('Goodbye')
            return

        elif command == 'shorten':
            if len(line) != 2:
                print('Error : shorten requires a url arguments')
                continue

            url = line[1]
            short = url_s.shorten(url)
            print(short)

        elif command == 'restore':
            if len(line) != 2:
                print('Error : restore requires a short arguments')
                continue

            short = line[1]
            url = url_s.restore(short)
            print(url)

        elif command == 'print':
            if len(line) != 1:
                print('Error : print requires no arguments')
                continue

            shorts = url_s.short_to_url.keys()

            for key in shorts:
                msg = '{}: {}'.format(key, url_s.restore(key))
                print(msg)

        else:
            print('Error : invalid command')

if __name__ == '__main__':
    main()