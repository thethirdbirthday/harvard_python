#ask for file name
#Remove spaces and make input lowercase
#replace file extension with MIME type
#image application text octet

file = input("What is the file name? ").lower().strip()

if 'gif' in file:
    print("image.gif")
elif 'jpg'in file:
    print("image/jpeg")
elif 'jpeg' in file:
    print("image/jpeg")
elif 'png' in file:
    print("image/png")
elif 'pdf' in file:
    print("application/pdf")
elif 'txt' in file:
    print("txt/plain")
elif 'zip' in file:
    print("application/zip")
else: 
  print("application/octet-stream")
