let playerName = '';
let characterClass = '';
let characterRace = '';
let characterImage = '';
let attack = 0;
let defense = 0;
let magic = 0;

function confirmName() {
    playerName = document.getElementById('playerName').value;
    document.getElementById('chooseClass').style.display = 'block'; 
    document.getElementById('intro').style.display = 'none';
}

function chooseClass(selectedClass, image, attackValue, defenseValue, magicValue) {
    characterClass = selectedClass;
    characterImage = image;
    attack = attackValue;
    defense = defenseValue;
    magic = magicValue;
    document.getElementById('chooseClass').style.display = 'none';
    document.getElementById('chooseRace').style.display = 'block';
}

function showCharacterSheet(race) {
    characterRace = race;

    document.getElementById('characterName').innerText = playerName;
    document.getElementById('classValue').innerText = characterClass;
    document.getElementById('raceValue').innerText = characterRace;
    document.getElementById('characterImage').src = characterImage;
    document.getElementById('attackValue').innerText = attack;
    document.getElementById('defenseValue').innerText = defense;
    document.getElementById('magicValue').innerText = magic;

    document.getElementById('chooseRace').style.display = 'none';
    document.getElementById('characterSheet').style.display = 'block';
}

function startAdventure() {
  const randomChallenge = Math.floor(Math.random() * 2); 
  if (randomChallenge === 0) {
    window.location.href = "chests_adventure.html"; 
  } else {
    window.location.href = "monster_adventure.html"; 
  }
}