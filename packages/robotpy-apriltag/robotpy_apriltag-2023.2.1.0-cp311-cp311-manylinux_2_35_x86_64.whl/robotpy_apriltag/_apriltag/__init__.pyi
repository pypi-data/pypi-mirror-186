from __future__ import annotations
import robotpy_apriltag._apriltag
import typing
import wpimath.geometry._geometry

__all__ = [
    "AprilTag",
    "AprilTagDetection",
    "AprilTagDetector",
    "AprilTagField",
    "AprilTagFieldLayout",
    "AprilTagPoseEstimate",
    "AprilTagPoseEstimator",
    "loadAprilTagLayoutField"
]


class AprilTag():
    def __eq__(self, arg0: AprilTag) -> bool: 
        """
        Checks equality between this AprilTag and another object.
        """
    def __init__(self) -> None: ...
    @property
    def ID(self) -> int:
        """
        :type: int
        """
    @ID.setter
    def ID(self, arg0: int) -> None:
        pass
    @property
    def pose(self) -> wpimath.geometry._geometry.Pose3d:
        """
        :type: wpimath.geometry._geometry.Pose3d
        """
    @pose.setter
    def pose(self, arg0: wpimath.geometry._geometry.Pose3d) -> None:
        pass
    __hash__ = None
    pass
class AprilTagDetection():
    """
    A detection of an AprilTag tag.
    """
    class Point():
        """
        A point. Used for center and corner points.
        """
        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, x: float, y: float) -> None: ...
        def __repr__(self) -> str: ...
        @property
        def x(self) -> float:
            """
            :type: float
            """
        @x.setter
        def x(self, arg0: float) -> None:
            pass
        @property
        def y(self) -> float:
            """
            :type: float
            """
        @y.setter
        def y(self, arg0: float) -> None:
            pass
        pass
    def __repr__(self) -> str: ...
    def getCenter(self) -> AprilTagDetection.Point: 
        """
        Gets the center of the detection in image pixel coordinates.

        :returns: Center point
        """
    def getCorner(self, ndx: int) -> AprilTagDetection.Point: 
        """
        Gets a corner of the tag in image pixel coordinates. These always
        wrap counter-clock wise around the tag.

        :param ndx: Corner index (range is 0-3, inclusive)

        :returns: Corner point
        """
    def getCorners(self, cornersBuf: typing.Tuple[float, float, float, float, float, float, float, float]) -> typing.Tuple[float, float, float, float, float, float, float, float]: 
        """
        Gets the corners of the tag in image pixel coordinates. These always
        wrap counter-clock wise around the tag.

        :param cornersBuf: Corner point array (X and Y for each corner in order)

        :returns: Corner point array (copy of cornersBuf span)
        """
    def getDecisionMargin(self) -> float: 
        """
        Gets a measure of the quality of the binary decoding process: the
        average difference between the intensity of a data bit versus
        the decision threshold. Higher numbers roughly indicate better
        decodes. This is a reasonable measure of detection accuracy
        only for very small tags-- not effective for larger tags (where
        we could have sampled anywhere within a bit cell and still
        gotten a good detection.)

        :returns: Decision margin
        """
    def getFamily(self) -> str: 
        """
        Gets the decoded tag's family name.

        :returns: Decoded family name
        """
    def getHamming(self) -> int: 
        """
        Gets how many error bits were corrected. Note: accepting large numbers of
        corrected errors leads to greatly increased false positive rates.
        NOTE: As of this implementation, the detector cannot detect tags with
        a hamming distance greater than 2.

        :returns: Hamming distance (number of corrected error bits)
        """
    def getHomography(self) -> typing.Tuple[float, float, float, float, float, float, float, float, float]: 
        """
        Gets the 3x3 homography matrix describing the projection from an
        "ideal" tag (with corners at (-1,1), (1,1), (1,-1), and (-1,
        -1)) to pixels in the image.

        :returns: Homography matrix data
        """
    def getHomographyMatrix(self) -> numpy.ndarray[numpy.float64, _Shape[3, 3]]: 
        """
        Gets the 3x3 homography matrix describing the projection from an
        "ideal" tag (with corners at (-1,1), (1,1), (1,-1), and (-1,
        -1)) to pixels in the image.

        :returns: Homography matrix
        """
    def getId(self) -> int: 
        """
        Gets the decoded ID of the tag.

        :returns: Decoded ID
        """
    pass
class AprilTagDetector():
    """
    An AprilTag detector engine. This is expensive to set up and tear down, so
    most use cases should only create one of these, add a family to it, set up
    any other configuration, and repeatedly call Detect().
    """
    class Config():
        """
        Detector configuration.
        """
        def __eq__(self, arg0: AprilTagDetector.Config) -> bool: ...
        def __init__(self) -> None: ...
        @property
        def debug(self) -> bool:
            """
            Debug mode. When true, the decoder writes a variety of debugging images
            to the current working directory at various stages through the detection
            process. This is slow and should *not* be used on space-limited systems
            such as the RoboRIO. Default is disabled (false).

            :type: bool
            """
        @debug.setter
        def debug(self, arg0: bool) -> None:
            """
            Debug mode. When true, the decoder writes a variety of debugging images
            to the current working directory at various stages through the detection
            process. This is slow and should *not* be used on space-limited systems
            such as the RoboRIO. Default is disabled (false).
            """
        @property
        def decodeSharpening(self) -> float:
            """
            How much sharpening should be done to decoded images. This can help
            decode small tags but may or may not help in odd lighting conditions or
            low light conditions. Default is 0.25.

            :type: float
            """
        @decodeSharpening.setter
        def decodeSharpening(self, arg0: float) -> None:
            """
            How much sharpening should be done to decoded images. This can help
            decode small tags but may or may not help in odd lighting conditions or
            low light conditions. Default is 0.25.
            """
        @property
        def numThreads(self) -> int:
            """
            How many threads should be used for computation. Default is
            single-threaded operation (1 thread).

            :type: int
            """
        @numThreads.setter
        def numThreads(self, arg0: int) -> None:
            """
            How many threads should be used for computation. Default is
            single-threaded operation (1 thread).
            """
        @property
        def quadDecimate(self) -> float:
            """
            Quad decimation. Detection of quads can be done on a lower-resolution
            image, improving speed at a cost of pose accuracy and a slight decrease
            in detection rate. Decoding the binary payload is still done at full
            resolution. Default is 2.0.

            :type: float
            """
        @quadDecimate.setter
        def quadDecimate(self, arg0: float) -> None:
            """
            Quad decimation. Detection of quads can be done on a lower-resolution
            image, improving speed at a cost of pose accuracy and a slight decrease
            in detection rate. Decoding the binary payload is still done at full
            resolution. Default is 2.0.
            """
        @property
        def quadSigma(self) -> float:
            """
            What Gaussian blur should be applied to the segmented image (used for
            quad detection). Very noisy images benefit from non-zero values (e.g.
            0.8). Default is 0.0.

            :type: float
            """
        @quadSigma.setter
        def quadSigma(self, arg0: float) -> None:
            """
            What Gaussian blur should be applied to the segmented image (used for
            quad detection). Very noisy images benefit from non-zero values (e.g.
            0.8). Default is 0.0.
            """
        @property
        def refineEdges(self) -> bool:
            """
            When true, the edges of the each quad are adjusted to "snap to" strong
            gradients nearby. This is useful when decimation is employed, as it can
            increase the quality of the initial quad estimate substantially.
            Generally recommended to be on (true). Default is true.

            Very computationally inexpensive. Option is ignored if
            quad_decimate = 1.

            :type: bool
            """
        @refineEdges.setter
        def refineEdges(self, arg0: bool) -> None:
            """
            When true, the edges of the each quad are adjusted to "snap to" strong
            gradients nearby. This is useful when decimation is employed, as it can
            increase the quality of the initial quad estimate substantially.
            Generally recommended to be on (true). Default is true.

            Very computationally inexpensive. Option is ignored if
            quad_decimate = 1.
            """
        __hash__ = None
        pass
    class QuadThresholdParameters():
        """
        Quad threshold parameters.
        """
        def __eq__(self, arg0: AprilTagDetector.QuadThresholdParameters) -> bool: ...
        def __init__(self) -> None: ...
        @property
        def criticalAngle(self) -> radians:
            """
            Critical angle. The detector will reject quads where pairs of edges have
            angles that are close to straight or close to 180 degrees. Zero means
            that no quads are rejected. Default is 10 degrees.

            :type: radians
            """
        @criticalAngle.setter
        def criticalAngle(self, arg0: radians) -> None:
            """
            Critical angle. The detector will reject quads where pairs of edges have
            angles that are close to straight or close to 180 degrees. Zero means
            that no quads are rejected. Default is 10 degrees.
            """
        @property
        def deglitch(self) -> bool:
            """
            Whether the thresholded image be should be deglitched. Only useful for
            very noisy images. Default is disabled (false).

            :type: bool
            """
        @deglitch.setter
        def deglitch(self, arg0: bool) -> None:
            """
            Whether the thresholded image be should be deglitched. Only useful for
            very noisy images. Default is disabled (false).
            """
        @property
        def maxLineFitMSE(self) -> float:
            """
            When fitting lines to the contours, the maximum mean squared error
            allowed. This is useful in rejecting contours that are far from being
            quad shaped; rejecting these quads "early" saves expensive decoding
            processing. Default is 10.0.

            :type: float
            """
        @maxLineFitMSE.setter
        def maxLineFitMSE(self, arg0: float) -> None:
            """
            When fitting lines to the contours, the maximum mean squared error
            allowed. This is useful in rejecting contours that are far from being
            quad shaped; rejecting these quads "early" saves expensive decoding
            processing. Default is 10.0.
            """
        @property
        def maxNumMaxima(self) -> int:
            """
            How many corner candidates to consider when segmenting a group of pixels
            into a quad. Default is 10.

            :type: int
            """
        @maxNumMaxima.setter
        def maxNumMaxima(self, arg0: int) -> None:
            """
            How many corner candidates to consider when segmenting a group of pixels
            into a quad. Default is 10.
            """
        @property
        def minClusterPixels(self) -> int:
            """
            Threshold used to reject quads containing too few pixels. Default is 5
            pixels.

            :type: int
            """
        @minClusterPixels.setter
        def minClusterPixels(self, arg0: int) -> None:
            """
            Threshold used to reject quads containing too few pixels. Default is 5
            pixels.
            """
        @property
        def minWhiteBlackDiff(self) -> int:
            """
            Minimum brightness offset. When we build our model of black & white
            pixels, we add an extra check that the white model must be (overall)
            brighter than the black model. How much brighter? (in pixel values,
            [0,255]). Default is 5.

            :type: int
            """
        @minWhiteBlackDiff.setter
        def minWhiteBlackDiff(self, arg0: int) -> None:
            """
            Minimum brightness offset. When we build our model of black & white
            pixels, we add an extra check that the white model must be (overall)
            brighter than the black model. How much brighter? (in pixel values,
            [0,255]). Default is 5.
            """
        __hash__ = None
        pass
    class _Results():
        """
        Array of detection results. Each array element is a pointer to an
        AprilTagDetection.
        """
        def get(self, arg0: int) -> AprilTagDetection: ...
        pass
    def __init__(self) -> None: ...
    def addFamily(self, fam: str, bitsCorrected: int = 2) -> bool: 
        """
        Adds a family of tags to be detected.

        :param fam:           Family name, e.g. "tag16h5"
        :param bitsCorrected: 

        :returns: False if family can't be found
        """
    def clearFamilies(self) -> None: 
        """
        Unregister all families.
        """
    def detect(self, image: buffer) -> typing.List[AprilTagDetection]: 
        """
        Detect tags from an 8-bit grayscale image with shape (width, height)

        :return: list of results
        """
    def getConfig(self) -> AprilTagDetector.Config: 
        """
        Gets detector configuration.

        :returns: Configuration
        """
    def getQuadThresholdParameters(self) -> AprilTagDetector.QuadThresholdParameters: 
        """
        Gets quad threshold parameters.

        :returns: Parameters
        """
    def removeFamily(self, fam: str) -> None: 
        """
        Removes a family of tags from the detector.

        :param fam: Family name, e.g. "tag16h5"
        """
    def setConfig(self, config: AprilTagDetector.Config) -> None: 
        """
        Sets detector configuration.

        :param config: Configuration
        """
    def setQuadThresholdParameters(self, params: AprilTagDetector.QuadThresholdParameters) -> None: 
        """
        Sets quad threshold parameters.

        :param params: Parameters
        """
    pass
class AprilTagField():
    """
    Members:

      k2022RapidReact

      k2023ChargedUp

      kNumFields
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'k2022RapidReact': <AprilTagField.k2022RapidReact: 0>, 'k2023ChargedUp': <AprilTagField.k2023ChargedUp: 1>, 'kNumFields': <AprilTagField.kNumFields: 2>}
    k2022RapidReact: robotpy_apriltag._apriltag.AprilTagField # value = <AprilTagField.k2022RapidReact: 0>
    k2023ChargedUp: robotpy_apriltag._apriltag.AprilTagField # value = <AprilTagField.k2023ChargedUp: 1>
    kNumFields: robotpy_apriltag._apriltag.AprilTagField # value = <AprilTagField.kNumFields: 2>
    pass
class AprilTagFieldLayout():
    """
    Class for representing a layout of AprilTags on a field and reading them from
    a JSON format.

    The JSON format contains two top-level objects, "tags" and "field".
    The "tags" object is a list of all AprilTags contained within a layout. Each
    AprilTag serializes to a JSON object containing an ID and a Pose3d. The
    "field" object is a descriptor of the size of the field in meters with
    "width" and "length" values.  This is to account for arbitrary field sizes
    when transforming the poses.

    Pose3ds in the JSON are measured using the normal FRC coordinate system, NWU
    with the origin at the bottom-right corner of the blue alliance wall.
    SetOrigin(OriginPosition) can be used to change the poses returned from
    GetTagPose(int) to be from the perspective of a specific alliance.

    Tag poses represent the center of the tag, with a zero rotation representing
    a tag that is upright and facing away from the (blue) alliance wall (that is,
    towards the opposing alliance).
    """
    class OriginPosition():
        """
        Members:

          kBlueAllianceWallRightSide

          kRedAllianceWallRightSide
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        __members__: dict # value = {'kBlueAllianceWallRightSide': <OriginPosition.kBlueAllianceWallRightSide: 0>, 'kRedAllianceWallRightSide': <OriginPosition.kRedAllianceWallRightSide: 1>}
        kBlueAllianceWallRightSide: robotpy_apriltag._apriltag.AprilTagFieldLayout.OriginPosition # value = <OriginPosition.kBlueAllianceWallRightSide: 0>
        kRedAllianceWallRightSide: robotpy_apriltag._apriltag.AprilTagFieldLayout.OriginPosition # value = <OriginPosition.kRedAllianceWallRightSide: 1>
        pass
    def __eq__(self, arg0: AprilTagFieldLayout) -> bool: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a new AprilTagFieldLayout with values imported from a JSON file.

        :param path: Path of the JSON file to import from.

        Construct a new AprilTagFieldLayout from a vector of AprilTag objects.

        :param apriltags:   Vector of AprilTags.
        :param fieldLength: Length of field the layout is representing.
        :param fieldWidth:  Width of field the layout is representing.
        """
    @typing.overload
    def __init__(self, apriltags: typing.List[AprilTag], fieldLength: meters, fieldWidth: meters) -> None: ...
    @typing.overload
    def __init__(self, path: str) -> None: ...
    def getTagPose(self, ID: int) -> typing.Optional[wpimath.geometry._geometry.Pose3d]: 
        """
        Gets an AprilTag pose by its ID.

        :param ID: The ID of the tag.

        :returns: The pose corresponding to the ID that was passed in or an empty
                  optional if a tag with that ID is not found.
        """
    def serialize(self, path: str) -> None: 
        """
        Serializes an AprilTagFieldLayout to a JSON file.

        :param path: The path to write the JSON file to.
        """
    @typing.overload
    def setOrigin(self, origin: AprilTagFieldLayout.OriginPosition) -> None: 
        """
        Sets the origin based on a predefined enumeration of coordinate frame
        origins. The origins are calculated from the field dimensions.

        This transforms the Pose3ds returned by GetTagPose(int) to return the
        correct pose relative to a predefined coordinate frame.

        :param origin: The predefined origin

        Sets the origin for tag pose transformation.

        This tranforms the Pose3ds returned by GetTagPose(int) to return the
        correct pose relative to the provided origin.

        :param origin: The new origin for tag transformations
        """
    @typing.overload
    def setOrigin(self, origin: wpimath.geometry._geometry.Pose3d) -> None: ...
    __hash__ = None
    pass
class AprilTagPoseEstimate():
    """
    A pair of AprilTag pose estimates.
    """
    def __init__(self) -> None: ...
    def getAmbiguity(self) -> float: 
        """
        Gets the ratio of pose reprojection errors, called ambiguity. Numbers
        above 0.2 are likely to be ambiguous.

        :returns: The ratio of pose reprojection errors.
        """
    @property
    def error1(self) -> float:
        """
        Object-space error of pose 1.

        :type: float
        """
    @error1.setter
    def error1(self, arg0: float) -> None:
        """
        Object-space error of pose 1.
        """
    @property
    def error2(self) -> float:
        """
        Object-space error of pose 2.

        :type: float
        """
    @error2.setter
    def error2(self, arg0: float) -> None:
        """
        Object-space error of pose 2.
        """
    @property
    def pose1(self) -> wpimath.geometry._geometry.Transform3d:
        """
        Pose 1.

        :type: wpimath.geometry._geometry.Transform3d
        """
    @pose1.setter
    def pose1(self, arg0: wpimath.geometry._geometry.Transform3d) -> None:
        """
        Pose 1.
        """
    @property
    def pose2(self) -> wpimath.geometry._geometry.Transform3d:
        """
        Pose 2.

        :type: wpimath.geometry._geometry.Transform3d
        """
    @pose2.setter
    def pose2(self, arg0: wpimath.geometry._geometry.Transform3d) -> None:
        """
        Pose 2.
        """
    pass
class AprilTagPoseEstimator():
    """
    Pose estimators for AprilTag tags.
    """
    class Config():
        """
        Configuration for the pose estimator.
        """
        def __eq__(self, arg0: AprilTagPoseEstimator.Config) -> bool: ...
        def __init__(self, tagSize: meters, fx: float, fy: float, cx: float, cy: float) -> None: ...
        @property
        def cx(self) -> float:
            """
            Camera horizontal focal center, in pixels.

            :type: float
            """
        @cx.setter
        def cx(self, arg0: float) -> None:
            """
            Camera horizontal focal center, in pixels.
            """
        @property
        def cy(self) -> float:
            """
            Camera vertical focal center, in pixels.

            :type: float
            """
        @cy.setter
        def cy(self, arg0: float) -> None:
            """
            Camera vertical focal center, in pixels.
            """
        @property
        def fx(self) -> float:
            """
            Camera horizontal focal length, in pixels.

            :type: float
            """
        @fx.setter
        def fx(self, arg0: float) -> None:
            """
            Camera horizontal focal length, in pixels.
            """
        @property
        def fy(self) -> float:
            """
            Camera vertical focal length, in pixels.

            :type: float
            """
        @fy.setter
        def fy(self, arg0: float) -> None:
            """
            Camera vertical focal length, in pixels.
            """
        @property
        def tagSize(self) -> meters:
            """
            The tag size.

            :type: meters
            """
        @tagSize.setter
        def tagSize(self, arg0: meters) -> None:
            """
            The tag size.
            """
        __hash__ = None
        pass
    def __init__(self, config: AprilTagPoseEstimator.Config) -> None: 
        """
        Creates estimator.

        :param config: Configuration
        """
    @typing.overload
    def estimate(self, detection: AprilTagDetection) -> wpimath.geometry._geometry.Transform3d: 
        """
        Estimates tag pose. This method is an easier to use interface to
        EstimatePoseOrthogonalIteration(), running 50 iterations and returning the
        pose with the lower object-space error.

        :param detection: Tag detection

        :returns: Pose estimate

        Estimates tag pose. This method is an easier to use interface to
        EstimatePoseOrthogonalIteration(), running 50 iterations and returning the
        pose with the lower object-space error.

        :param homography: Homography 3x3 matrix data
        :param corners:    Corner point array (X and Y for each corner in order)

        :returns: Pose estimate
        """
    @typing.overload
    def estimate(self, homography: typing.Tuple[float, float, float, float, float, float, float, float, float], corners: typing.Tuple[float, float, float, float, float, float, float, float]) -> wpimath.geometry._geometry.Transform3d: ...
    @typing.overload
    def estimateHomography(self, detection: AprilTagDetection) -> wpimath.geometry._geometry.Transform3d: 
        """
        Estimates the pose of the tag using the homography method described in [1].

        :param detection: Tag detection

        :returns: Pose estimate

        Estimates the pose of the tag using the homography method described in [1].

        :param homography: Homography 3x3 matrix data

        :returns: Pose estimate
        """
    @typing.overload
    def estimateHomography(self, homography: typing.Tuple[float, float, float, float, float, float, float, float, float]) -> wpimath.geometry._geometry.Transform3d: ...
    @typing.overload
    def estimateOrthogonalIteration(self, detection: AprilTagDetection, nIters: int) -> AprilTagPoseEstimate: 
        """
        Estimates the pose of the tag. This returns one or two possible poses for
        the tag, along with the object-space error of each.

        This uses the homography method described in [1] for the initial estimate.
        Then Orthogonal Iteration [2] is used to refine this estimate. Then [3] is
        used to find a potential second local minima and Orthogonal Iteration is
        used to refine this second estimate.

        [1]: E. Olson, “Apriltag: A robust and flexible visual fiducial system,” in
        2011 IEEE International Conference on Robotics and Automation,
        May 2011, pp. 3400–3407.
        [2]: Lu, G. D. Hager and E. Mjolsness, "Fast and globally convergent pose
        estimation from video images," in IEEE Transactions on Pattern
        Analysis and Machine Intelligence, vol. 22, no. 6, pp. 610-622, June 2000.
        doi: 10.1109/34.862199
        [3]: Schweighofer and A. Pinz, "Robust Pose Estimation from a Planar
        Target," in IEEE Transactions on Pattern Analysis and Machine Intelligence,
        vol. 28, no. 12, pp. 2024-2030, Dec. 2006. doi: 10.1109/TPAMI.2006.252

        :param detection: Tag detection
        :param nIters:    Number of iterations

        :returns: Initial and (possibly) second pose estimates

        Estimates the pose of the tag. This returns one or two possible poses for
        the tag, along with the object-space error of each.

        :param homography: Homography 3x3 matrix data
        :param corners:    Corner point array (X and Y for each corner in order)
        :param nIters:     Number of iterations

        :returns: Initial and (possibly) second pose estimates
        """
    @typing.overload
    def estimateOrthogonalIteration(self, homography: typing.Tuple[float, float, float, float, float, float, float, float, float], corners: typing.Tuple[float, float, float, float, float, float, float, float], nIters: int) -> AprilTagPoseEstimate: ...
    def getConfig(self) -> AprilTagPoseEstimator.Config: 
        """
        Gets estimator configuration.

        :returns: Configuration
        """
    def setConfig(self, config: AprilTagPoseEstimator.Config) -> None: 
        """
        Sets estimator configuration.

        :param config: Configuration
        """
    pass
def loadAprilTagLayoutField(field: AprilTagField) -> AprilTagFieldLayout:
    """
    Loads an AprilTagFieldLayout from a predefined field

    :param field: The predefined field
    """
