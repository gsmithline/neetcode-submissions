class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        components = []
        graph = {}
        result = 0
        for i in range(0, n):
            graph[i] = []

        for edge in edges:
            if edge[0] in graph.keys():
                graph[edge[0]].append(edge[1])
            if edge[1] in graph.keys():
                graph[edge[1]].append(edge[0])

        def dfs(node, current_component):
            visited.add(node)
            current_component.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, current_component)

        for node in graph:
            if node not in visited:
                component = []
                dfs(node, component)
                components.append(component)

        return len(components)
        


        




            
        


