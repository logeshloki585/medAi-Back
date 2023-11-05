import os
import base64
import face_recognition

def recognize_person_base64(base64_image, db_directory):
    image_data = base64.b64decode(base64_image.split(',')[1])
    input_image_path = 'input_image.jpg' 
    with open(input_image_path, 'wb') as f:
        f.write(image_data)

    input_image = face_recognition.load_image_file(input_image_path)
    input_face_encoding = face_recognition.face_encodings(input_image)

    if not input_face_encoding:
        return "No face found in the input image"

    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(db_directory):
        if filename.endswith(".jpg"):
            name = os.path.splitext(filename)[0]
            image_path = os.path.join(db_directory, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(name)
    results = face_recognition.compare_faces(known_face_encodings, input_face_encoding[0])

    if True in results:
        return known_face_names[results.index(True)]
    else:
        return "The person is not registered"