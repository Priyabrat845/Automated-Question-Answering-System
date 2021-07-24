import string

def clean_book(text_file):
  book = open(text_file,"r+") 
  book = book.read()
  
  book = book.replace('\n\n',' ')
  book = book.replace('\n',' ')
  book = book.lower()
  latters_to_keep = list((string.ascii_letters)+(string.ascii_uppercase) + " ")
  book_word = list(book)
  book_selected_latters = []
  for i in book_word:
    if i in latters_to_keep:
      book_selected_latters.append(i)
  book = ''.join(book_selected_latters)
  book_word_list = book.split()
  ultra_clean = []
  for i in book_word_list:
    if len(list(i))>1:
      ultra_clean.append(i)
  book = ' '.join(ultra_clean)
  return book



  def interview(text):
    for i in range(len(text)):
      text[i] = text[i].replace('\xa0','')
      text[i] = text[i].strip()
    return text

  