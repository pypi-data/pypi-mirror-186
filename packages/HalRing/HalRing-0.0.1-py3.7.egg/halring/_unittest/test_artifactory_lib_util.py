import unittest
from halring.artifactory.artifactory_lib_util import ArtifactoryLibUtil


class TestPubArtifactoryLib(unittest.TestCase):
    def test_artifactorylibutil_001(self):
        """
        使用util
        """
        user = "aqc001"
        password = "l1nx1L1n@n6"
        artifactory_lib_util = ArtifactoryLibUtil(user, password)
        path_string = "http://artifactory.test.com:8081/artifactory/Daily/BPC"
        print(artifactory_lib_util.artifactory_path_exist(path_string))

    def test_artifactorylibutil_002(self):
        """
        直接使用三方库的path
        """
        user = "aqc001"
        password = "l1nx1L1n@n6"
        artifactory_lib_util = ArtifactoryLibUtil(user, password)
        path_string = "http://artifactory.test.com:8081/artifactory/Daily/BPC"
        mypath = artifactory_lib_util.get_ArtifactoryPath(path_string)

        print(mypath.exists())

    def test_artifactorylibutil_003(self):
        user = "aqc001"
        password = "l1nx1L1n@n6"
        artifactory_lib_util = ArtifactoryLibUtil(user, password)
        path_string = "http://artifactory.test.com:8081/artifactory/Delivery/MCBM/MCBM_V0.10.2/6/"
        result = artifactory_lib_util.artifactory_list_child(path_string,"nr","a")
        print(result)


