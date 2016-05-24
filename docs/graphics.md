# The Graphics Module

The graphics module contains utilities for visualizing the structures of dynamical systems, neural networks, and more. These utilities are contained in the graphics.py file inside the fovea directory and can be modified and extended to provide additional functionality.


## `plotter2D`
----
* ### **class** `plotter2D`
	----
		def	__init__(self, dm=None)

	Called during class instantiation. 
	
	* `dm`: An optional **diagnostic manager** object.
	
	Initializing the plotter2D object cleans all existing figures and plots from memory.

	Example of proper object instantiation:

		myplotter = plotter2D()

	----
		def auto_scale_domain(self, xcushion=0.05, ycushion=0.05, subplot=None, figure=None)
	
	Automatically scales domain limits so as to fit the data in all layers in the figure display.

	* `xcushion`: Percentage of x-domain size by which the x domain should be extended. Defaults to 0.
	* `ycushion`: Percentage of y-domain size by which the y domain should be extended. Defaults to 0.
	* `subplot`: The subplot for which the domain should be extended. Defaults to `None`, i.e. extend the domain of the master plot.
	* `figure`: The figure for which the domain should be extended. Defaults to `None`.

	Example:
		
		# Original figure has x-domain: (-5, 5) and y-domain: (2, 2)
		plotter.addFig('Master', title='quadratic', xlabel='x', ylabel='y', domain=[(-5, 5), (2,2)])
		
		# Data points outside of the domain are added to the figure.
		gui.addDataPoints([[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]], layer='fn_data', style='g.')

		# Domain is scaled to x-domain: (-5, 5) and y-domain: (0, 25)
		plotter.auto_scale_domain()

	----
		def set_active_layer(self, layer, figure=None)

	Sets the `plotter2D.active_layer` attribute to `(figure, layer)`.
	
	* `layer`: The layer to be set as active.
	* `figure`: The figure in which the active layer resides. Defaults to `None`.
	
	Example:
		
		>>> plotter.add_layer('layer_one')
		>>> plotter.add_layer('layer_two')
		>>> print(plotter.active_layer)
		>>> ('Master', 'layer_two')
		>>> plotter.set_active_layer('layer_one')
		>>> print(plotter.active_layer)
		>>> ('Master', 'layer_one') 	

	----
		def show_legends(self, figure=None, subplot=None)
	
	Prints the following to **STDOUT**:
	
	For each layer
	
	1. The layer name.
	2. The associated subplots.
	3. The plot style(s).
	4. The defined axes.
	5. The layer data.


	* `figure`: The target figure. Defaults to `None`, i.e. display information for all figures and associated layers.
	* `subplot`: The target subplot. Must be associated a subplot associated with `figure`. Defaults to `None`, i.e. display information for all associated
	subplots.

	Example:

		>>> plotter.addFig('Master', title='quadratic', xlabel='x', ylabel='y', domain=[(-5, 5), (2,2)])

		>>> plotter.addLayer('fn_data')

		>>> plotter.arrangeFig([1,1], {'11':
								   {'name': 'BEFORE',
									'scale': [(-5,5),(-2,2)],
									'layers': ['fn_data'],
									'axes_vars': ['x', 'y'],
								   }})
				
		>>> plotter.show_legends()
		LAYER: fn_data
		  sub-plot: 11
		  style b-

	**TO DO** Finish the example.
	
	----
		def add_fig(self, label, title="", xlabel="", ylabel="", tdom=None, domain=None, display=True)

	Adds a figure to the `plotter2D` object. Labels specifying figures are stored in the instance attribute dictionary
	`plotter2D.figs`. The keys for this dictionary are the figure "labels" specified in the creation of a figure via
	`addFig`.

	* `label`: A string identifier for the figure. Also serves as the dictionary key associated with the figure object.
	* `title`: A string to be used as the display title for the figure.
	* `xlabel`: A string specifying a display label for the x-axis.
	* `ylabel`: A string specifying a display label for the y-axis.
	* `tdom`: Optional tuple specifying a time domain. Defaults to `None`.	
	* `domain`: A two-element list specifying two tuples giving the domain ranges for the x and y axes, respectively.
	* `display`: A boolean determining whether figure should be plotted when the plotter is built. Defaults to `True`.

	**TO DO** Add example use case.

	----
		def copy_fig(self, newFig, oldFig)
	
	Copies the figure object specified the label passed as `oldFig` to a new figure object specified by the label passed to `newFig`.

	* `newFig`: String label for the new figure to be created.
	* `oldFig`: String label for the old figure to be copied.

	**TO DO** Add example use case.

	----
		def set_fig(self, label=None, **kwargs)

	Sets the figure object specified by `label` as the current figure of the `plotter2D` object.

	* `label`: String label for the figure to be set as the current figure.
	* `**kwargs`: A list of key, value pairs for the setting of properties of the new current figure.

	**TO DO** Add example use case.

	----
		def clear_fig_data(self, figure_name)

	Clears all of the figure data associated with the figure given by `figure_name`.

	* `figure_name`: String label for the figure to be cleared.

	**TO DO** Add example use case.		 
