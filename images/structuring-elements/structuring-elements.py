from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

# Rank=3 Connectivity=1
r3c1 = ndimage.generate_binary_structure(3, 1)

ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r3c1, facecolors="#377eb8", edgecolor='k')
ax.set_aspect('equal')
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.grid(False)
plt.tight_layout()
plt.savefig('r3c1.png', dpi=200, transparent=True)

# Rank=3 Connectivity=2
r3c2 = ndimage.generate_binary_structure(3, 2)
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r3c2, facecolors="#377eb8", edgecolor='k')
ax.set_aspect('equal')
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.grid(False)
plt.tight_layout()
plt.savefig('r3c2.png', dpi=200, transparent=True)

# Rank=3 Connectivity=3
r3c3 = ndimage.generate_binary_structure(3, 3)
ax = plt.figure().add_subplot(projection='3d')
ax.voxels(r3c3, facecolors="#377eb8", edgecolor='k')
ax.set_aspect('equal')
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.grid(False)
plt.tight_layout()
plt.savefig('r3c3.png', dpi=200, transparent=True)

