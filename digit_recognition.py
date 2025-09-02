# Import libraries
import cv2
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# Step 1: Load and train SVM on digits dataset
digits = load_digits()
X = digits.data
y = digits.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

svm_model = SVC(kernel='rbf', gamma='scale', C=10)
svm_model.fit(X_train, y_train)

# Step 2: Load your image
img_path = "images.jpeg"  # replace with your image path
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Step 3: Preprocess image
# Resize to 8x8 (same as sklearn digits dataset)
img_resized = cv2.resize(img, (8, 8), interpolation=cv2.INTER_AREA)

# Invert colors if necessary (MNIST style: white digit on black background)
if np.mean(img_resized) > 128:
    img_resized = 255 - img_resized

# Flatten and scale the image like the training data
img_flatten = img_resized.flatten()
img_scaled = scaler.transform([img_flatten])

# Step 4: Predict digit
predicted_digit = svm_model.predict(img_scaled)
print(f"Predicted Digit: {predicted_digit[0]}")

# Optional: Show the image
cv2.imshow("Digit", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
