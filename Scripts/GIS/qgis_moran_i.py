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

        # Output will be a feature sink for now: CHANGE TO TABLE | CSV!!!
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr("Output Layer:")
            )
        )


    # ------------------------------------------------------------------------------------------------------------------
    # The following function defines the main logic of the tool

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(
            parameters,
            self.INPUT,
            context
        )

        # If source was not found, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSourceError method to return a standard
        # helper text for when a source cannot be evaluated
        if source is None:
            raise QgsProcessingException(self.invalidSourceError(parameters, self.INPUT))

        (sink, dest_id) = self.parameterAsSink(
            parameters,
            self.OUTPUT,
            context,
            source.fields(),
            source.wkbType(),
            source.sourceCrs()
        )

        # Send some information to the user
        feedback.pushInfo('CRS is {}'.format(source.sourceCrs().authid()))

        # If sink was not created, throw an exception to indicate that the algorithm
        # encountered a fatal error. The exception text can be any string, but in this
        # case we use the pre-built invalidSinkError method to return a standard
        # helper text for when a sink cannot be evaluated
        if sink is None:
            raise QgsProcessingException(self.invalidSinkError(parameters, self.OUTPUT))

        # Compute the number of steps to display within the progress bar and
        # get features from source
        total = 100.0 / source.featureCount() if source.featureCount() else 0
        features = source.getFeatures()

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break

            # Add a feature in the sink
            sink.addFeature(feature, QgsFeatureSink.FastInsert)

            # Update the progress bar
            feedback.setProgress(int(current * total))

        # To run another Processing algorithm as part of this algorithm, you can use
        # processing.run(...). Make sure you pass the current context and feedback
        # to processing.run to ensure that all temporary layer outputs are available
        # to the executed algorithm, and that the executed algorithm can send feedback
        # reports to the user (and correctly handle cancellation and progress reports!)
        if False:
            buffered_layer = processing.run("native:buffer", {
                'INPUT': dest_id,
                'DISTANCE': 1.5,
                'SEGMENTS': 5,
                'END_CAP_STYLE': 0,
                'JOIN_STYLE': 0,
                'MITER_LIMIT': 2,
                'DISSOLVE': False,
                'OUTPUT': 'memory:'
            }, context=context, feedback=feedback)['OUTPUT']

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {self.OUTPUT: dest_id}
