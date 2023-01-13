from Directory import Directory
from BinaryFile import BinaryFile
import pytest


class TestDirectory:

    def test_directory_creation(self):
        maxElements = 10
        dirName = 'dir'
        directory = Directory(dirName=dirName, maxElements=maxElements)
        assert directory.dirName == dirName
        assert directory.dirMaxElem == maxElements
        assert directory.elementsCount == 0

    def test_directory_move(self):
        directory = Directory(dirName='dir')
        parentDirectory = Directory('parentDir')
        directory.move(parentDirectory)
        assert directory.parent == parentDirectory

    def test_directory_deletion(self):
        directory = Directory(dirName='dir')
        directory.delete()
        tryToGetDirName = directory.dirName
        print(tryToGetDirName)
        assert pytest.raises(Exception)

    def test_directory_list_elements(self):
        directory = Directory(dirName='dir',maxElements=10)
        binaryFile1 = BinaryFile(fileName="file1", content="1")
        binaryFile1.move(directory)
        binaryFile2 = BinaryFile(fileName="file2", content="2")
        binaryFile2.move(directory)
        binaryFile3 = BinaryFile(fileName="file3", content="3")
        binaryFile3.move(directory)
        dirElements = directory.list_elements()
        assert dirElements[0] == binaryFile1
        assert dirElements[1] == binaryFile2
        assert dirElements[2] == binaryFile3

    def test_element_is_not_added_when_directory_is_full(self):
        maxElements = 0
        directory = Directory(dirName='dir', maxElements=maxElements)
        binaryFile1 = BinaryFile(fileName="file1", content="1")
        binaryFile1.move(directory)
        assert pytest.raises(OverflowError)

    def test_directory_is_not_moved_when_target_dir_does_not_exist(self):
        directory = Directory(dirName='dir', maxElements=10)
        parentDirectory = None
        with pytest.raises(Exception):
            directory.move(parentDirectory)