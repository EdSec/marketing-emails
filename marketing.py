3
���Z;  �               @   s8  d dl Zd dlZd dlZd dlZd dlZd dlmZ d dlmZ e	d� ej
d� �yxed�Zej
d� x ed�Zed	kr|qjed
krjP qjW edkr�dZnfedkr�dZnXedkr�dZnJed
kr�ed�Zed�Zed e Zn$e	d� ed�Zed�Zed e Zx\y2ed�Zed�Zeje�Zej�  ejee� W n   e	d� �w Y nX e	d� P �q W ed�Zed�Zx8ed�Zejje�dk�r�P ejje�dk�rn�qn�qnW x(ed�Zedk�r�P edk�r��q��q�W edk�r*dZed �Zd!e Zx�yed!7 Zeed"�7 ZW n ek
�r    P Y nX �q�W nXedk�r�d#Zed$�Zd!e Zx8yed!7 Zeed%�7 ZW n ek
�rz   P Y nX �qJW d Z d Z!eee�Z"e	d&� e#e���Z$�xe$D �]Z%ed'�Zeed(< ed) ed*< e%ed+< ej&e"� ej'ed* ed+ ej(� �Z)e d7 Z e!d7 Z!e	d,e*e!� d- e% � e d.k�r�e	d/� ej
d0� d Z n�q�yNe!d1k�r�ed2�Z+e+d3k�r~e	d4� ej
d� ne	d5� ej
d� ej,�  W n ek
�r�   dZ-Y nX �q�W W dQ R X d Z-W n ek
�r�   dZ-Y nX e	d6� e-dk�re	d7� ej
d� e-d k�r4e	d8e*e!� d9 � ej
d� dS ):�    N)�MIMEMultipart)�MIMETextz�
 ::::::::::::::::::::::::::::::::::::::::::::

 [+] Script para envio de e-mails em massa!

 [+] Coded By: Bob (MaryenSecurity)
 [+] Modified By: EdSec

 ::::::::::::::::::::::::::::::::::::::::::::
�   z"
 [+] Tecle enter para continuar: �   zs

 Qual servidor smtp deseja usar?

 [ 1 ]=> GMAIL
 [ 2 ]=> HOTMAIL
 [ 3 ]=> YAHOO
 [ 4 ]=> outro

 Servidor SMTP: �5�4�1zsmtp.gmail.com:587�2zsmtp.live.com:587�3zsmtp.yahoo.com:587z
 Digite o dominio do smtp: z Digite a porta do smtp: �:z

 ERRO !!!u   
 Seu endereço de e-mail: z Senha do seu e-mail: u(   
 Login não efetuado, tente novamente !z
 Login efetuado com sucesso !
u"   
 Digite o assunto do cabeçalho: z Digite o seu nome: uS   

 Digite o diretorio onde está o arquivo
 ex: /pasta1/local/arquivo.txt
 Digite: TFzZ

 Deseja usar qual tipo de texto ?

 [ 1 ]=> HTML
 [ 2 ]=> TEXTO NORMAL

 Tipo de texto: Zhtmlzb

 Digite o codigo html linha por linha
 Quando concluir, digite CTRL+C

 Primeira linha do HTML: �
z Proxima linha do HTML: Zplainza

 Digite o seu texto linha por linha
 Quando concluir, digite CTRL+C

 Primeira linha do texto: z Proxima linha do conteudo: z"

 INICIANDO ENVIO DE E-MAILS...

ZalternativeZSubjectz <mail@gmail.com>ZFromZTou    [✓]>> Email z enviado para: �2   u>   
 [ ! ]>> Pausa para não sobrecarregar o servidor, aguarde!

�   i�  u$  

 !! Você já enviou 499 e-mails, se estiver usando gmail,hotmail ou algo do tipo, seu e-mail será bloqueado por enviar mais de 500 e-mails e vai constar como spam!
 >> Se você sabe do risco e quer continuar, tecle ENTER
 >> Se você deseja sair e não correr riscos, digite alguma letra!� u   
 [✓]>> Continuando ...
z
 [+] Saindo ...
� u'   
 Você usou CTRL+C e está saindo...

u9   

 Envio de e-mails concluido com sucesso!
 Você enviou z. e-mails

 Obrigado por usar o nosso script!

).Zos.path�osZtime�sysZsmtplibZemail.mime.multipartr   Zemail.mime.textr   �printZsleep�inputZincio1ZserverZsmtpZdominioZportaZloginZsenhaZSMTP�sZstarttlsZassuntoZnomeZarquivo�path�isfileZemailZtipoZbody1Zbody�KeyboardInterruptZqtdZqtdXZconteudo�openZemailsZdestinoZattachZsendmailZ	as_stringZenvio�strZaviso�exitZsair� r   r   �%/storage/emulated/legacy/marketing.py�<module>   s�   	

	



















