acl=int(input("Igrese acl: "))
if acl >= 1 and acl <= 99:
    print("Es una acl estandar")
elif acl >= 100 and acl <= 199:
    print ("es una acl extendida")
else:
    print("NO es una acl valida")