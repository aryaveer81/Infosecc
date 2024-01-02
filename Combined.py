#CAESAR CIPHER
#Encrypt
def encryptcaesar():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    inp=input("Enter Message to be encrypted\n")
    inp_length=len(inp)
    output=""
    for i in range(0,inp_length):
        charater=inp[i]
        if charater==" ":
            output+=" "
        else:
            locat=alphabet.find(charater)
            newlocat=(locat+3)%26
            output+=alphabet[newlocat]
    print("The encrypted message is:\n",output)

#DECRYPT
def decryptcaesar():
    alphabet="abcdefghijklmnopqrstuvwxyz"
    output=input("Enter the encrypted message\n")
    out_length=len(output)
    decrypt=""
    for i in range(0,out_length):
        character=output[i]
        if character==" ":
            decrypt+=" "
        else:
            loc=alphabet.find(character)
            newloc=loc-3
            decrypt+=alphabet[newloc]
    print("The decrypted message is:\n",decrypt)

#SUBSTITUTION
import random
#ENCRYPT
def encryptsubstitution():
    alpha=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    alpha=list(alpha)
    key=list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    random.shuffle(key)
    key_length=len(key)
    keyz=""
    for i in range(0,key_length):
        keyz+=key[i]
    print("The key is :\n",keyz)
    inp=input("Enter message to be encrypted\n")
    inp_length=len(inp)
    output=""
    for i in range(0,inp_length):
        charac=inp[i]
        loc=alpha.index(charac)
        output+=key[loc]
    print("The encrypted message is:\n",output)

#DECRYPT
def decryptsubstitution():
    alpha=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    alpha=list(alpha)
    output=input("Enter the message to be decrypted\n")
    key=list(input("Enter the key\n"))
    out_length=len(output)
    decrypt=""
    for i in range(0,out_length):
        chara=output[i]
        loca=key.index(chara)
        decrypt+=alpha[loca]
    print("The decrypted message is:\n",decrypt)

#RSA

import random
import math

def is_prime(number):
    if number<2:
        return False
    else:
        for i in range(2,(number//2)+1):
          if number%i==0:
             return False
        return True                 ######is_prime function will check all possible divisors before determining if a number is prime or not
        

def gen_prime(min_val, max_val):
    prime= random.randint(min_val, max_val)
    while is_prime(prime)==False:
        prime=random.randint(min_val,max_val)
    return prime     ##### Return nexessary



def calcprivkey():
    e=int(input("Enter the Public Key\n"))
    p,q=input("Enter the primes\n").split(' ')
    p=int(p)
    q=int(q)
    phi_n=(p-1)*(q-1)
    for d in range(2,phi_n):
       if (e*d)%phi_n == 1 and d<phi_n:           #####d>phi_n cases not dealt leading to problems
        return print("Your Private key is:\n",d)
    else:
        return("privkey DNE")
    
def generateyourprimes():
    p,q=gen_prime(700,800), gen_prime(100,200)
    print("The primes are:\n",p,q)
    print("Their product is:\n",p*q)

''' d=privkey(e, phi_n) '''
#Encryption Algo
def encryptrsa():
    message=input("Enter message to be encrypted\n")
    e=int(input("Enter public key\n"))
    n=int(input("Enter the Number 'n' \n"))
    message_encoded=[ord(c) for c in message] ########
    ciphertext=[(i**e)%n for i in message_encoded] ########
    meraj = '$'.join(str(i) for i in ciphertext) ###Serves the purpose
    print("The encrypted message is:\n",meraj)

#decryption algo
def decryptrsa():
    ciphertext=input("Enter encrypted message\n")
    d=int(input("Enter Private key\n"))
    n=int(input("Enter the Number 'n' \n"))
    ciphertext_list = [int(x) for x in ciphertext.split('$')]
     ####ciphertext.split('$'): This method takes the input string ciphertext and splits
     ###it into a list
    ###of substrings wherever it finds the "$" sign.
    decoded=[(i**d)%n for i in ciphertext_list]   
    msg_decoded="".join(chr(c) for c in decoded) ###### chr function opposite of ord function
    print("The decrypted message is:\n",msg_decoded)
    
def genpublickey():
    p,q=input("Enter the primes\n").split(' ')
    p=int(p)
    q=int(q)
    n=p*q
    phi_n=(p-1)*(q-1)
    e=random.randint(3,phi_n-1)
    while math.gcd(e,phi_n)!=1:
        e=random.randint(3,phi_n-1)
    return print("The public key is:\n",e)

def check_prim_root(g,m):
    if math.gcd(g,m)!=1:
        return False
    res_set=set()
    for i in range(1,m):
        res_set.add((g**i)%m)
    if len(res_set)==m-1:
        return True
    else: return False

def genprimroot():
   m=int(input("Enter the generated prime number\n"))
   primitiveroot=random.randint(2,m)
   while check_prim_root(primitiveroot, m)==False:
       primitiveroot=random.randint(2,m)
   return print("The primitive root is",primitiveroot) #The return primitiveroot statement was inside the while loop, causing the function to return after generating only one random number.
#print(gen_prim_root(11))

def generateyourprime():
    q=gen_prime(100,400)
    return print("The generated prime is",q)

def genprivkey():
    x=int(input("Enter any number less than generated prime to be chosen as private key\n"))
    return print("Your private key has been fixed as",x)

def calcpublickey():
    generatedprime=int(input("Enter the generated prime\n"))
    primitiveroot=int(input("Enter the primitive root\n"))
    privatekey=int(input("Enter the private key\n"))
    public_key=(primitiveroot**privatekey)%generatedprime
    return print("Your public key is",public_key)

def gensecretkey():
    privatekey=int(input("Enter YOUR private key\n"))
    publickey=int(input("Enter OTHER PERSON's Publickey\n"))
    prime=int(input("Enter the generated prime\n"))
    secretkey=(publickey**privatekey)%prime
    return print("The generated secret key is",secretkey)
def rsakeysgen():
    generateyourprimes()
    genpublickey()
    calcprivkey()
    
def diffiekeysgen():
    generateyourprime()
    genprivkey()
    calcpublickey()
