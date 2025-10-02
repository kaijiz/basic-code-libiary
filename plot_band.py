import matplotlib.pyplot as plt
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter

# Load VASP band structure from vasprun.xml
vasprun = Vasprun("vasprun.xml", parse_projected_eigen=True)
band_structure = vasprun.get_band_structure(line_mode=True)

plt.figure(figsize=(18, 8))

# Plot using pymatgen's built-in Band Structure Plotter
plotter = BSPlotter(band_structure)
plotter.get_plot()

plt.gcf().canvas.draw()  # populate tick labels
ax = plt.gca()
labels = [tick.get_text() for tick in ax.get_xticklabels()]
new_labels = []
for s in labels:
    s2 = s.replace("Gamma", r"$\Gamma$").replace("GAMMA", r"$\Gamma$")
    new_labels.append(s2)
ax.set_xticklabels(new_labels, fontsize=14)

plt.ylim(-1, 1.5)

plt.savefig("band.pdf",format='pdf', dpi=300, bbox_inches='tight')
