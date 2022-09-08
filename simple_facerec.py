import face_recognition
import cv2
import os
import glob
import numpy as np


class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []  
        self.frame_resizing = 0.25
    def load_encoding_images(self, images_path):
        
        images_path = glob.glob(os.path.join(images_path, "*.*"))
        print("{} encoding images found.".format(len(images_path)))
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)     
            try:
                img_encoding = face_recognition.face_encodings(rgb_img)[0]    
            except:
                print('pls capture with more clear images.')
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
        print("Encoding images loaded")

    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_percent_value = 0
        percent = 0
        face_names = []
        for face_encoding in face_encodings:           
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            face_percent_value = (1-face_distances[best_match_index])*100
            percent = round(face_percent_value,2)
            
            if matches[best_match_index] and percent >=50 :
                name = self.known_face_names[best_match_index]
            else:
                name = 'Unknown'
                
            face_names.append(name)
            
        face_locations = np.array(face_locations)
        face_locations = face_locations / self.frame_resizing
        return face_locations.astype(int), face_names, percent

    def getClassesFrom(self, name):
        classes = str(name[5:8])
        return classes
    
    def getNumberFrom(self, n):
        number = str(n[9:11])
        return number
    
    def getNameFrom(self, n):
        onlyName = str(n[12:])
        return onlyName
    
    def getStudentIdFrom(self, n):
        studentid = str(n[0:4])
        return studentid


