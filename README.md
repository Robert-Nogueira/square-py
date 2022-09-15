[SquareCloud]: https://squarecloud.app
[API]: https://docs.squarecloud.app/api/introducao


# Square-py
### square-py é um wrapper não oficial da [API] da [SquareCloud]

## Instalando
````python
pip install square-py
````

## Começando
### Onde pegar a minha chave de api?
para pegar a sua chave de api/token basta ir no site da [SquareCloud] e se registrar/logar, após isso vá em `dashboard` > `minha conta` > `Regenerar API/CLI KEY`

## Obtendo informações da sua applicação
````python
import square


API_KEY = 'api key' # seu token da api
APP_ID = 12345678 # id da sua aplicação

api = square.Api(api_key=API_KEY)
app = api.get_app(app_id=APP_ID)

app.info_dict() # todas as informações(ram cpu etç): dict
app.is_running() # se sua aplicação está ligada: bool
app.logs() # um resumo das logs da sua aplicação: str
app.logs_complete() # uma url para as logs completas: str
````
### Gerenciando sua aplicação
````python
import square


API_KEY = 'api key' # seu token da api
APP_ID = 12345678 # id da sua aplicação

api = square.Api(api_key=API_KEY)
app = api.get_app(app_id=APP_ID)

app.start() # inicia sua aplicaçâo
app.stop() # para sua aplicação
app.restart() # reinicia sua aplicação
````

## Licença
MIT License
