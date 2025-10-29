import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
'''
# we are doing numerical mapping to reduce strain
0 - ben afflek
1 - elton john
etc
'''

#windows_DIR =  os.listdir()
#mac_DIR = os.listdir('C: etc.../Faces/train')
mac_DIR = r'Faces/train'
print(f'DIR: {mac_DIR}')


#training set: features & labels - this is supervised learning
features = []   #images of faces
labels = []     #ground-truths
haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    '''
    will loop every folder in faces
    then loop over every image in person_folder
    then take each image and add it to the training set
    '''
    for person in people:       #loop every person folder in faces
        path = os.path.join(mac_DIR, person)
        label = people.index(person)        
        print(path,label)   
        
        for img in os.listdir(path):        #loop every image in person folder
            img_path = os.path.join(path, img)
            #print(img_path)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)   #recycled from face_detect.py

            '''
            before adding to training set, we want to lighten the load by cropping out the face
            so we draw a rect around what haar_cascade considers a face, 
            but in practicality, verify if it crops all faces properly, i'm assuming the tutorial picked images and scaleFactor/minNeighbor values that work
            '''
            for (x,y,w,h) in faces_rect:        #we are cropping out the face in the image, don't draw a rect
                faces_region_of_interest = gray[y:y+h, x:x+w]   
                features.append(faces_region_of_interest)
                labels.append(label)
                
                #cv.imshow('detected faces') - for practicality would be necessary to verify

create_train()
print(f'length of features list: {len(features)}')
print(f'length of labels list: {len(labels)}')
print("---Training Done---")

#before training, we want to convert these to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

#use a built in opencv trainer?
face_recognizer = cv.face.LBPHFaceRecognizer_create() #contrib package exclusive

#Train the recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yaml') #yaml - human-readable data serialization language
np.save('features.npy',features)
np.save('labels.npy', labels)