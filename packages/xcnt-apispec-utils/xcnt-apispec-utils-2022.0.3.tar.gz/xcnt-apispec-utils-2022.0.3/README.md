# APISpec Utils

This library contains common logic required for correctly serving swagger documentation
files with our Python libraries.

Example Usage:

```python
from xcnt.apispec.utils import apispec_plugins, APISpec


spec = APISpec(
    title="DRIVR - Example",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=apispec_plugins(),
)
```
