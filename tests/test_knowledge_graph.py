from medreasoner.knowledge_graph import LocalKnowledgeGraph

def test_graph_retrieval():
    graph = LocalKnowledgeGraph()
    matches = graph.retrieve(["fever"])
    assert matches
    assert matches[0]["related_concept"] == "elevated body temperature"
