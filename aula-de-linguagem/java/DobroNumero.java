import java.util.Scanner; // importa a classe Scanner para ler os dados

public class DobroNumero {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); // cria o leitor de dados

        System.out.println("Digite um número inteiro: ");
        int numero = in.nextInt(); // lê o número digitado pelo usuário

        int dobro = numero * 2; // calcula o dobro do valor

        System.out.println("O dobro de " + numero + " é: " + dobro); // exibe o resultado do calculo

        in.close(); // fecha o leitor de dados
    }
}