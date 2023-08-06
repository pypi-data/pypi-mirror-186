from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from matplotlib import _pylab_helpers, figure
from math import log
from typing import Union

from . import _states, _circs, _hists, _master_show, _show_plt, _round_to
from ._src import _get_path

_circ_count = 0
_state_count = 0
_hist_count = 0

def _message(msg):
    pass
    #warnings.warn(f"From UC_Quantum_Lab: {msg}", stacklevel=3)
    #print(f"From UC_Quantum_Lab: {msg}")

def _show_at_exit():
    global _show_plt
    if _show_plt:
        #print("opening mpl figures")
        plt.show()

# diplays the image in the viewer or saves the image to the inputted path
def display(obj:Union[QuantumCircuit, figure.Figure]=None, path:str="", delete:bool=True, dpi=None)->None:
    global _circ_count, _circs, _master_show, _show_plt

    # handles the different input types
    if isinstance(obj, QuantumCircuit) or obj is None:
        if isinstance(obj, QuantumCircuit): obj.draw(output='mpl')
        else:
            if _pylab_helpers.Gcf.get_active() is None:
                raise TypeError("\"display\" function can not get latest figure matplotlib figure (it does not exist)")
        
        fig = _pylab_helpers.Gcf.get_active().canvas.figure
        
    elif isinstance(obj, figure.Figure): fig = obj
    else:
        raise TypeError("input to \"display\" function must a qiskit quantum circuit or matplotlib figure or nothing")

    fig.tight_layout()
    if len(path): 
        _message(f"display function outputing to:\"{path}\"")
        fig.savefig(path, dpi=dpi)
    elif _master_show:
        #print("displaying circuit")
        p = _get_path(f"_circ_{_circ_count}.png")
        fig.savefig(p, dpi=dpi)
        _circs.append(p)
        _circ_count+=1
    else: 
        _show_plt = True
        delete = False
    
    # if it should delete the current figure
    if delete:
        # deleting the figure "fig"
        plt.close(fig)
    

# generates binary strings
def _getbin(n, s=['']):
    global _config
    if n > 0: return [*_getbin(n - 1, [i + '0' for i in s]), *_getbin(n - 1, [j + '1' for j in s])]
    return s

# displays the statevector of the circuit and can return it
def state(circuit:QuantumCircuit, show:bool=True)->list[complex]:
    global _state_count, _states, _master_show, _show_plt
    _state = Statevector.from_instruction(circuit).data
    _num_bits = int(log(len(_state))/log(2))
    
    _options = _getbin(_num_bits)
    _data = {}
    for i in range(len(_state)):
        val = _state[i]
        if type(val) == complex:
            val = round(val.real, _round_to) + round(val.imag, _round_to) *1j
        else:
            val = round(val, _round_to)
        _data[_options[i]] = str(val).replace("(", "").replace(")", "")

    if show and _master_show:
        #print("showing state vector")
        if len(_states):
            if len(_options[-1]) > len(list(_states.keys())[0]):
                raise KeyError("States must be obtained from the same circuit")
            for item in _data:
                _states[item].append(_data[item])
        else:
            for item in _data:
                _states[item] = [_data[item]]

    return _state

# displays the histogram of the circuit after execution in the viewer
def counts(circuit:QuantumCircuit, backend=Aer.get_backend('qasm_simulator'), path:str="", show:bool=True, dpi=None, shots=1024) -> dict[str, int]:
    global _hist_count, _hists, _master_show, _show_plt
    cs = execute(circuit, backend=backend, shots=shots).result().get_counts()
    # accounting for weirdness of counts result from qiskit
    for item in list(cs):
        if len(item.split(" ")) - 1:
            new_item = item.split(" ")[0]
            cs[new_item] = cs[item]
            del cs[item]

    if len(path): 
        _message(f"outputing histogram to \"{path}\"")
        plt.savefig(path, dpi=dpi)
    elif _master_show and show:
        #print("displaying histogram")
        plot_histogram(cs)
        p = _get_path(f"_hist_{_hist_count}.png")
        plt.savefig(p, dpi=dpi)
        _hists.append(p)
        _hist_count+=1
    elif show:
        plot_histogram(cs)
        _show_plt = True

    return cs


