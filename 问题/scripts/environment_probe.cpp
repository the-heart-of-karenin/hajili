#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

// Tiny environment test: five labelled parallel edges on two vertices, k=2.
// Bit 1 means 0 -> 1; bit 0 means 1 -> 0.
int main() {
    constexpr int m = 5, k = 2, states = 1 << m;
    std::vector<int> legal;
    std::vector<bool> allowed(states, false);
    for (int mask = 0; mask < states; ++mask) {
        int forward = __builtin_popcount(static_cast<unsigned>(mask));
        if (forward >= k && m - forward >= k) {
            legal.push_back(mask);
            allowed[mask] = true;
        }
    }
    std::vector<std::vector<int>> adj(states);
    int twice_edges = 0;
    for (int mask : legal) {
        for (int bit = 0; bit < m; ++bit) {
            int next = mask ^ (1 << bit);
            if (allowed[next]) {
                adj[mask].push_back(next);
                ++twice_edges;
            }
        }
    }
    int components = 0, maximum_component_diameter = 0;
    std::vector<bool> seen(states, false);
    for (int start : legal) {
        if (!seen[start]) ++components;
        std::vector<int> distance(states, -1);
        std::queue<int> pending;
        distance[start] = 0;
        pending.push(start);
        while (!pending.empty()) {
            int here = pending.front();
            pending.pop();
            seen[here] = true;
            maximum_component_diameter = std::max(maximum_component_diameter, distance[here]);
            for (int next : adj[here]) {
                if (distance[next] == -1) {
                    distance[next] = distance[here] + 1;
                    pending.push(next);
                }
            }
        }
    }
    std::cout << "{\n  \"vertices\": 2,\n  \"physical_edges\": 5,\n"
              << "  \"k\": 2,\n  \"orientations_checked\": " << states
              << ",\n  \"legal_orientations\": " << legal.size()
              << ",\n  \"reconfiguration_edges\": " << twice_edges / 2
              << ",\n  \"components\": " << components
              << ",\n  \"maximum_component_diameter\": " << maximum_component_diameter
              << "\n}\n";
}
