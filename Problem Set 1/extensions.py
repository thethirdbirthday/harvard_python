#ask for file name
#Remove spaces and make input lowercase
#replace file extension with MIME type
#image application text octet

file = input("What is the file name? ").lower.strip()
#true_file = file.lower() condensed to one line
if 'gif' in true_file:
    print("image.gif")
elif 'jpg' or 'jpeg' in true_file:
    print(image/jpeg)
elif 'png' in true_file:
    print("image/png")
elif 'pdf' in true_file:
    print("application/pdf")
elif 'txt' in true_file:
    print("txt/plain")
elif 'zip' in true_file:
    print("application/zip")
else:
    print("application/octet-stream")
