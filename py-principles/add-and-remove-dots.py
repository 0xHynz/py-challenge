
def add_dots(text):
    text = [t for t in text]
    return '.'.join(text)

def remove_dots(text):
    text = ''.join(text.split('.'))
    return text

if __name__=="__main__":
   print (remove_dots(add_dots('test')))


