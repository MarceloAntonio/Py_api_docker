Para rodar o serviço:

1.  Ir para diretório
    ```bash
    cd API
    ```

2.  Criar imagem
    ```bash
    docker build -t python-api-flask .
    ```

3.  Rodar
    ```bash
    docker run -d -p 5001:5000 --name api-flask python-api-flask
    ```