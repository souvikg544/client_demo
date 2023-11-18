## Description

1. Create a web server with a `/start` endpoint (you can use any library you want).
   1. It only responds to a POST request.
   2. When it receives the parameter `rtsp_url`, start a new process.
2. The new process reads the video stream from `rtsp_url` using `opencv`.
3. Add a `/stop` endpoint.
   1. Save an image with size 900x900 of the top 9 brightest frames from the video in a grid.
   2. Stop the video reading process.
   3. Display the image in the HTML response.
4. Save this image and send it on the Upwork chat.

Notes:
- Your solution will be judged based on readability, correctness and documentation.
- This task should not take more than 1-2 hours.
- Do NOT post your answer on a public URL.

## Submission

- Create a zip file exercise.zip
- After it's unzipped, it should contain the project source code.
- The program MUST run inside Docker. We will run your script using the following command:

