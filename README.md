FlaskImageClassifier é um aplicativo web desenvolvido em Flask que permite o upload de imagens para classificação entre gatos e cachorros usando um modelo de aprendizado de máquina pré-treinado. Este projeto demonstra como integrar um modelo de classificação de imagens com uma interface web simples e moderna.

## Funcionalidades
- Upload de imagens através de uma interface web amigável.
- Visualização de prévia da imagem antes da classificação.
- Classificação automática das imagens como "Gato" ou "Cachorro".
- Resultados exibidos de forma clara e intuitiva.
- Uso de Bootstrap para um design responsivo e atraente.

## Tecnologias Utilizadas
- Flask
- TensorFlow/Keras
- Bootstrap
- HTML/CSS
- JavaScript

## Como Executar
1. Clone o repositório:
    ```bash
    git clone https://github.com/SEU_USUARIO/FlaskImageClassifier.git
    cd FlaskImageClassifier
    ```

2. Crie um ambiente virtual e instale as dependências:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Coloque o modelo `cats_dogs_model.h5` na pasta do projeto.

4. Execute o aplicativo:
    ```bash
    python app.py
    ```

5. Acesse o aplicativo em `http://127.0.0.1:5001/`.

## Estrutura do Projeto
- `app.py`: Script principal do Flask.
- `cats_dogs_model.h5`: Modelo pré-treinado.
- `templates/`: Diretório contendo os templates HTML.
- `uploads/`: Diretório para armazenar as imagens carregadas.
- `requirements.txt`: Arquivo com as dependências do projeto.
- `README.md`: Este arquivo com instruções e informações sobre o projeto.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
