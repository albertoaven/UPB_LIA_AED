tokens = ["ia", "datos", "ia", "python", "datos", "modelo"]
vocabulario = set(tokens)

print(f"Vocabulario: {vocabulario}")

print(f"¿'python' está en el vocabulario? {'Sí' if 'python' in vocabulario else 'No'}")
print(f"Tamaño del vocabulario: {len(vocabulario)}")