import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

public class HeroChallenge {

    private String defineRank(int heroExp, String nome) {
        Map<Integer, String> ranks = new TreeMap<>();

        ranks.put(1000, "Ferro");
        ranks.put(2000, "Bronze");
        ranks.put(5000, "Prata");
        ranks.put(7000, "Ouro");
        ranks.put(8000, "Platina");
        ranks.put(9000, "Ascendente");
        ranks.put(10000, "Imortal");

        String level =  ranks.entrySet().stream()
                .filter(xp -> heroExp <= xp.getKey())
                .map(Map.Entry::getValue)
                .findFirst()
                .orElse("Radiante");

        return "O Herói de nome " + nome + " está no nível de " + level;
    }

    public static void main(String[] args) {

        String nome;
        int exp;

        HeroChallenge heroChallenge = new HeroChallenge();
        Scanner sc = new Scanner(System.in);

        System.out.println("Digite o nome do herói: ");
        nome = sc.next();
        System.out.println("Digite a quantidade de exp atual: ");
        exp = sc.nextInt();

        sc.close();
        System.out.println(heroChallenge.defineRank(exp, nome));
    }
}
