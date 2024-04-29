import java.util.Scanner;

public class CalculateRank {

    public static String calculaNivelRanked(int vitorias, int derrotas){
/*        """
    Calcula o nível rankeado do jogador com base em suas vitórias e derrotas.

    @param vitorias: Número de vitórias do jogador.
    @param derrotas: Número de derrotas do jogador.

    @return: Uma string com a mensagem informando o saldo de vitórias e o nível rankeado.
    """*/

        int saldoVitorias = vitorias - derrotas;
        String nivel;

        if (saldoVitorias < 10) {
            nivel = "Ferro";
        } else if (saldoVitorias < 21) {
            nivel = "Bronze";
        } else if (saldoVitorias < 51) {
            nivel = "Prata";
        } else if (saldoVitorias < 81) {
            nivel = "Ouro";
        } else if (saldoVitorias < 91) {
            nivel = "Diamante";
        } else if (saldoVitorias <= 100) {
            nivel = "Lendário";
        } else {
            nivel = "Imortal";
        }

        return String.format("O Herói tem um saldo de %d vitórias e está no nível %s.", saldoVitorias, nivel);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número de vitórias do jogador: ");
        int vitoriasJogador = scanner.nextInt();

        System.out.print("Digite o número de derrotas do jogador: ");
        int derrotasJogador = scanner.nextInt();

        String nivelRankeado = calculaNivelRanked(vitoriasJogador, derrotasJogador);
        System.out.println(nivelRankeado);

        scanner.close();
    }
}