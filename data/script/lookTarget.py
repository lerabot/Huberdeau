import bge

cont = bge.logic.getCurrentController()
own = cont.owner
scene = bge.logic.getCurrentScene()

if own["target"] in scene.objects:
        target = scene.objects[own['target']]
        direction = own.worldPosition - target.worldPosition
        direction = direction.normalized()
        #position = mathutils.Vector((0,0,10))
        #print(direction)
        own.alignAxisToVect(direction, )
