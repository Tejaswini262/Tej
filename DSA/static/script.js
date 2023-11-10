document.getElementById('startCamera').addEventListener('click', function () {
    const videoElement = document.getElementById('cameraFeed');
    const capturedImage = document.getElementById('capturedImage');
    const captureButton = document.getElementById('captureImage');

    navigator.mediaDevices
        .getUserMedia({ video: true })
        .then(function (stream) {
            videoElement.srcObject = stream;
            videoElement.classList.remove('hidden');
            videoElement.play();

            // Wait for the camera stream to load
            videoElement.onloadedmetadata = () => {
                captureButton.classList.remove('hidden');
                captureButton.addEventListener('click', function () {
                    // Capture a frame from the video stream and display it as an image
                    const canvas = document.createElement('canvas');
                    canvas.width = videoElement.videoWidth;
                    canvas.height = videoElement.videoHeight;
                    canvas.getContext('2d').drawImage(videoElement, 0, 0, canvas.width, canvas.height);
                    capturedImage.src = canvas.toDataURL('image/jpeg');
                    capturedImage.classList.remove('hidden');

                    // Stop the camera stream
                    stream.getTracks().forEach((track) => track.stop());
                });
            };
        })
        .catch(function (error) {
            console.error('Error accessing the camera:', error);
        });
});
