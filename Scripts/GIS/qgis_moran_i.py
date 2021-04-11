# Name:                                            Renacin Matadeen
# Date:                                               04/03/2021
# Title                   Interval House Data Analytics Project: QGIS Python Implementation
#
# ----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import time

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing, QgsProcessingParameterVectorDestination, QgsProcessingException,
                       QgsProcessingAlgorithm, QgsProcessingParameterFeatureSource, QgsProcessingParameterField,
                       QgsField, QgsFields)

from qgis import processing
# ----------------------------------------------------------------------------------------------------------------------


class Morans_I_Calculator(QgsProcessingAlgorithm):
    """
    This script attempts to calculate Moran's I statistic for a number of fields within
    a shapefile provided by the user. This tool requires the use of a centroid representation of
    the users data file.
    """

    # Constants used to refer to parameters and outputs.
    INPUT = "INPUT"
    UID_FIELD = "UID_FIELD"
    OUTPUT = "OUTPUT"


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
                [QgsProcessing.TypeVectorPolygon]
            )
        )

        # Ask user for field that will uniquely identify polygons
        self.addParameter(
            QgsProcessingParameterField(
                self.UID_FIELD,
                "Choose Field That IDs Polygons",
                "",
                self.INPUT))

        # Output will be a vector destination for now: CHANGE TO TABLE | CSV!!!
        self.addParameter(
            QgsProcessingParameterVectorDestination(
                self.OUTPUT,
                self.tr("Output Layer:")
            )
        )


    # ------------------------------------------------------------------------------------------------------------------
    # The following function defines the main logic of the tool

    def processAlgorithm(self, parameters, context, feedback):
        """ Here is where the processing itself takes place. """

        # Define input/output file that will store/provide data | Can be in memory or a file depending on user
        source = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )

        uid_field = self.parameterAsString(
                parameters,
                self.UID_FIELD,
                context)

        outputFile = self.parameterAsOutputLayer(
            parameters,
            self.OUTPUT,
            context
        )

        # Give user feedback | Introduce algorithm & first step | And check if user wants to cancel
        feedback.pushInfo("This algorithm will calculate Moran's I statistic for each field within the provided data layer.\n")


        # Step 1: Ensure number of polygons matches up with number of number of rows in user defined UID field
        if feedback.isCanceled():
            return {}
        features = source.getFeatures()
        user_uids = [f[uid_field] for f in features]


        # Step 2): Create dataframe index, and columns are the unique identifiers
        if feedback.isCanceled():
            return {}
        dist_matrix = {id:[0]*len(user_uids) for id in user_uids}
        df = pd.DataFrame(dist_matrix)
        df[uid_field] = user_uids
        df.insert(0, uid_field, user_uids, True)




        out_path = r"C:\Users\renac\Downloads\TESTDATA.csv"
        df.to_csv(out_path, index=False)



        # Step 2): Create Centroid Representation For Distance Calculation
        if feedback.isCanceled():
            return {}

        feedback.pushInfo("(Step 1): Creating Centroid Representation Of Polygon Layer.")

        # centroid_layer = processing.run("native:centroids",
        #     {
        #         'INPUT': parameters['INPUT'],
        #     },
        #     is_child_algorithm=True,
        #     context=context,
        #     feedback=feedback
        # )

        # Step 2): Create Centroid Representation For Distance Calculation


        return {}





"""
For Help See:
    + https://www.qgistutorials.com/id/docs/3/processing_python_scripts.html
    + https://www.youtube.com/watch?v=kkrqnj-iUHM
    + https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis-101-writing-a-processing-script/
    + https://anitagraser.com/2018/03/25/processing-script-template-for-qgis3/
"""
