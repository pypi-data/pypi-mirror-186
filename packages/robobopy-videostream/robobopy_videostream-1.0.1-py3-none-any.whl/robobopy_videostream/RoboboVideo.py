from robobopy_videostream.my_socket import MySocket


class RoboboVideo:

    def __init__(self, ip, robot_id=0):
        self.port = 40405 + (robot_id * 10)
        self.ip = ip
        self.socket = MySocket()

    def connect(self):
        self.socket.connect(self.ip,self.port)
        self.socket.start_image_thread()

    def getImage(self):
        image, cv2_image,timestamp, sync_id, frame_id = self.socket.get_image()
        return cv2_image


    def getImageWithMetadata(self):
        image, cv2_image,timestamp, sync_id, frame_id = self.socket.get_image()
        return cv2_image, timestamp, sync_id, frame_id

    def disconnect(self):
        self.socket.disconnect()

