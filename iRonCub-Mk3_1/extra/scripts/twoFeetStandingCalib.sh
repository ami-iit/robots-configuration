echo "!!Now I will calib the wholeBodyDynamics!!"
sleep 0.1
echo "calibStanding all 300"  | yarp rpc /wholeBodyDynamics/rpc
sleep 0.1
yarp clean --timeout 0.2

