# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ood_metrics']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.0,<4.0', 'numpy>=1.22,<2.0', 'scikit-learn>=1.0,<2.0']

setup_kwargs = {
    'name': 'ood-metrics',
    'version': '1.1.0',
    'description': 'Calculate common OOD detection metrics',
    'long_description': "# OOD Detection Metrics\n\nFunctions for computing metrics commonly used in the field of out-of-distribution (OOD) detection.\n\n[![tests](https://github.com/tayden/ood-metrics/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/tayden/ood-metrics/actions/workflows/tests.yml)\n\n## Installation\n\n`pip install ood-metrics`\n\n## Metrics functions\n\n### AUROC\n\nCalculate and return the area under the ROC curve using unthresholded predictions on the data and a binary true label.\n\n```python\nfrom ood_metrics import auroc\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nassert auroc(scores, labels) == 0.75\n```\n\n### AUPR\n\nCalculate and return the area under the Precision Recall curve using unthresholded predictions on the data and a binary true\nlabel.\n\n```python\nfrom ood_metrics import aupr\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nassert aupr(scores, labels) == 0.25\n```\n\n### FPR @ 95% TPR\n\nReturn the FPR when TPR is at least 95%.\n\n```python\nfrom ood_metrics import fpr_at_95_tpr\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nassert fpr_at_95_tpr(scores, labels) == 0.25\n```\n\n### Detection Error\n\nReturn the misclassification probability when TPR is 95%.\n\n```python\nfrom ood_metrics import detection_error\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nassert detection_error(scores, labels) == 0.05\n```\n\n### Calculate all stats\n\nUsing predictions and labels, return a dictionary containing all novelty detection performance statistics.\n\n```python\nfrom ood_metrics import calc_metrics\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nassert calc_metrics(scores, labels) == {\n    'fpr_at_95_tpr': 0.25,\n    'detection_error': 0.05,\n    'auroc': 0.75,\n    'aupr_in': 0.25,\n    'aupr_out': 0.94375\n}\n```\n\n## Plotting functions\n\n### Plot ROC\n\nPlot an ROC curve based on unthresholded predictions and true binary labels.\n\n```python\n\nfrom ood_metrics import plot_roc\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nplot_roc(scores, labels)\n# Generate Matplotlib AUROC plot\n```\n\n### Plot PR\n\nPlot an Precision-Recall curve based on unthresholded predictions and true binary labels.\n\n```python\n\nfrom ood_metrics import plot_pr\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nplot_pr(scores, labels)\n# Generate Matplotlib Precision-Recall plot\n```\n\n### Plot Barcode\n\nPlot a visualization showing inliers and outliers sorted by their prediction of novelty.\n\n```python\n\nfrom ood_metrics import plot_barcode\n\nlabels = [0, 0, 0, 1, 0]\nscores = [0.1, 0.3, 0.6, 0.9, 1.3]\n\nplot_barcode(scores, labels)\n# Shows visualization of sort order of labels occording to the scores.\n```\n",
    'author': 'Taylor Denouden',
    'author_email': 'taylordenouden@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tayden/ood-metrics',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
