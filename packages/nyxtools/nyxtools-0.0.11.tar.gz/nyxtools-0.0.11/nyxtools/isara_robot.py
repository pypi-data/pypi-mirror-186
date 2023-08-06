from ophyd import Device, EpicsSignal, EpicsSignalRO
from ophyd import Component as Cpt
print("LOADING ISARA_OPHYD")
#TIMEOUT in seconds, should be declared elsewhere
ISARA_TIMEOUT = 100

class IsaraRobotDevice(Device):
  ### Commands

  ## Generic command channels
  # power
  power_on = Cpt(EpicsSignal, 'Pwr:On-Cmd', put_complete=True)
  power_off = Cpt(EpicsSignal, 'Pwr:Off-Cmd', put_complete=True)

  # arm movement speed
  speed_up = Cpt(EpicsSignal, 'Spd:Up-Cmd', put_complete=True)
  speed_down = Cpt(EpicsSignal, 'Spd:Dn-Cmd', put_complete=True)
  # 0 - 100
  speed_setpoint = Cpt(EpicsSignal, 'Speed-SP', put_complete=True)

  # heater
  heater_on = Cpt(EpicsSignal, 'Htr:On-Cmd', put_complete=True)
  heater_off = Cpt(EpicsSignal, 'Htr:Off-Cmd', put_complete=True)

  # dewar lid
  dewar_lid_open = Cpt(EpicsSignal, 'Lid:Opn-Cmd', put_complete=True)
  dewar_lid_close = Cpt(EpicsSignal, 'Lid:Cls-Cmd', put_complete=True)

  # gripper a
  gripper_a_open = Cpt(EpicsSignal, 'OpnA-Cmd', put_complete=True)
  gripper_a_close = Cpt(EpicsSignal, 'ClsA-Cmd', put_complete=True)
  
  # gripper b
  gripper_b_open = Cpt(EpicsSignal, 'OpnB-Cmd', put_complete=True)
  gripper_b_close = Cpt(EpicsSignal, 'ClsB-Cmd', put_complete=True)

  ## Trajectories
  # write 1 to start move
  home_traj = Cpt(EpicsSignal,'Move:Home-Cmd', put_complete=True)
  recover_traj = Cpt(EpicsSignal,'Move:Rcvr-Cmd', put_complete=True)
  get_traj = Cpt(EpicsSignal,'Move:Get-Cmd', put_complete=True)
  put_traj = Cpt(EpicsSignal,'Move:Put-Cmd', put_complete=True)
  getput_traj = Cpt(EpicsSignal,'Move:GetPut-Cmd', put_complete=True)
  back_traj = Cpt(EpicsSignal,'Move:Bck-Cmd', put_complete=True)
  dry_traj = Cpt(EpicsSignal, 'Move:Dry-Cmd', put_complete=True)
  soak_traj = Cpt(EpicsSignal, 'Move:Sk-Cmd', put_complete=True)
  pick_traj = Cpt(EpicsSignal, 'Move:Pck-Cmd', put_complete=True)

  ## Trajectory Arguments
  # 0 = "ToolChanger"
  # 1 = "Cryotong"
  # 2 = "SingleGripper"
  # 3 = "DoubleGripper"
  # 4 = "MiniSpineGripper"
  # 5 = "RotatingGripper"
  # 6 = "PlateGripper"
  # 7 = "Spare"
  # 8 = "LaserTool"
  tool_selected = Cpt(EpicsSignal,'Tl-Sel')

  # limits 0-29
  # argument is interchangeable for puck/plate selection field
  puck_num_sel = Cpt(EpicsSignal, 'Plt-SP', put_complete=True)
  puck_n_selected = Cpt(EpicsSignal, 'Plt:N-SP', put_complete=True)

  # limits 0-16
  sample_num_sel = Cpt(EpicsSignal, 'Samp-SP', put_complete=True)
  samp_n_selected = Cpt(EpicsSignal, 'Samp:N-SP', put_complete=True)

  # 0 = "Skip"
  # 1 = "Scan"
  dm_selected = Cpt(EpicsSignal, 'DM-Sel', put_complete=True)

  ### Statuses

  # interface from denso, try to maintain types
  #int
  #status

  #bool
  #busy_sts

  #bool
  #mount_ready_sts

  #is mounting bool
  #mounting_sts

  #is dismounting bool
  #dismounting_sts

  # is drying bool
  # 0 = "Idle"
  # 1 = "Drying"
  drying_sts = Cpt(EpicsSignalRO, 'GripDry-Sts')
  # new 
  # 0 = "Hold off"
  # 1 = "Permit"
  drying_permitted_sts = Cpt(EpicsSignalRO,'DryPmt-I')

  # spindle occupied bool
  spindle_occupied_sts = Cpt(EpicsSignalRO, 'Samp:Dif-Sts')

  # New statuses for ISARA

  # Last Message
  last_message = Cpt(EpicsSignalRO, 'LastMsg-I')
 
  # Fault Status
  # 0 = "Ok"
  # 1 = "Fault"
  fault_sts = Cpt(EpicsSignalRO, 'Flt-Sts')

  # Alarm Status
  # TODO: What does this return?
  alarm_sts = Cpt(EpicsSignalRO, 'Alarm-I')

  # Current Position
  position_sts = Cpt(EpicsSignalRO, 'Pos:Name-I')

  # Moving Status
  # 0 = "Stopped"
  # 1 = "Moving"
  moving_sts = Cpt(EpicsSignalRO, 'Seq:Run-Sts')

  # Paused Status
  # 0 = "Normal"
  # 1 = "Paused"
  paused_sts = Cpt(EpicsSignalRO, 'Seq:Paus-Sts')

  # Speed Status
  speed_sts = Cpt(EpicsSignalRO, 'Speed-I')

  # Current Tool
  # 0 = "ToolChanger"
  # 1 = "Cryotong"
  # 2 = "SingleGripper"
  # 3 = "DoubleGripper"
  # 4 = "MiniSpineGripper"
  # 5 = "RotatingGripper"
  # 6 = "PlateGripper"
  # 7 = "Spare"
  # 8 = "LaserTool"
  current_tool = Cpt(EpicsSignal, 'Tl-I')

  # Power status
  # 0 = "Off"
  # 1 = "On"
  power_sts = Cpt(EpicsSignalRO, 'Pwr-Sts')

  # Occupied statuses
  # 0 = "Empty"
  # 1 = "Present"
  samp_a_occ_sts = Cpt(EpicsSignalRO, 'Samp:A-Sts')
  samp_b_occ_sts  = Cpt(EpicsSignalRO, 'Samp:B-Sts')
  samp_dif_occ_sts = Cpt(EpicsSignalRO, 'Samp:Dif-Sts')

  # Gripper Statuses
  # 0 = "Open"
  # 1 = "Closed"
  grip_a_sts = Cpt(EpicsSignalRO, 'Grp:A-Sts')
  grip_b_sts = Cpt(EpicsSignalRO, 'Grp:B-Sts')
  
  # Samples occupying gripper/spindle
  # returns 0-29
  # returns -1 if empty
  puck_a_read = Cpt(EpicsSignalRO, 'Pck:A-I')
  puck_b_read = Cpt(EpicsSignalRO, 'Pck:B-I')
  puck_dif_read = Cpt(EpicsSignalRO, 'Pck:Dif-I')
  
  # returns 0-16
  # returns -1 if empty
  samp_a_read = Cpt(EpicsSignalRO, 'Samp:A-I')
  samp_b_read = Cpt(EpicsSignalRO, 'Samp:B-I')
  samp_dif_read = Cpt(EpicsSignalRO, 'Samp:Dif-I')

  def set_and_check(signal, value):
    signal_status = signal.set(value)
    signal_status.wait(ISARA_TIMEOUT)
    return signal_status.success

  # deprecated possibly by doublegripper functions
  def selectSample(self, sample_no):
    return set_and_check(self.sample_num_sel, sample_no)

  def selectPlate(self, plate_no):
    return set_and_check(self.plate_selected, plate_no)

  def openGripper(self):
    pass   

  def closeGripper(self):
    pass

  def openGripperA(self):
    return set_and_check(self.gripper_a_open, 1)

  def openGripperB(self):
    return set_and_check(self.gripper_a_open, 1)

  def closeGripperA(self):
    return set_and_check(self.gripper_a_close, 1)

  def closeGripperB(self):
    return set_and_check(self.gripper_b_close, 1)

  def warmupGripper(self):
    pass

  def DewarHeaterOff(self):
    return set_and_check(self.heater_off, 1)

  def DewarHeaterOn(self):
    return set_and_check(self.heater_on, 1)

  def parkGripper(self):
    pass

  def testRobot(self):
    pass

  def openPort(self, PortNo):
    pass

  def closePorts(self):
    pass

  def dryGripper(self):
    self.dry_traj.set(1)

  def movement_ready(self):
    if not self.power_sts.get():
      return [False, "Power is off"]
    if self.moving_sts.get():
      return [False, "Moving"]
    if self.paused_sts.get():
      return [False, "Paused"]
    return [True, "mount ready"]

  # Recover Trajectory
  #  required arguments
  #  --current_tool_number
  def recoverRobot(self):
    if self.current_tool.get() != self.tool_selected.get():
      raise RuntimeError(f"Bad tool argument")
    traj_status = self.recover_traj.set(1)
    traj_status.wait(ISARA_TIMEOUT)
    return traj_status.success

  def finish():
    pass

  # Mount (Put Trajectory)
  #  required arguments:
  #  --current_tool_number
  #  --sample_num
  #  --puck_num
  #  optional arguments:
  #  --next_sample_num
  #  --next_puck_num
  #def mountRobotSample(self):
  #  if self.current_tool.get() != self.tool_selected.get():
  #    raise RuntimeError(f"Bad tool argument")
  #  return self.put_traj.set(1).wait(ISARA_TIMEOUT)

  # unmount Trajectory
  #  required arguments
  #  --current_tool_number
  #def unmountRobotSample(self):
  #  if self.current_tool.get() != self.tool_selected.get():
  #    raise RuntimeError(f"Bad tool argument")
  #  return self.back_traj.set(1).wait(ISARA_TIMEOUT)

  # Home Trajectory
  #  required arguments
  #  --current_tool_number
  def homeRobot(self):
    if self.current_tool.get() != self.tool_selected.get():
      raise RuntimeError(f"Bad tool argument")
    traj_status = self.home_traj.set(1)
    traj_status.wait(ISARA_TIMEOUT)
    return traj_status.success

  # Soak Trajectory
  #  required arguments
  #  --current_tool_number
  def soakGripper(self):
    if self.current_tool.get() != self.tool_selected.get():
      raise RuntimeError(f"Bad tool argument")
    traj_status = self.soak_traj.set(1)
    traj_status.wait(ISARA_TIMEOUT)
    return traj_status.success

  def set_sample(self, puck: str, sample: str):
    sample_str = f"{sample}{puck}"

    #TODO: switch status.wait to callbacks
    puck_sel_status = self.puck_num_sel.set(puck)
    sample_sel_status = self.sample_num_sel.set(sample)
    puck_sel_status.wait(ISARA_TIMEOUT)
    sample_sel_status.wait(ISARA_TIMEOUT)

    if not sample_sel_status.success:
      raise RuntimeError(f"Failed to set sample_select: '{sample_str}'")
    if not puck_sel_status.success:
      raise RuntimeError(f"Failed to set puck_select: '{sample_str}'")

    return sample_str

  def mount(self, puck: str, sample: str):
    # check robot is ready
    ready, desc = self.movement_ready()
    if not ready:
      raise RuntimeError(f"Can't mount: {desc}")
    # check trajectory arguments
    if self.current_tool.get() != self.tool_selected.get():
      raise RuntimeError(f"Bad tool argument")
    sample_str = self.set_sample(puck, sample)
    # check that position == soak
    if position_sts.get() != "SOAK":
      if not self.set_and_check(self.soak_traj, 1):
        raise RuntimeError("Failed to reach soak position before mounting")
    mount_status = self.put_traj.set(1)
    mount_status.wait(ISARA_TIMEOUT)

    if not mount_status.success:
      raise RuntimeError(f"Can't mount {sample_str}: failed to mount")
    return mount_status

  def dismount(self):
    # check robot is ready
    ready, desc = self.movement_ready()
    if not ready:
      raise RuntimeError(f"Can't dismount {sample_str}: busy")
    # check spindle is actually occupied
    if not self.spindle_occupied_sts.get():
      raise RuntimeError(f"Can't dismount {sample_str}: spindle not occupied")
    # check trajectory arguments
    if self.current_tool.get() != self.tool_selected.get():
      raise RuntimeError(f"Bad tool argument")

    dismount_status = self.get_traj.set(1)
    dismount_status.wait(ISARA_TIMEOUT)

    if not dismount_status.success:
      raise RuntimeError(f"Can't dismount {sample_str}: failed to dismount")
    return dismount_status
