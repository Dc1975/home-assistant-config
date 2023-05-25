# `data` is available as builtin and is a dictionary with the input data.
name = data.get("name")
world = data.get("world")
# `logger` and `time` are available as builtin without the need of explicit import.
logger.info("Hello {} at {}".format(name, time.time()))
#hass.bus.fire("hello_world_event", {"wow": "from a Python script!"})
#hass.bus.fire("hello_world_event", {name:  "world"})
hass.bus.fire("hello_world_event", {"input": world})