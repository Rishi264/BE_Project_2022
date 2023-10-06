#!/usr/bin/env python
# coding: utf-8

# In[16]:


from PIL import Image
import glob


# In[17]:


#img_path="C:\Users\asus\Documents\images\1000-receipt.jpg"

im=Image.open("C:/Users/asus/Documents/images/1000-receipt.jpg")
print('{}'.format(im.format))
print('size:{}'.format(im.size))
print('image mode: {}'.format(im.mode))
im.show()


# In[18]:


image_list=[]
resized_images=[]


# In[19]:


for filename in glob.glob('C:/Users/asus/Documents/images/*.jpg'):
    print(filename)
    img=Image.open(filename)
    image_list.append(img)


# In[20]:


image_list


# In[21]:


for image in image_list:
    image=image.resize((250,250))
    resized_images.append(image)


# In[22]:


resized_images


# In[24]:


for (i,new) in enumerate(resized_images):
    new.save('{}{}{}'.format('C:/Users/asus/Documents/images2/images',i+1,'.jpg'))


# In[ ]:


from PIL import Image
import glob
im=Image.open("C:/Users/asus/Documents/images/1000-receipt.jpg")
print('{}'.format(im.format))
print('size:{}'.format(im.size))
print('image mode: {}'.format(im.mode))
im.show()

image_list=[]
resized_images=[]

for filename in glob.glob('C:/Users/asus/Documents/images/*.jpg'):
    print(filename)
    img=Image.open(filename)
    image_list.append(img)
for image in image_list:
    image=image.resize((600,600))
    resized_images.append(image)
    
for (i,new) in enumerate(resized_images):
    new.save('{}{}{}'.format('C:/Users/asus/Documents/images2/images',i+1,'.jpg'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




