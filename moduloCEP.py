import consultaCEP

cep = input("Digite o CEP para consulta: ")
dados_cep = consultaCEP.consult_cep(cep)
state = dados_cep.get("logradouro")

if  state != None:
    print("\nVerificando CEP")
    print("CEP:", dados_cep.get("cep"))
    print("Logradouro:", dados_cep.get("logradouro"))
    print("Complemento:", dados_cep.get("complemento"))
    print("Bairro:", dados_cep.get("bairro"))
    print("Cidade:", dados_cep.get("localidade"))
    print("Estado:", dados_cep.get("uf"))
    print("Imprimir dicionário:", dados_cep)
    print("Tipo:", type(dados_cep))
    print("Quantidade de elementos:", len(dados_cep))
else:
    print("\nCEP não encontrado.")


