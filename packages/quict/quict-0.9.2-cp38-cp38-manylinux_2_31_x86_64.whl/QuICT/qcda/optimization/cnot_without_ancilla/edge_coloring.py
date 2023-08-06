#!/usr/bin/env python
# -*- coding:utf8 -*-

import heapq
from typing import *
from .graph import *
from .utility import *


class EdgeColoring:
    """
    This class provides a quick algorithm to decompose
    a bipartite graph into multiple matching.
    """

    def __init__(self):
        pass

    @staticmethod
    def _merge_one_side(bipartite: Bipartite, is_left: bool, mx_deg: int) -> List[Merged]:
        """

        Args:
            bipartite(Bipartite) : exec merge on this bipartite
            is_left(bool) : Whether it's left
            mx_deg(int) : max degree of bipartite


        Returns:
            List[Merged] : Merged side
        """
        side = copy.copy(bipartite.left) if is_left else copy.copy(bipartite.right)
        hq = []
        for i in side:
            heapq.heappush(hq, Merged(
                bipartite.get_degree(i),
                [i]
            ))
        while len(hq) >= 2:
            a: Merged = heapq.heappop(hq)
            b: Merged = heapq.heappop(hq)
            if a.deg + b.deg < mx_deg:
                heapq.heappush(hq, a + b)
            else:
                heapq.heappush(hq, a)
                heapq.heappush(hq, b)
                break
        return hq

    @classmethod
    def get_regular(cls, bipartite: Bipartite) -> Tuple[dict, dict, Bipartite]:
        """
        Get a regular graph(all nodes have the same degree) from a bipartite graph.
        After the transformation, some indices of nodes might be merged.

        Args:
            bipartite(Bipartite) : a bipartite graph

        Returns:
            A tuple of (new_to_olds, old_to_new, regular_graph). Where new_to_olds
            is a dict from new index to old indices, old_to_new as the one from the
            old to the new and regular_graph is the graph we get.
        """
        new_to_olds = {}
        """int-int dict
        """
        old_to_new = {}
        """int-List[int] dict
        """
        cnt = 1
        left = []
        right = []

        # merge left side
        mx_deg = bipartite.get_max_degree()
        hq = cls._merge_one_side(bipartite, True, mx_deg)
        for old in hq:
            new_to_olds[cnt] = old.nodes
            left.append(cnt)
            cnt += 1

        # merge right side
        hq: List[Merged] = cls._merge_one_side(bipartite, False, mx_deg)
        for old in hq:
            new_to_olds[cnt] = old.nodes
            right.append(cnt)
            cnt += 1

        while len(left) < len(right):
            new_to_olds[cnt] = []
            left.append(cnt)
            cnt += 1
        while len(right) < len(left):
            new_to_olds[cnt] = []
            right.append(cnt)
            cnt += 1

        for new_idx in new_to_olds:
            for idx in new_to_olds[new_idx]:
                old_to_new[idx] = new_idx

        regular_graph = Bipartite(left, right)
        # for edge in bipartite.edges:
        #     s = old_to_new[edge.start]
        #     e = old_to_new[edge.end]
        #     regular_graph.add_edge(s, e, mark=1)

        # you have to add it pairwise
        for node in bipartite.left:
            eid = bipartite.head[node]
            while eid != -1:
                edge = bipartite.edges[eid]
                s = old_to_new[edge.start]
                e = old_to_new[edge.end]
                regular_graph.add_edge(s, e, valid=True)
                regular_graph.add_edge(e, s, valid=True)
                eid = edge.next

        # add some extra "fake" edges
        hql = []
        hqr = []
        heapq.heapify(hql)
        heapq.heapify(hqr)
        for i in regular_graph.left:
            heapq.heappush(hql, (regular_graph.get_degree(i), i))
        for i in regular_graph.right:
            heapq.heappush(hqr, (regular_graph.get_degree(i), i))
        while True:
            a = heapq.heappop(hql)
            b = heapq.heappop(hqr)
            if a[0] == mx_deg:
                break
            regular_graph.add_edge(a[1], b[1], valid=False)
            regular_graph.add_edge(b[1], a[1], valid=False)
            heapq.heappush(hql, (a[0] + 1, a[1]))
            heapq.heappush(hqr, (b[0] + 1, b[1]))
        return new_to_olds, old_to_new, regular_graph

    @classmethod
    def hungarian_dfs(
            cls,
            color: int,
            bipartite: Bipartite,
            cur: int,
            in_alter_path: List[bool],
            matching: List[int]
    ) -> bool:
        """
        Dfs used in hungarian algorithm

        Args:
            color(int) : mark this color for matching edges
            bipartite(Bipartite) : execute dfs on this bipartite
            cur(int) : start point of current dfs
            in_alter_path(List[bool]) : if some point is in an alternative path
            matching(List[int]) : match point, -1 for no match

        Returns:
            bool : dfs success
        """

        eid: int = bipartite.head[cur]  # edge index
        while eid != -1:
            edge = bipartite.edges[eid]
            to = edge.end
            eid = edge.next
            if not in_alter_path[to]:
                in_alter_path[to] = True
                if matching[to] == -1 or cls.hungarian_dfs(
                        color,
                        bipartite,
                        matching[to],
                        in_alter_path,
                        matching
                ):  # :(
                    matching[to] = cur
                    matching[cur] = to
                    return True
        return False

    @classmethod
    def get_colored_matching(
            cls,
            bipartite: Bipartite,
            color: int,
            change_input: bool = True
    ) -> Tuple[int, Bipartite, Bipartite]:
        """
        Get a matching of a regular bipartite graph and color it if needed.
        Remember that a regular graph always has a perfect matching.

        In fact, in the original paper, matching is found using a O(ElogD) algorithm.
        It's too difficult to implement. Use Hungarian instead. Time complexity is increased
        but it has no effect on the ultimate cycle.

        TODO: replace Hungarian matching algorithm(which runs in O(VE)) for a O(ElogE) or O(ElogD) one.

        Args:
            bipartite(Bipartite) : Exec colored matching on this bipartite
            color(int) : Integer index of some color
            change_input(bool) : Whether put color on the original graph

        Returns:
            Tuple[int, Bipartite, Bipartite]: Matching edge number, Match bipartite, Bipartite removed matching.
        """
        n = len(bipartite.nodes)
        matching = [-1 for _ in range(n + 1)]
        cnt = 0
        for node in bipartite.left:
            if matching[node] == -1:
                in_alter_path = [False for _ in range(n + 1)]
                # DO NOT change color during dfs cause there is possible backtracing.
                if cls.hungarian_dfs(color, bipartite, node, in_alter_path, matching):
                    cnt += 1

        matching_bipartite = Bipartite(bipartite.left, bipartite.right)
        for node in matching_bipartite.left:
            other = matching[node]
            if other == -1:
                continue
            s = node
            e = other
            matching_bipartite.add_edge(start=s, end=e, valid=True, color=color)
            matching_bipartite.add_edge(start=e, end=s, valid=True, color=color)

            # Color original bipartite if needed.
            if change_input:
                eid = bipartite.head[s]
                while eid != -1:
                    edge = bipartite.edges[eid]
                    if edge.end == e:
                        edge.color = color
                        break
                    eid = edge.next
                eid = bipartite.head[e]
                while eid != -1:
                    edge = bipartite.edges[eid]
                    if edge.end == s:
                        edge.color = color
                        break
                    eid = edge.next

        extracted_bipartite = Bipartite(bipartite.left, bipartite.right)
        for node in bipartite.left:
            eid = bipartite.head[node]
            while eid != -1:
                edge = bipartite.edges[eid]
                s = edge.start
                e = edge.end
                if matching[s] == e:
                    matching[s] = -1
                    matching[e] = -1
                    eid = edge.next
                    continue
                extracted_bipartite.add_edge(s, e)
                extracted_bipartite.add_edge(e, s)
                eid = edge.next
        assert len(extracted_bipartite.edges) + len(matching_bipartite.edges) == len(bipartite.edges)
        return cnt, matching_bipartite, extracted_bipartite

    @classmethod
    def get_euler_partition(cls, bipartite: Bipartite, skip_colored: bool = True) -> Tuple[Bipartite, Bipartite]:
        """
        Split original 2r-regular bipartite into 2 r-regular bipartite.


        Args:
            bipartite(Bipartite) : Split this.
            skip_colored(bool) : Whether to skip the colored edges in the graph.
            If true, edges without color should form a 2r-regular graph.

        Returns:
            Tuple[Bipartite, Bipartite] : 2 bipartite after split
        """
        e = len(bipartite.edges)
        b1 = Bipartite(bipartite.left, bipartite.right)
        b2 = Bipartite(bipartite.left, bipartite.right)
        """
        Original graph might not be connected, se we have to iterate over
        all possible connected component.
        """
        visited = [False for _ in range(e + 1)]
        nid = 0
        n_cnt = len(bipartite.left)
        visited_cnt = 0
        left_turn = True
        while nid < n_cnt:
            cur = bipartite.left[nid]
            while True:
                """
                Actually, for 2r-regular bipartite graph, that has_out==False
                is only possible when we exhaust a connected component and return
                to start point.
                """
                # check if there's an outward edge
                eid = bipartite.head[cur]
                while eid != -1:
                    edge = bipartite.edges[eid]
                    # skip visited edges
                    if visited[eid]:
                        eid = edge.next
                        continue
                    # skip colored edges
                    elif skip_colored and edge.color != -1:
                        eid = edge.next
                        continue
                    break
                if eid == -1:
                    break
                visited[eid] = True
                visited[eid ^ 1] = True
                visited_cnt += 1
                end = bipartite.edges[eid].end
                if left_turn:
                    b1.add_edge(cur, end)
                    b1.add_edge(end, cur)
                else:
                    b2.add_edge(cur, end)
                    b2.add_edge(end, cur)
                left_turn = not left_turn
                cur = end
            nid += 1
        # assert e // 2 == visited_cnt
        # print(f"undirected edges: {e // 2}, visited: {visited_cnt}")
        return b1, b2

    @classmethod
    def _cpy_edge(cls, _b: Bipartite, _ret: Bipartite):
        for _node in _b.left:
            _eid = _b.head[_node]
            while _eid != -1:
                _edge = _b.edges[_eid]
                _ret.add_edge(
                    start=_edge.start,
                    end=_edge.end,
                    valid=_edge.valid,
                    color=_edge.color
                )
                _ret.add_edge(
                    start=_edge.end,
                    end=_edge.start,
                    valid=_edge.valid,
                    color=_edge.color
                )
                _eid = _edge.next

    @classmethod
    def get_edge_coloring_for_regular(cls, bipartite: Bipartite, start_color: int) -> Bipartite:
        """
        Coloring this regular bipartite

        Args:
            bipartite(Bipartite) : exec on this bipartite
            start_color(int) : color used would start with this index

        Returns:
            Bipartite
        """

        ret = Bipartite(bipartite.left, bipartite.right)
        deg = bipartite.get_any_degree()
        # assert deg > 0
        if deg == 0:  # Sometimes there is really a empty graph
            return ret
        if deg == 1:
            for node in bipartite.left:
                eid = bipartite.head[node]
                if eid == -1:
                    continue
                edge = bipartite.edges[eid]
                ret.add_edge(
                    start=edge.start,
                    end=edge.end,
                    valid=edge.valid,
                    color=start_color
                )
                ret.add_edge(
                    start=edge.end,
                    end=edge.start,
                    valid=edge.valid,
                    color=start_color
                )
        elif deg % 2 == 0:
            b1, b2 = cls.get_euler_partition(bipartite)
            b3 = cls.get_edge_coloring_for_regular(b1, start_color)
            b4 = cls.get_edge_coloring_for_regular(b2, start_color + deg // 2)

            cls._cpy_edge(b3, ret)
            cls._cpy_edge(b4, ret)
        else:  # deg%2 == 1
            _, b1, b2 = cls.get_colored_matching(bipartite, start_color)
            cls._cpy_edge(b1, ret)
            start_color += 1
            b3, b4 = cls.get_euler_partition(b2)
            b5 = cls.get_edge_coloring_for_regular(b3, start_color)
            b6 = cls.get_edge_coloring_for_regular(b4, start_color + deg // 2)
            cls._cpy_edge(b5, ret)
            cls._cpy_edge(b6, ret)
        return ret

    @classmethod
    def get_edge_coloring(cls, bipartite: Bipartite) -> Bipartite:
        """
        Coloring all edges on this bipartite.

        The input color attribute of edges in input bipartite would be ignored.

        Args:
        bipartite(Bipartite) : exec edge coloring on this bipartite

        Returns:
            Bipartite : return a new bipartite with color. Color is represented as an integer, starting from 0.
        """
        new_to_olds: Dict[int, List[int]]
        old_to_new: Dict[int, int]
        bipartite_regular: Bipartite
        new_to_olds, old_to_new, bipartite_regular = cls.get_regular(bipartite)
        colored_regular = cls.get_edge_coloring_for_regular(bipartite_regular, 0)
        # del bipartite_regular
        colored_bipartite = Bipartite(bipartite.left, bipartite.right)
        e = len(colored_regular.edges)
        new_eid_visited = [False for _ in range(e + 1)]
        """
        There are no parallel edges in the input bipartite graph. But parallel edges might be found
        in the regularized bipartite. We iterate over all old edges in the old bipartite to
        find their corresponding edges in the colored bipartite.
        """
        for node in bipartite.left:
            old_eid = bipartite.head[node]
            while old_eid != -1:
                old_edge = bipartite.edges[old_eid]

                old_s = node
                old_e = old_edge.end
                new_s = old_to_new[old_s]
                new_e = old_to_new[old_e]
                new_eid = colored_regular.head[new_s]
                while new_eid != -1:
                    new_edge = colored_regular.edges[new_eid]

                    if new_eid_visited[new_eid] or (not new_edge.valid) or (new_edge.end != new_e):
                        new_eid = new_edge.next
                        continue

                    new_eid_visited[new_eid] = True
                    new_eid_visited[new_eid ^ 1] = True

                    clr = new_edge.color
                    colored_bipartite.add_edge(
                        start=old_s,
                        end=old_e,
                        valid=True,
                        color=clr
                    )
                    colored_bipartite.add_edge(
                        start=old_e,
                        end=old_s,
                        valid=True,
                        color=clr
                    )

                    break

                old_eid = old_edge.next

        return colored_bipartite
