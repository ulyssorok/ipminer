# utils/visualization.py

import matplotlib.pyplot as plt
import networkx as nx

def create_keyword_graph(top_keywords):
    G = nx.Graph()
    
    for i, keywords in enumerate(top_keywords):
        G.add_node(f"Document {i+1}")
        for keyword in keywords:
            G.add_node(keyword)
            G.add_edge(f"Document {i+1}", keyword)
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw_networkx(G, pos, with_labels=True, node_size=500, font_size=10, edge_color='gray', node_color='lightblue')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("outputs/keyword_graph.png")
    plt.close()