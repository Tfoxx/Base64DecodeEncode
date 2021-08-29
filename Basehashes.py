import base64
class EngineEncode():
    def __init__(self,data):
        self.data = data
    def Base64Encode(hash):
        hash_bytes=hash.data.encode("utf-8")
        base64_data= base64.b64encode(hash_bytes)
        base64_message=base64_data.decode("ascii")
        print("base64 hash==> "+base64_message)
    def Base32Encode(hash):
        hash_bytes=hash.data.encode("utf-8")
        base32_data= base64.b32encode(hash_bytes)
        base32_message=base32_data.decode("utf-8")
        print("base32 hash==> "+base32_message)
    def Base16Encode(hash):
        hash_bytes=hash.data.encode("utf-8")
        base16_data=base64.b16encode(hash_bytes)
        base16_message=base16_data.decode("utf-8")
        print("base16 hash==>  "+base16_message)
    def Base85Encode(hash):
        hash_bytes=hash.data.encode("utf-8")
        base85_data=base64.b85encode(hash_bytes)
        base85_message=base85_data.decode("utf-8")
        print("base85 hash==>  "+ base85_message)


class EngineDecode():
    def __init__(self,data):
        self.data = data
    def Base64Decode(hash):
        base64_bytes=hash.data.encode("ascii")
        base64_data=base64.b64decode(base64_bytes)
        message = base64_data.decode("ascii")
        print("base64 text ==> "+ message)
    def Base85Decode(hash):
        base64_bytes=hash.data.encode("ascii")
        base64_data=base64.b85decode(base64_bytes)
        message = base64_data.decode("ascii")
        print("base85 text ==> "+ message)
    def Base32Decode(hash):
        base32_bytes=hash.data.encode("ascii")
        base32_data=base64.b32decode(base32_bytes)
        message= base32_data.decode("ascii")
        print("base32 text ==> "+message)




print("""Script Of Engine
Whichone do you want ?
1-Encode
2-Decode """)
Choice=int(input("Enter :"))
if (Choice == 1):
    ForEncodeText=input("Please enter hash: ")
    Engine = EngineEncode(ForEncodeText)
    Engine.Base85Encode()
    Engine.Base64Encode()
    Engine.Base32Encode()
    Engine.Base16Encode()
elif (Choice == 2):
    Choice2=int(input("1-Base64\n2-Base32\n3-Base85\nEnter :"))
    ForDecodeText=input("Please Enter Hash: ")
    EngineDec = EngineDecode(ForDecodeText)
    if (Choice2 == 1):
        EngineDec.Base64Decode()
       
    elif (Choice2 == 2):
        EngineDec.Base32Decode()
        
    elif (Choice2 == 3):
        EngineDec.Base85Decode()
    else:
        print("You Are Enter Wrong Menu Key")
        exit

else:
    print("You Are Enter Wrong Menu Key")
    exit



