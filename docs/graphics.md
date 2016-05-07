# The Graphics Module

The graphics module contains utilities for visualizing the structures of dynamical systems, neural networks, and more. These utilities are contained in the graphics.py file inside the fovea directory and can be modified to
and extended to provide additional functionality.


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
		def auto_scale_domain(self, xcushion, ycushion, subplot, figure)
	
	Automatically scales domain limits so as to fit the data in all layers in the figure display.

	* `xcushion`: Percentage of x-domain size by which the x domain should be extended. Defaults to 5%.
	* `ycushion`: Percentage of y-domain size by which the y domain should be extended. Defaults to 0.05.
	* `subplot`: The subplot for which the domain should be extended. Defaults to `None`, i.e. extend the domain of the master plot.
	* `figure`: The figure for which the domain should be extended. Defaults to `None`.

	Example:
		
		# Original figure has x-domain: (-5, 5) and y-domain: (2, 2)
		plotter.addFig('Master', title='quadratic', xlabel='x', ylabel='y', domain=[(-5, 5), (2,2)])
		
		# Data points outside of the domain are added to the figure.
		gui.addDataPoints([[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]], layer='fn_data', style='g.')

		# Domain is scaled to x-domain: (-5, 5) and y-domain: (0, 25)
		plotter.auto_scale_domain()


