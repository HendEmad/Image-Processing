# Boundary Box dimensions: (x, y, width, height)
import cv2

cap = cv2.VideoCapture(0)
tracker = cv2.legacy.TrackerMOSSE_create()
# tracker = cv2.legacy.TrackerCSRT_create()  # A bit slower than MOSSE, but more accurate
# Initialize a frame from the webcam
success, img = cap.read()
# Then, we will drag a bounding box around an image
bbox = cv2.selectROI("Tracking", img, False)
# Initialize the tracker using the boundary box
tracker.init(img, bbox)


# Function to draw the boundary box
def drawBox(img, bbox):
    # Get dimensions of the boundary box form the tuple of bbox
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    # Create the bounding box
    cv2.rectangle(img, (x, y), ((x+w), (y+h)), (255, 0, 255), 3, 1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)  # Display the fps

    pass


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    # Update the tracker value
    success, bbox = tracker.update(img)
    print(type(bbox))  # The boundary box is not a list, it is a tuple
    # If it can update the tracker, so it is still working, which means drawing the box
    if success:
        drawBox(img, bbox)
    else:
        cv2.putText(img, "Lost!", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  # Display the fps

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)  # Frequency per second
    cv2.putText(img, str(int(fps)), (75, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  # Display the fps

    cv2.imshow("Tracking", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
