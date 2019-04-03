"""
cryptography.py
Author: Rain Liu
Credit: Mr. Dennison, Mr. Healy, Miriam

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
listers=[]
Z = 'b'
while Z != 'q':
    Z = input('Enter e to encrypt, d to decrypt, or q to quit: ')
    if Z == 'e':
        Message = input('Message: ')
        Key = input('Key: ')
        M = [associations.find(x) for x in Message]
        K = [associations.find(x) for x in Key]
        for i in range(len(M)):
            Sum = M[i] + K[i%(len(K))]
            lister.append(Sum)
            for i in range(len(lister)):
                if lister[i] >= len(associations):
                    lister[i] = lister[i]-len(associations)
        associations1= list(associations)
        LEM = [(associations1[x]) for x in lister]
        EM="".join(LEM)
        print(EM)
    if Z == 'd':
        DMessage = input('Message: ')
        DKey = input('Key: ')
        M1 = [associations.find(x) for x in DMessage]
        K1 = [associations.find(x) for x in DKey]
        for i in range(len(M1)):
            Sum1 = M1[i] - K1[i%(len(K1))]
            listers.append(Sum1)
            for i in range(len(listers)):
                if listers[i] >= len(associations):
                    listers[i] = listers[i]-len(associations)
        associations1= list(associations)
        LDM = [(associations1[x]) for x in listers]
        DM = "".join(LDM)
        print(DM)
    if Z != 'e' and Z != 'd' and Z != 'q':
        print('Did not understand command, try again.')
    if Z == 'q':
        print('Goodbye!')
   
   
    








