import picamera
from subprocess import call
from time import sleep

print "Accessing Camera"
with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_recording("./sampleVideo.h264")
    sleep(10)
    camera.stop_recording()

print "Video being converted"
command1 = "MP4Box --add sampleVideo.h264 " + "converted.mp4"
command2 = "sudo rm sampleVideo.h264"
call([command1, command2], shell=True)

print "File finished"