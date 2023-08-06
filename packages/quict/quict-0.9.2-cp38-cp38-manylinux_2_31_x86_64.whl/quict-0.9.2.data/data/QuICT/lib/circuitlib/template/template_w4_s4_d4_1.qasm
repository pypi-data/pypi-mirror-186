OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg c[4];
ccx q[1], q[2], q[3];
ccx q[0], q[2], q[3];
ccx q[1], q[2], q[3];
ccx q[0], q[2], q[3];
