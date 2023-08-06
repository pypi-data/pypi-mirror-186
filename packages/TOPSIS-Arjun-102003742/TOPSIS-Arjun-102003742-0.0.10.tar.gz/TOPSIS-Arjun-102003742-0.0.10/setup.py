from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.10'
DESCRIPTION = 'TOPSIS-Ranking Algorithm for MUltiple Criteria Decision Making'
LONG_DESCRIPTION = 'TOPSIS, or the Technique for Order Preference by Similarity to an Ideal Solution, is a method used in multi-criteria decision-making (MCDM) to determine the best alternative among a set of options.It works by first defining a set of criteria and then weighting these criteria based on their relative importance. Next, the alternatives are evaluated against each criterion and a performance score is assigned to each alternative for each criterion. The scores are then normalized to ensure that all criteria are on the same scale.After normalization, the alternatives are then ranked according to their similarity to the "ideal solution," which is the alternative that has the best performance for each criterion. The alternative that is most similar to the ideal solution is considered the best alternative.The steps of the TOPSIS method can be summarized as follows:Define the decision problem and the alternatives to be considered Define the criteria and weight them according to their relative importance Evaluate the alternatives against the criteria and assign performance scores Normalize the performance scores Determine the distance of each alternative from the positive ideal solution and the negative ideal solution Rank the alternatives based on the distance from the positive ideal solution TOPSIS can be implemented in any programming language, and it is easy to understand, simple to use and computationally efficient.You can use this method to help make better decisions in your projects.'

# Setting up
setup(
    name="TOPSIS-Arjun-102003742",
    version=VERSION,
    author="Arjun Pundir",
    author_email="<arjunpundir1106@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy', 'sys', 'pandas'],
    keywords=['python', 'TOPSIS', 'Ranking', 'MCDM'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)