"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

'''
Enter e to encrypt, d to decrypt, or q to quit: z
Did not understand command, try again.
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!
'''

associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
lister=[]
Z = 'b'
while Z != 'q':
    Z = input('Enter e to encrypt, d to decrypt, or q to quit: ')
    if Z == 'e' or Z == 'd':
        Message = input('Message: ')
        Key = input('Key: ')
        M = [associations.find(x) for x in Message]
        K = [associations.find(x) for x in Key]
        for i in range(len(M)):
            Sum = M[i] + K[i%(len(K))]
            lister.append(Sum)
        print(lister)
        associations1= list(associations)
        T = [(associations1[x]) for x in lister]
        print("".join(T))
    if Z != 'e' and Z != 'd' and Z != 'q':
        print('Did not understand command, try again.')
    if Z == 'q':
        print('Goodbye!')
   
   
    








