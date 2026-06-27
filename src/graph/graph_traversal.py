from collections import deque


def get_reasoning_paths(G, emotion):

    if emotion not in G:
        return []

    queue = deque([(emotion, [emotion])])

    paths = []

    while queue:

        current, path = queue.popleft()

        neighbors = list(G.successors(current))

        if not neighbors:
            paths.append(path)
            continue

        for neighbor in neighbors:
            queue.append(
                (
                    neighbor,
                    path + [neighbor]
                )
            )

    return paths