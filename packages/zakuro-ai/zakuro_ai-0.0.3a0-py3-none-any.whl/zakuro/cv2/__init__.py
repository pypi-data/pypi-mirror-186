import cv2
import pickle
import hashlib
import numpy as np
def main(str, img):
    print(str + " from main@zakuro.cv2")
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # cv2.imshow("", gray)
    # cv2.waitKey(1)
    return True

# if __name__ == "__main__":
#     path = "/home/jcadic/Downloads/x2bc6a65bb48ed4b117e1cb6e5bab1dfe"
#     img = cv2.imread("/mnt/.cpj/ZAK/zak-python/lena.png")
#     pickle.dump(img, open(path, "wb"))
#     content = pickle.load(open(path, "rb"))
#     a=1
#     # img = pickle.dumps(img)
#     # fingerprint = hashlib.md5(img).hexdigest()
#     # path = f"/tmp/x{fingerprint}"
#     # print(path)
#     # pickle.dump(img, open(path, "wb"))
#     #
#     # main("hello world", pickle.load(open(path, "rb")))
#
#
#     img = list(img)
#     main("hello world", np.array(img))
