with open("token.txt") as f:
    TOKEN = f.read().strip()
client.run(TOKEN)