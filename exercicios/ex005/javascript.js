// script.js
document.addEventListener('DOMContentLoaded', () => {
  const botao = document.getElementById('saudacao-btn');

  if (botao) {
    botao.addEventListener('click', () => {
      const hora = new Date().getHours();
      let mensagem;

      if (hora < 12) {
        mensagem = "Bom dia! Seja bem-vindo ao meu portfólio.";
      } else if (hora < 18) {
        mensagem = "Boa tarde! Aproveite para conhecer meus projetos.";
      } else {
        mensagem = "Boa noite! Obrigado por visitar meu portfólio.";
      }

      alert(mensagem);
    });
  } else {
    console.error("Botão de saudação não encontrado.");
  }
});
