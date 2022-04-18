using System;

namespace exercicios.desafioWhatsapp.Mensagem
{
    public class Whatsapp : Mensagem
    {
        public Contatinho contato;
        public Mensagem mensagens;

        public Whatsapp()
        {
        }

        public void listarContatos()
        {
            Console.WriteLine(this.contato);

        }

        public void listarMensagens()
        {
            Console.WriteLine(this.mensagens);
        }


    }
}

