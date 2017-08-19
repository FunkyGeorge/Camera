import picamera
from subprocess import call
from time import localtime, sleep, strftime

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.start_recording("./sampleVideo.h264")
    sleep(300)
    camera.stop_recording()

command1 = "MP4Box -add sampleVideo.h264 ./videos/{0}.mp4".format(strftime('%b%d_%H:%M', localtime()))
call([command1], shell=True)

print "video ready"