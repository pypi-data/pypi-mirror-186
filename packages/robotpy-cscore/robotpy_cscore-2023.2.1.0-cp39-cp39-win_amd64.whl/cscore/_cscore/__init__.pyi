from __future__ import annotations
import cscore._cscore
import typing

__all__ = [
    "AxisCamera",
    "CameraServer",
    "CvSink",
    "CvSource",
    "HttpCamera",
    "ImageSink",
    "ImageSource",
    "MjpegServer",
    "RawEvent",
    "UsbCamera",
    "UsbCameraInfo",
    "VideoCamera",
    "VideoEvent",
    "VideoListener",
    "VideoMode",
    "VideoProperty",
    "VideoSink",
    "VideoSource",
    "runMainRunLoop",
    "runMainRunLoopTimeout",
    "stopMainRunLoop"
]


class VideoSource():
    """
    A source for video that provides a sequence of frames.
    """
    class ConnectionStrategy():
        """
        Connection strategy.  Used for SetConnectionStrategy().

        Members:

          kConnectionAutoManage : Automatically connect or disconnect based on whether any sinks are
        connected to this source.  This is the default behavior.

          kConnectionKeepOpen : Try to keep the connection open regardless of whether any sinks are
        connected.

          kConnectionForceClose : Never open the connection.  If this is set when the connection is open,
        close the connection.
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
        __members__: dict # value = {'kConnectionAutoManage': <ConnectionStrategy.kConnectionAutoManage: 0>, 'kConnectionKeepOpen': <ConnectionStrategy.kConnectionKeepOpen: 1>, 'kConnectionForceClose': <ConnectionStrategy.kConnectionForceClose: 2>}
        kConnectionAutoManage: cscore._cscore.VideoSource.ConnectionStrategy # value = <ConnectionStrategy.kConnectionAutoManage: 0>
        kConnectionForceClose: cscore._cscore.VideoSource.ConnectionStrategy # value = <ConnectionStrategy.kConnectionForceClose: 2>
        kConnectionKeepOpen: cscore._cscore.VideoSource.ConnectionStrategy # value = <ConnectionStrategy.kConnectionKeepOpen: 1>
        pass
    class Kind():
        """
        Members:

          kUnknown

          kUsb

          kHttp

          kCv
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
        __members__: dict # value = {'kUnknown': <Kind.kUnknown: 0>, 'kUsb': <Kind.kUsb: 1>, 'kHttp': <Kind.kHttp: 2>, 'kCv': <Kind.kCv: 4>}
        kCv: cscore._cscore.VideoSource.Kind # value = <Kind.kCv: 4>
        kHttp: cscore._cscore.VideoSource.Kind # value = <Kind.kHttp: 2>
        kUnknown: cscore._cscore.VideoSource.Kind # value = <Kind.kUnknown: 0>
        kUsb: cscore._cscore.VideoSource.Kind # value = <Kind.kUsb: 1>
        pass
    def __eq__(self, arg0: VideoSource) -> bool: ...
    def __init__(self) -> None: ...
    def enumerateProperties(self) -> typing.List[VideoProperty]: 
        """
        Enumerate all properties of this source.
        """
    def enumerateSinks(self) -> typing.List[VideoSink]: 
        """
        Enumerate all sinks connected to this source.

        :returns: Vector of sinks.
        """
    @staticmethod
    def enumerateSources() -> typing.List[VideoSource]: 
        """
        Enumerate all existing sources.

        :returns: Vector of sources.
        """
    def enumerateVideoModes(self) -> typing.List[VideoMode]: 
        """
        Enumerate all known video modes for this source.
        """
    def getActualDataRate(self) -> float: 
        """
        Get the data rate (in bytes per second).

        :returns: Data rate averaged over the telemetry period.
        """
    def getActualFPS(self) -> float: 
        """
        Get the actual FPS.

        :returns: Actual FPS averaged over the telemetry period.
        """
    def getConfigJson(self) -> str: 
        """
        Get a JSON configuration string.

        :returns: JSON configuration string
        """
    def getConfigJsonObject(self) -> json: 
        """
        Get a JSON configuration object.

        :returns: JSON configuration object
        """
    def getDescription(self) -> str: 
        """
        Get the source description.  This is source-kind specific.
        """
    def getHandle(self) -> int: ...
    def getKind(self) -> VideoSource.Kind: 
        """
        Get the kind of the source.
        """
    def getLastFrameTime(self) -> int: 
        """
        Get the last time a frame was captured.
        This uses the same time base as wpi::Now().

        :returns: Time in 1 us increments.
        """
    def getLastStatus(self) -> int: ...
    def getName(self) -> str: 
        """
        Get the name of the source.  The name is an arbitrary identifier
        provided when the source is created, and should be unique.
        """
    def getProperty(self, name: str) -> VideoProperty: 
        """
        Get a property.

        :param name: Property name

        :returns: Property contents (of kind Property::kNone if no property with
                  the given name exists)
        """
    def getVideoMode(self) -> VideoMode: 
        """
        Get the current video mode.
        """
    def isConnected(self) -> bool: 
        """
        Is the source currently connected to whatever is providing the images?
        """
    def isEnabled(self) -> bool: 
        """
        Gets source enable status.  This is determined with a combination of
        connection strategy and the number of sinks connected.

        :returns: True if enabled, false otherwise.
        """
    @typing.overload
    def setConfigJson(self, config: json) -> bool: 
        """
        Set video mode and properties from a JSON configuration string.

        The format of the JSON input is:

        ::

          {
              "pixel format": "MJPEG", "YUYV", etc
              "width": video mode width
              "height": video mode height
              "fps": video mode fps
              "brightness": percentage brightness
              "white balance": "auto", "hold", or value
              "exposure": "auto", "hold", or value
              "properties": [
                  {
                      "name": property name
                      "value": property value
                  }
              ]
          }

        :param config: configuration

        :returns: True if set successfully

        Set video mode and properties from a JSON configuration object.

        :param config: configuration

        :returns: True if set successfully
        """
    @typing.overload
    def setConfigJson(self, config: str) -> bool: ...
    def setConnectionStrategy(self, strategy: VideoSource.ConnectionStrategy) -> None: 
        """
        Sets the connection strategy.  By default, the source will automatically
        connect or disconnect based on whether any sinks are connected.

        This function is non-blocking; look for either a connection open or
        close event or call IsConnected() to determine the connection state.

        :param strategy: connection strategy (auto, keep open, or force close)
        """
    def setFPS(self, fps: int) -> bool: 
        """
        Set the frames per second (FPS).

        :param fps: desired FPS

        :returns: True if set successfully
        """
    def setPixelFormat(self, pixelFormat: VideoMode.PixelFormat) -> bool: 
        """
        Set the pixel format.

        :param pixelFormat: desired pixel format

        :returns: True if set successfully
        """
    def setResolution(self, width: int, height: int) -> bool: 
        """
        Set the resolution.

        :param width:  desired width
        :param height: desired height

        :returns: True if set successfully
        """
    @typing.overload
    def setVideoMode(self, mode: VideoMode) -> bool: 
        """
        Set the video mode.

        :param mode: Video mode

        Set the video mode.

        :param pixelFormat: desired pixel format
        :param width:       desired width
        :param height:      desired height
        :param fps:         desired FPS

        :returns: True if set successfully
        """
    @typing.overload
    def setVideoMode(self, pixelFormat: VideoMode.PixelFormat, width: int, height: int, fps: int) -> bool: ...
    __hash__ = None
    pass
class CameraServer():
    """
    Singleton class for creating and keeping camera servers.

    Also publishes camera information to NetworkTables.
    """
    @staticmethod
    @typing.overload
    def addAxisCamera(host: str) -> AxisCamera: 
        """
        Adds an Axis IP camera.

        This overload calls AddAxisCamera() with name "Axis Camera".

        :param host: Camera host IP or DNS name (e.g. "10.x.y.11")

        Adds an Axis IP camera.

        This overload calls AddAxisCamera() with name "Axis Camera".

        :param hosts: Array of Camera host IPs/DNS names

        Adds an Axis IP camera.

        :param name: The name to give the camera
        :param host: Camera host IP or DNS name (e.g. "10.x.y.11")

        Adds an Axis IP camera.

        :param name:  The name to give the camera
        :param hosts: Array of Camera host IPs/DNS names
        """
    @staticmethod
    @typing.overload
    def addAxisCamera(hosts: typing.List[str]) -> AxisCamera: ...
    @staticmethod
    @typing.overload
    def addAxisCamera(name: str, host: str) -> AxisCamera: ...
    @staticmethod
    @typing.overload
    def addAxisCamera(name: str, hosts: typing.List[str]) -> AxisCamera: ...
    @staticmethod
    def addCamera(camera: VideoSource) -> None: 
        """
        Adds an already created camera.

        :param camera: Camera
        """
    @staticmethod
    @typing.overload
    def addServer(name: str) -> MjpegServer: 
        """
        Adds a MJPEG server at the next available port.

        :param name: Server name

        Adds a MJPEG server.

        :param name: Server name
        :param port: Port number

        Adds an already created server.

        :param server: Server
        """
    @staticmethod
    @typing.overload
    def addServer(name: str, port: int) -> MjpegServer: ...
    @staticmethod
    @typing.overload
    def addServer(server: VideoSink) -> None: ...
    @staticmethod
    def addSwitchedCamera(name: str) -> MjpegServer: 
        """
        Adds a virtual camera for switching between two streams.  Unlike the
        other addCamera methods, this returns a VideoSink rather than a
        VideoSource.  Calling SetSource() on the returned object can be used
        to switch the actual source of the stream.
        """
    @staticmethod
    def enableLogging(level: typing.Optional[int] = None) -> None: 
        """
        Enable cscore logging
        """
    @staticmethod
    @typing.overload
    def getServer() -> VideoSink: 
        """
        Get server for the primary camera feed.

        This is only valid to call after a camera feed has been added with
        StartAutomaticCapture() or AddServer().

        Gets a server by name.

        :param name: Server name
        """
    @staticmethod
    @typing.overload
    def getServer(name: str) -> VideoSink: ...
    @staticmethod
    @typing.overload
    def getVideo() -> CvSink: 
        """
        Get OpenCV access to the primary camera feed.  This allows you to
        get images from the camera for image processing on the roboRIO.

        This is only valid to call after a camera feed has been added
        with startAutomaticCapture() or addServer().

        Get OpenCV access to the specified camera.  This allows you to get
        images from the camera for image processing on the roboRIO.

        :param camera: Camera (e.g. as returned by startAutomaticCapture).

        Get OpenCV access to the specified camera.  This allows you to get
        images from the camera for image processing on the roboRIO.

        :param name: Camera name
        """
    @staticmethod
    @typing.overload
    def getVideo(camera: VideoSource) -> CvSink: ...
    @staticmethod
    @typing.overload
    def getVideo(name: str) -> CvSink: ...
    @staticmethod
    def putVideo(name: str, width: int, height: int) -> CvSource: 
        """
        Create a MJPEG stream with OpenCV input. This can be called to pass custom
        annotated images to the dashboard.

        :param name:   Name to give the stream
        :param width:  Width of the image being sent
        :param height: Height of the image being sent
        """
    @staticmethod
    def removeCamera(name: str) -> None: 
        """
        Removes a camera by name.

        :param name: Camera name
        """
    @staticmethod
    def removeServer(name: str) -> None: 
        """
        Removes a server by name.

        :param name: Server name
        """
    @staticmethod
    def setSize(size: int) -> None: 
        """
        Sets the size of the image to use. Use the public kSize constants to set
        the correct mode, or set it directly on a camera and call the appropriate
        StartAutomaticCapture method.

        :deprecated: Use SetResolution on the UsbCamera returned by
                     StartAutomaticCapture() instead.

        :param size: The size to use
        """
    @staticmethod
    @typing.overload
    def startAutomaticCapture() -> UsbCamera: 
        """
        Start automatically capturing images to send to the dashboard.

        You should call this method to see a camera feed on the dashboard. If you
        also want to perform vision processing on the roboRIO, use getVideo() to
        get access to the camera images.

        The first time this overload is called, it calls StartAutomaticCapture()
        with device 0, creating a camera named "USB Camera 0".  Subsequent calls
        increment the device number (e.g. 1, 2, etc).

        Start automatically capturing images to send to the dashboard.

        This overload calls StartAutomaticCapture() with a name of "USB Camera
        {dev}".

        :param dev: The device number of the camera interface

        Start automatically capturing images to send to the dashboard.

        :param name: The name to give the camera
        :param dev:  The device number of the camera interface

        Start automatically capturing images to send to the dashboard.

        :param name: The name to give the camera
        :param path: The device path (e.g. "/dev/video0") of the camera

        Start automatically capturing images to send to the dashboard from
        an existing camera.

        :param camera: Camera
        """
    @staticmethod
    @typing.overload
    def startAutomaticCapture(camera: VideoSource) -> MjpegServer: ...
    @staticmethod
    @typing.overload
    def startAutomaticCapture(dev: int) -> UsbCamera: ...
    @staticmethod
    @typing.overload
    def startAutomaticCapture(name: str, dev: int) -> UsbCamera: ...
    @staticmethod
    @typing.overload
    def startAutomaticCapture(name: str, path: str) -> UsbCamera: ...
    @staticmethod
    def waitForever() -> None: 
        """
        Infinitely loops until the process dies
        """
    kBasePort = 1181
    kSize160x120 = 2
    kSize320x240 = 1
    kSize640x480 = 0
    pass
class VideoSink():
    """
    A sink for video that accepts a sequence of frames.
    """
    class Kind():
        """
        Members:

          kUnknown

          kMjpeg

          kCv
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
        __members__: dict # value = {'kUnknown': <Kind.kUnknown: 0>, 'kMjpeg': <Kind.kMjpeg: 2>, 'kCv': <Kind.kCv: 4>}
        kCv: cscore._cscore.VideoSink.Kind # value = <Kind.kCv: 4>
        kMjpeg: cscore._cscore.VideoSink.Kind # value = <Kind.kMjpeg: 2>
        kUnknown: cscore._cscore.VideoSink.Kind # value = <Kind.kUnknown: 0>
        pass
    def __eq__(self, arg0: VideoSink) -> bool: ...
    def __init__(self) -> None: ...
    def enumerateProperties(self) -> typing.List[VideoProperty]: 
        """
        Enumerate all properties of this sink.
        """
    @staticmethod
    def enumerateSinks() -> typing.List[VideoSink]: 
        """
        Enumerate all existing sinks.

        :returns: Vector of sinks.
        """
    def getConfigJson(self) -> str: 
        """
        Get a JSON configuration string.

        :returns: JSON configuration string
        """
    def getConfigJsonObject(self) -> json: 
        """
        Get a JSON configuration object.

        :returns: JSON configuration object
        """
    def getDescription(self) -> str: 
        """
        Get the sink description.  This is sink-kind specific.
        """
    def getHandle(self) -> int: ...
    def getKind(self) -> VideoSink.Kind: 
        """
        Get the kind of the sink.
        """
    def getLastStatus(self) -> int: ...
    def getName(self) -> str: 
        """
        Get the name of the sink.  The name is an arbitrary identifier
        provided when the sink is created, and should be unique.
        """
    def getProperty(self, name: str) -> VideoProperty: 
        """
        Get a property of the sink.

        :param name: Property name

        :returns: Property (kind Property::kNone if no property with
                  the given name exists)
        """
    def getSource(self) -> VideoSource: 
        """
        Get the connected source.

        :returns: Connected source (empty if none connected).
        """
    def getSourceProperty(self, name: str) -> VideoProperty: 
        """
        Get a property of the associated source.

        :param name: Property name

        :returns: Property (kind Property::kNone if no property with
                  the given name exists or no source connected)
        """
    @typing.overload
    def setConfigJson(self, config: json) -> bool: 
        """
        Set properties from a JSON configuration string.

        The format of the JSON input is:

        ::

          {
              "properties": [
                  {
                      "name": property name
                      "value": property value
                  }
              ]
          }

        :param config: configuration

        :returns: True if set successfully

        Set properties from a JSON configuration object.

        :param config: configuration

        :returns: True if set successfully
        """
    @typing.overload
    def setConfigJson(self, config: str) -> bool: ...
    def setSource(self, source: VideoSource) -> None: 
        """
        Configure which source should provide frames to this sink.  Each sink
        can accept frames from only a single source, but a single source can
        provide frames to multiple clients.

        :param source: Source
        """
    __hash__ = None
    pass
class ImageSource(VideoSource):
    """
    A base class for single image providing sources.
    """
    def createBooleanProperty(self, name: str, defaultValue: bool, value: bool) -> VideoProperty: 
        """
        Create a boolean property.

        :param name:         Property name
        :param defaultValue: Default value
        :param value:        Current value

        :returns: Property
        """
    def createIntegerProperty(self, name: str, minimum: int, maximum: int, step: int, defaultValue: int, value: int) -> VideoProperty: 
        """
        Create an integer property.

        :param name:         Property name
        :param minimum:      Minimum value
        :param maximum:      Maximum value
        :param step:         Step value
        :param defaultValue: Default value
        :param value:        Current value

        :returns: Property
        """
    def createProperty(self, name: str, kind: VideoProperty.Kind, minimum: int, maximum: int, step: int, defaultValue: int, value: int) -> VideoProperty: 
        """
        Create a property.

        :param name:         Property name
        :param kind:         Property kind
        :param minimum:      Minimum value
        :param maximum:      Maximum value
        :param step:         Step value
        :param defaultValue: Default value
        :param value:        Current value

        :returns: Property
        """
    def createStringProperty(self, name: str, value: str) -> VideoProperty: 
        """
        Create a string property.

        :param name:  Property name
        :param value: Current value

        :returns: Property
        """
    def notifyError(self, msg: str) -> None: 
        """
        Signal sinks that an error has occurred.  This should be called instead
        of NotifyFrame when an error occurs.

        :param msg: Notification message.
        """
    def setConnected(self, connected: bool) -> None: 
        """
        Set source connection status.  Defaults to true.

        :param connected: True for connected, false for disconnected
        """
    def setDescription(self, description: str) -> None: 
        """
        Set source description.

        :param description: Description
        """
    def setEnumPropertyChoices(self, property: VideoProperty, choices: typing.List[str]) -> None: 
        """
        Configure enum property choices.

        :param property: Property
        :param choices:  Choices
        """
    pass
class VideoCamera(VideoSource):
    """
    A source that represents a video camera.
    """
    class WhiteBalance():
        """
        Members:

          kFixedIndoor

          kFixedOutdoor1

          kFixedOutdoor2

          kFixedFluorescent1

          kFixedFlourescent2
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
        __members__: dict # value = {'kFixedIndoor': <WhiteBalance.kFixedIndoor: 3000>, 'kFixedOutdoor1': <WhiteBalance.kFixedOutdoor1: 4000>, 'kFixedOutdoor2': <WhiteBalance.kFixedOutdoor2: 5000>, 'kFixedFluorescent1': <WhiteBalance.kFixedFluorescent1: 5100>, 'kFixedFlourescent2': <WhiteBalance.kFixedFlourescent2: 5200>}
        kFixedFlourescent2: cscore._cscore.VideoCamera.WhiteBalance # value = <WhiteBalance.kFixedFlourescent2: 5200>
        kFixedFluorescent1: cscore._cscore.VideoCamera.WhiteBalance # value = <WhiteBalance.kFixedFluorescent1: 5100>
        kFixedIndoor: cscore._cscore.VideoCamera.WhiteBalance # value = <WhiteBalance.kFixedIndoor: 3000>
        kFixedOutdoor1: cscore._cscore.VideoCamera.WhiteBalance # value = <WhiteBalance.kFixedOutdoor1: 4000>
        kFixedOutdoor2: cscore._cscore.VideoCamera.WhiteBalance # value = <WhiteBalance.kFixedOutdoor2: 5000>
        pass
    def __init__(self) -> None: ...
    def getBrightness(self) -> int: 
        """
        Get the brightness, as a percentage (0-100).
        """
    def setBrightness(self, brightness: int) -> None: 
        """
        Set the brightness, as a percentage (0-100).
        """
    def setExposureAuto(self) -> None: 
        """
        Set the exposure to auto aperature.
        """
    def setExposureHoldCurrent(self) -> None: 
        """
        Set the exposure to hold current.
        """
    def setExposureManual(self, value: int) -> None: 
        """
        Set the exposure to manual, as a percentage (0-100).
        """
    def setWhiteBalanceAuto(self) -> None: 
        """
        Set the white balance to auto.
        """
    def setWhiteBalanceHoldCurrent(self) -> None: 
        """
        Set the white balance to hold current.
        """
    def setWhiteBalanceManual(self, value: int) -> None: 
        """
        Set the white balance to manual, with specified color temperature.
        """
    pass
class ImageSink(VideoSink):
    """
    A base class for single image reading sinks.
    """
    def getError(self) -> str: 
        """
        Get error string.  Call this if WaitForFrame() returns 0 to determine
        what the error is.
        """
    def setDescription(self, description: str) -> None: 
        """
        Set sink description.

        :param description: Description
        """
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enable or disable getting new frames.

        Disabling will cause processFrame (for callback-based CvSinks) to not
        be called and WaitForFrame() to not return.  This can be used to save
        processor resources when frames are not needed.
        """
    pass
class CvSource(ImageSource, VideoSource):
    """
    A source for user code to provide OpenCV images as video frames.
    """
    @typing.overload
    def __init__(self, name: str, mode: VideoMode) -> None: 
        """
        Create an OpenCV source.

        :param name: Source name (arbitrary unique identifier)
        :param mode: Video mode being generated

        Create an OpenCV source.

        :param name:        Source name (arbitrary unique identifier)
        :param pixelFormat: Pixel format
        :param width:       width
        :param height:      height
        :param fps:         fps
        """
    @typing.overload
    def __init__(self, name: str, pixelFormat: VideoMode.PixelFormat, width: int, height: int, fps: int) -> None: ...
    def putFrame(self, image: numpy.ndarray) -> None: 
        """
        Put an OpenCV image and notify sinks.

        Only 8-bit single-channel or 3-channel (with BGR channel order) images
        are supported. If the format, depth or channel order is different, use
        cv::Mat::convertTo() and/or cv::cvtColor() to convert it first.

        :param image: OpenCV image
        """
    pass
class MjpegServer(VideoSink):
    """
    A sink that acts as a MJPEG-over-HTTP network server.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Create a MJPEG-over-HTTP server sink.

        :param name:          Sink name (arbitrary unique identifier)
        :param listenAddress: TCP listen address (empty string for all addresses)
        :param port:          TCP port number

        Create a MJPEG-over-HTTP server sink.

        :param name: Sink name (arbitrary unique identifier)
        :param port: TCP port number
        """
    @typing.overload
    def __init__(self, name: str, listenAddress: str, port: int) -> None: ...
    @typing.overload
    def __init__(self, name: str, port: int) -> None: ...
    def getListenAddress(self) -> str: 
        """
        Get the listen address of the server.
        """
    def getPort(self) -> int: 
        """
        Get the port number of the server.
        """
    def setCompression(self, quality: int) -> None: 
        """
        Set the compression for clients that don't specify it.

        Setting this will result in increased CPU usage for MJPEG source cameras
        as it will decompress and recompress the image instead of using the
        camera's MJPEG image directly.

        :param quality: JPEG compression quality (0-100), -1 for unspecified
        """
    def setDefaultCompression(self, quality: int) -> None: 
        """
        Set the default compression used for non-MJPEG sources.  If not set,
        80 is used.  This function has no effect on MJPEG source cameras; use
        SetCompression() instead to force recompression of MJPEG source images.

        :param quality: JPEG compression quality (0-100)
        """
    def setFPS(self, fps: int) -> None: 
        """
        Set the stream frames per second (FPS) for clients that don't specify it.

        It is not necessary to set this if it is the same as the source FPS.

        :param fps: FPS, 0 for unspecified
        """
    def setResolution(self, width: int, height: int) -> None: 
        """
        Set the stream resolution for clients that don't specify it.

        It is not necessary to set this if it is the same as the source
        resolution.

        Setting this different than the source resolution will result in
        increased CPU usage, particularly for MJPEG source cameras, as it will
        decompress, resize, and recompress the image, instead of using the
        camera's MJPEG image directly.

        :param width:  width, 0 for unspecified
        :param height: height, 0 for unspecified
        """
    pass
class RawEvent():
    """
    Listener event
    """
    pass
class UsbCamera(VideoCamera, VideoSource):
    """
    A source that represents a USB camera.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Create a source for a USB camera based on device number.

        :param name: Source name (arbitrary unique identifier)
        :param dev:  Device number (e.g. 0 for /dev/video0)

        Create a source for a USB camera based on device path.

        :param name: Source name (arbitrary unique identifier)
        :param path: Path to device (e.g. "/dev/video0" on Linux)
        """
    @typing.overload
    def __init__(self, name: str, dev: int) -> None: ...
    @typing.overload
    def __init__(self, name: str, path: str) -> None: ...
    @staticmethod
    def enumerateUsbCameras() -> typing.List[UsbCameraInfo]: 
        """
        Enumerate USB cameras on the local system.

        :returns: Vector of USB camera information (one for each camera)
        """
    def getInfo(self) -> UsbCameraInfo: 
        """
        Get the full camera information for the device.
        """
    def getPath(self) -> str: 
        """
        Get the path to the device.
        """
    def setConnectVerbose(self, level: int) -> None: 
        """
        Set how verbose the camera connection messages are.

        :param level: 0=don't display Connecting message, 1=do display message
        """
    def setPath(self, path: str) -> None: 
        """
        Change the path to the device.
        """
    pass
class UsbCameraInfo():
    """
    USB camera information
    """
    def __init__(self) -> None: ...
    @property
    def dev(self) -> int:
        """
        Device number (e.g. N in '/dev/videoN' on Linux)

        :type: int
        """
    @dev.setter
    def dev(self, arg0: int) -> None:
        """
        Device number (e.g. N in '/dev/videoN' on Linux)
        """
    @property
    def name(self) -> str:
        """
        Vendor/model name of the camera as provided by the USB driver

        :type: str
        """
    @name.setter
    def name(self, arg0: str) -> None:
        """
        Vendor/model name of the camera as provided by the USB driver
        """
    @property
    def otherPaths(self) -> typing.List[str]:
        """
        Other path aliases to device (e.g. '/dev/v4l/by-id/...' etc on Linux)

        :type: typing.List[str]
        """
    @otherPaths.setter
    def otherPaths(self, arg0: typing.List[str]) -> None:
        """
        Other path aliases to device (e.g. '/dev/v4l/by-id/...' etc on Linux)
        """
    @property
    def path(self) -> str:
        """
        Path to device if available (e.g. '/dev/video0' on Linux)

        :type: str
        """
    @path.setter
    def path(self, arg0: str) -> None:
        """
        Path to device if available (e.g. '/dev/video0' on Linux)
        """
    @property
    def productId(self) -> int:
        """
        USB Product Id

        :type: int
        """
    @productId.setter
    def productId(self, arg0: int) -> None:
        """
        USB Product Id
        """
    @property
    def vendorId(self) -> int:
        """
        USB Vendor Id

        :type: int
        """
    @vendorId.setter
    def vendorId(self, arg0: int) -> None:
        """
        USB Vendor Id
        """
    pass
class HttpCamera(VideoCamera, VideoSource):
    """
    A source that represents a MJPEG-over-HTTP (IP) camera.
    """
    class HttpCameraKind():
        """
        Members:

          kUnknown

          kMJPGStreamer

          kCSCore

          kAxis
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
        __members__: dict # value = {'kUnknown': <HttpCameraKind.kUnknown: 0>, 'kMJPGStreamer': <HttpCameraKind.kMJPGStreamer: 1>, 'kCSCore': <HttpCameraKind.kCSCore: 2>, 'kAxis': <HttpCameraKind.kAxis: 3>}
        kAxis: cscore._cscore.HttpCamera.HttpCameraKind # value = <HttpCameraKind.kAxis: 3>
        kCSCore: cscore._cscore.HttpCamera.HttpCameraKind # value = <HttpCameraKind.kCSCore: 2>
        kMJPGStreamer: cscore._cscore.HttpCamera.HttpCameraKind # value = <HttpCameraKind.kMJPGStreamer: 1>
        kUnknown: cscore._cscore.HttpCamera.HttpCameraKind # value = <HttpCameraKind.kUnknown: 0>
        pass
    @typing.overload
    def __init__(self, name: str, url: str, kind: HttpCamera.HttpCameraKind = HttpCameraKind.kUnknown) -> None: 
        """
        Create a source for a MJPEG-over-HTTP (IP) camera.

        :param name: Source name (arbitrary unique identifier)
        :param url:  Camera URL (e.g. "http://10.x.y.11/video/stream.mjpg")
        :param kind: Camera kind (e.g. kAxis)

        Create a source for a MJPEG-over-HTTP (IP) camera.

        :param name: Source name (arbitrary unique identifier)
        :param url:  Camera URL (e.g. "http://10.x.y.11/video/stream.mjpg")
        :param kind: Camera kind (e.g. kAxis)

        Create a source for a MJPEG-over-HTTP (IP) camera.

        :param name: Source name (arbitrary unique identifier)
        :param url:  Camera URL (e.g. "http://10.x.y.11/video/stream.mjpg")
        :param kind: Camera kind (e.g. kAxis)

        Create a source for a MJPEG-over-HTTP (IP) camera.

        :param name: Source name (arbitrary unique identifier)
        :param urls: Array of Camera URLs
        :param kind: Camera kind (e.g. kAxis)
        """
    @typing.overload
    def __init__(self, name: str, urls: typing.List[str], kind: HttpCamera.HttpCameraKind = HttpCameraKind.kUnknown) -> None: ...
    def getHttpCameraKind(self) -> HttpCamera.HttpCameraKind: 
        """
        Get the kind of HTTP camera.

        Autodetection can result in returning a different value than the camera
        was created with.
        """
    def getUrls(self) -> typing.List[str]: 
        """
        Get the URLs used to connect to the camera.
        """
    def setUrls(self, urls: typing.List[str]) -> None: 
        """
        Change the URLs used to connect to the camera.
        """
    pass
class VideoEvent(RawEvent):
    """
    An event generated by the library and provided to event listeners.
    """
    def __init__(self) -> None: ...
    def getProperty(self) -> VideoProperty: 
        """
        Get the property associated with the event (if any).
        """
    def getSink(self) -> VideoSink: 
        """
        Get the sink associated with the event (if any).
        """
    def getSource(self) -> VideoSource: 
        """
        Get the source associated with the event (if any).
        """
    pass
class VideoListener():
    """
    An event listener.  This calls back to a desigated callback function when
    an event matching the specified mask is generated by the library.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Create an event listener.

        :param callback:        Callback function
        :param eventMask:       Bitmask of VideoEvent::Kind values
        :param immediateNotify: Whether callback should be immediately called with
                                a representative set of events for the current library state.
        """
    @typing.overload
    def __init__(self, callback: typing.Callable[[VideoEvent], None], eventMask: int, immediateNotify: bool) -> None: ...
    pass
class VideoMode():
    """
    Video mode
    """
    class PixelFormat():
        """
        Members:

          kUnknown

          kMJPEG

          kYUYV

          kRGB565

          kBGR

          kGray

          kY16

          kUYVY
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
        __members__: dict # value = {'kUnknown': <PixelFormat.kUnknown: 0>, 'kMJPEG': <PixelFormat.kMJPEG: 1>, 'kYUYV': <PixelFormat.kYUYV: 2>, 'kRGB565': <PixelFormat.kRGB565: 3>, 'kBGR': <PixelFormat.kBGR: 4>, 'kGray': <PixelFormat.kGray: 5>, 'kY16': <PixelFormat.kY16: 6>, 'kUYVY': <PixelFormat.kUYVY: 7>}
        kBGR: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kBGR: 4>
        kGray: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kGray: 5>
        kMJPEG: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kMJPEG: 1>
        kRGB565: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kRGB565: 3>
        kUYVY: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kUYVY: 7>
        kUnknown: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kUnknown: 0>
        kY16: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kY16: 6>
        kYUYV: cscore._cscore.VideoMode.PixelFormat # value = <PixelFormat.kYUYV: 2>
        pass
    def __eq__(self, arg0: VideoMode) -> bool: ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, pixelFormat_: VideoMode.PixelFormat, width_: int, height_: int, fps_: int) -> None: ...
    def compareWithoutFps(self, other: VideoMode) -> bool: ...
    @property
    def fps(self) -> int:
        """
        :type: int
        """
    @fps.setter
    def fps(self, arg0: int) -> None:
        pass
    @property
    def height(self) -> int:
        """
        :type: int
        """
    @height.setter
    def height(self, arg0: int) -> None:
        pass
    @property
    def pixelFormat(self) -> int:
        """
        :type: int
        """
    @pixelFormat.setter
    def pixelFormat(self, arg0: int) -> None:
        pass
    @property
    def width(self) -> int:
        """
        :type: int
        """
    @width.setter
    def width(self, arg0: int) -> None:
        pass
    __hash__ = None
    pass
class VideoProperty():
    """
    A source or sink property.
    """
    class Kind():
        """
        Members:

          kNone

          kBoolean

          kInteger

          kString

          kEnum
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
        __members__: dict # value = {'kNone': <Kind.kNone: 0>, 'kBoolean': <Kind.kBoolean: 1>, 'kInteger': <Kind.kInteger: 2>, 'kString': <Kind.kString: 4>, 'kEnum': <Kind.kEnum: 8>}
        kBoolean: cscore._cscore.VideoProperty.Kind # value = <Kind.kBoolean: 1>
        kEnum: cscore._cscore.VideoProperty.Kind # value = <Kind.kEnum: 8>
        kInteger: cscore._cscore.VideoProperty.Kind # value = <Kind.kInteger: 2>
        kNone: cscore._cscore.VideoProperty.Kind # value = <Kind.kNone: 0>
        kString: cscore._cscore.VideoProperty.Kind # value = <Kind.kString: 4>
        pass
    def __init__(self) -> None: ...
    def get(self) -> int: ...
    def getChoices(self) -> typing.List[str]: ...
    def getDefault(self) -> int: ...
    def getKind(self) -> VideoProperty.Kind: ...
    def getLastStatus(self) -> int: ...
    def getMax(self) -> int: ...
    def getMin(self) -> int: ...
    def getName(self) -> str: ...
    def getStep(self) -> int: ...
    @typing.overload
    def getString(self) -> str: ...
    @typing.overload
    def getString(self, buf: typing.List[str]) -> str: ...
    def isBoolean(self) -> bool: ...
    def isEnum(self) -> bool: ...
    def isInteger(self) -> bool: ...
    def isString(self) -> bool: ...
    def set(self, value: int) -> None: ...
    def setString(self, value: str) -> None: ...
    pass
class CvSink(ImageSink, VideoSink):
    """
    A sink for user code to accept video frames as OpenCV images.
    """
    def __init__(self, name: str) -> None: 
        """
        Create a sink for accepting OpenCV images.

        :param name: Source name (arbitrary unique identifier)
        """
    def grabFrame(self, image: numpy.ndarray, timeout: float = 0.225) -> typing.Tuple[int, numpy.ndarray]: 
        """
        Wait for the next frame and get the image.
        Times out (returning 0) after timeout seconds.
        The provided image will have three 8-bit channels stored in BGR order.

        :returns: Frame time, or 0 on error (call GetError() to obtain the error
                  message); the frame time is in the same time base as wpi::Now(),
                  and is in 1 us increments.
        """
    def grabFrameNoTimeout(self, image: numpy.ndarray) -> typing.Tuple[int, numpy.ndarray]: 
        """
        Wait for the next frame and get the image.  May block forever.
        The provided image will have three 8-bit channels stored in BGR order.

        :returns: Frame time, or 0 on error (call GetError() to obtain the error
                  message); the frame time is in the same time base as wpi::Now(),
                  and is in 1 us increments.
        """
    pass
class AxisCamera(HttpCamera, VideoCamera, VideoSource):
    """
    A source that represents an Axis IP camera.
    """
    @typing.overload
    def __init__(self, name: str, host: str) -> None: 
        """
        Create a source for an Axis IP camera.

        :param name: Source name (arbitrary unique identifier)
        :param host: Camera host IP or DNS name (e.g. "10.x.y.11")

        Create a source for an Axis IP camera.

        :param name: Source name (arbitrary unique identifier)
        :param host: Camera host IP or DNS name (e.g. "10.x.y.11")

        Create a source for an Axis IP camera.

        :param name: Source name (arbitrary unique identifier)
        :param host: Camera host IP or DNS name (e.g. "10.x.y.11")

        Create a source for an Axis IP camera.

        :param name:  Source name (arbitrary unique identifier)
        :param hosts: Array of Camera host IPs/DNS names
        """
    @typing.overload
    def __init__(self, name: str, hosts: typing.List[str]) -> None: ...
    pass
def _setLogger(func: typing.Callable[[int, str, int, str], None], min_level: int) -> None:
    pass
def runMainRunLoop() -> None:
    pass
def runMainRunLoopTimeout(timeoutSeconds: float) -> int:
    pass
def stopMainRunLoop() -> None:
    pass
_cleanup: typing.Any  # PyCapsule()
