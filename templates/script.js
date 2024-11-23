document.getElementById('characterForm').addEventListener('submit', function(event) {
    event.preventDefault();
    submitCharacterForm();
});

function submitCharacterForm() {
    const name = document.getElementById('playerName').value;
    const raceId = document.getElementById('race').value;
    const vocationId = document.getElementById('vocation').value;

    const characterData = {
        name: name,
        race_id: parseInt(raceId),
        vocation_id: parseInt(vocationId)
    };

    fetch('http://127.0.0.1:5000/character', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(characterData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        localStorage.setItem('characterId', data.id);
        window.location.href = 'information';
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}