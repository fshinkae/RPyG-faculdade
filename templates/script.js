let playerName = '';

        function confirmName() {
            playerName = document.getElementById('playerName').value;
            document.getElementById('chooseClass').style.display = 'block'; 
            document.getElementById('intro').style.display = 'none';
        }

        function showCharacterSheet(characterClass, image, attack, defense, magic) {
            document.getElementById('characterName').innerText = playerName;
            document.getElementById('characterClass').innerText = characterClass;
            document.getElementById('characterImage').src = image;
            document.getElementById('attackValue').innerText = attack;
            document.getElementById('defenseValue').innerText = defense;
            document.getElementById('magicValue').innerText = magic;
            document.getElementById('chooseClass').style.display = 'none';
            document.getElementById('characterSheet').style.display = 'block';
}