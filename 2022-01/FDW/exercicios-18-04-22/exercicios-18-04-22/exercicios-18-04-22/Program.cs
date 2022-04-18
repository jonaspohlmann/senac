using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using exercicios;
using exercicios.desafioBancoMundial;

namespace exercicios_18_04_22
{
    internal class Program
    {
        static void Main(string[] args)
        {

            Quadrado quadrado = new Quadrado(4, "quadrado");
            quadrado.Area();

            Triangulo Triangulo = new Triangulo(2, 3, "Triangulo");
            Triangulo.Area();

            Circulo circulo = new Circulo(10, "circulo");
            circulo.Area();



            PessoaFisica pf1 = new PessoaFisica(
                "Rua 123",
                "000000000000000",
                "jonas@gmail.com",
                "Jonas",
                "Araujo",
                "000000000000000",
                "000000000000000",
                new DateTime(1991, 01, 07),
                1000
                );

            PessoaFisica pf2 = new PessoaFisica(
                "Rua 123",
                "000000000000000",
                "jonas@gmail.com",
                "Jonas 2",
                "Araujo",
                "000000000000000",
                "000000000000000",
                new DateTime(1991, 01, 07),
                1000
                );

            PessoaJuridica pj1 = new PessoaJuridica(
                "Rua 123",
                "000000000000000",
                "jonas@gmail.com",
                "TI",
                "informatica",
                0000,
                new DateTime(1991, 01, 07),
                15000
                );



            //ContaSalario contaSalario = new ContaSalario(pf2, 23, 50);
            ContaCorrente conta2 = new ContaCorrente(pf1, 24, 50);
            ContaPoupança conta3 = new ContaPoupança(pf2, 24, 50);

            conta2.setSaldo(1000);
            conta2.Pagar("987654321");

            Console.WriteLine("" + conta2.ConsultarSaldo());
            //Console.WriteLine("Limite "+ conta2.Limite);
            //Console.WriteLine("Taxa do limite "+ conta2.TaxaDoLimite);



        }
    }
}
