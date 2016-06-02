# The Graphics Module

The graphics module contains utilities for visualizing the structures of dynamical systems, neural networks, and more. These utilities are contained in the graphics.py file inside the fovea directory and can be modified and extended to provide additional functionality.


## `Plotter`
----
* ### **class** `Plotter`
	----
		def	__init__(self, dm=None)

	Called during class instantiation. 
	
	* `dm`: An optional **diagnostic manager** object.
	
	Initializing the Plotter object cleans all existing figures and plots from memory.

	Example of proper object instantiation:

		myplotter = Plotter()

	----
		def auto_scale_domain(self, xcushion=0.05, ycushion=0.05, subplot=None, figure=None)
	
	Automatically scales domain limits so as to fit the data in all layers in the figure display.

	* `xcushion`: Percentage of x-domain size by which the x domain should be extended. Defaults to 0.
	* `ycushion`: Percentage of y-domain size by which the y domain should be extended. Defaults to 0.
	* `subplot`: The subplot for which the domain should be extended. Defaults to `None`, i.e. extend the domain of the master plot.
	* `figure`: The figure for which the domain should be extended. Defaults to `None`.

	Example:
		
		# Original figure has x-domain: (-5, 5) and y-domain: (2, 2)
		plotter.add_fig('Master', title='quadratic', xlabel='x', ylabel='y', domain=[(-5, 5), (2,2)])
		
		# Data points outside of the domain are added to the figure.
		gui.add_data_points([[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]], layer='fn_data', style='g.')

		# Domain is scaled to x-domain: (-5, 5) and y-domain: (0, 25)
		plotter.auto_scale_domain()

	----
		def set_active_layer(self, layer, figure=None)

	Sets the `Plotter.active_layer` attribute to `(figure, layer)`.
	
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

		>>> plotter.add_fig('Master', title='quadratic', xlabel='x', ylabel='y', domain=[(-5, 5), (2,2)])

		>>> plotter.add_layer('fn_data')

		>>> plotter.arrange_fig([1,1], {'11':
								   {'name': 'Quadratic Plot',
									'scale': [(-5,5),(-2,2)],
									'layers': ['fn_data'],
									'axes_vars': ['x', 'y'],
								   }})

		>>> plotter.add_data(([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]), layer='fn_data')				

		>>> plotter.show_legends()
		LAYER: fn_data
		  sub-plot: 11
		  style b-
		  data:
			name: Master_fn_data, style: b-
	
	----
		def add_fig(self, label, title="", xlabel="", ylabel="", tdom=None, domain=None, display=True)

	Adds a figure to the `Plotter` object. Labels specifying figures are stored in the instance attribute dictionary
	`Plotter.figs`. The keys for this dictionary are the figure "labels" specified during the creation of a figure via
	`add_fig`.

	* `label`: A string identifier for the figure. Also serves as the dictionary key associated with the figure object.
	* `title`: A string to be used as the window title for the figure.
	* `xlabel`: A string specifying a display label for the x-axis.
	* `ylabel`: A string specifying a display label for the y-axis.
	* `tdom`: Optional tuple specifying a time domain. Defaults to `None`.	
	* `domain`: A two-element list specifying two tuples giving the domain ranges for the x and y axes, respectively.
	* `display`: A boolean determining whether figure should be plotted when the plotter is built. Defaults to `True`.

	Example:
	
		>>> plotter = Plotter()
		>>> gui = diagnosticGUI(plotter)
		>>> plotter.add_fig('Figure 1', title='EEG Data', domain=[(-5, 5), (-5, 5)])
		>>> plotter.add_fig('Figure 2', title='EKG Data', domain=[(-10, 10), (-10, 10)]
		# Two figure windows will appear upon calling gui.build_plotter()
		>>> gui.build_plotter()

	----
		def copy_fig(self, newFig, oldFig)
	
	Copies the figure object specified the label passed as `oldFig` to a new figure object specified by the label passed to `newFig`.

	* `newFig`: String label for the new figure to be created.
	* `oldFig`: String label for the old figure to be copied.

	Example:
	
		>>> plotter = Plotter()
		>>> plotter.add_fig('Master', title="The One Figure to Rule Them All, domain=[(-10, 10), (-10, 10)])
		>>> plotter.copy_fig('Challenger', 'Master')
		>>> plotter.figs

		{'Master': args (
		 title = The One Figure to Rule Them All,
		 layers = {},
		 ylabel = ,
		 xlabel = ,
		 autoscaling = True,
		 display = True,
		 domain = [(-10, 10), (-10, 10)],
		 fignum = 1,
		 window = None,
		 arrange = [],
		 shape = [1, 1],
		 tdom = None
		), 'Challenger': args (
		 title = The One Figure to Rule Them All,
		 layers = {},
		 ylabel = ,
		 xlabel = ,
		 shape = [1, 1],
		 autoscaling = True,
		 display = True,
		 fignum = 2,
		 window = None,
		 arrange = []
		)}
	
		# There is no longer but one figure to rule them all! 	
	----
		def set_fig(self, label=None, **kwargs)

	Sets the figure object specified by `label` as the current figure of the `Plotter` object.

	* `label`: String label for the figure to be set as the current figure.
	* `**kwargs`: A list of key, value pairs for the setting of properties of the new current figure.

	**TO DO** Add example use case.

	----
		def clear_fig_data(self, figure_name)

	Clears all of the figure data associated with the figure given by `figure_name`.

	* `figure_name`: String label for the figure to be cleared.

	Example:
		
		from graphics import *
		from numpy import *
		from matplotlib.pyplot import *
		import time
		
		x = linspace(-5, 5)
		y = x ** 2
		
		plotter = Plotter()
		gui = diagnosticGUI(plotter)
		
		plotter.add_fig('Master', title='x**2', xlabel='x', ylabel='y', domain=[(-100, 100), (-100, 100)])
		plotter.add_fig('Minor', title='x**3', xlabel='x', ylabel='y', domain=[(-100, 100), (-100, 100)])
		
		plotter.add_layer('x2_data', figure='Master')
		
		plotter.add_data([x,y], layer='x2_data', figure='Master', style='g-')
		
		plotter.add_layer('x3_data', figure='Minor')
		
		x = linspace(-5, 5)
		y = x ** 3
		
		plotter.add_data([x, y], figure='Minor', layer='x3_data', style='r-')
		plotter.arrange_fig([1,1], {'11':
										{'name': 'Plot of x**2',
										 'scale': [(-20,20),(-50,50)],
										 'layers': ['x2_data'],
										 'axes_vars': ['x', 'y'],
										}}, figure='Master')
		
		plotter.arrange_fig([1,1], {'11':
										{'name': 'Plot of x**3',
										 'scale': [(-20,20),(-50,50)],
										 'layers': ['x3_data'],
										 'axes_vars': ['x', 'y'],
										}}, figure='Minor')
	
		plotter.auto_scale_domain(figure='Master', subplot='11')
		plotter.auto_scale_domain(figure='Minor', subplot='11')
		
		gui.build_plotter((20, 20), with_times=False)
		
		time.sleep(10)
		
		plotter.clear_fig_data('Minor')
		
		gui.build_plotter((20, 20), with_times=False)

	----
		def arrange_fig(self, shape, arrPlots, figure=None)

	For the figure given by `figure`, arranges figure layers into subplots defined as a series
	of dictionaries in `arrPlots`. Each subplot dictionary specifies the subplot's grid position 
	within the figure window. The value associated with each of these position keys is another
	dictionary specifying the subplot name, axes scales, layers, and axes variables.

	* `shape`: The total row-by-column size of the subplots grid. For example, a 2x3 grid of subplots
	can be specified by passing `[2, 3]` for `shape`.

	* `arrPlots`: A nested dictionary specifying subplot grid positions and plot data as explained above.

	* `figure`: The figure to be arranged. Defaults to the current figure.

	Example:

		# Creates a single-row, three-column arrangement of subplots with their associated characteristics.
		plotter.arrange_fig([1,3], {'11':
									   {'name': 'BEFORE',
										'scale': [(-10,10),(-10,10)],
										'layers': ['pre_processed_data'],
										'axes_vars': ['x', 'y', 'z'],
										'projection':'3d'},
									   '12':
									   {'name': 'AFTER',
										'scale': [(-20,20),(-20,20)],
										'layers': ['post_processed_data'],
										'axes_vars': ['a', 'b']},
									   '13':
									   {'name': 'Variance by Components',
										'scale': [(0.5,10),(0,1)],
										'layers': ['variance_data'],
										'axes_vars': ['x', 'y']},
									   })
	----
		def add_layer(self, layer_name, figure=None, set_to_active=True, subplot=None, **kwargs):

	Adds an empty layer to the figure specified by `figure`. By default, the most recent layer added becomes
	the figure's active layer unless set_to_active is `False`.

	* `layer_name`:		The string label used to reference the layer in such contexts as that of `arrange_fig()`.
	* `figure`:			The name of the figure to which the layer should be added. Defaults to the current figure.
	* `set_to_active`:	Boolean specifying whether the layer to be added should be the figure's active layer.
	* `subplot`:			The figure subplot to which the layer should be attached. Defaults to `None`.
	* `**kwargs`:			A series of optional arguments specifying layer attributes. Possible options include...
							** `display`:	A boolean specifying whether the layer should be displayed.
							** `kind`:		A string identifier of the layer's data-type. E.g. 'data', 'vline', 'text', etc.
							** `scale`:		A list of tuples specifying axes scales.

	Example: **TO DO**: Add example use case.

	----
		def set_layer(self, label, figure=None, **kwargs):
	
	Use to set layer attributes to provided values.

	* `label`:	The layer name.
	* `figure`:	The figure in which the target layer resides.
	* `**kwargs:	A series of layer attribute names and their associated values.

	----
		def add_patch(self, data, patch, figure=None, layer=None, subplot=None,
					  name=None, display=True, force=False, log=None, **kwargs):

	Add a Matplotlib patch object to `figure`, `layer`, and/or `subplot`.
	
	* `data`:			The patch data.
	* `patch`:		The patch object instance.
	* `figure`:		The figure to which the patch is to be added.
	* `layer`:		The layer to which the patch is to be added.
	* `subplot`:		The subplot to which the patch is to be added.
	* `name`:			The name of the patch.
	* `display`:		Boolean specifying whether the patch is to be displayed.
	* `force`:
	* `log`:			A log object to which log information is to be written.
	* `**kwargs`:		Patch instantiation values.
