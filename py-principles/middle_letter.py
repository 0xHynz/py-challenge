
def mid(text):
    if text.isalpha():
       if len(text) % 2 == 1:
          text = [t for t in text]
          bagi = int(len(text) / 2 )
          return text[bagi]
       else:
           return ''
    else:
       return ''


if __name__=="__main__":
   print(mid('abc'))

