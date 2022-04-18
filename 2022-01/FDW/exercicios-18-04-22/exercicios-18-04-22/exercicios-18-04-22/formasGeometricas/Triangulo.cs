using System;
namespace exercicios
{
    public class Triangulo : Forma
    {
        public double LadoA;
        public override string Nome { get; set; }
        public double LadoB;

        public Triangulo(double LadoA, double LadoB, string Nome)
        {
            this.LadoA = LadoA;
            this.LadoB = LadoB;
            this.Nome = Nome;
        }

        public override void Area()
        {
            double area = (this.LadoA * this.LadoB) / 2;
            Console.WriteLine(area);
            Console.WriteLine(this.Nome);
        }
    }
}

