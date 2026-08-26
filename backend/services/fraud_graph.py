import networkx as nx


def build_fraud_graph(df):
    graph = nx.Graph()

    for customer in df["customer_id"].unique():
        graph.add_node(customer)

    # Shared device relationships
    for device, group in df.groupby("device_id"):
        customers = group["customer_id"].unique()

        for i in range(len(customers)):
            for j in range(i + 1, len(customers)):
                graph.add_edge(
                    customers[i],
                    customers[j],
                    weight=1,
                    relationships=["shared_device"],
                )

    # Shared IP relationships
    for ip, group in df.groupby("ip_address"):
        customers = group["customer_id"].unique()

        for i in range(len(customers)):
            for j in range(i + 1, len(customers)):
                customer_a = customers[i]
                customer_b = customers[j]

                if graph.has_edge(customer_a, customer_b):
                    edge = graph[customer_a][customer_b]
                    edge["weight"] += 1
                    edge["relationships"].append("shared_ip")
                else:
                    graph.add_edge(
                        customer_a,
                        customer_b,
                        weight=1,
                        relationships=["shared_ip"],
                    )

    return graph