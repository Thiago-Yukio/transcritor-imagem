#Bibliotecas usadas
import streamlit as st
from  streamlit_paste_button  import  paste_image_button  as  pbutton
import easyocr as orc
import numpy as np


st.title('Transcritor de texto Print Screen: (Simples)',
         text_alignment='center')

#Espaçamento
st.divider()
#Texto de aviso e alerta
st.markdown("""
<div style="
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: red;
    border: 2px solid red;
    border-radius: 8px;
    padding: 10px;
    margin-bottom: 10px;
">
⚠️ !!! ATENÇÃO !!! ⚠️
</div>
""", unsafe_allow_html=True)
st.markdown("""
- A imagem deve estar armazenada no computador;
- Caso contenha texto manuscrito, a transcrição poderá apresentar imprecisões;
- Caso contenha números manuscritos, a transcrição também poderá apresentar imprecisões;
- Não envie arquivos do Word, PowerPoint ou de outros formatos não suportados;
- Os formatos aceitos são: **PNG**, **JPG** e **JPEG**.

**Bom proveito da ferramenta! 😉**
""")
#Espaçamento
st.divider()

#Local de envio de print screen:
imagem_print=pbutton('📸 Cole a sua imagem do Print Screen aqui:')

#Mostrar a imagem colada...
if  imagem_print.image_data is not None:
    st.write ( 'Sua Imagem:' )
    st.image ( imagem_print.image_data )

#Espaçamento
    st.divider()

    with st.spinner('Lendo a imagem...'):
        #Conversão da imagem
        imagem = np.array(imagem_print.image_data)
        #Iniciando o leitor easyocr para português
        leitor=orc.Reader(['pt'])
        #Transcrevendo a imagem
        texto_transcrito=leitor.readtext(imagem, detail=0)
        #Texto tratado
        lista_tratado=[]
        for palavra in texto_transcrito:
            temp=palavra.strip()
            lista_tratado.append(temp)
        #juntado as palavras
        texto=" ".join(lista_tratado)
        st.write(texto)