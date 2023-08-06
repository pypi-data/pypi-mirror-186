## Pre Deployment/Merge Checklist
1) Make sure to update the __version__ variable in rhino_health/__init__.py if you wish to publish a new version so the documentation refers to the correct version
2) Make sure to test the interation tests against the branch. If you are adding new endpoints please write new integration tests in the cloud repository. You can go to the cloud repository and kick off an integration test against a specific SDK branch.
3) Once merged the documentation should be auto generated and updated. If any issues occur please ask the developers.
