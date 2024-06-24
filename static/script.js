document.getElementById('startBtn').addEventListener('click', () => {
    fetch('/start_tracking')
        .then(response => response.json())
        .then(data => console.log(data));
});

document.getElementById('stopBtn').addEventListener('click', () => {
    fetch('/stop_tracking')
        .then(response => response.json())
        .then(data => console.log(data));
});

document.getElementById('configForm').addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(event.target);
    const config = {
        pinch: formData.get('pinch'),
        double_pinch: formData.get('double_pinch')
    };
    fetch('/config', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(config)
    })
    .then(response => response.json())
    .then(data => console.log(data));
});
