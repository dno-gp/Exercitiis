/* Classificação de triângulos segundo seus lados. */

fun main() {

    fun tri(a: Int, b: Int, c: Int) {

        println("CLASSIFICAÇÃO DO TRIÂNGULO")
        println("Primeiro lado: $a. Segundo lado: $b. Terceiro lado: $c")

        if ((a - b < c && a + b > c) && (a - c < b && a + c > b)) {
            println("O os lados informados atendem as condições de existência.")

            if (a == b && b == c) {
                print("Classificação: Equilátero.")

            } else if ((a == b && b != c) || (a == c && c != b)) {
                print("Classificação: Isóceles.")

            } else if (a != b && b != c) {
                println("Classificação: Escaleno.")
            }
        }else {
            print("Os lados informados NÂO atendem as condições de existência de um triângulo.")
        }
    }
    tri(2,3,6) //Usa função.
}