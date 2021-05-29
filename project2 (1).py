"Generating PAN Number."

'''
Structure of PAN number:

The PAN (or PAN number) is a ten-character long alpha-numeric unique identifier.

The PAN structure is as follows: Fourth character [P — Individual or Person ] Example: AAAPZ1234C

# The first five characters are letters (in uppercase by default), followed by four numerals, and the last (tenth) character is a letter.
# The first three characters of the code are three letters forming a sequence of alphabets letters from AAA to ZZZ
# The fourth character identifies the type of holder of the card. Each holder type is uniquely defined by a letter from the list below:
   A — Association of persons (AOP)
   B — Body of individuals (BOI)
   C — Company
   F — Firm
   G — Government
   H — HUF (Hindu undivided family)
   L — Local authority
   J — Artificial juridical person
   P — Individual or Person
   T — Trust (AOP)
# The fifth character of the PAN is the first character of either:
 1.of the surname or last name of the person, in the case of a "personal" PAN card, where the fourth character is "P" or
 2.of the name of the entity, trust, society, or organisation in the case of a company/HUF/firm/AOP/trust/BOI/local authority/artificial judicial person/government, where the fourth character is "C", "H", "F", "A", "T", "B", "L", "J", "G".
# The last (tenth) character is an alphabetic digit used as a check-sum to verify the validity of that current code
 ''' 

import random 
alphabet = {
         '1':'A' , '2':'B' , '3':'C'  , '4':'D' ,
         '5':'E' , '6':'F' , '7':'G'  , '8':'H' ,
         '9':'I' , '10':'J', '11':'K' , '12':'L',
         '13':'M', '14':'N', '15':'O' , '16':'P',
         '17':'Q', '18':'R', '19':'S' , '20':'T', '21':'U',
         '22':'V', '23':'W', '24':'X' , '25':'Y', '26':'Z'
         }
type_of_card = {
         'COMPANY':'C',
         'FIRM':'F',
         'GOVERNMENT':'G',
         'HUF':'H',
         'LOCALAUTHORITY':'L',
         'PERSONAL':'P',
         'TRUST':'T'  
         }  
def main(): 
    print(" Welcome ")
    Type = input("Please enter the type of card :")
    Normalized_Type = normalize_name(Type)
    if Normalized_Type == 'PERSONAL':
        first_name = input("Please enter your first name : ")
        last_name = input("Please enter your last name : ")
        age = int(input("Please enter your age : "))
        # If your age is not 18 , you can't have pan card.
        if age < 18 :
          print("You are not eligible for PAN card ")
        else : 
          pan = get_pan_number(last_name,Normalized_Type)
          print("Your PAN card number is : ",pan)
          data = {}
          data['Name']= first_name + " " + last_name
          data['Age'] = age
          data['PAN Number'] = pan
          print ('Your PAN card detaiils : ',data)
    else : 
        others = input("Please enter name : ")
        pan_others = get_pan_number(others,Normalized_Type)
        print ('PAN card number is : ',pan_others)
        pan_2 = {}
        pan_2['Name'] = others
        pan_2['PAN Number'] = pan_others
        print ('PAN card details : ',pan_2)


def normalize_name(s):
    '''
    This function takes a string of alphabets and returns upper case alphabets excluding other charecters between alphabets.
    >>> normalize_name('jodhpur park boys school')
    'JODHPURPARKBOYSSCHOOL'
    '''
    normalized = ''
    for ch in s:
        if ch.isalpha():
            normalized += ch.upper()
    return normalized


def pad(num, length):
    '''
    >>> pad(457,4)
    0457
    '''
    num_string = str(num)
    while len(num_string) < length:
    # insert a 0 at the start of the string, increasing its length by one
          num_string = "0" + num_string
    return num_string


def get_pan_number(name,Type):
        norm = normalize_name(name)
        First = alphabet[str(random.randint(1,26))]
        second = alphabet[str(random.randint(1,26))]
        third = alphabet[str(random.randint(1,26))]
        fourth = type_of_card[Type]
        fifth = norm[0]
        number = pad(random.randint(0,9999),4)
        sixth = norm[random.randint(0,len(norm)-1)]
        pan_id = (First + second + third + fourth + fifth + number + sixth)
        
        return pan_id

if __name__ == '__main__':
    main()
