import qrcode 
text = input ("Enter text that could be inside qr : ")
filename = input ("Enter the file name where qr will be saved in : ") 

def qrcode_generator (text , filename) :
  qr_code = qrcode.make (text)
  qr_code.save(filename)

qrcode_generator(text , filename)