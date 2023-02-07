
def main():
    
    
    
    
    data= "sadas"
    rawData=bytes(data,'ascii')
    print(rawData)
    rawData=bytes("\x68\x65\x6c\x6c",'ascii')
    print(rawData)
    
    mutable_bytes=bytearray(b"\x68\x65\x6c\x6c\x6f")
    mutable_bytes.append(65)
    print(mutable_bytes)









if __name__ == "__main__":
    main()
  