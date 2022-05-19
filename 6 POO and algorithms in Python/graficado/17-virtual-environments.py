from bokeh.plotting import figure, output_file, show

"""

    To generate a virtual environment -> python3.10 -m venv <name>
    To get inside -> source <name>/bin/activate
    To get out -> deactivate

    pip freeze to see our packages
    
    always use packages locally, not globally
"""
if __name__ == "__main__":
    output_file('simple_graph.html')
    fig = figure()
    
    tot_values = int(input('values number: '))
    x_vals = list( range(tot_values) )
    y_vals = []
    
    for i in x_vals:
        val = int( input('gimmi a value') )
        y_vals.append(val)
        
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
    