const secretNumber = Math.floor(Math.random() * 20) + 1;
let lives = 3;

document.getElementById('submit').addEventListener('click', () => {
  const userGuess = parseInt(document.getElementById('guess').value, 10);
  const result = document.getElementById('result');
  const livesCount = document.getElementById('lives-count');

  if (!userGuess || userGuess < 1 || userGuess > 20) {
    result.textContent = 'Por favor, digite um número entre 1 e 20!';
    result.style.color = 'orange';
    return;
  }

  if (userGuess === secretNumber) {
    result.textContent = 'Parabéns! Você acertou o número!';
    result.style.color = 'green';
    document.getElementById('submit').disabled = true;
  } else {
    lives -= 1;
    livesCount.textContent = lives;

    if (lives > 0) {
      result.textContent = 'Errou! Tente novamente.';
      result.style.color = 'red';
    } else {
      result.textContent = `Você perdeu! O número era ${secretNumber}.`;
      result.style.color = 'black';
      document.getElementById('submit').disabled = true;
    }
  }
});
