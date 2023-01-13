from LogTextFile import LogTextFile
from Directory import Directory
import pytest


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