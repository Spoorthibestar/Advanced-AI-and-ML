import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
xc = 0.5
w, h = 0.5, 0.08
xs = xc - w / 2

text_props = {'ha': 'center', 'fontsize': 9, 'weight': 'bold'}
ax.text(xc, 0.95, "Input Vector (Q, K, V)", **text_props)
ax.annotate("", xy=(xc, 0.89), xytext=(xc, 0.93),
            arrowprops=dict(arrowstyle="->"))

blocks = [
    ("Multi-Head Attention", 0.81, 'blue', '-'),
    ("Add & Norm 1", 0.70, 'gray', '--'),
    ("Feed-Forward Network", 0.59, 'green', '-'),
    ("Add & Norm 2", 0.48, 'gray', '--')
]

ys = [y for _, y, _, _ in blocks]

for label, y, c, ls in blocks:
    ax.add_patch(plt.Rectangle((xs, y), w, h,
                 fill=False, edgecolor=c, linestyle=ls))
    ax.text(xc, y + h / 2, label, **text_props)

for y1, y2 in zip(ys, ys[1:]):
    ax.annotate("", xy=(xc, y2 + h), xytext=(xc, y1),
                arrowprops=dict(arrowstyle="->", linewidth=1.5))

ax.annotate("", xy=(xc, 0.40), xytext=(xc, ys[-1]),
            arrowprops=dict(arrowstyle="->", linewidth=1.5))
ax.text(xc, 0.35, "Block Output", **text_props)

residual_paths = [
    (0.89, 0.70 + h / 2),
    (0.70, 0.48 + h / 2)
]

skip_offset = 0.04

for start_y, end_y in residual_paths:
    ax.annotate("", xy=(xs - skip_offset, end_y),
                xytext=(xs - skip_offset, start_y),
                arrowprops=dict(arrowstyle="-", linestyle='--',
                                 color='red', linewidth=1.5))
    ax.annotate("", xy=(xs, end_y),
                xytext=(xs - skip_offset, end_y),
                arrowprops=dict(arrowstyle="->", linestyle='--',
                                 color='red', linewidth=1.5))

ax.axis("off")
plt.title("Transformer Block (With Residual Connections)")
plt.show()
