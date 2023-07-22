import getpass
import telnetlib

device = "127.0.0.1"

tn = telnetlib.Telnet()
tn.open(host=device , port = 49664)


PROTOCOL_COMMAND = """
<!-- Root Node, use OmniaXB -->
<OmniaXB>
  <!-- This is the subsystem to which the command belongs to -->
  <System>
    <!-- This is the command to execute -->
    <GetProtocolLevel />
  </System>
</OmniaXB>
"""

create_session_command = """
<OmniaXB> 
  <System> 
    <CreateSessionKey /> 
  </System> 
</OmniaXB> 
"""
# tn.read_until("login: ")

tn.write(create_session_command.encode("utf-8"))

print(tn.read_all().decode("utf-8"))
tn.close()
