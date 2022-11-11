import face_recognition
from PIL import Image, ImageDraw
image_of_modi = face_recognition.load_image_file('./Images/known/modi.jpg')
modi_face_encoding = face_recognition.face_encodings(image_of_modi)[0]
image_of_yogi_Adityanath =
face_recognition.load_image_file('./Images/Known/Yogi_Adityanath.jpg')
yogi_face_encoding =
face_recognition.face_encodings(image_of_yogi_Adityanath)[0]
image_of_Trump =
face_recognition.load_image_file('./Images/known/Donald_Trump.jpg')
Trump_face_encoding = face_recognition.face_encodings(image_of_Trump)[0]
known_face_encodings = [
modi_face_encoding,
yogi_face_encoding,
Trump_face_encoding
]
known_face_names = [
"modi",
"yogi",
"Trump"
]
test_image =
face_recognition.load_image_file('./Images/Unknown/yogi_modi.jpg')
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)
pil_image = Image.fromarray(test_image)
draw = ImageDraw.Draw(pil_image)
for(top, right, bottom, left), face_encoding in zip(face_locations,
face_encodings):
matches = face_recognition.compare_faces(
known_face_encodings, face_encoding)
name = "Unknown"
if True in matches:
first_match_index = matches.index(True)
name = known_face_names[first_match_index]
draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0))
text_width, text_height = draw.textsize(name)
draw.rectangle(((left, bottom - text_height - 10), (right, bottom)),
fill=(255, 255, 0), outline=(350, 255, 0))
draw.text((left + 6, bottom - text_height - 5), name, fill=(0, 0, 0))
del draw
pil_image.show()
# Save image
# pil_image.save('identify.jpg')
