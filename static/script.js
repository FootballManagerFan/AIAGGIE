document.getElementById('dreamHomeForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    let description = document.getElementById('description').value;
    
    if (!description) {
        alert('Please enter a description.');
        return;
    }
    
    try {
        let response = await fetch('/generate', {  // 🔥 Make sure this matches Flask's endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ description: description })
        });

        let result = await response.json();

        if (result.generated_image) {
            let outputImage = document.getElementById('generatedImage');
            outputImage.src = result.generated_image;
            outputImage.style.display = 'block';
        } else {
            alert('Error: ' + (result.error || 'Unknown error occurred'));
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to generate image. Please try again.');
    }
});
