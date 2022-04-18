using System;
namespace exercicios
{
    public class Circulo : Forma
    {
        public double Raio { get; set; }
        public override string Nome { get; set; }

        public Circulo(double Raio, string Nome)
        {
            this.Raio = Raio;
            this.Nome = Nome;
        }


        public override void Area()
        {
            double pi = 3.14;
            double result = pi * (this.Raio * this.Raio);
            Console.WriteLine(result);
        }
    }
}

