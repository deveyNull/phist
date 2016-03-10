import image_scraper
from hashFunk import *
from phash import *

hashem = 0
dirToHash = "Test"
flatDbName = "hashes.txt"
omaraxDirectory = "Screenshots"
domainFile = "domain.txt"


def showImage(img):
    Image.open(img).show()  # WTFFFFF ( A month later, not sure what this meant)
    print(img)


if hashem == 1:
    newFile(dirToHash, flatDbName)

else:
    flatFileLoad("hashes.txt")
    os.system("python omarax_local.py -f " + domainFile)

    # PULL OUT ALL IMAGES
    print("Omarax Complete")
    with open(domainFile, 'r') as f:
        domains = f.readlines()

        for name in domains:
            print(name)
            os.system("image-scraper " + name.strip() + " >/dev/null 2>&1")

            domainDirectory = "images_" + name.strip()

            a = cDirectory(domainDirectory, flatDbName)
            print(a)
        # return(hester)

        a = checkImage(omaraxDirectory + "/" + name.replace("/", "-").strip() + ".png", flatDbName)
        if a:
            print(name + str(a))

        # return(hester)
