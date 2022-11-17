import csv 
import xml.etree.cElementTree as et
import os 

def get_files():
    files = []
    di = "OperaBase"
    for file in os.listdir(di):
        files.append(file)

    return files


def email_ext(files):

    emails = []
    di = "OperaBase"

    for file in files:
        tree = et.parse(f"{di}/{file}")
        root = tree.getroot()
        print(file)
        for item in root.iter("email"):
            if not item.text.strip() in emails: 
                emails.append(item.text.strip())

    # print(emails)
    with open("email.csv", "w") as file:

        writer = csv.DictWriter(file, fieldnames=["email"])
        for email in emails:  
            writer.writerow({"email": email})


if __name__=="__main__":
    email_ext(get_files())
  