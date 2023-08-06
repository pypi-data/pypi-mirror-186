"""A collection of utility functions for drawing."""


import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


OPTIONS = {
    "with_labels": True,
    "font_size": 20,
    "font_weight": "bold",
    "font_color": "white",
    "node_size": 2000,
    "width": 3,
}


def draw_samples_with_auxiliary(
    sample, qubits, anxiliary, title: str = "Sample Distribution", save_path=None
):
    """Draw the sample distribution.

    Args:
        sample (list): The sample list.
        qubits (int): The number of data qubits.
        anxiliary (int): The number of auxiliary qubits.
        title (str, optional): The title of the figure. Defaults to "Sample Distribution".
        save_path (str, optional): The path to save the figure. Defaults to None.
    """
    distribution = np.zeros(1 << qubits)
    idx = 0
    for i in range(0, 1 << qubits + anxiliary, 1 << anxiliary):
        for j in range(qubits):
            distribution[idx] += sample[i + j]
        idx += 1
    plt.bar(range(1 << qubits), distribution)
    if save_path:
        plt.savefig(save_path + "/{}.png".format(title), transparent=True)
    plt.show()


def draw_graph(nodes, edges, title: str = "Graph", save_path=None):
    """Draw an undirected graph based on given nodes and edges.

    Args:
        nodes (list): The nodes of the graph.
        edges (list): The edges of the graph.
        title (str, optional): The title of the figure. Defaults to "Graph".
        save_path (str, optional): The path to save the figure. Defaults to None.
    """
    plt.figure()
    plt.title(title)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    pos = nx.circular_layout(G)
    nx.draw_networkx(G, pos, node_color="#416DB6", **OPTIONS)
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    if save_path:
        plt.savefig(save_path + "/{}.png".format(title), transparent=True)
    plt.show()
    return


def draw_maxcut_result(
    nodes,
    edges,
    solution_bit,
    title: str = "The result of MaxCut",
    save_path=None,
):
    """Draw an undirected graph based on given nodes and edges.

    Args:
        nodes (list): The nodes of the graph.
        edges (list): The edges of the graph.
        solution_bit (str): The result state as a binary string.
        title (str, optional): The title of the figure. Defaults to "The result of MaxCut".
        save_path (str, optional): The path to save the figure. Defaults to None.
    """
    plt.figure()
    plt.title(title)
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    pos = nx.circular_layout(G)

    node_color = ["red" if solution_bit[v] == "1" else "#416DB6" for v in nodes]
    edge_color = []
    edge_style = []
    for (u, v) in G.edges:
        if solution_bit[u] != solution_bit[v]:
            edge_color.append("red")
            edge_style.append("dashed")
        else:
            edge_color.append("black")
            edge_style.append("solid")

    nx.draw(
        G,
        pos,
        node_color=node_color,
        edge_color=edge_color,
        style=edge_style,
        **OPTIONS
    )
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    if save_path:
        plt.savefig(save_path + "/{}.png".format(title), transparent=True)
    plt.show()
