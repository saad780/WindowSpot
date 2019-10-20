import os
from PIL import Image

PATH = os.getenv('LOCALAPPDATA') + '\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
SP = os.getenv('USERPROFILE') + '\Pictures\Spotlight'

if not os.path.exists(SP):
    os.makedirs(SP)

for root, dirs, files in os.walk(PATH):
    for name in files:
        filePath = os.path.join(root, name)
        try: img = Image.open(filePath)
        except IOError: continue
        if img.width >= 1920:
            img.save(SP + f'\\{name}.jpg')

os.startfile(SP)