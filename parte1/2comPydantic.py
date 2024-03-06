from pydantic import BaseModel
from pydantic import ValidationError
class FormularioPydanticTabelaPessoa(BaseModel):
    nome: str
    idade: int
    email: str
# Dados do formulário (normalmente, esses dados viriam 
# de uma solicitação da web)
dados_do_formulario = {
    "nome": "Alice",
    "idade": "Lu",
    "email": "alice@example.com"
}
# Usando o modelo Pydantic para validar os dados do formulário
try:
    formulario_validado = FormularioPydanticTabelaPessoa(**dados_do_formulario)
    print("Dados válidos:", formulario_validado.dict())
except ValidationError as e:
    print(e.errors())
# O Pydantic é uma ferramenta poderosa para simplificar a validação de dados em projetos Python. Com sua sintaxe limpa, tipagem estática e suporte a validações personalizadas, ele se tornou uma escolha popular entre desenvolvedores Python. Se você deseja garantir a integridade dos dados em seu aplicativo e evitar erros devido a dados incorretos, o Pydantic é uma biblioteca que vale a pena explorar. Considerando o cenário atual de desenvolvimento de software, onde a qualidade e a segurança dos dados são essenciais, o Pydantic se destaca como uma ferramenta valiosa para a comunidade Python. Experimente e simplifique a validação de dados em seus projetos Python hoje mesmo!