import keyboard, queue

input_values=queue.Queue()

keyboard.start_recording(recorded_events_queue=input_values)

new_String=""
while True:
    val = input_values.get(block=True)
    if val==" ":
        break
    else:
        new_String+=val
        