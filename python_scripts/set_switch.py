entity_id = data.get("entity_id")

if entity_id is not None:
    service_data = {"entity_id": entity_id}
    logger.info("entity_id: %s", entity_id)
    state = data.get("state")
    #state_to_set = "turn_on"
    state_to_set = state
    #if state == "off":
      #state_to_set = "turn_off"

    hass.services.call("lock", state_to_set, service_data, False)
else:
  logger.info("unknown entity_id: %s", entity_id)
#hass.bus.fire("hello_world_event", {"entity_id": entity_id})
# run with parameter:    
#    entity_id: switch.Dachgeschossdeckenlicht
