from vectorfieldplot import FieldplotDocument
from vectorfieldplot import FieldLine
from vectorfieldplot import Field

doc = FieldplotDocument('VFPt_wire_in', width=400, height=400, commons=True)
field = Field({'wires':[[0,0,-1]]})
doc.draw_currents(field)
r0 = 0.19
r1 = 2.2
n = 8
for i in range(n):
    r = r0 * pow(r1 / r0, i / (n - 1.))
    line = FieldLine(field, [0, r*(-1)**i], directions='both')
    doc.draw_line(line, arrows_style={'dist':2.,
        'min_arrows':1, 'offsets':[0.0, 0.5, 0.5, 1.0]})
doc.write('vfpt_wire_endview')
