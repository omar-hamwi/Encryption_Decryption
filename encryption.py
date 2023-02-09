def encrypt(text,shift):
  cipher_text=""
  for i in text:
      position=alphabet.index(i)
      new_position=position+shift
      new_letter=alphabet[new_position]
      cipher_text +=new_letter
  print("the encoded text is:{}".format(cipher_text))

def decryt(text, shift):
    clear_text=" "
    for i in text:
        position =alphabet.index(i)
        new_position=position-shift
        new_letter=alphabet[new_position]
        clear_text+=new_letter
    print("the decode text is:{}".format(clear_text))
while True:
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    direction=input("Type 'encode' to шифрование ,Type 'decode' to расшифрован : \n")
    
    if  direction=="encode":
        encrypt(text,shift)
        
    elif direction=="decode":
            decryt(text,shift) 
    else:
            break
    text=input("type your message :\n").lower()
    shift=int(input("type the shift number:\n"))

