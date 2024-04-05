

from pytesseract import image_to_string 
import pytesseract
from PIL import  Image
import  cv2
import  numpy as np

def texts(img):
	text = pytesseract.image_to_string(img)

	return text



# url = 'https://192.168.43.1:8080/video'
# cam = cv2.VideoCapture(url)
# cam = cv2.VideoCapture('ocr.mp4')

file = open('result.text', 'w')
file.write('')
file.close()

while True:
	# __,img = cam.read()
	img = cv2.imread('love.png')
	text = texts(img) 
	new = text.split('\n', 1)[-1]

	blank_img = np.zeros([500, 500, 3], dtype=np.uint8)	
	cv2.putText(blank_img, text, (20,100), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,200,255), 2)
	cv2.imshow('img',img)
	cv2.imshow('Text Image',blank_img)
	key  = cv2.waitKey(1) & 0xFF
	if key == ord('s'):
		file_app = open('result.text','a')
		file_app.write(text)
		file_app.close()
	elif key == ord('q'):
		break

				
print('print successful')


# cam.release()
cv2.destroyAllWindows()




# Import the required module for text 
# to speech conversion 
from gtts import gTTS 
import os 
 
file = open('result.text', 'r')
text = file.read()
mytext = text

 
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("welcome.mp3") 


