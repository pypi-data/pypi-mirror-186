""" This is a file with auxiliary functions for GUI template using Nanosurf Studio Style
Copyright Nanosurf AG 2021
License - MIT
"""
import pathlib
import pyqtgraph.exporters

# Save data in multiple columns: data[channel][data] fist dimension = channels, second dimension = data stream
def savedata_txt(file_name: pathlib.Path, data, header:str="", separator="\t"):
    with open(file_name, 'w+') as f:
        if header != "":
            f.write(header+"\n")
        for i in range(len(data[0])):
            write_string = ""
            for j in range(len(data)):
                if j == len(data)-1:
                    write_string =  write_string + str(data[j][i]) + "\n"
                else:
                    write_string =  write_string + str(data[j][i]) + separator
            f.write(write_string)
        f.close()

# Load data
def loaddata_txt(file_name: pathlib.Path, vertical = True, skip_header: int = 0, separator="\t"):
    result = []
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if skip_header <= 0:
                sline = line.rstrip()
                splitline = sline.split(separator)
                floatline = [float(i) for i in splitline]
                result.append(floatline)
            else:
                skip_header -= 1
    if vertical:
        result = list(map(list, zip(*result)))
    return result


def saveplot_png(file_name: pathlib.Path, plotitem):
    exporter = pyqtgraph.exporters.ImageExporter(plotitem)
    #exporter.parameters()['width'] = 100   # (note this also affects height parameter)
    file_name.with_suffix('.png')
    print(file_name)
    exporter.export(str(file_name))
    return file_name

def save_results(file_name: pathlib.Path, resulttable):    
    with open(file_name, 'w+') as f:
        for id in range(resulttable.rowCount()):
            name_str = resulttable.item(id,0).text()
            val_str = resulttable.item(id,1).text()
            result_string = name_str + "; "+ val_str +("\n")
            f.write(result_string)
    f.close()
