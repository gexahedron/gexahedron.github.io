#!/usr/bin/env python3
"""Render House of Graphs thumbnails (research/hog/<id>.svg) from the stored embeddings.

Usage: tools/hog_thumbnails.py 58029 58030 ...
"""
import json
import pathlib
import sys
import urllib.request

API = "https://houseofgraphs.org/api/graphs/{}"
OUT = pathlib.Path(__file__).resolve().parent.parent / "research" / "hog"
SIZE, PAD, R = 120, 8, 2.2


def fetch(url):
    with urllib.request.urlopen(url) as r:
        return json.load(r)


def render(gid):
    adj = fetch(API.format(gid))["adjacencyList"]
    emb = fetch(API.format(gid) + "/embedding")["_embedded"]["embeddingModelList"][0]["entity"]["embedding"]
    xs, ys = [p[0] for p in emb], [p[1] for p in emb]
    span = max(max(xs) - min(xs), max(ys) - min(ys)) or 1
    k = (SIZE - 2 * PAD) / span
    ox = (SIZE - (max(xs) - min(xs)) * k) / 2
    oy = (SIZE - (max(ys) - min(ys)) * k) / 2
    pt = [(ox + (x - min(xs)) * k, oy + (max(ys) - y) * k) for x, y in emb]
    lines = [f'<line x1="{pt[u][0]:.1f}" y1="{pt[u][1]:.1f}" x2="{pt[v][0]:.1f}" y2="{pt[v][1]:.1f}"/>'
             for u, nbrs in enumerate(adj) for v in nbrs if u < v]
    dots = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{R}"/>' for x, y in pt]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}" width="{SIZE}" height="{SIZE}">'
           f'<g stroke="#555" stroke-width="0.5">{"".join(lines)}</g>'
           f'<g fill="#a5d6a7" stroke="#43a047" stroke-width="0.6">{"".join(dots)}</g></svg>\n')
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{gid}.svg").write_text(svg)


if __name__ == "__main__":
    for gid in sys.argv[1:]:
        render(gid)
        print("wrote", OUT / f"{gid}.svg")
