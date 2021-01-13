import lib601.sm as sm
import lib601.util as util
import math

# Use this line for running in idle
import lib601.io as io
# Use this line for testing in soar
# from soar.io import io


class DynamicMoveToPoint(sm.SM):
    minFVel = 0
    maxFVel = 0.3
    minRVel = -0.3
    maxRVel = 0.3
    distEps = 0.001
    angleEps = 0.001

    def getNextValues(self, state, inp):
        # Replace this definition
        # print 'DynamicMoveToPoint', 'state=', state, 'inp=', inp
        # assert isinstance(inp,tuple), 'inp should be a tuple'
        # assert len(inp) == 2, 'inp should be of length 2'
        # assert isinstance(inp[0],util.Point), 'inp[0] should be a Point'
        # return (state, io.Action())

        (target, sensorInput) = inp
        pose = sensorInput.odometry
        
        if not pose.point().isNear(target, self.distEps):
            fvel = util.clip(
                pose.point().distance(target),
                self.minFVel,
                self.maxFVel
            )
        else:
            fvel = 0

        print pose.point(), target, pose.point().angleTo(target)
        if not util.nearAngle(0, pose.point().angleTo(target), self.angleEps):
            rvel = util.clip(
                util.fixAnglePlusMinusPi(pose.point().angleTo(target)),
                self.minRVel,
                self.maxRVel
            )
        else:
            rvel = 0

        return (state, io.Action(fvel=fvel, rvel=rvel))
