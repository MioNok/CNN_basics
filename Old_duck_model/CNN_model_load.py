#You can use you own image on my model and try it out, donwload the model from the repo "Duck_Sign_model".
#The model takes in only 100x100 images.


from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np
from keras.models import load_model
#Import image
img1 = Image.open('Duck.jpg').convert('L')

#Show image
plt.imshow(img1)

#Reshape the image to the correct format
img_array  = np.array(img1)
img_flat = (img_array/255.0)


#Final shape of the Image should be (1,100,100,1)
x_train_img = img_flat.reshape(1, 100, 100,1)

#Import my model
model = load_model("Duck_Sign_Model")

#Use your own image!
res = model.predict_classes(x_train_img)
res_precentage = model.predict(x_train_img)

if res == 0:
    print("Model predicted that you picture contains a rubber duck with a confidence of ",res_precentage.flat[0]*100,"%")
else:
    print("Model predicted that you picture contains a stop sign with a confidence of ",res_precentage.flat[1]*100,"%")
