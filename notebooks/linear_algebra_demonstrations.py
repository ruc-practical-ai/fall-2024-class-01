import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


def compute_norm(x_component, y_component):
    """Compute the norm of a 2-element vector."""
    return np.sqrt(x_component**2 + y_component**2)


class L2NormDemo:
    """Demonstrate computing the norm of a 2-element vector."""

    def __init__(self):
        self._label_x_location = 7
        self._label_y_location = 9.5
        self._initial_x = 3.0
        self._initial_y = 4.0
        self._plot_max = 12
        self._plot_min = -12
        self._ORIGIN_X = 0
        self._ORIGIN_Y = 0

    def instantiate_plot(self):
        self.create_plot()
        self.configure_plot_axes()
        self.plot_initial_vector()
        self.build_sliders()
        self._slider_x.on_changed(self.update)
        self._slider_y.on_changed(self.update)
        plt.show()

    def create_plot(self):
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.1, bottom=0.3)

    def configure_plot_axes(self):
        self.ax.set_xlim([self._plot_min, self._plot_max])
        self.ax.set_ylim([self._plot_min, self._plot_max])
        self.ax.axhline(self._ORIGIN_X, color="black", lw=2)
        self.ax.axvline(self._ORIGIN_Y, color="black", lw=2)
        self.ax.set_title("L-2 Norm Demonstration")

    def plot_initial_vector(self):
        self.ax.arrow(
            self._ORIGIN_X,
            self._ORIGIN_Y,
            self._initial_x,
            self._initial_y,
            head_width=0.5,
            head_length=0.7,
            fc="k",
            ec="k",
        )
        norm = compute_norm(self._initial_x, self._initial_y)
        self._vector_length_text = self.ax.text(
            self._label_x_location,
            self._label_y_location,
            f"Length = {norm:.2f}",
            fontsize=9,
            color="k",
            bbox=dict(facecolor="grey", edgecolor="black", pad=8.0),
        )

    def build_sliders(self):
        x_slider_position = [0.1, 0.15, 0.8, 0.05]
        y_slider_position = [0.1, 0.05, 0.8, 0.05]
        ax_x = plt.axes(x_slider_position, facecolor="lightgoldenrodyellow")
        ax_y = plt.axes(y_slider_position, facecolor="lightgoldenrodyellow")
        self._slider_x = Slider(
            ax_x, "X", -10.0, 10.0, valinit=self._initial_x
        )
        self._slider_y = Slider(
            ax_y, "Y", -10.0, 10.0, valinit=self._initial_y
        )

    def update(self, val):
        new_x = self._slider_x.val
        new_y = self._slider_y.val
        [p.remove() for p in reversed(self.ax.patches)]
        self.ax.arrow(
            0, 0, new_x, new_y, head_width=0.5, head_length=0.7, fc="k", ec="k"
        )
        norm = compute_norm(new_x, new_y)
        self._vector_length_text.set_text(f"Length: {norm:.2f}")
        self.fig.canvas.draw_idle()
