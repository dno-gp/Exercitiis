fun main() {

    /*Cálculo Fatorial*/

    fun fatorial(fator: Int) {

        var i = fator - 1
        var result = fator

        while (i >= 2) {
            result *= i
            i--
        }
        print("O resultado de $fator! é igual a $result.")
    }
fatorial(3)
}
