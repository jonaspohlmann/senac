using System;
namespace exercicios
{
    public class Quadrado : Forma
    {
        public double Lado { get; set; }

        public override string Nome { get; set; }

        public Quadrado(double Lado, string Nome)
        {
            this.Lado = Lado;
            this.Nome = Nome;
        }

        public override void Area()
        {
            double result = this.Lado * this.Lado;
            Console.WriteLine(result);

        }
    }
}

