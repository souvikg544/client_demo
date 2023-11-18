import cv2

# # RTSP URL of the video stream
# rtsp_url = 'rtsp://platerec:8S5AZ7YasGc3m4@video.platerecognizer.com:8554/demo'

# # Open the RTSP stream
# cap = cv2.VideoCapture(rtsp_url)

# # Check if the RTSP stream opened successfully
# if not cap.isOpened():
#     print("Error: Could not open RTSP stream.")
# else:
#     # Read and display frames from the RTSP stream
#     while True:
#         # Read a frame from the RTSP stream
#         ret, frame = cap.read()

#         # Check if the frame was read successfully
#         if not ret:
#             print("Error: Could not read frame.")
#             break

#         # Display the frame
#         cv2.imshow('RTSP Stream', frame)

#         # Break the loop if 'q' key is pressed
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             break

#     # Release the RTSP stream capture object and close the window
#     cap.release()
#     cv2.destroyAllWindows()

print(cv2.getBuildInformation())
