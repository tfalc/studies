// Desafios JavaScript na DIO têm funções "gets" e "print" acessíveis globalmente:
//- "gets" : lê UMA linha com dado(s) de entrada (inputs) do usuário;
//- "print" : imprime um texto de saída (output), pulando linha.

const entrada = gets();
const votos = entrada.split(' ');

const contagemVotos = {};

// Usamos o metodo JavaScript forEach que executa uma função de retorno de chamada para cada elemento da lista para iterar sobre a lista de votos e conta quantos votos cada mapa recebeu.
votos.forEach(voto => {
    contagemVotos[voto] = (contagemVotos[voto] || 0) + 1;
});

let mapaVencedor;
let maxVotos = 0;

// TODO: Itere sobre cada mapa na contagem de votos para encontrar o vencedor
for(const mapa in contagemVotos){
  const votosMapa = contagemVotos[mapa]; //A B C B A B A A = A - 4, B - 3, C - 1. 
  //contagemVotos[0] = 4
  //contagemVotos[1] = 3
  //contagemVotos[2] = 1
  if (votosMapa > maxVotos) {
    mapaVencedor = mapa;
    maxVotos = votosMapa;
  }
}

print(mapaVencedor);

