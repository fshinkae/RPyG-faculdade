let playerHealth = 100;
let enemyHealth = 100;

document.getElementById('attackButton').addEventListener('click', () => {
  let playerDamage = Math.floor(Math.random() * 20) + 10; // Dano do jogador
  let enemyDamage = Math.floor(Math.random() * 15) + 5; // Dano do inimigo

  playerHealth -= enemyDamage;
  enemyHealth -= playerDamage;

  // Atualiza a saúde na tela
  document.getElementById('playerHealth').textContent = playerHealth;
  document.getElementById('enemyHealth').textContent = enemyHealth;

  // Verifica se alguém venceu
  let result = document.getElementById('result');
  if (playerHealth <= 0 && enemyHealth <= 0) {
    result.textContent = "Empate! Ambos caíram em combate.";
  } else if (playerHealth <= 0) {
    result.textContent = "Você perdeu! O inimigo venceu.";
  } else if (enemyHealth <= 0) {
    result.textContent = "Você venceu! O inimigo foi derrotado.";
  } else {
    result.textContent = `Você causou ${playerDamage} de dano! O inimigo causou ${enemyDamage} de dano.`;
  }
});
