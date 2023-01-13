from BufferFile import BufferFile
from Directory import Directory
import pytest


class TestBufferFile:

    def test_buffer_file_creation(self):
        fileName = "file1"
        maxSize = 10
        bufferFile = BufferFile(fileName=fileName, maxSize=maxSize)
        assert bufferFile.fileName == fileName
        assert bufferFile.maxSize == maxSize

    def test_buffer_file_deletion(self):
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        bufferFile.delete()
        tryToGetFileName = bufferFile.fileName
        print(tryToGetFileName)
        assert pytest.raises(Exception)

    def test_buffer_file_move(self):
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        parentDir = Directory(dirName="dir", maxElements=10)
        bufferFile.move(parentDir)
        assert bufferFile.parent == parentDir

    def test_buffer_file_push(self):
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        pushedElement = 1
        bufferFile.push(pushedElement)
        assert bufferFile.content[0] == pushedElement

    def test_element_is_not_pushed_when_buffer_file_is_full(self):
        bufferFile = BufferFile(fileName="file1", maxSize=0)
        pushedElement = 1
        with pytest.raises(OverflowError):
            bufferFile.push(pushedElement)

    def test_buffer_file_consume(self):
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        pushedElement = 1
        bufferFile.push(pushedElement)
        assert bufferFile.consume() == pushedElement

    def test_buffer_file_is_not_moved_when_target_dir_does_not_exist(self):
        bufferFile = BufferFile(fileName="file1", maxSize=10)
        parentDirectory = None
        with pytest.raises(Exception):
            bufferFile.move(parentDirectory)