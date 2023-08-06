OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];
x q[0];
h q[0];
rzz(0.22207677364349365) q[0], q[1];
rzx(0.45610785484313965) q[0], q[1];
h q[0];
