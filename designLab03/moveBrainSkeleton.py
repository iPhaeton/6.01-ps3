from sys import path
import os
labPath = os.getcwd()
if not labPath in path:
    path.append(labPath)
print 'setting labPath to', labPath
from secretMessage import secret
import ffSkeleton
import dynamicMoveToPointSkeleton
from soar.io import io
import lib601.gfx as gfx
import lib601.sm as sm
import lib601.util as util
import math


# Remember to change the import in dynamicMoveToPointSkeleton in order
# to use it from inside soar
reload(dynamicMoveToPointSkeleton)

reload(ffSkeleton)


# Set to True for verbose output on every step
verbose = False

# Rotated square points
squarePoints = [util.Point(0.5, 0.5), util.Point(0.0, 1.0),
                util.Point(-0.5, 0.5), util.Point(0.0, 0.0)]

# Put your answer to step 1 here
goalGenerator = sm.Constant(util.Point(1.0, 0.5))
dynamicMoveToPoint = dynamicMoveToPointSkeleton.DynamicMoveToPoint()

mySM = sm.Cascade(
    sm.Parallel(
        goalGenerator,
        sm.Wire()
    ),
    dynamicMoveToPoint
)

######################################################################
###
# Brain methods
###
######################################################################


def setup():
    robot.gfx = gfx.RobotGraphics(drawSlimeTrail=True)
    robot.behavior = mySM


def brainStart():
    robot.behavior.start(traceTasks=robot.gfx.tasks(),
                         verbose=verbose)


def step():
    robot.behavior.step(io.SensorInput()).execute()
    io.done(robot.behavior.isDone())


def brainStop():
    pass


def shutdown():
    pass
