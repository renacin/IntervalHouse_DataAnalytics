# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: QGIS Python Implementation
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink)
from qgis import processing
# ----------------------------------------------------------------------------------------------------------------------


class Morans_I_Calculator(QgsProcessingAlgorithm):
    """
    This script attempts to calculate Moran's I statistic for a number of fields within
    a shapefile provided by the user. This tool requires the use of a centroid representation of
    the users data file.
    """

    # Constants used to refer to parameters and outputs.
    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'


    # ------------------------------------------------------------------------------------------------------------------
    # The Following Functions Are Used As Basic Setup Tools For The Script

    def createInstance(self):
        return Morans_I_Calculator()


    def tr(self, string):
        """ Returns a translatable string with the self.tr() function. """
        return QCoreApplication.translate('Processing', string)


    def name(self):
        """ Returns the algorithm name, used for identifying the algorithm. Can be found when hovering over tool option. """
        return "Morans_I"


    def displayName(self):
        """ Returns algorithm name for GUI. Can be found within rendered GUI. """
        return self.tr("Moran's I Calculation")


    def group(self):
        """ Returns the name of the group that this algorithm belongs to. If not present, group will be created. Can be found within Toolbox panel."""
        return self.tr("Python Tools")


    def groupId(self):
        """ Returns the unique ID of the group this algorithm belongs to. Can be found within Toolbox panel. """
        return "AnalysisTools"


    def shortHelpString(self):
        """ Returns a short helper string for the algorithm. Can be found within rendered GUI. """

        helper_string = """
        This script will calculate Moran's I statistic for each field within a provided shapefile.
        Data will be written to either a temporary table found within the layer legend, or a CSV as indicated by the user.
        """

        return self.tr(helper_string)


    # ------------------------------------------------------------------------------------------------------------------
    # The following function defines the main layout of inputs & outputs within the GUI

    def initAlgorithm(self, config=None):
        """ Defines the inputs and outputs of this script. """

        # Ask user for shapefile contaning fields that will be used to calculate Moran's I
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr("Input Layer:"),
                [QgsProcessing.TypeVectorAnyGeometry]
            )
        )

        # # Output will be a feature sink for now: CHANGE TO TABLE | CSV!!!
        # self.addParameter(
        #     QgsProcessingParameterFeatureSink(
        #         self.OUTPUT,
        #         self.tr("Output Layer:")
        #     )
        # )


    # ------------------------------------------------------------------------------------------------------------------
    # The following function defines the main logic of the tool

    def processAlgorithm(self, parameters, context, feedback):
        """ Here is where the processing itself takes place. """




        return None





"""
For Help See:
    + https://www.qgistutorials.com/id/docs/3/processing_python_scripts.html
    + https://www.youtube.com/watch?v=kkrqnj-iUHM
"""
