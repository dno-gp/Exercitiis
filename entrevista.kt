fun main(){

    /* Entrevista */

 fun entrevista(){

        println("Qual o seu nome?")
        var nome = readLine()

        println("Qual a sua idade?")
        var idade: Int = readLine()!!.toInt()

        println("Qual a sua nacionalidade?")
        var natural = readLine()

        println("Qual o seu estado civil?")
        var estadocivil = readLine()

        println("Informe a sua profissão.")
        var prof = readLine()

        println("Qualificação: $nome, $idade anos, $natural, $estadocivil, $prof.")
    }

    entrevista()
}