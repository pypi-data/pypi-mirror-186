# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['omars_analysis']

package_data = \
{'': ['*'], 'omars_analysis': ['data/*']}

install_requires = \
['numpy>=1.23.5,<2.0.0', 'scipy>=1.9.3,<2.0.0']

setup_kwargs = {
    'name': 'omars-analysis',
    'version': '1.0.7',
    'description': '',
    'long_description': '# Documentation for package omars-analysis\n\nThis package has one function \'get_omars_analysis\'\n\nFirst run the following:\n\n```python\nfrom omars_analysis.main import get_omars_analysis\n```\n\nRunning the above command will make the function \'get_omars_analysis\' available for use.\n\n## Function usage\n\nThe function can be used with nine inputs (only the first two are required):\n\n- smat\n  \n  the first input is the design matrix. This should be a numpy array. The design matrix need not be coded, however it must only consist of continuous variables. The function is meant to be used with designs that have all factors either with two levels or three levels per factor column. The design should **NOT** consist of headers. The design matrix should not consist of second order effects since this will be built internally in the function.\n\n- cy\n  \n  This is the response. This should be a one dimensional column vector (1-D numpy).\n\n- qheredity\n  \n  This is to specify heredity constraints for quadratic effects. The accepted inputs are \'y\' or \'n\' (\'y\'- strong heredity, \'n\'- no heredity, \'n\'- No heredity). The input must be a string in lowercase. The default is \'n\'.\n\n- iheredity\n  \n  This is to specify heredity constraints for two-factor interaction effects. The accepted inputs are \'s\', \'w\' or \'n\' (\'s\'- strong heredity, \'w\'- weak heredity, \'n\'- no heredity). The input must be a string in lowercase. The default is \'n\'.\n\n- alpha\n  Here the three different alpha values can be specified (refer paper for mor information). The input must be a list of alpha values in float format. The default value for this parameter is [0.05, 0.2, 0.2].\n\n- effects_to_drop\n  \n  This is to specify second order effects that must be excluded from the analysis. The input must be a list of strings. For example: [\'1_1\', \'2_3\']. This input specifies that the quadratic effect of the first factor and the interaction effect between factor two and three must be excluded from the second step of the analysis (subset selection). The default value for this parameter is an empty list.\n\n  Note: Entering interaction between factor one and two should be represented as \'1_2\' and not as \'2_1\'. The smaller factor number should always come first.\n\n- full\n  \n  \'n\' -  analysis is performed on the main effects only\n  \n  \'y\' - analysis is performed on the main effects and second order effects.\n\n  The default is set to \'y\'\n\n- force_me\n  \n  Here certain main effects can be forced into the model. This can be used in cases where a main effect is statistically insignificant but by only a small margin. Forcing such main effects into the model can have an impact in reducing the updated estimate of the error.\n  \n  The input can be defined as a list of string values corresponding to the factor number that is to be forced. eg: [\'3\', \'4\']. The default value for this parameter is an empty list.\n\n- user_limit_for_step_two\n  \n  The max limit on the number of second order effects to be fit can be specified using this parameter. The input should be an integer. The default value for this parameter is "None". If the user has specified a limit, then this limit will be considered, otherwise the limit on the terms is case dependent. More information is given below:\n  - No limit is set if all second order terms for all factors are jointly estimable.\n  - The limit is set to the number of second order terms specified using the heredity parameters (qheredity and iheredity), if this number is less than the maximum number of jointly estimable terms for all second order effects.\n  - Otherwise, the limit will be always set to run size divided by four (refer paper).\n\n## Output\n\nThe function will auttomatically print out the following:\n\n- Initial error degrees of freedom available\n- Initial estimate of the error variance\n- Main effects that are declared active\n- p-values for the different main effects tested during main effects selection\n- Main effects that are forced into the model (if any)\n- Updated estimate of the error variance taking into account inactive main effects\n- p-value for the initial F-test (Step 4a from paper)\n- Limit on the number of terms for subset selection (Step 4b from paper)\n- Rank of matrix with only second order terms (this gives the possible maximum number of second order terms that can be fit during subset selection)\n- p-value for the final F-test (Step 4b from paper)\n- Active interaction effects\n- Active quadratic effects\n\nThe function outputs one return value. This value is the p-value from the last failed F-test during the second order effects selection.\n\n## Example code\n\n```python\noutput = get_omars_analysis(smat=design_matrix, cy=response, alpha=[0.05, 0.2, 0.2], qheredity=\'n\', iheredity=\'n\', effects_to_drop=[\'1_3\', \'2_6\'], full=\'y\', force_me=[\'4\'], user_limit_for_step_two=None)\n```\n',
    'author': 'Mohammed Saif Ismail Hameed',
    'author_email': 'saifismailh@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/saif-ismail/omars_analysis/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
