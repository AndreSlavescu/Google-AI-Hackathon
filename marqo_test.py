import marqo
import pprint

mq = marqo.Client(url="http://localhost:8882")

results = mq.index("models").search(
    q="I want to use gpt2 to generate text for my writing class."
)

for result in results["hits"]:
    if result["_score"] > 0.7:
        pprint.pprint(result["model"])