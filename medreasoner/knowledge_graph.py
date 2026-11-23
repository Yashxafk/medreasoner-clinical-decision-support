import json
from pathlib import Path

DEFAULT_GRAPH = Path(__file__).resolve().parent.parent / "data" / "knowledge_graph.json"

class LocalKnowledgeGraph:
    """Tiny illustrative graph for software demonstration; not a clinical ontology."""
    def __init__(self, path=DEFAULT_GRAPH):
        self.path = Path(path)
        self.nodes = json.loads(self.path.read_text(encoding="utf-8"))

    def retrieve(self, terms):
        terms = {t.lower() for t in terms}
        matches = []
        for node in self.nodes:
            labels = {node["concept"].lower(), *[x.lower() for x in node.get("aliases", [])]}
            if terms & labels:
                matches.append(node)
        return matches
