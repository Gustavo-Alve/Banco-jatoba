const fmr = document.querySelector("form");
const nome = document.getElementById("nome");
const descricao = document.getElementById("descricao");

fmr.addEventListener("submit", function (e) {
  e.preventDefault();

  const jsonData = {
    nome: nome.value,
    descricao: descricao.value
  };

  fetch("http://localhost:5000/api/fabricantes", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(jsonData)  // ✅ Aqui estava faltando
  })
    .then(res => res.json())
    .then(data => {
      console.log("Servidor respondeu:", data);
    })
    .catch(err => {
      console.error("Erro ao enviar:", err);
    });
});
