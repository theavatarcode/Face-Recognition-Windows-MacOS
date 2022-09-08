import shutil as s
from tkinter import image_types
import PySimpleGUI as sg
import os
import faceAddtoExel
import cv2
from cv2 import VideoCapture
import webbrowser as wb

sg.theme('LightGrey1')
font = ("Verdana", 14)
layout = [  [sg.Text('Add images to system. File must be only .JPG',font= font), sg.Button('Capture from Webcam',font=font)],
            [sg.Text('Path of Images',font=font), sg.InputText(key='-in-', do_not_clear=False,font=font), sg.FileBrowse(file_types= (("image","*.JPG*"),),font=font), sg.Button('Open',font=font),sg.Button('Delete',font=font)],
            [sg.Text('Name',font=font),sg.InputText(key = '-name-',size=(20,1), do_not_clear= False,font=font), sg.Text('Student-ID',font=font), sg.InputText(key='-StudentID-',size= (7,1), do_not_clear= False,font=font), sg.Text('Class-ID',font=font), sg.InputText(key='-id-',size= (3,1), do_not_clear= False,font=font), sg.Text('Classroom (Ex. 6-3, 6-2, 6-1)',font=font), sg.InputText(key='-class-',size=(5,1),do_not_clear= False,font=font)],
            [sg.Text('Register face to system.',font=font),sg.Button('Upload',font=font)],
            [sg.VerticalSeparator(color=(0,0,0))],
            [sg.HorizontalSeparator(color=(0,0,0))],
            [sg.VerticalSeparator(color=(0,0,0))],
            [sg.StatusBar('Warming : Start Face-Recognition will start Excel attendance list too. ',key='-l-'),sg.Button('Start Face-Recognition',font=font), sg.Button('Cancel',font=font)],
            [sg.Text('Attendances list have save in Excel, You can open files here',font=font), sg.Button('OpenFolderExcel',font=font),sg.StatusBar('Support : Window7 64-bit, Window10 64-bit, MacOS')]]
icon = os.path.realpath('icon/ip-camera.ico')
excel = 'ExcelData' ## Path Fix!!!!
real_path_excelData = os.path.realpath(excel)
image_folder = os.path.realpath('images')


window = sg.Window('Face-Recogintion by M6/3', layout, icon= icon)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break

    if event == 'Upload':
        name = str(values['-name-'])
        if len(str(values['-id-'])) == 1:
            id = '0'+str(values['-id-'])
        else:
            id = str(values['-id-'])
        classes = str(values['-class-'])
        stdId = str(values['-StudentID-'])
        old_name = values['-in-']
        try:
            
            locate_of_image = f"{image_folder}/{stdId}_{classes}_{id}_{name}.jpg" ## Path Fix!!!
            s.move(old_name, locate_of_image)
            sg.popup(f'image uploaded! move to {locate_of_image}')
        except:
            sg.popup('Error : None image or None info!, Path failed!')
    
    if event == 'Start Face-Recognition':
        sg.popup('Wait for endcoding images....')
        try:
            faceAddtoExel.start()
        except:
            sg.popup('Error to Run!')
    if event == 'OpenFolderExcel':
        os.system(f'start {os.path.realpath(real_path_excelData)}')

    if event == 'Capture from Webcam':
    # capture('name', 'id', 'class')     #return class_id_name.JPG
    # path_file = '//Users//admin//Desktop//face req//class_id_name.JPG'
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('Press Spacebar to capture/ESC to quit', frame)
            k = cv2.waitKey(1)
            if k%256==27:
                break
            elif k%256 ==32:
                img_name = 'class_id_name.jpg'
                cv2.imwrite(img_name, frame)

                # path_file = f'C:/Users/PC/Desktop/face_rq/FaceRecognition/{img_name}'
                real_path_file_capture_image = os.path.realpath(img_name)
                window.FindElement('-in-').update(real_path_file_capture_image)
                values['-in-'] = real_path_file_capture_image
                break            
        cap.release()
        cv2.destroyAllWindows()
    
    if event =='Open':
        
        os.system(f'start {os.path.realpath(image_folder)}')
        
    if event == 'Delete':
        os.remove(values['-in-'])
        window.find_element('-in-').update('')






window.close()
