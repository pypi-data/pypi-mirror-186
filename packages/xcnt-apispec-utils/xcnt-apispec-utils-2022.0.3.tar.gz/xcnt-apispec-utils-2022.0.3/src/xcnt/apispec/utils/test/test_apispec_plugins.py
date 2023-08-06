from xcnt.apispec.utils import APISpec, apispec_plugins


def test_get_plugins():
    plugins = apispec_plugins()
    assert len(plugins) >= 3


def test_api_spec_creation():
    spec = APISpec(
        title="DRIVR - TEst API Spec",
        version="1.0.0",
        openapi_version="3.0.2",
        plugins=apispec_plugins(),
    )
    assert spec.to_flasgger(None) is not None
