using System;
namespace exercicios.desafioWhatsapp.Mensagem
{
    public class MsgFoto : Mensagem
    {
        public int tamanho;

        public MsgFoto(int tamanho, Contatinho Contato, string horaEnvio, string conteudo)
        {
            this.tamanho = tamanho;
            this.Destinatrio = Contato;
            this.horaEnvio = horaEnvio;
            this.conteudo = conteudo;
        }
    }

}