using System;
namespace exercicios.desafioWhatsapp.Mensagem
{
    public class MsgAudio : Mensagem
    {
        public int duracao;

        public MsgAudio(int duracao, Contatinho Contato, string horaEnvio, string conteudo)
        {
            this.duracao = duracao;
            this.Destinatrio = Contato;
            this.horaEnvio = horaEnvio;
            this.conteudo = conteudo;
        }
    }
}

