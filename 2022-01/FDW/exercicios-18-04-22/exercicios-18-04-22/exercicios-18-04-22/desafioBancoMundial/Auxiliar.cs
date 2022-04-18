using System;
namespace exercicios.desafioBancoMundial
{
    public static class Auxiliar
    {
        public static int CalcularIdade(DateTime anoNascimento)
        {
            DateTime dataCorrente = DateTime.Now;
            int anoCorrente = dataCorrente.Year;
            int anoNasc = anoNascimento.Year;

            return anoCorrente - anoNasc;

        }

        public static string FaixaEtaria(int idade)
        {
            if (idade <= 11)
            {
                return "Criança";
            }
            else if (idade >= 12 && idade <= 21)
            {
                return "Jovem";
            }
            else if (idade >= 22 && idade <= 59)
            {
                return "" +
                    "Adulto";
            }
            else
            {
                return "Idoso";
            }


        }
    }
}

