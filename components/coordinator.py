import sys
import time

sys.path.insert(0, '..')

import ecal.core.core as ecal_core
from ecal.core.publisher import StringPublisher
from ecal.core.publisher import ProtoPublisher
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.subscriber import StringSubscriber

import datatypes.offender_detector_pb2 as offender_detector_pb2
import datatypes.victim_detector_pb2 as victim_detector_pb2
import datatypes.coordinator_pb2 as coordinator_pb2

class Coordinator:

  def __init__(self) -> None:
    print("Coordinator init...")

    ecal_core.initialize(sys.argv, "Python Coordinator")

    self.offenderDetector_Detected = False
    self.victimDetector_Detected = False
    
    self.pub_Coordinator = ProtoPublisher("Coordinator", coordinator_pb2.Coordinator)

    self.sub_OfferDetector = ProtoSubscriber("OffenderDetector", offender_detector_pb2.OfferDetector)
    self.sub_VictimDetector = ProtoSubscriber("VictimDetector", victim_detector_pb2.VictimDetector)
    
    self.sub_OfferDetector.set_callback(self.callback_OffenderDetector)
    self.sub_VictimDetector.set_callback(self.callback_VictimDetector)

  def run(self):
    while ecal_core.ok():

      print(f'offenderDetector_Detected: {self.offenderDetector_Detected}')
      print(f'victimDetector_Detected: {self.victimDetector_Detected}')
      print()


      msg_coordinator = coordinator_pb2.Coordinator()
      msg_coordinator.warning = self.offenderDetector_Detected and self.victimDetector_Detected
      self.pub_Coordinator.send(msg_coordinator)


      
      time.sleep(0.5)
    
    # finalize eCAL API
    ecal_core.finalize()
    
  def callback_OffenderDetector_Detected(self, topic_name, msg, time):
    # print("Debug eCAL callback_OffenderDetector_Detected: {}".format(msg))
    self.offenderDetector_Detected = (msg == "True")

  def callback_VictimDetector_Detected(self, topic_name, msg, time):
    # print("Debug eCAL callback_VictimDetector_Detected: {}".format(msg))
    self.victimDetector_Detected = (msg == "True")
  
  def callback_OffenderDetector(self, topic_name, msg, time):
    # print("Debug eCAL OffenderDetector: {}".format(msg.detected))
    self.offenderDetector_Detected = msg.detected

  def callback_VictimDetector(self, topic_name, msg, time):
    # print("Debug eCAL VictimDetector: {}".format(msg.detected))
    self.victimDetector_Detected = msg.detected


if __name__ == "__main__":
  coordinator = Coordinator()
  coordinator.run()