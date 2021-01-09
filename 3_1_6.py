import lib601.sm as sm

negate = sm.PureFunction(lambda x: 'undefined' if x == 'undefined' else not x)

alternating = sm.Feedback(
    sm.Cascade(
        negate,
        sm.Delay(True)
    )
)

print alternating.run(n = 20)