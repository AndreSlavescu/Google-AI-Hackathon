import marqo

mq = marqo.Client(url="http://localhost:8882")

results = mq.index("models").search(
    q="I want to use gpt2 to generate text for my writing class."
)

print(results)