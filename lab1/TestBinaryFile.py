from BinaryFile import BinaryFile
from Directory import Directory
import pytest


class TestBinaryFile:

    def test_binary_file_creation(self):
        fileName = "file1"
        content = "1"
        binaryFile = BinaryFile(fileName=fileName, content=content)
        assert binaryFile.fileName == fileName
        assert binaryFile.content == content

    def test_binary_file_deletion(self):
        binaryFile = BinaryFile(fileName="file1", content="1")
        binaryFile.delete()
        assert binaryFile == None

    def test_binary_file_move(self):
        binaryFile = BinaryFile(fileName="file1", content="1")
        parentDir = Directory(dirName="dir", maxElements=10)
        binaryFile.move(parentDir)
        assert binaryFile.parent == parentDir

    def test_binary_file_read(self):
        fileName = "file1"
        expected_content = "1"
        binaryFile = BinaryFile(fileName=fileName, content=expected_content)
        actual_content = binaryFile.read()
        assert expected_content == actual_content

    def test_binary_file_is_not_moved_when_target_dir_does_not_exist(self):
        binaryFile = BinaryFile(fileName="file1", content="1")
        parentDirectory = None
        binaryFile.move(parentDirectory)
        assert pytest.raises(Exception)