# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['worstcase']

package_data = \
{'': ['*']}

install_requires = \
['Pint>=0.20,<0.21', 'networkx>=2.5.1,<3.0.0', 'pyDOE>=0.3.8,<0.4.0']

setup_kwargs = {
    'name': 'worstcase',
    'version': '0.4.0',
    'description': 'Worst case analysis and sensitivity studies. Extreme Value, Root-Sum-Square, Monte Carlo.',
    'long_description': '# worstcase\n\nFor a detailed example of how this software may be leveraged in a true to life example, consider reading this [blog post](https://www.osborneee.com/worstcase/), where the end-to-end measurement uncertainty of a high-side current-sensing circuit is computed.\n\n## What\'s the worst that could happen?\n\nProfessional engineers spend a disproportionate amount of time considering the worst case, especially in fields such as aerospace where the cost of failure can be enormous and therefore the tolerance for technical risk is low.\n\nWhen delivering hardware to a customer it is typical to also deliver analyses as data products. One such analysis is the worst-case analysis. Hardware performance must be analytically verified to meet requirements for the life of the mission, across all operational environments, with worst-case component variations.\n\nThe typical method for performing such an analysis is a spreadsheet like [this one](https://docs.google.com/spreadsheets/d/1OWK2Hds00IrvRUNogDVzHMQhLLowioNIzL4SbS0E3kI/edit#gid=0)... the `worstcase` Python package offers a far more effective solution.\n\n## Usage\n\nAt its core, the `worstcase` Python package computes three values: the nominal, the lower bound, and the upper bound. These values may be determind either by Extreme Value, Root-Sum-Square, or Monte Carlo methods.\n\nInput parameters are defined by their range or tolerance, (`param.byrange`, `param.bytol`).\n\n```python\n# define the resistor uncertainties\nR1 = param.bytol(nom=100 * unit.mohm, tol=0.01, rel=True, tag="R1")\nR2 = param.bytol(nom=1.001 * unit.kohm, tol=0.01, rel=True, tag="R2")\nR3 = param.bytol(nom=50.5 * unit.kohm, tol=0.01, rel=True, tag="R3")\nR4 = param.bytol(nom=1.001 * unit.kohm, tol=0.01, rel=True, tag="R4")\nR5 = param.bytol(nom=50.5 * unit.kohm, tol=0.01, rel=True, tag="R5")\n\n# define the amplifier offset voltage\nVOS = param.bytol(nom=0 * unit.mV, tol=150 * unit.uV, rel=False, tag="VOS")\n```\n\nDerived parameters use a decorator to map worst case input parameters to function arguments (`derive.byev`, `derive.bymc`, or `derive.byrss`).\n\n```python\n# define the output voltage\n@derive.byev(r1=R1, r2=R2, r3=R3, r4=R4, r5=R5, vos=VOS)\ndef VO(vbus, iload, r1, r2, r3, r4, r5, vos):\n    vp = vbus * r3 / (r2 + r3)\n    vn = vp + vos\n    vo = vn - (vbus - r1 * iload - vn) * r5 / r4\n    return vo\n\n# define the end-to-end uncertainty\n@derive.byev(r1=R1, r2=R2, r3=R3, r4=R4, r5=R5, vos=VOS)\ndef IUNC(r1, r2, r3, r4, r5, vos, vbus, iload):\n    vo = VO(vbus, iload, r1, r2, r3, r4, r5, vos)\n    return vo / VO(vbus, iload).nom * iload - iload\n```\n\nThe worst case solution is determined by brute force. If desired, the resulting derived parameter can then be used in the definition of another derived parameter to build up a more complicated analysis.\n\n```python\n# calculate at 36V, 1A operating point\nVOUT_1A = VO(vbus=36 * unit.V, iload=1 * unit.A, tag="VOUT_1A")\nIUNC_1A = IUNC(vbus=36 * unit.V, iload=1 * unit.A, tag="IUNC_1A")\n\nprint([VOUT_1A, IUNC_1A])\n\n# [VOUT_1A: 5.045 V (nom), 3.647 V (lb), 6.387 V (ub),\n#  IUNC_1A: 0 A (nom), -277 mA (lb), 266 mA (ub)]\n```\n\nParameter units are supported via the default [Pint](https://pypi.org/project/Pint/) `UnitRegistry` object. Results can also be further analyzed for their uncertainty drivers by performing a sensitivity study (`ss()`).\n\n```python\n# perform sensitivity study at the 36V, 1A operating point\nIUNC_1A_sensitivities = [\n    IUNC_1A(tag="IUNC_1A-R1-sens").ss(R1),\n    IUNC_1A(tag="IUNC_1A-VOS-sens").ss(VOS),\n    IUNC_1A(tag="IUNC_1A-R2-thru-R5-sens").ss([R2, R3, R4, R5]),\n]\n\nprint(IUNC_1A_sensitivities)\n\n# [IUNC_1A-R1-sens: 0 A (nom), -10 mA (lb), 10 mA (ub),\n#  IUNC_1A-VOS-sens: 0 A (nom), -1.53 mA (lb), 1.53 mA (ub),\n#  IUNC_1A-R2-thru-R5-sens: 0 A (nom), -265.3 mA (lb), 254.7 mA (ub)]\n```\n\n## Installation\n\n`pip install worstcase`\n',
    'author': 'amosborne',
    'author_email': 'amosborne@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/amosborne/worstcase',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
