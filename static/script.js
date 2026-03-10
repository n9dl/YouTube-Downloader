document.getElementById('downloadForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const urlInput = document.getElementById('videoUrl').value;
    const qualityInput = document.getElementById('videoQuality').value;
    const submitBtn = document.getElementById('submitBtn');
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');
    const titleElement = document.getElementById('videoTitle');
    const downloadLink = document.getElementById('downloadLink');

    submitBtn.disabled = true;
    submitBtn.style.opacity = '0.5';
    resultDiv.style.display = 'none';
    loadingDiv.style.display = 'block';

    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({
                'video_url': urlInput,
                'quality': qualityInput
            })
        });

        const data = await response.json();

        if (data.error) {
            alert('Error: ' + data.error);
        } else {
            titleElement.textContent = data.title;
            downloadLink.href = '/serve/' + encodeURIComponent(data.filename);
            resultDiv.style.display = 'block';
        }
    } catch (error) {
        alert('Server error. Please try again.');
    } finally {
        submitBtn.disabled = false;
        submitBtn.style.opacity = '1';
        loadingDiv.style.display = 'none';
    }
});