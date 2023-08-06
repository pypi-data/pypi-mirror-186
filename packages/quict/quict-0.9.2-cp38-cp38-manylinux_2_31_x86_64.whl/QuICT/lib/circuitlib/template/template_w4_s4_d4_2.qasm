OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg c[4];
ccx q[0], q[1], q[3];
cx q[1], q[2];
ccx q[0], q[1], q[3];
cx q[1], q[2];
