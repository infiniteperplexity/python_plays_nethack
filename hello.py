import pty, os
(process_id, fd) = pty.fork()
print(process_id, fd)
print("hello world")
