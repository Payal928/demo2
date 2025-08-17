Face, Eye & Smile Detection using OpenCV

This project demonstrates real-time Face, Eye, and Smile Detection using OpenCV and the Haar Cascade Classifier. The application uses your webcam to detect faces and then applies additional models to detect eyes and smiles within the detected faces.

✨ Built with simplicity in mind, this project is great for anyone exploring computer vision basics and OpenCV’s powerful pre-trained models.

📌 Features

✅ Real-time face detection using webcam.
✅ Eye detection inside detected faces.
✅ Smile detection inside detected faces.
✅ Uses Haar Cascade Classifiers – lightweight, fast, and effective.
✅ Beginner-friendly code with comments.

📂 What are Haar Cascades?

Haar Cascades are pre-trained XML classifiers available in OpenCV. They work like filters that scan an image and detect specific objects based on trained patterns.
Some common cascades include:
haarcascade_frontalface_default.xml → Detects faces.
haarcascade_eye.xml → Detects eyes.
haarcascade_smile.xml → Detects smiles.
OpenCV provides these cascades in its data directory, and they are trained on thousands of positive and negative images.

📖 How It Works

Load the Haar Cascade files (haarcascade_frontalface_default.xml, haarcascade_eye.xml, haarcascade_smile.xml).
Start the webcam feed (cv2.VideoCapture(0)).
Convert each frame to grayscale for faster detection.
Apply the cascades:
Detect faces → draw rectangles around them.
Inside each face, detect eyes and smiles.
Display the results in real-time.

🎯 Use Cases
Basic computer vision learning project.
Build a smile-triggered camera app 📸.
Step towards attendance systems, emotion recognition, and surveillance.

🙌 Acknowledgements

OpenCV
Pre-trained Haar Cascade models from OpenCV
