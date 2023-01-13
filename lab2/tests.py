from BinaryFile import BinaryFile
from BufferFile import BufferFile
from LogTextFile import LogTextFile
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
        tryToGetFileName = binaryFile.fileName
        print(tryToGetFileName)
        assert pytest.raises(Exception)

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

        with pytest.raises(Exception):
            binaryFile.move(parentDirectory)

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

class TestLogTextFile:
    def test_log_text_file_creation(self):
        fileName = "file1"
        logTextFile = LogTextFile(fileName=fileName)
        assert logTextFile.fileName == fileName

    def test_log_text_file_deletion(self):
        fileName = "file1"
        logTextFile = LogTextFile(fileName=fileName)
        logTextFile.delete()
        tryToGetDirName = logTextFile.fileName
        print(tryToGetDirName)
        assert pytest.raises(Exception)

    def test_log_text_file_move(self):
        fileName = "file1"
        logTextFile = LogTextFile(fileName=fileName)
        parentDir = Directory(dirName="dir", maxElements=10)
        logTextFile.move(parentDir)
        assert logTextFile.parent == parentDir

    def test_log_text_file_read(self):
        fileName = "file1"
        newLine = "new line"
        expected_content = "new line new line new line "
        logTextFile = LogTextFile(fileName=fileName)
        logTextFile.append_line(newLine)
        logTextFile.append_line(newLine)
        logTextFile.append_line(newLine)
        actual_content = logTextFile.read()
        assert expected_content == actual_content

    def test_log_text_file_is_not_moved_when_target_dir_does_not_exist(self):
        fileName = "file1"
        logTextFile = LogTextFile(fileName=fileName)
        parentDirectory = None
        with pytest.raises(Exception):
            logTextFile.move(parentDirectory)