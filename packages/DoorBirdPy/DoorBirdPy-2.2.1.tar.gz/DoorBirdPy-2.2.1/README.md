# doorbirdpy
Python wrapper for the DoorBird LAN API v0.21

[View on PyPI](https://pypi.org/project/DoorBirdPy/)

# Features

[DoorBird API Documentation](https://www.doorbird.com/downloads/api_lan.pdf?rev=0.21)

Note that no image data is handled by this wrapper; it only returns the URLs to access images and streams. It was designed this way so that the fetching of images could be handled by the client application and so that this library would not have so many dependencies.

## Supported

- Live video request
- Live image request
- Open door/other relays
- Light on
- History image requests
- Schedule requests
- Favorites requests
- Check request
- Info request
- RTSP

## Not yet supported

- Monitor request
- Live audio transmit
- Live audio receive
- SIP

# Contributors

- @klikini
- @oblogic7
- @bdraco
- [alandtse](https://github.com/alandtse)
