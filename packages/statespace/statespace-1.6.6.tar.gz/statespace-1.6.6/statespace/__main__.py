"""interesting and important applications of computing in the 40s, 50s, and 60s - stuff that drove forward the early
generations of hardware, and what eventually became known as software - what some of the machines in the old film
clips were actually doing, and why fortran was a big deal - tons of large scale linear algebra - floating-point
matrix and vector operations.

for the purposes here, the beginnings were dantzig and von neumann linear programming - all woven through operations
research around the time of the transition from mechanical to digital computing - early cold war. one of the things
kalman then brought in on top was nonlinear elements capable of representing uncertainty - the classic covariance
matrix quadratic form ATAx. this was happening across fields, as the same appeared in finance via markowitz portfolio
theory at the same time - what was driving all this organic evolution was the increasing floating point computing
power - flops - and the ability to harness it via fortran. and the impact was immediate - high cold war - late 50s
early 60s - with the early integrated circuitry of the apollo guidance computer and minuteman missile guidance
system. how do life-or-death automated control systems make better decisions? the birth of machine learning -
adaptive closed-loop feedback control.

increasing flops and fortran drove the appearance of covariance matrices in what was purely linear optimization - but
things were definitely on the edge - quadratic forms immediately blew up the numerical ranges and numerical
instability. there weren't enough bits in the floating point representations - plain and simple. what immediately
happened was a cottage industry within applied mathematics and electrical engineering - optimize the fortran and
floating point units, and factorize the matrices. what does factorize the matrices mean? in a nutshell,
only represent something very much like their square roots - at least internally within the processing. this all
dominated the 60s, 70s, and 80s - high cold war onward through baroque/neo-classical cold war - the era when the name
'cray' inspired awe. one of the objectives here is a straightforward minimalistic representation of the real-world
factorized forms, alongside the classic textbook forms. names like thornton and bierman aren't widely remembered
today - but without the factorized form 'square root' ekf, the apollo guidance computer wasn't possible at that time
- and they were crucial for the transit/gps satnav systems as well. those who know about ud decomposition,
cholesky decomposition, singular value decomposition, etc - know."""
import sys
import argparse


def main():
    """configure and call process_model(). -h and --help are built in, so 'python statespace -h' displays an options
    text. """
    cli = argparse.ArgumentParser()
    cli.add_argument('-p', '--processor', choices=['ekf', 'spkf', 'pf'], default='ekf', type=str)
    cli.add_argument('-m', '--model', choices=['one', 'three', 'bearings'], default='three', type=str)
    cli.add_argument('-f', '--factorized', dest='factorized', action='store_true', default=False)
    conf = cli.parse_args()
    if not len(sys.argv) > 1:
        conf.processor = 'ekf'
        conf.model = 'one'
        conf.factorized = False
    process_model(conf)


def process_model(conf):
    """bring in a processor and a model, process the model, evaluate the results. """
    processor, model = None, None
    match conf.processor:
        case 'ekf':
            from statespace.extended_kalman_filter import Kalman
            processor = Kalman(conf)
        case 'spkf':
            from statespace.sigma_point_kalman_filter import SigmaPoint
            processor = SigmaPoint(conf)
        case 'pf':
            from statespace.particle_filter import Particle
            processor = Particle(conf)
    match conf.model:
        case 'one':
            from statespace.one_state import Onestate
            model = Onestate(conf)
        case 'three':
            from statespace.three_state import Threestate
            model = Threestate(conf)
        case 'bearings':
            from statespace.bearings_only import BearingsOnly
            model = BearingsOnly(conf)
    processor.run(model)
    model.eval.estimate(processor.log)
    # model.eval.autocorr.run(processor.log)
    model.eval.show()


if __name__ == "__main__":
    main()
