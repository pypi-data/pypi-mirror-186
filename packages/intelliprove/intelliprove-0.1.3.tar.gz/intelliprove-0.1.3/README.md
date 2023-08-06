<h1 align="center"> IntelliProve Python SDK</h1>

<div align="center">
    <img src="https://img.shields.io/pypi/dm/intelliprove" />
    <img src="https://img.shields.io/pypi/pyversions/intelliprove" />
    <img src="https://img.shields.io/badge/version-0.1.2-blue" />
</div>

## Requirements

- Python ^3.9

## Installation
```pip install intelliprove```

## Example usage

```python
import os
from pathlib import Path

from intelliprove.api import IntelliproveApi, IntelliproveApiSettings, Biomarkers, Quality

# define api key and settings
apikey = os.environ.get('apikey')
settings = IntelliproveApiSettings(
    base_url=''
)

# init api
api = IntelliproveApi(apikey, settings)

# define the path of the video you want to upload
video_path = Path('./mydir/example.mp4')
image_path = Path('./mydir/example.png')

# manually check quality of a video of image
quality: Quality = api.check_conditions(video_path)
quality: Quality = api.check_conditions(image_path)

# Optional: define the performer and patient
performer: str = 'performer-a'
patient: str = 'patient-1'

# upload video to IntelliProve
# performer and patient are optional
uuid: str = api.upload(video_path)
# or
uuid: str = api.upload(video_path, performer=performer, patient=patient)

# get the results of the uploaded video
results: Biomarkers = api.get_results(uuid)
```

### Dataclasses
- Biomarkers
  - contains the results of an uploaded video
- Quality
  - contains the quality parameters of a video or image

### Exceptions
- ImageQualityException
- MediaException
- InvalidUuidException
- ApiException
  - ApiNotFoundException
  - ApiForbiddenException
  - ApiErrorException
  - ApiResultNotAvailable