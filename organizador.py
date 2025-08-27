mochila=["camiseta", "calça", "meias","escova", "carregador", "livro"]
print("mochila")
mochila.remove("livro")
mochila.remove("carregador")
mochila.pop(2)
mochila.append("remédios")
mochila.append("powerbank")
mochila[0]= "blusa"
mochila_ordenada= sorted(mochila)
print("mochila final:")
for item in mochila_ordenada:
    print(f"-{item}")