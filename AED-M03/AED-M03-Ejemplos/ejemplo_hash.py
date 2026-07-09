keys = ["model", "dataset", "epoch", "loss", "accuracy"]

for k in keys:
  print(k, "->", hash(k))