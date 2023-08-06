import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from PIL import Image
import matplotlib.pyplot as plt
def akame():
    img = Image.open('/usr/local/lib/python3.8/dist-packages/Econometric/akamegakill_4.jpg')
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    ax.imshow(img)

    plt.show()
akame()